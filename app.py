from pathlib import Path
import streamlit as st
from PIL import Image


#path settings                      
current_dir= Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file= current_dir/"styles"/"main.css"
resume_file= current_dir/"assets"/"cv.pdf"
profile_pic= current_dir/"assets"/"profile-pic.png"

#general settings

page_title ="Digital CV | Mohan"
page_icon = ":wave:"
name= "Mohan"
description= """Data Analyst, assisting enterprises by supporting data-driven decision making."""
email="mohain@gmail.com"
social_media={
    "yooutube": "https://youtube.com/",
    "LinkedIn": "",
}
projects= {
    "Dashbouards - Comparing sales across two call agents": "https://youtub/"
    "Desktop Application",
}

st.set_page_config(page_title=page_title,page_icon=page_icon)
st.title("Digital ")

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
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
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
    - 7 years fo experisen form data
    - excellent tem-player
    """
)

#skills
st.write("#")
st.subheader("Hard dkills")
st.write(
    """
    - Programming: python 7 years fo experisen form data
    - Databases: MySQL, MongoDB
    """
)



#work history

st.write("#")
st.subheader("Work History")
st.write("---")

#Job 1
st.write("Senior Data Analyst")
st.write("02/2021 - Present")
st.write(
    """
    - User PowerBI and SQL
    - Redesigned dat model through iterations that improved predictons by 30%
    """
)

#projects and accomplishments
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project,link in projects.items():
    st.write(f"[{project}]({link})")



