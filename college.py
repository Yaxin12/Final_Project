import streamlit as st
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#st.set_page_config(page_title='University Employee Salaries Explorer',  layout='wide', page_icon=':school:')



#this is the header
t1, t2 = st.columns((0.35,1)) 

t1.image('ohio.jpg', width = 200)
t2.title("University Employee Explorer")
tab1, tab2 = st.tabs(["Introduction", "Employee Explorer"])

# Description of the app
with tab1:
    st.write("""
    ### 🎈Welcome to the University Employee Salaries Explorer! 
    ### 🔎This app allows you to explore and analyze salary data for university employees.
    #### 🚀How to Use
    1. **Filter by Year:** Select a specific year or choose "All Years" to view data for all years.
    2. **Filter by College:** Select a college or choose "All Colleges" to view data for all colleges.
    3. **Filter by Department:** Select a department or choose "All Departments" to view data for all departments.
    4. **View Jobs and Staff Count:** Once you've selected the filters, the app will display the unique jobs within the selected department, along with the number of staff working in each job.

    💡Feel free to explore and analyze the salary data to gain insights into university employee salaries!
    """)

import pandas as pd
import streamlit as st

salary_df = pd.read_csv('higher_ed_employee_salaries.csv')


with tab2:
    # Get unique values from the "Year" column
    unique_year = salary_df['Year'].unique()
    # Convert unique years to a Python list
    year_list = sorted(unique_year.tolist())
    # Add "All Years" option to the year list
    year_list.insert(0, 'All Years')
    # Create a selectbox for the years
    selected_year = st.selectbox('Select a Year', year_list)

    # Filter the DataFrame based on the selected year
    if selected_year != 'All Years':
        filtered_year_df = salary_df[salary_df['Year'] == selected_year]
    else:
        filtered_year_df = salary_df

    # Get unique values from the "School" column
    unique_colleges = filtered_year_df['School'].unique()
    # Convert unique colleges to a Python list
    college_list = unique_colleges.tolist()
    college_list.insert(0, 'All Colleges')
    # Create a selectbox for the colleges
    selected_college = st.selectbox('Select a College', college_list)
    # Filter the DataFrame based on the selected college
    if selected_college != 'All Colleges':
        filtered_college_df = filtered_year_df[filtered_year_df['School'] == selected_college]
    else:
        filtered_college_df = filtered_year_df

    # Get unique values from the "Department" column
    unique_departments = filtered_college_df['Department'].unique()
    # Convert unique departments to a Python list
    department_list = unique_departments.tolist()
    department_list.insert(0, 'All Dept')
    # Create a selectbox for the departments within the selected college
    selected_department = st.selectbox('Select a Department', department_list)
    # Filter the DataFrame based on the selected department
    if selected_department != 'All Dept':
        filtered_department_df = filtered_college_df[filtered_college_df['Department'] == selected_department]
    else:
        filtered_department_df = filtered_college_df

    # Drop rows where the job description is NaN
    filtered_department_df = filtered_department_df.dropna(subset=['Job Description'])

    # Get unique values from the "Job" column
    unique_jobs = filtered_department_df['Job Description'].unique()
    # Convert unique jobs to a DataFrame
    job_df = pd.DataFrame(unique_jobs, columns=['Jobs'])
    # Center the DataFrame in the middle of the screen
    st.markdown("<h2 style='text-align: center;'>Jobs in {} of {}  {}</h2>".format(selected_department, selected_college, selected_year), unsafe_allow_html=True)

    total_employees = filtered_department_df.shape[0]
    st.write(f"Total number of employees: {total_employees}")

    # Set default number of jobs to display
    default_num_jobs = 12

    # Add dropdown option for more information
    show_more_info = st.checkbox("Show More Information")

    # Create columns to display the metrics for each job
    num_columns = 4
    job_chunks = [unique_jobs[i:i + num_columns] for i in range(0, len(unique_jobs), num_columns)]
    for job_chunk in job_chunks:
        cols = st.columns(len(job_chunk))
        for col, job in zip(cols, job_chunk):
            num_staff = filtered_department_df[filtered_department_df['Job Description'] == job].shape[0]
            if show_more_info:
                col.metric(label=job, value=num_staff)
            else:
                if default_num_jobs > 0:
                    col.metric(label=job, value=num_staff)
                    default_num_jobs -= 1