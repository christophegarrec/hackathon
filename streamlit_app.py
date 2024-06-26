import streamlit as st
import random

# Create three columns with specified width proportions
col1, col2, col3 = st.columns([1, 2, 1])

# Initialize session state for button press count if not already done
if 'button_press_count' not in st.session_state:
    st.session_state.button_press_count = 0

# Column 1 for fitness data
with col1:
    st.header("🏃 Fitness Data")  # Added space after emoji for consistency

    # Generate random values for each refresh
    steps = random.randint(2000, 10000)  # Realistic range for daily steps
    sleep_length = round(random.uniform(6.0, 9.0), 1)  # Realistic range for sleep in hours
    cal_burn = random.randint(1800, 3500)  # Realistic calorie burn range for a day

    # Display metrics with emojis as icons
    st.metric(label="👟 Steps taken", value=f"{steps} steps")
    st.metric(label="🌙 Sleep duration", value=f"{sleep_length} hours")
    st.metric(label="🔥 Calories burned", value=f"{cal_burn} calories")

    # Button to increment the press count
    if st.button('Press me'):
        st.session_state.button_press_count += 1
    
    # Display the current count
    st.write(f"Button has been pressed {st.session_state.button_press_count} times.")

# Column 2 for injury rehab plan
with col2:
    st.header("🩹 Injury Rehab Plan")
    st.write("""
        ### Day 1: Gentle Range of Motion
        - Focus on slowly moving the injured joint through the full range of motion.
        - Do three sets of ten repetitions, twice a day.
    """)

# Column 3 for motivational quotes
with col3:
    st.header("💪 Motivation for the Day")
    st.write("“It does not matter how slowly you go as long as you do not stop.” – Confucius")

# Additional customization can be added here as needed
