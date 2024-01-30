from pathlib import Path
import streamlit as st
from PIL import Image
                   
css_file= "main.css"
resume_file= "CV.pdf"
profile_pic= "profile-pic.png"

#general settings

page_title ="Digital CV | Mohan"
page_icon = ":wave:"
name= "MohanKumar"
description= """Accomplished BI & Data Analytics Specialist with a robust foundation in computer science, 
showcasing expertise in creating automated solutions. Acknowledged for adeptly leading  BI development, IT support and 
data analyst teams, overseeing comprehensive service delivery, and actively contributing to the conception and execution. 
Proven track record of leveraging technical skills to drive operational efficiency and deliver impactful solutions.
"""
email="mohain@gmail.com"
social_media={
   # "yooutube": "https://youtube.com/",
    "LinkedIn": "https://www.linkedin.com/in/mohankumar-n/",
}
projects= {
    "Dashboards - Live with customer filter and report download": "https://medium.com/@mohain/live-dashboard-using-streamlit-50cd51d62b77"
    "Desktop Application",
}

st.set_page_config(page_title=page_title,page_icon=page_icon)
with st.sidebar:
    st.write("**KEY SKILLS**")
    st.write("""
    ★★★★★ Data Analyst.	
    ★★★★★ BI Developer.
    :	
    Data Visualization   :	★★★★★ 
    Intellectual curiosity:	★★★★★ 
    Analytics Engineer   :	★★★★☆ 
    BI Analyst           :	★★★★☆ 
    IT Service delivery  : 	★★★★☆ 
    Programmer Analyst   :	★★★☆☆
    Incident Mgmt.       :	★★☆☆☆
    Data Engineer        :	★★☆☆☆
    """) 
    st.write("") 
    st.write("**HARD SKILLS**") 
    st.write("""
    - SQL and Database Querying.
    - Data Visualization and Reporting ToolS. 
    - Advanced Excel and Spreadsheet Skills.
    - Programming Skills (e.g., Python).
    - Data Warehousing and ETL Processes.
    """)
    st.write("") 
    st.write("**LANGUAGES**") 
    st.write(
    """
    - English (C1)
    - French (B2)
    - German (B1)
    """
)



st.title(" ")

#load css, pdf & profile pic
with open (css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open (resume_file,"rb") as pdf_file:
    PDFbyte=pdf_file.read()
    profile_pic=Image.open(profile_pic)
    
#hero section
col1,col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic, width =230)

with col2:
    st.title(name)
    st.write(description)
    st.download_button(
        label="Download Resume (Deutsch)",
        data=PDFbyte,
        file_name=resume_file,
        mime="applicaton/octet-stream",
    )
    st.write("...",email)
    
    
#solical links
st.write("#")
cols=st.columns(len(social_media))
for index,(platform,link) in enumerate(social_media.items()):
    cols [index].write(f"[{platform}]({link})")
    
#experience &qualifications
st.write("#")
st.subheader("Experience & Qualificaitons")
st.write(
    """
    - Developed automated solutions for various projects within outlook, MS office....
    - Developed live forecast using live data, trigger emails, automated reports and a live dashboard. 
    - Built automation software to streamline business processes using Robotic desktop automation (RDA) and robotic process automation (RPA).
    - Extensive knowledge of using tools such as Power BI, KNIME, TIBCO Sportfire, Apache Superset, csv and xlsx files and programming language such as Python.
    """
)
# EDUCATION & CREDENTIAL
st.write("#")
st.subheader("EDUCATION & CREDENTIAL")
st.write(
    """
    - Bachelor of Science (Computer science)
    - ITIL V3 Foundation from AXELOS

    """
)

#skills
st.write("#")
st.subheader("Skills")
st.write(
    """
    - Knowledge in Python, DAX, XML, .NET, ASP, VisualBasic...
    - Softwares - SAP SuccessFactors, Adobe Photoshop…..
    - BI tools – KNIME, Power BI, TIBCO Spot fire and Superset
    - Ticketing tools - Clear Quest, Cornerstone and JIRA
    - Database – MySQL, MS SQL Server, DuckDB and MongoDB(Beginner)

    """
)



#work history

st.write("#")
st.subheader("CAREER PROGRESSION")
st.write("---")

#Job 1
st.write("**BI & Data Analytics Specialist** - WebID solutions (Solingen and Hamburg)")
st.write("03/2022 – Present")
st.write(
    """
    - Dashboards for multiple users within using Power BI.
    - Live dashboards for Management team using Apache Superset.
    - Process automation like report generation, email sender…. 
    - Data download, manipulation, refresh and transfer using Python and Excel.
    - Multiple IT related activities on a daily basis.

    """
)

#Job 2
st.write("Project Owner - JuiceUP (Start-up)")
st.write("Dec 2016 – Nov 2018")
st.write(
    """
    - Ideate and implement an automated retail juice vending system 
    - Research the idea, workflow procedure, raise funds for the startup, develop the front design and the back of house setup 
    """
)
st.write("**Subject Matter Expert** - AXA Technologies Shared Services  (Bangalore and Paris)")
st.write("03/2015 – 09/2016")
st.write(
    """
    - Team Lead for IT support and data analyst teams in India.
    - Service delivery Manager for IRIS platform globally. (France, Poland and Spain)
    - A reliable source of information, proactively managing customer’s functional needs into technical specifications 
    - Experience with cross-functional teams and multiple stakeholders
    - Technical specialist and competence in ITSM process and product management.
    """
)

#Job 4
st.write("**BI/Data Analyst**")
st.write("03/2013 – 03/2015")
st.write(
    """
    - A client-facing role, driving the end-to-end implementation of Business Intelligence engagement
    - Delivery management (Delivery Director):
        - Bridge between the programmer and the executor during file execution.
        - Plan and control the delivery on each execution of package(files)
        - Monitor the production server to identify incident.
    -	Information security management:
        - Work on Access management using ITIL standards.
        - Create, provision, delete and manage users, groups and roles for different systems using Active Directory.
        - Manage role assignments in development and pre-production servers
    - Document management:
        - Manage and control all process related documents within shared drive, without external software.
    - Incident Management:
        - Handle L1 and L2 incidents within Data Management team.
        - Identify L3 incidents and assign to production technical team members.
        - Introduced best practices and procedures for faster resolution of Incidents
    """
)

#Job 5
st.write("**Senior Software Engineer**")
st.write("09/2011 – 03/2013")
st.write(
    """
    - Business Intelligence Monitoring and Reporting: 
        - Monitoring the execution of files in production server.
        - Daily reports (SQL Management studio) on the availability of applications.
    - Experience in dealing with system logs, especially network traffic analyzes, payload, event logs, application logs, etc..
    """
)

#Job 6
st.write("**Senior Process Associate** - I Gate (Bangalore)")
st.write("01/2010 – 09/2011")
st.write(
    """
    - Handling online banking and insurance transactions (only individuals) within Canada. 
    """
)

#Job 7
st.write("**Associate** - HSBC (Bangalore)")
st.write("11/2008 – 01/2010")
st.write(
    """
    - Handling multiple online banking transactions (individual and corporate) within France.
    """
)

#Job 8
st.write("**Associate** - Aditya Birla Minacs (Bangalore)")
st.write("07/2008 – 11/2008")
st.write(
    """
    - A typical French call center selling Bank credit cards.
    """
)

#Job 9
st.markdown("**Programmer Analyst** - ADIVA Systems  (Chennai)")
st.write("01/2005 – 12/2005")
st.write(
    """
    - Developer or programmer, coded in .NET, XML, ASP and JavaScript. Queries in SQL and Python. 
    - Knowledge in runtime analysis and procedures for ensuring the correctness of software components (test, validation, verification) in the environment of parallel and distributed systems.

    """
)
