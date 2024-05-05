import streamlit as st
import pandas as pd
import altair as alt

#st.set_page_config(page_title='University Salaries in Ohio(2011 - Present)',  layout='wide', page_icon=':school:')

#this is the header
t1, t2 = st.columns((0.35,1)) 

t1.image('ohio.jpg', width = 200)
t2.title("University Salaries Charts" )
tab1, tab2 = st.tabs(["Introduction", "Salaries Charts"])

with tab1:
    st.markdown("""
    ## 🎈Welcome to the Higher Education Employee Salaries Explorer!

    🔎This interactive tool allows you to explore average salary trends for different job descriptions in the higher education sector. You can select a specific job description from the sidebar to view the average earnings over time.

    ### 🚀How to Use:

    1. **Select a Job Description:**
    Use the dropdown menu on the sidebar to choose a job description that you're interested in exploring. You can select from various job descriptions available in the dataset.

    2. **Explore the Data:**
    After selecting a job description, the chart will display the average earnings over time for that particular job. If there is only one year of data available for the selected job, the chart will display it as a point. Otherwise, it will show the trend as a line chart.

    ### 💡Insights:
    - Use this tool to analyze salary trends for different job roles within the higher education sector.
    - Compare average earnings across different years for a specific job description.
    - Gain insights into salary patterns and fluctuations over time.

    😇Start exploring the salary trends for higher education job descriptions now!

    --- 
    """)
df = pd.read_csv("higher_ed_employee_salaries.csv")

with tab2:
    # st.dataframe(df)
    df = df.dropna() 
    # group by years and find the mean
    grouped_data = df.groupby(['Year', 'Job Description'])['Earnings'].mean()

    # Resetting the index and renaming columns
    grouped_df = grouped_data.reset_index()
    grouped_df = grouped_df.rename(columns={'Earnings': 'Average Earnings'})

    # Filter out job descriptions with only one year of data
    grouped_df = grouped_df.groupby('Job Description').filter(lambda x: x['Year'].nunique() > 1)

    # Sidebar for selecting job description
    job_description = st.selectbox("Pick your job", grouped_df['Job Description'].unique())

    # Filter data by selected job description
    filtered_df = grouped_df[grouped_df['Job Description'] == job_description]

    # Check the number of years for the selected job
    num_years = filtered_df['Year'].nunique()

    if num_years == 1:  # If only one year, show as points
        mm_chart = alt.Chart(filtered_df).mark_point().encode(
            x='Year',
            y='Average Earnings'
        ).properties(
            title=f"Average Earnings for {job_description} in {filtered_df['Year'].iloc[0]}"
        ).configure_axis(
            labelFontSize=12,  # Adjust font size of axis labels
            titleFontSize=14,  # Adjust font size of axis title
            grid=False,        # Hide grid lines
            domain=True,      # Hide axis lines
            labelColor='black' # Set axis label color to black
        )
    else:  # If multiple years, show as line chart with trend line
        # Line chart
        line_chart = alt.Chart(filtered_df).mark_line().encode(
            x='Year',
            y='Average Earnings'
        )

        # Trend line
        trend_line = line_chart.transform_regression(
            'Year', 'Average Earnings', method='poly', order=3
        ).mark_line(color='lightgray')  # Adjust color to light gray

        # Combine line chart and trend line
        mm_chart = (line_chart + trend_line).properties(
            title=f"Average Earnings Over Time for {job_description}",
            width=600,
            height=400,
        ).configure_axis(
            labelFontSize=12,  # Adjust font size of axis labels
            titleFontSize=14,  # Adjust font size of axis title
            grid=False,        # Hide grid lines
            domain=True,      # Hide axis lines
            labelColor='black' # Set axis label color to black
        )



    # Display the Altair chart
    st.altair_chart(mm_chart)   

    st.markdown('<p style="color: lightgrey;">--：trendline</p>', unsafe_allow_html=True)