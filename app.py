import streamlit as st

from utils.resume_parser import extract_text
from utils.skill_extractor import extract_skills
from utils.skill_matcher import compare_skills


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.markdown(
    """
    <style>
    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    [data-testid="stSidebar"] {
        border-right: 1px solid rgba(128, 128, 128, 0.2);
    }

    div[data-testid="stMetric"] {
        background: rgba(128, 128, 128, 0.08);
        border: 1px solid rgba(128, 128, 128, 0.2);
        border-radius: 0.75rem;
        padding: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.title("🤖 AI Resume Analyzer")

    st.subheader("Features")
    st.markdown(
        """
        - Analyze PDF and DOCX resumes
        - Compare skills with a job description
        - Highlight matching and missing skills
        - Show a resume match score
        - Provide improvement suggestions
        """
    )

    st.subheader("How the application works")
    st.markdown(
        """
        1. Upload your resume.
        2. Paste the job description.
        3. Select **Analyze Resume** to review the match and suggestions.
        """
    )

st.title("🤖 AI Resume Analyzer")
st.write(
    "Analyze your resume against a job description, find matching and missing "
    "skills, review your resume score, and get suggestions to improve your "
    "application."
)

st.divider()

resume_column, job_column = st.columns(2)

with resume_column:
    st.subheader("📄 Resume Upload")
    uploaded_file = st.file_uploader(
        "Choose your resume",
        type=["pdf", "docx"]
    )

    resume_text = ""

    if uploaded_file is not None:
        st.success(f"Resume uploaded successfully: {uploaded_file.name}")
        resume_text = extract_text(uploaded_file)

        with st.expander("Preview extracted resume text"):
            st.text_area(
                "Resume Content",
                resume_text,
                height=250
            )

with job_column:
    st.subheader("💼 Job Description")
    job_description = st.text_area(
        "Paste the job description here",
        height=250,
        placeholder="Paste the job description here..."
    )

st.divider()
st.subheader("🔍 Analyze Resume")

if st.button("🔍 Analyze Resume", type="primary"):
    if uploaded_file is None:
        st.warning("⚠️ Please upload your resume first.")

    elif not job_description.strip():
        st.warning("⚠️ Please paste the job description first.")

    else:
        st.success("✅ Resume and Job Description are ready for analysis!")

        # Extract skills
        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_description)

        # Compare skills
        matching_skills, missing_skills, match_percentage = compare_skills(
            resume_skills,
            job_skills
        )

        st.divider()
        st.subheader("📊 Resume Match Analysis")
        st.metric(
            "Job Match Percentage",
            f"{match_percentage}%"
        )

        matching_column, missing_column = st.columns(2)

        with matching_column:
            st.subheader("✅ Matching Skills")

            if matching_skills:
                for skill in matching_skills:
                    st.markdown(f"- {skill}")
            else:
                st.info("No matching skills found.")

        with missing_column:
            st.subheader("❌ Missing Skills")

            if missing_skills:
                for skill in missing_skills:
                    st.markdown(f"- {skill}")
            else:
                st.success("🎉 No major skills are missing!")

        with st.expander("View extracted skills"):
            resume_skills_column, job_skills_column = st.columns(2)

            with resume_skills_column:
                st.markdown("**Skills found in resume**")
                if resume_skills:
                    st.write(", ".join(resume_skills))
                else:
                    st.info("No skills were detected in the resume.")

            with job_skills_column:
                st.markdown("**Skills required by job**")
                if job_skills:
                    st.write(", ".join(job_skills))
                else:
                    st.info("No skills were detected in the job description.")

        st.subheader("📈 Resume Score")
        resume_score = match_percentage
        score_column, status_column = st.columns([1, 2])

        with score_column:
            st.metric("Resume Score", f"{resume_score}%")

        with status_column:
            if resume_score >= 80:
                st.success(f"Excellent Resume Score: {resume_score}%")
            elif resume_score >= 60:
                st.warning(f"Good Resume Score: {resume_score}%")
            else:
                st.error(
                    f"Resume Score: {resume_score}% — Needs Improvement"
                )

        st.subheader("💡 Improvement Suggestions")

        if missing_skills:
            st.write("Add these missing skills where they accurately reflect your experience:")
            for skill in missing_skills:
                st.markdown(f"- {skill}")
        else:
            st.success("🎉 Your resume contains all the required job skills!")

        if resume_score < 60:
            st.markdown("- Add more relevant technical skills.")
            st.markdown("- Add measurable achievements to your experience.")
            st.markdown("- Keep your resume clear and ATS-friendly.")
        elif resume_score < 80:
            st.markdown("- Add more project details and achievements.")
            st.markdown("- Improve the description of your technical skills.")
        else:
            st.markdown("- Your resume is well matched to the selected job.")
            st.markdown("- Keep your skills and projects updated.")
