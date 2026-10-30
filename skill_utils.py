import re

SKILLS = {
    "Python": ["python"],
    "SQL": ["sql", "mysql", "postgresql"],
    "Pandas": ["pandas"],
    "NumPy": ["numpy"],
    "Machine Learning": ["machine learning", "ml"],
    "Scikit-learn": ["scikit-learn", "sklearn"],
    "Statistics": ["statistics", "statistical analysis"],
    "Deep Learning": ["deep learning"],
    "TensorFlow": ["tensorflow"],
    "Data Visualization": [
        "data visualization", "matplotlib", "seaborn"
    ],
    "Git": ["git", "github"],
    "Excel": ["excel", "spreadsheets"],
    "NLP": ["natural language processing", "nlp"],
    "Streamlit": ["streamlit"],
    "Power BI": ["power bi"],
}


def extract_skills(text):
    """Return the known skills found in a piece of text."""
    found_skills = set()
    text = text.lower()

    for skill, aliases in SKILLS.items():
        for alias in aliases:
            pattern = r"(?<!\w)" + re.escape(alias) + r"(?!\w)"

            if re.search(pattern, text):
                found_skills.add(skill)
                break

    return found_skills