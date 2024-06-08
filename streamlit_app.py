import streamlit as st

# Create three columns with specified width proportions
col1, col2, col3 = st.columns([1, 2, 1])

# Column 1 for fitness data
with col1:
    st.header("Fitness Data")
    # Assuming these variables are fetched or computed elsewhere in your code
    steps = 5000  # Example data, replace with actual data fetching logic
    sleep_length = 7.5  # Example data
    cal_burn = 300  # Example data

    # Using cards to make the data stand out
    st.metric(label="Steps taken", value=f"{steps} steps")
    st.metric(label="Sleep duration", value=f"{sleep_length} hours")
    st.metric(label="Calories burned", value=f"{cal_burn} calories")

# Column 2 for injury rehab plan
with col2:
    st.header("Injury Rehab Plan")
    st.write("""
        ## Day X 
        ### Gentle Range of Motion
        - Focus on slowly moving the injured joint through the full range of motion.
        - Do three sets of ten repetitions, twice a day.

    """)

# Column 3 for motivational quotes
with col3:
    st.header("Motivation for the Day")
    st.write("“It does not matter how slowly you go as long as you do not stop.” – Confucius")

# Additional customization can be added here as needed
