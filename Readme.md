Simple Flask app example (student-style)

Run locally:

1. Create a virtualenv (optional): `python -m venv venv && venv\Scripts\activate`
2. Install deps: `pip install -r requirements.txt`
3. Run: `python app.py`

Run tests:

```
pip install -r requirements.txt
pytest -q
```

Build Docker image:

```
docker build -t app:latest .
docker run -p 8080:8080 app:latest
```

CI notes:

- Jenkinsfile is present for Docker-enabled nodes labeled `docker`.
- Multibranch or webhook required to trigger builds on branch push.
