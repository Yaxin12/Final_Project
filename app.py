import streamlit as st
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

st.set_page_config(page_title='University Employee Salaries in Ohio(2011 - Present)',  layout='wide', page_icon=':school:')


show_pages(
    [
        Page("app.py", "Project Introduction", "💻"),


        Section("University Employee Salaries", "🧙‍♂️"),
        Page("college.py", "University Explorer", ":school:", in_section=True),
        Page("salary_compare.py", "Salaries Compare", "💰", in_section=True),
        Page("linechart.py", "Salaries Linechart", ":chart:", in_section=True)
    ]
)
#this is the header
t1, t2 = st.columns((0.35,1)) 

t1.image('ohio.jpg', width = 200)
t2.title("University Employee Salaries in Ohio(2011 - Present)")

st.image("CollegeProfessor_1920x1080.jpg")
# Introduction
tab1, tab2 = st.tabs(["Project Introduction", "Dataset Source"])

with tab1: 
    st.markdown("""
    #### 🔎Exploring Higher Education Employee Salaries in Ohio

    Most universities are public institutions that receive government oversight and financial support. As public entities, their financial status and expenditures need to be transparent to ensure the reasonable use of taxpayers' funds. Publicizing the salaries of university employees helps ensure fairness and transparency in the compensation system. A transparent salary system can reduce potential discrimination and bias, while providing employees with a clear understanding of their compensation, thus enhancing internal fairness and trust within the organization. Making salary information public can also aid universities in recruiting and retaining talent, as some prospective employees may consider salary information when deciding whether to apply for or accept a position. Moreover, employees' awareness of their salary status within the institution helps universities remain competitive and attract and retain high-quality faculty and staff. Despite this information being publicly available online, it's often not convenient for comparison.

    Therefore, this tool aims to delve into the salaries of higher education employees from Ohio's public universities dating back to 2011 and visualize this data. Through such efforts, we aim to provide users with an easy way to access useful information. This will help government, media, and the public monitor the financial management and expenditure of universities, provide deeper insights into professional salaries for faculty and staff, and offer valuable information support for those intending to work in Ohio.

    In doing so, we can continually pursue transparency and fairness while providing more beneficial services to university administrators, faculty, staff, and job seekers.
    """)

with tab2:
    st.image("The_Buckeye_Institute_Logo.png")
    st.markdown("##### 👨‍🔧 Data come from [Buckeye Institute](https://www.buckeyeinstitute.org/about/)")
    st.markdown("""
    ### 📓 About Buckeye Institute
                
    Founded in 1989, The Buckeye Institute is an independent research and educational institution—a think tank—whose mission is to advance free-market public policy in the states.
   
    The staff at Buckeye accomplish the organization’s mission by performing timely and reliable research on key issues, compiling and synthesizing data, formulating sound free-market policies, and promoting those solutions for implementation in Ohio and replication across the country.
    
    The Buckeye Institute is located directly across the street from the Ohio Statehouse on Capitol Square in Columbus, where it assists legislative and executive branch policymakers by providing ideas, research, and data to enable the lawmakers’ effectiveness in advocating free-market public policy solutions.
    
    The Buckeye Institute is a non-partisan, non-profit, and tax-exempt organization, as defined by section 501(c)(3) of the Internal Revenue code. As such, it relies on support from individuals, corporations, and foundations that share a commitment to individual liberty, free enterprise, personal responsibility, and limited government. The Buckeye Institute does not seek or accept government funding.
    """)