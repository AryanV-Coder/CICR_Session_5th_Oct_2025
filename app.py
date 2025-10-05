import streamlit as st

st.title("Student Percentage Calculator")

# Input fields
st.header("Enter Student Information")

name = st.text_input("Enter Student Name:", placeholder="e.g., John Doe")

age = st.slider("Select Student Age:", min_value=5, max_value=100, value=18, step=1)

marks_obtained = st.number_input("Enter Marks Obtained:", min_value=0.0, max_value=1000.0, step=1.0, value=0.0)

total_marks = st.number_input("Enter Total Marks:", min_value=0.0, max_value=1000.0, step=1.0, value=100.0)

# Calculate and display percentage
button = st.button("Calculate Percentage")
if button:
    if name.strip() == "":
        st.warning("Please enter a student name!")
    elif total_marks == 0:
        st.error("Total marks cannot be zero!")
    else:
        percentage = (marks_obtained / total_marks) * 100
        
        st.success(f"**Student Name:** {name}")
        st.success(f"**Marks Obtained:** {marks_obtained}/{total_marks}")
        st.success(f"**Percentage:** {percentage:.2f}%")
        
        # Display grade based on percentage
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"
        
        st.info(f"**Grade:** {grade}")