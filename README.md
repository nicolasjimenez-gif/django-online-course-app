# Online Course Assessment

A Django course app with an exam feature added. A learner enrols, works through the
lessons, answers multiple-choice questions and is scored immediately, with each answer
marked right or wrong.

Grading handles single-answer and multi-select questions. A multi-select only counts as
correct when the chosen set matches exactly — no partial credit. Tests cover the course
list, that scoring rule, and the submission round-trip.

## Run it

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then `http://127.0.0.1:8000/onlinecourse/`.

---

Built on the IBM Developer Skills Network starter project.
