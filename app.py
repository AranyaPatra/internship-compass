
import streamlit as st
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from skill_utils import extract_skills, SKILLS
import pdfplumber


def reset_inputs():
    st.session_state["resume_input"] = ""
    st.session_state["job_input"] = ""

st.set_page_config(
    page_title="Internship Compass",
    page_icon="🧭",
    layout="wide"
)

st.set_page_config(
    page_title="Internship Compass",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Internship Compass")
st.write(
    "An AI-powered internship readiness platform that analyzes "
    "your resume, identifies skill gaps, compares job requirements, "
    "and generates a personalized learning roadmap."
)


st.subheader("Find your skill gaps. Prepare for your next internship.")

st.write(
    "Compare your resume with an internship description "
    "to discover your matching skills and learning needs."
)



ROADMAP = {
    "Python": {
        "learn": "Functions, lists, dictionaries and file handling.",
        "project": "Build a command-line task manager."
    },
    "SQL": {
        "learn": "SELECT, WHERE, JOIN, GROUP BY and subqueries.",
        "project": "Analyze student marks using SQL queries."
    },
    "Pandas": {
        "learn": "DataFrames, filtering, missing values and grouping.",
        "project": "Clean and analyze a messy CSV dataset."
    },
    "NumPy": {
        "learn": "Arrays, indexing and vectorized calculations.",
        "project": "Build a simple numerical data analysis tool."
    },
    "Machine Learning": {
        "learn": "Regression, classification, train-test splits and evaluation.",
        "project": "Predict student performance using sample data."
    },
    "Scikit-learn": {
        "learn": "Preprocessing, model fitting and evaluation metrics.",
        "project": "Train and evaluate a classification model."
    },
    "Statistics": {
        "learn": "Mean, variance, probability and distributions.",
        "project": "Explore patterns in a public dataset."
    },
    "Deep Learning": {
        "learn": "Neural networks, activation functions and backpropagation.",
        "project": "Build a small neural network classifier."
    },
    "TensorFlow": {
        "learn": "Tensors, layers, model training and evaluation.",
        "project": "Create a simple image classification model."
    },
    "Data Visualization": {
        "learn": "Charts, labels and choosing appropriate visualizations.",
        "project": "Create a data insights dashboard."
    },
    "Git": {
        "learn": "Repositories, commits, branches and pull requests.",
        "project": "Publish a project with a clear commit history."
    },
    "Excel": {
        "learn": "Formulas, pivot tables, sorting and charts.",
        "project": "Create a monthly expense analysis workbook."
    },
    "NLP": {
        "learn": "Text cleaning, tokenization and text classification.",
        "project": "Build a simple review sentiment classifier."
    },
    "Streamlit": {
        "learn": "Widgets, layouts, session state and deployment.",
        "project": "Build an interactive analytics dashboard."
    },
    "Power BI": {
        "learn": "Data modelling, visuals and basic DAX measures.",
        "project": "Create an interactive business dashboard."
    }
}




ROLE_SKILLS = {
    "Data Science Intern": [
        "Python", "SQL", "Pandas", "NumPy",
        "Statistics", "Machine Learning"
    ],
    "Machine Learning Intern": [
        "Python", "NumPy", "Pandas",
        "Machine Learning", "Scikit-learn",
        "Statistics", "Deep Learning"
    ],
    "Python Developer Intern": [
        "Python", "SQL", "Git"
    ],
    "Data Analyst Intern": [
        "Python", "SQL", "Pandas",
        "Excel", "Statistics", "Data Visualization",
        "Power BI"
    ],
    "NLP Intern": [
        "Python", "Machine Learning",
        "Deep Learning", "NLP"
    ],
    "Software Developer Intern": [
        "Python", "SQL", "Git"
    ],
    "Other": []
}





st.divider()


st.header("Choose your target role")

target_role = st.selectbox(
    "Which internship are you applying for?",
    [
        "Data Science Intern",
        "Machine Learning Intern",
        "Python Developer Intern",
        "Data Analyst Intern",
        "NLP Intern",
        "Software Developer Intern",
        "Other"
    ]
)

st.write(f"Target role: **{target_role}**")

st.header("1. Enter your resume")

uploaded_resume = st.file_uploader(
    "Or upload your resume as a PDF",
    type=["pdf"]
)

if uploaded_resume is not None:
    try:
        with pdfplumber.open(uploaded_resume) as pdf:
            extracted_text = "\n".join(
                page.extract_text() or ""
                for page in pdf.pages
            )

        if extracted_text.strip():
            st.success("Resume text extracted successfully!")
            st.session_state["resume_input"] = extracted_text
        else:
            st.warning(
                "No readable text found. "
                "This PDF may be scanned or image-based."
            )

    except Exception:
        st.error("Could not read this PDF. Please try another file.")


resume = st.text_area(
    "Resume text",
    height=200,
    placeholder="Paste your education, skills and projects...",
    key="resume_input"
)


st.header("2. Enter the internship description")


job_description = st.text_area(
    "Internship description",
    height=200,
    placeholder="Paste the internship requirements...",
    key="job_input"
)



col_analyze, col_reset = st.columns(2)

with col_analyze:
    analyze_clicked = st.button(
        "Analyze my internship fit",
        type="primary"
    )

with col_reset:
    reset_clicked = st.button(
    "🔄 Reset inputs",
    on_click=reset_inputs
)


if analyze_clicked:


    if not resume.strip() or not job_description.strip():
        st.warning("Please fill in both text fields.")

    else:
        
        vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=3000
        )

        tfidf_matrix = vectorizer.fit_transform(
            [resume, job_description]
        )

        similarity = cosine_similarity(
            tfidf_matrix[0:1],
            tfidf_matrix[1:2]
        )[0][0]

        similarity_percentage = similarity * 100

        resume_skills = extract_skills(resume)
        job_skills = extract_skills(job_description)

        matched_skills = resume_skills & job_skills
        missing_skills = job_skills - resume_skills

        role_skills = set(ROLE_SKILLS.get(target_role, []))
        role_missing_skills = role_skills - resume_skills

        st.divider()
        st.header("3. Your skill-gap report")

        if not job_skills:
            st.warning(
                "No supported skills were detected in the job description. "
                "Try a description containing technical skills."
            )

        else:
            coverage = (
                len(matched_skills) / len(job_skills)
            ) * 100

            metric1, metric2, metric3 = st.columns(3)

            with metric1:
                st.metric(
                    "Job skill coverage",
                    f"{coverage:.1f}%"
                )

            with metric2:
                st.metric(
                    "Resume–Job Text Similarity",
                    f"{similarity_percentage:.1f}%"
                )

            with metric3:
                st.metric(
                    "Matched skills",
                    len(matched_skills)
                )
            

            st.progress(coverage / 100)

            chart_data = pd.DataFrame({
                "Skill category": ["Matched", "To develop"],
                "Number of skills": [
                    len(matched_skills),
                    len(missing_skills)
                ]
            })

            st.subheader("📊 Skill comparison")
            st.bar_chart(
                chart_data,
                x="Skill category",
                y="Number of skills"
            )

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("✅ Matched skills")
                if matched_skills:
                    for skill in sorted(matched_skills):
                        st.success(skill)
                else:
                    st.write("No matching skills found yet.")

            with col2:
                st.subheader("📚 Skills to develop")
                if missing_skills:
                    for skill in sorted(missing_skills):
                        st.warning(skill)
                else:
                    st.write("All detected job skills are matched!")



        with st.expander("View all detected skills"):
            st.write("**Skills found in your resume:**")
            st.write(", ".join(sorted(resume_skills)) or "None detected")

            st.write("**Skills found in the job description:**")
            st.write(", ".join(sorted(job_skills)) or "None detected")

        
        st.divider()
        st.header("4. Your personalized learning roadmap")

        if missing_skills:
            st.write(
                "Focus on these skills to better align your resume "
                "with the selected internship."
            )

            for skill in sorted(missing_skills):
                if skill in ROADMAP:
                    with st.expander(f"📘 Learn {skill}"):
                        st.write(
                            "**What to learn:** "
                            + ROADMAP[skill]["learn"]
                        )
                        st.write(
                            "**Mini-project to practise:** "
                            + ROADMAP[skill]["project"]
                        )
        else:
            st.success(
                "No missing supported skills were detected. "
                "Consider building an advanced project for this role."
            )


        st.caption(
            "This is a keyword-based prototype. Coverage only measures "
            "overlap among the skills this application recognizes. "
            "It does not measure overall employability."
        )


        
        
        report = f"""
INTERNSHIP COMPASS - SKILL GAP REPORT
=====================================

TARGET ROLE: {target_role}
JOB SKILL COVERAGE: {coverage:.1f}%
RESUME-JOB TEXT SIMILARITY: {similarity_percentage:.1f}%

MATCHED SKILLS:
{", ".join(sorted(matched_skills)) or "None"}

SKILLS TO DEVELOP:
{", ".join(sorted(missing_skills)) or "None"}

RECOMMENDED LEARNING ROADMAP:
"""


        for skill in sorted(missing_skills):
            if skill in ROADMAP:
                report += (
                    f"\n{skill}\n"
                    f"What to learn: {ROADMAP[skill]['learn']}\n"
                    f"Mini-project: {ROADMAP[skill]['project']}\n"
                )

        st.download_button(
            label="📥 Download Skill Gap Report",
            data=report,
            file_name="internship_skill_gap_report.txt",
            mime="text/plain"
        )

