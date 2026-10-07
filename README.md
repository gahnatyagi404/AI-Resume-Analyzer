# 🤖 AI Resume Analyzer + Job Matcher

An AI-powered web application that analyzes resumes and compares them with job descriptions to identify matching skills, missing skills, resume score, and improvement suggestions.

## 🚀 Features

- 📄 Upload PDF or DOCX resumes
- 🔍 Extract text from resumes
- 🧠 Automatically extract technical skills
- 💼 Analyze job descriptions
- ✅ Find matching skills
- ❌ Find missing skills
- 📊 Calculate resume/job match percentage
- 📈 Generate resume score
- 💡 Provide resume improvement suggestions
- 🎨 Professional Streamlit user interface

## 🛠️ Technologies Used

- Python
- Streamlit
- PyPDF
- Python-DOCX
- Pandas
- NumPy
- Scikit-learn
- spaCy

## 📁 Project Structure

```text
AI resume analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── skills.json
│
├── utils/
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   └── skill_matcher.py
│
├── models/
├── assets/
└── venv/