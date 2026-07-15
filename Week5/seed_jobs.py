from app import app
from extension import db
from models import Job

jobs = [

    {
        "company_name": "Google",
        "title": "Python Developer",
        "location": "Bangalore",
        "experience": "1-3 Years",
        "salary": "8-12 LPA",
        "skills": "Python, Flask, SQL",
        "description": "Develop scalable backend applications using Flask."
    },

    {
        "company_name": "Microsoft",
        "title": "AI Engineer",
        "location": "Hyderabad",
        "experience": "2-4 Years",
        "salary": "12-18 LPA",
        "skills": "Python, TensorFlow, ML",
        "description": "Build and deploy AI models."
    },

    {
        "company_name": "Amazon",
        "title": "Data Analyst",
        "location": "Chennai",
        "experience": "1-2 Years",
        "salary": "6-10 LPA",
        "skills": "SQL, Excel, Power BI",
        "description": "Analyze business data and generate insights."
    },

    {
        "company_name": "Infosys",
        "title": "Full Stack Developer",
        "location": "Pune",
        "experience": "2-5 Years",
        "salary": "7-14 LPA",
        "skills": "Python, JavaScript, React",
        "description": "Develop full-stack web applications."
    },

    {
        "company_name": "TCS",
        "title": "Cloud Engineer",
        "location": "Mumbai",
        "experience": "2-4 Years",
        "salary": "8-15 LPA",
        "skills": "AWS, Docker, Linux",
        "description": "Manage cloud infrastructure."
    },

    {
        "company_name": "Accenture",
        "title": "Business Analyst",
        "location": "Coimbatore",
        "experience": "1-3 Years",
        "salary": "6-11 LPA",
        "skills": "Requirement Gathering, Agile",
        "description": "Work with stakeholders and teams."
    },

    {
        "company_name": "Zoho",
        "title": "Backend Developer",
        "location": "Chennai",
        "experience": "0-2 Years",
        "salary": "5-9 LPA",
        "skills": "Python, Django, APIs",
        "description": "Develop backend APIs."
    },

    {
        "company_name": "Wipro",
        "title": "DevOps Engineer",
        "location": "Bangalore",
        "experience": "2-5 Years",
        "salary": "9-16 LPA",
        "skills": "Docker, Jenkins, AWS",
        "description": "Automate deployment pipelines."
    },

    {
        "company_name": "Cognizant",
        "title": "Machine Learning Engineer",
        "location": "Hyderabad",
        "experience": "1-4 Years",
        "salary": "10-18 LPA",
        "skills": "Python, Scikit-Learn",
        "description": "Build machine learning solutions."
    },

    {
        "company_name": "HCL",
        "title": "Frontend Developer",
        "location": "Noida",
        "experience": "1-3 Years",
        "salary": "5-10 LPA",
        "skills": "HTML, CSS, JavaScript",
        "description": "Create responsive user interfaces."
    },

    {
        "company_name": "IBM",
        "title": "Cyber Security Analyst",
        "location": "Bangalore",
        "experience": "2-5 Years",
        "salary": "9-17 LPA",
        "skills": "Security, SIEM, Linux",
        "description": "Monitor and secure systems."
    },

    {
        "company_name": "Capgemini",
        "title": "UI UX Designer",
        "location": "Chennai",
        "experience": "1-3 Years",
        "salary": "6-12 LPA",
        "skills": "Figma, Adobe XD",
        "description": "Design modern user experiences."
    },

    {
        "company_name": "Oracle",
        "title": "Database Administrator",
        "location": "Hyderabad",
        "experience": "2-6 Years",
        "salary": "10-20 LPA",
        "skills": "SQL, Oracle DB",
        "description": "Manage enterprise databases."
    },

    {
        "company_name": "PayPal",
        "title": "Software Engineer",
        "location": "Bangalore",
        "experience": "1-4 Years",
        "salary": "10-18 LPA",
        "skills": "Java, Python",
        "description": "Develop fintech applications."
    },

    {
        "company_name": "Flipkart",
        "title": "Product Analyst",
        "location": "Bangalore",
        "experience": "1-3 Years",
        "salary": "8-14 LPA",
        "skills": "Analytics, SQL",
        "description": "Improve product decisions using data."
    },

    {
        "company_name": "Swiggy",
        "title": "Data Scientist",
        "location": "Bangalore",
        "experience": "2-5 Years",
        "salary": "12-22 LPA",
        "skills": "Python, ML, Statistics",
        "description": "Build predictive models."
    },

    {
        "company_name": "Zomato",
        "title": "Marketing Analyst",
        "location": "Delhi",
        "experience": "1-3 Years",
        "salary": "6-10 LPA",
        "skills": "Marketing, Analytics",
        "description": "Analyze campaign performance."
    },

    {
        "company_name": "Freshworks",
        "title": "Support Engineer",
        "location": "Chennai",
        "experience": "0-2 Years",
        "salary": "4-8 LPA",
        "skills": "Technical Support",
        "description": "Provide customer support."
    },

    {
        "company_name": "Razorpay",
        "title": "QA Engineer",
        "location": "Bangalore",
        "experience": "1-4 Years",
        "salary": "7-13 LPA",
        "skills": "Testing, Selenium",
        "description": "Ensure software quality."
    },

    {
        "company_name": "Dell",
        "title": "System Engineer",
        "location": "Chennai",
        "experience": "1-4 Years",
        "salary": "7-12 LPA",
        "skills": "Linux, Networking",
        "description": "Manage enterprise systems."
    }
]

with app.app_context():

    for item in jobs:

        db.session.add(Job(**item))

    db.session.commit()

print("Jobs Inserted Successfully")