import streamlit as st
import pandas as pd
import os

# School Name in the header
st.set_page_config(page_title="Result System", layout="wide")
st.title("Result Management System")

# Sidebar Navigation
st.sidebar.title("Navigation")
sidebar_option = st.sidebar.radio("Go to", ["Add Result", "View All Results", "Delete Result", "Analytics"])

# Subjects and max marks
subjects = {
    "English": 100,
    "Urdu": 100,
    "Math": 100,
    "Science": 100,
    "Social Studies": 75,
    "Islamiat": 75,
    "Computer": 75
}

# Function to calculate grade and percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

# Add Result Page
if sidebar_option == "Add Result":
    st.subheader("Enter Student Information")
    name = st.text_input("Student Name")
    student_class = st.selectbox("Select Class", ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7"])

    st.subheader("Enter Marks Obtained")
    marks_obtained = {}
    total_obtained = 0
    total_max = sum(subjects.values())

    for subject, max_marks in subjects.items():
        marks = st.number_input(f"{subject} (out of {max_marks})", min_value=0, max_value=max_marks, step=1)
        marks_obtained[subject] = marks
        total_obtained += marks

    percentage = (total_obtained / total_max) * 100
    grade = calculate_grade(percentage)

    if st.button("Save Result"):
        if name:
            new_data = {
                "Name": name,
                "Class": student_class,
                "Total Marks": total_obtained,
                "Percentage": f"{percentage:.2f}%",
                "Grade": grade
            }
            for subject in subjects:
                new_data[subject] = marks_obtained[subject]

            class_file = f"data/{student_class.lower().replace(' ', '_')}_results.csv"
            folder_path = os.path.dirname(class_file)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            if os.path.exists(class_file):
                try:
                    df = pd.read_csv(class_file)
                    if not isinstance(df, pd.DataFrame):
                        df = pd.DataFrame()
                except Exception:
                    df = pd.DataFrame()
                df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            else:
                df = pd.DataFrame([new_data])

            df.to_csv(class_file, index=False)
            st.success(f"Result for {name} in {student_class} saved successfully!")
        else:
            st.warning("Please enter the Student Name.")

# View All Results
elif sidebar_option == "View All Results":
    student_class = st.selectbox("Select Class to View Results", ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7"])
    class_file = f"data/{student_class.lower().replace(' ', '_')}_results.csv"

    if os.path.exists(class_file):
        df = pd.read_csv(class_file)
        df['Percentage'] = df['Percentage
