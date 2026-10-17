# SkillMatch AI

A lightweight Streamlit MVP that compares resume text with a job description and reports:
- a transparent keyword-overlap score,
- detected matching skills,
- missing skills to consider developing,
- practical resume-improvement suggestions.

## Run locally

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## Deploy with Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload `app.py`, `requirements.txt`, and this `README.md`.
3. Go to https://share.streamlit.io/ and sign in with GitHub.
4. Choose the repository, branch, and `app.py` as the main file.
5. Deploy and wait for the public app URL.
6. Open the public URL on your phone and test both text fields.

## Important limitations

This is a prototype that uses a curated keyword list, not a trained AI model. The score measures only overlap between supported keywords found in the two text boxes. It does not assess experience quality, verify qualifications, or predict hiring outcomes. Do not paste sensitive personal information into public demos.

## Demo checklist

- Enter sample resume text.
- Enter sample job-description text.
- Tap **Analyze skill match**.
- Show the score, matched skills, missing skills, and suggestions.
- Explain the keyword-overlap limitation honestly.
