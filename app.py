import re
import streamlit as st

st.set_page_config(page_title="SkillMatch AI", page_icon="🎯", layout="wide")

# A lightweight, transparent MVP. It uses keyword matching and does not claim to be
# a trained AI model or a substitute for human hiring decisions.
SKILL_GROUPS = {
    "Python": ["python"],
    "Java": ["java"],
    "JavaScript": ["javascript", "js"],
    "TypeScript": ["typescript"],
    "C++": ["c++", "cpp"],
    "SQL": ["sql", "mysql", "postgresql", "postgres"],
    "HTML/CSS": ["html", "css"],
    "React": ["react", "react.js"],
    "Node.js": ["node.js", "nodejs"],
    "Machine Learning": ["machine learning", "ml", "scikit-learn", "sklearn"],
    "Deep Learning": ["deep learning", "pytorch", "tensorflow", "keras"],
    "Natural Language Processing": ["natural language processing", "nlp", "spacy", "nltk"],
    "Data Analysis": ["data analysis", "data analytics", "pandas", "numpy"],
    "Data Visualization": ["data visualization", "matplotlib", "seaborn", "tableau", "power bi"],
    "Excel": ["excel", "spreadsheet"],
    "Statistics": ["statistics", "statistical analysis", "probability"],
    "Cloud": ["aws", "azure", "gcp", "cloud computing"],
    "Docker": ["docker", "containers"],
    "Git/GitHub": ["git", "github", "version control"],
    "REST APIs": ["rest api", "restful", "api development"],
    "Communication": ["communication", "presentation", "stakeholder"],
    "Project Management": ["project management", "agile", "scrum", "jira"],
    "Cybersecurity": ["cybersecurity", "network security", "penetration testing"],
    "Data Structures": ["data structures", "algorithms", "dsa"],
    "Computer Networks": ["computer networks", "networking", "tcp/ip"],
    "Operating Systems": ["operating systems", "linux", "unix"],
}

def contains_term(text, term):
    # Match whole words where possible, while supporting terms such as c++ and node.js.
    pattern = r"(?<![A-Za-z0-9])" + re.escape(term.lower()) + r"(?![A-Za-z0-9])"
    return re.search(pattern, text.lower()) is not None

def find_skills(text):
    found = []
    for skill, terms in SKILL_GROUPS.items():
        if any(contains_term(text, term) for term in terms):
            found.append(skill)
    return found

st.markdown("""
<style>
.stApp {background: #0b0d12; color: #f4f6f8;}
section[data-testid="stSidebar"] {background: #121722;}
.hero {padding: 1.2rem 1.4rem; border: 1px solid #b8f52b; border-radius: 16px;
       background: linear-gradient(120deg, #151c1d, #10131b);}
.hero h1 {margin-bottom: .35rem; color: #c4ff36;}
.small-note {color: #aab2bf; font-size: .92rem;}
div[data-testid="stMetric"] {background:#151a22; padding: 1rem; border-radius: 12px;
                             border:1px solid #303844;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <h1>🎯 SkillMatch AI</h1>
  <p>Understand how your resume aligns with a job description.</p>
  <p class="small-note">A student-built career assistant prototype. Matching is based on detectable skill keywords.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
with st.sidebar:
    st.header("About")
    st.write("SkillMatch AI helps students compare resume skills with job requirements.")
    st.write("**How it works:** identifies skill keywords in both texts and calculates a simple overlap score.")
    st.caption("Prototype only. It does not make hiring decisions or verify qualifications.")
    st.divider()
    st.write("**Privacy tip:** Use sample text for demos. Avoid entering sensitive personal information.")

left, right = st.columns(2)
with left:
    st.subheader("1. Your resume")
    resume = st.text_area(
        "Paste resume text",
        height=300,
        placeholder="Example: AIML engineering student with Python, SQL, pandas, machine learning and GitHub project experience..."
    )
with right:
    st.subheader("2. Job description")
    job = st.text_area(
        "Paste job description",
        height=300,
        placeholder="Example: Seeking an entry-level data analyst with Python, SQL, Excel, statistics and data visualization skills..."
    )

analyze = st.button("Analyze skill match", type="primary", use_container_width=True)

if analyze:
    if not resume.strip() or not job.strip():
        st.warning("Please enter both resume text and a job description.")
    else:
        resume_skills = set(find_skills(resume))
        job_skills = set(find_skills(job))
        matched = sorted(resume_skills & job_skills)
        missing = sorted(job_skills - resume_skills)
        extra = sorted(resume_skills - job_skills)
        score = round((len(matched) / len(job_skills)) * 100) if job_skills else 0

        st.divider()
        st.header("Your results")
        a, b, c = st.columns(3)
        a.metric("Skill match", f"{score}%")
        b.metric("Required skills detected", len(job_skills))
        c.metric("Skills matched", len(matched))

        if not job_skills:
            st.info("We couldn't detect supported skill keywords in the job description. Try including specific skills such as Python, SQL, Excel, or machine learning.")
        elif score >= 75:
            st.success("Strong keyword overlap. Review the role requirements and tailor your resume to the job.")
        elif score >= 45:
            st.info("Some overlap found. Focus on the missing skills that are genuinely relevant to the role.")
        else:
            st.warning("Limited keyword overlap. Check whether the role fits your current skills and learning goals.")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("✅ Matched skills")
            if matched:
                for item in matched:
                    st.write(f"- {item}")
            else:
                st.write("No supported skills matched yet.")
        with col2:
            st.subheader("📚 Skills to consider developing")
            if missing:
                for item in missing:
                    st.write(f"- {item}")
            else:
                st.write("No missing supported skills detected.")

        st.subheader("💡 Suggested next steps")
        suggestions = []
        if missing:
            suggestions.append("Choose one or two missing skills that are important for the role and learn them through a small practical project.")
            suggestions.append("If you already have a listed skill, make your resume evidence specific—for example, name the project where you used it.")
        if matched:
            suggestions.append("Move the most relevant matched skills and project examples nearer the top of your resume.")
        suggestions.append("Tailor your resume honestly to the job description; do not add skills or experience you do not have.")
        for suggestion in suggestions:
            st.write(f"- {suggestion}")

        with st.expander("Show detected skills and calculation"):
            st.write("**Skills detected in resume:**", ", ".join(sorted(resume_skills)) or "None")
            st.write("**Skills detected in job description:**", ", ".join(sorted(job_skills)) or "None")
            st.write("**Calculation:** matched detected job skills ÷ detected job skills × 100.")
            st.caption("This is a simple keyword-overlap score, not a measure of overall employability or a trained AI prediction.")

st.divider()
st.caption("SkillMatch AI • Hackathon MVP • Built for learning and career preparation")
