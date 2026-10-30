# 🎯 Internship Compass

### AI-Powered Internship Readiness & Skill Gap Analyzer

Internship Compass is a Python-based web application that helps students evaluate their readiness for internships by comparing their resumes with job descriptions.

It identifies matching and missing technical skills, calculates resume–job text similarity, and generates a personalized learning roadmap to help students improve their internship applications.

## 🚀 Features

- **Resume Upload:** Upload resumes in PDF format.
- **Skill Extraction:** Automatically identifies technical skills from resumes and job descriptions.
- **Skill Gap Analysis:** Highlights matched and missing skills.
- **Job Skill Coverage:** Calculates the percentage of required skills found in the resume.
- **Text Similarity:** Uses TF-IDF and Cosine Similarity to compare resume and job description text.
- **Interactive Dashboard:** Displays skill comparison charts and performance metrics.
- **Role-Based Recommendations:** Suggests skills based on the selected internship role.
- **Personalized Learning Roadmap:** Recommends learning topics and mini-projects.
- **Downloadable Report:** Generates a report of the analysis.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- TF-IDF
- Cosine Similarity
- PDFPlumber
- Matplotlib / Streamlit Charts

## 📂 Project Structure

```text
internship-compass/
│
├── app.py
├── skill_utils.py
├── app_backup.py
├── README.md
├── requirements.txt
│
└── tests/
    └── test_skill_utils.py
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd internship-compass
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

## 🧪 Run Tests

```bash
python -m unittest discover -s tests -v
```

## 📊 How It Works

1. Upload a resume in PDF format or paste resume text.
2. Paste the internship job description.
3. Select the target internship role.
4. Click Analyze.
5. View matching skills, missing skills, and similarity metrics.
6. Follow the personalized learning roadmap.
7. Download the analysis report.

## 🔮 Future Improvements

- Integration with real internship job portals.
- Advanced NLP-based skill extraction.
- Machine Learning-based job recommendations.
- Resume improvement suggestions.
- Support for more resume formats.

## 👩‍💻 Author

Developed as a personal portfolio project to demonstrate Python programming, NLP concepts, data analysis, and Streamlit application development.

## 📌 Disclaimer

Resume–job text similarity is a text comparison measure, not a hiring probability. Skill coverage only considers the technical skills recognized by the application.