import pandas as pd
import streamlit as st
import altair as alt

# Layout
t1, t2 = st.columns((0.45, 1))
t1.image('ohio.jpg', width=200)
t2.title("Compensation Compare")

tab1, tab2 = st.tabs(["Introduction", "Compensation Analytics"])

with tab1:
    st.write("""
    ### Welcome to the University Employee Salaries Explorer!          
    ### This interactive tool allows you to explore salary data for higher education employees. 
    """)

    st.markdown("### 🚀How to Use:")
    st.markdown("""
    1. **Choose a School:**
    Use the dropdown menu to select a specific school.
    2. **Filter by Job:**
    Narrow down your search by selecting a job description from the sidebar.
    3. **Explore the Data:**
    The app will display filtered data based on your selections, showing information such as earnings, minimum, maximum, and mean earnings for the selected school and job role. You'll also see the percentage of employees earning higher than the mean salary.
    """)

    st.markdown("### Note:")
    st.markdown("""
    If you encounter an error message stating "🔎Sorry, this school does not offer this position currently," it means there is no data available for the selected combination of school and job role.

    💡Feel free to adjust the filters and explore different combinations to gain insights into higher education employee salaries!
    """)

# Load dataset
salary_df = pd.read_csv('higher_ed_employee_salaries.csv')

with tab2:
    selected_school = st.selectbox('Choose a School', options=salary_df['School'].unique().tolist(), help='Filter report to show only one school')
    selected_job = st.selectbox('Choose a Job', options=salary_df['Job Description'].unique().tolist())

    if selected_school != '' and selected_job != '':
        filtered_data = salary_df[(salary_df['School'] == selected_school) & (salary_df['Job Description'] == selected_job)]

        # Calculate statistics
        earnings_min = filtered_data['Earnings'].min()
        earnings_max = filtered_data['Earnings'].max()
        earnings_mean = filtered_data['Earnings'].mean()
        earnings_median = filtered_data['Earnings'].median()

        total = len(filtered_data)
        if total == 0:
            earnings_min = '--'
            earnings_max = '--'
            earnings_mean = '--'
            percentage_higher_than_mean = '--'
            earnings_median = '--'
            st.error("🔎Sorry, this school does not offer this position currently.")
        else:
            higher_than_mean = filtered_data[filtered_data['Earnings'] > earnings_mean].shape[0]
            below_than_mean = total - higher_than_mean
            percentage_higher_than_mean = (higher_than_mean / total) * 100

            # Display statistics
            st.header('Statistics of Earnings')
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                if earnings_min != '--':
                    st.metric(label='Minimum Earnings', value=f"{earnings_min:.2f}")
                else:
                    st.metric(label='Minimum Earnings', value=earnings_min)
            with col2:
                if earnings_max != '--':
                    st.metric(label='Maximum Earnings', value=f"{earnings_max:.2f}")
                else:
                    st.metric(label='Maximum Earnings', value=earnings_max)
            with col3:
                if earnings_median != '--':
                    st.metric(label='Median Earnings', value=f"{earnings_median:.2f}")
                else:
                    st.metric(label='Median Earnings', value=earnings_median)
            with col4:
                if earnings_mean != '--':
                    st.metric(label='Mean Earnings', value=f"{earnings_mean:.2f}", delta=f"{percentage_higher_than_mean:.2f}% Higher", delta_color="inverse")
                else:
                    st.metric(label='Mean Earnings', value=earnings_mean)
            
            # Create a histogram to visualize the distribution of earnings
            histogram_chart = alt.Chart(filtered_data).mark_bar(color ='darkblue').encode(
                alt.X('Earnings', bin=True, title='Earnings'),
                alt.Y('count()', title='Frequency')
            ).properties(
                width=600,
                height=400
            ).configure_axis(
                labelFontSize=12,
                titleFontSize=14,
                grid=False,
                domain=True,
                labelColor='black'
            ).properties(
                title='Distribution of Earnings'
            )

            # Display the histogram
            st.altair_chart(histogram_chart)
