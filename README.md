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

## A note on the SECRET_KEY

`SECRET_KEY` and `DEBUG` are now read from the environment. Earlier commits in this
repository contain a hardcoded `SECRET_KEY` from the IBM starter project.

**That key was never a live credential.** It signs sessions for a course app that runs on
`localhost` — `ALLOWED_HOSTS` has only ever been `localhost`, `127.0.0.1` and `testserver`,
and the project has never been deployed anywhere. Nothing was protected by it, so nothing
is exposed by it remaining in the history.

It was moved to an environment variable because committing a real key is the wrong habit,
not because this one was sensitive.

---

Built on the IBM Developer Skills Network starter project.
