"""Automated tests for the assessment workflow."""

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Choice, Course, Enrollment, Lesson, Question, Submission


class AssessmentWorkflowTests(TestCase):
    """Verify models, course rendering, submission, and score calculation."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="student", password="safe-test-password", first_name="Nicolas"
        )
        self.course = Course.objects.create(
            name="Django Web Development",
            image="course_images/django.jpg",
            description="Build database-backed web applications with Django.",
        )
        self.lesson = Lesson.objects.create(
            course=self.course,
            title="Django Models and Views",
            order=0,
            content="Create models, routes, views, and templates.",
        )
        self.enrollment = Enrollment.objects.create(
            user=self.user, course=self.course, mode=Enrollment.HONOR
        )
        self.question = Question.objects.create(
            course=self.course,
            text="Which Django component maps URLs to views?",
            grade=10,
        )
        self.correct_choice = Choice.objects.create(
            question=self.question, text="URL configuration", is_correct=True
        )
        self.wrong_choice = Choice.objects.create(
            question=self.question, text="Database migration", is_correct=False
        )
        self.client.force_login(self.user)

    def test_course_details_display_course_lessons_and_exam(self):
        response = self.client.get(
            reverse("onlinecourse:course_details", args=(self.course.id,))
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.course.name)
        self.assertContains(response, self.lesson.title)
        self.assertContains(response, self.question.text)

    def test_question_scores_only_exact_correct_choices(self):
        self.assertTrue(self.question.is_get_score([self.correct_choice]))
        self.assertFalse(
            self.question.is_get_score([self.correct_choice, self.wrong_choice])
        )

    def test_submit_creates_submission_and_displays_passing_result(self):
        response = self.client.post(
            reverse("onlinecourse:submit", args=(self.course.id,)),
            {f"choice_{self.correct_choice.id}": str(self.correct_choice.id)},
            follow=True,
        )
        submission = Submission.objects.get(enrollment=self.enrollment)
        self.assertIn(self.correct_choice, submission.choices.all())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Congratulations")
        self.assertContains(response, "100/100")

# Create your tests here.
