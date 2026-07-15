import pdfplumber


SKILLS = [
    "python",
    "flask",
    "django",
    "sql",
    "mysql",
    "mongodb",
    "java",
    "html",
    "css",
    "javascript",
    "bootstrap"
]


def extract_resume_text(pdf_path):

    text = ""

    with pdfplumber.open(
        pdf_path
    ) as pdf:

        for page in pdf.pages:

            text += page.extract_text() or ""

    return text.lower()


def extract_skills(text):

    found_skills = []

    for skill in SKILLS:

        if skill in text:

            found_skills.append(skill)

    return found_skills
def calculate_match_score(
    resume_skills,
    job_skills
):

    job_skills = [
        skill.strip().lower()
        for skill in job_skills.split(",")
    ]

    matched = len(
        set(resume_skills)
        &
        set(job_skills)
    )

    if len(job_skills) == 0:
        return 0

    return round(
        (matched / len(job_skills))
        * 100
    )