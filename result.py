# import streamlit as st
# import pandas as pd
# import os

# # School Name in the header
# st.set_page_config(page_title="Beacon Valley Grammar School - Result System", layout="wide")
# st.title("Beacon Valley Grammar School - Result Management System")

# # Sidebar Navigation
# st.sidebar.title("Navigation")
# sidebar_option = st.sidebar.radio("Go to", ["Add Result", "View All Results", "Delete Result", "Analytics"])

# # Subjects and max marks
# subjects = {
#     "English": 100,
#     "Urdu": 100,
#     "Math": 100,
#     "Science": 100,
#     "Social Studies": 75,
#     "Islamiat": 75,
#     "Computer": 75
# }

# # Function to calculate grade and percentage
# def calculate_grade(percentage):
#     if percentage >= 90:
#         return "A+"
#     elif percentage >= 80:
#         return "A"
#     elif percentage >= 70:
#         return "B"
#     elif percentage >= 60:
#         return "C"
#     elif percentage >= 50:
#         return "D"
#     else:
#         return "F"

# # Add Result Page
# if sidebar_option == "Add Result":
#     st.subheader("Enter Student Information")
#     name = st.text_input("Student Name")
#     student_class = st.selectbox("Select Class", ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7"])

#     st.subheader("Enter Marks Obtained")
#     marks_obtained = {}
#     total_obtained = 0
#     total_max = sum(subjects.values())

#     for subject, max_marks in subjects.items():
#         marks = st.number_input(f"{subject} (out of {max_marks})", min_value=0, max_value=max_marks, step=1)
#         marks_obtained[subject] = marks
#         total_obtained += marks

#     # Calculate percentage and grade
#     percentage = (total_obtained / total_max) * 100
#     grade = calculate_grade(percentage)

#     # Save Result Button
#     if st.button("Save Result"):
#         if name:
#             new_data = {
#                 "Name": name,
#                 "Class": student_class,
#                 "Total Marks": total_obtained,
#                 "Percentage": f"{percentage:.2f}%",
#                 "Grade": grade
#             }
#             for subject in subjects:
#                 new_data[subject] = marks_obtained[subject]

#             # File for the selected class
#             class_file = f"data/{student_class.lower().replace(' ', '_')}_results.csv"

#             # Load or create class-specific file
#             if os.path.exists(class_file):
#                 df = pd.read_csv(class_file)
#                 df = df.append(new_data, ignore_index=True)
#             else:
#                 df = pd.DataFrame([new_data])

#             # Save to the class-specific file
#             df.to_csv(class_file, index=False)
#             st.success(f"Result for {name} in {student_class} saved successfully!")
#         else:
#             st.warning("Please enter the Student Name.")

# # View All Results Page
# elif sidebar_option == "View All Results":
#     student_class = st.selectbox("Select Class to View Results", ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7"])
    
#     # File for the selected class
#     class_file = f"data/{student_class.lower().replace(' ', '_')}_results.csv"

#     if os.path.exists(class_file):
#         df = pd.read_csv(class_file)
#         st.subheader(f"Results for {student_class}")
#         st.dataframe(df)
#     else:
#         st.info(f"No results available for {student_class}.")

# # Delete Result Page
# elif sidebar_option == "Delete Result":
#     student_class = st.selectbox("Select Class to Delete Results", ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7"])
    
#     # File for the selected class
#     class_file = f"data/{student_class.lower().replace(' ', '_')}_results.csv"

#     if os.path.exists(class_file):
#         df = pd.read_csv(class_file)
#         student_names = df["Name"].tolist()
        
#         # Dropdown for selecting a student to delete
#         student_to_delete = st.selectbox("Select a Student to Delete", student_names)

#         # Delete Button
#         if st.button("Delete Result"):
#             if student_to_delete:
#                 df = df[df["Name"] != student_to_delete]  # Filter out the selected student
#                 df.to_csv(class_file, index=False)
#                 st.success(f"Result for {student_to_delete} in {student_class} has been deleted.")
#             else:
#                 st.warning("Please select a student to delete.")
#     else:
#         st.info(f"No results available for {student_class}.")

# # Analytics Page (Top 3 Students)
# elif sidebar_option == "Analytics":
#     student_class = st.selectbox("Select Class for Analytics", ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7"])

#     # File for the selected class
#     class_file = f"data/{student_class.lower().replace(' ', '_')}_results.csv"

#     if os.path.exists(class_file):
#         df = pd.read_csv(class_file)
        
#         # Calculate total maximum marks (sum of all subject max marks)
#         total_max = sum(subjects.values())
        
#         # Calculate total percentage for each student
#         df['Total Marks'] = df[subjects.keys()].sum(axis=1)
#         df['Percentage'] = (df['Total Marks'] / total_max) * 100

#         # Get Top 3 Students
#         top_3 = df.nlargest(3, 'Percentage')
        
#         st.subheader(f"Top 3 Students in {student_class}")
#         st.dataframe(top_3[['Name', 'Class', 'Total Marks', 'Percentage', 'Grade']])

#         # Average Performance
#         average_percentage = df['Percentage'].mean()
#         st.metric("Average Percentage", f"{average_percentage:.2f}%")

#     else:
#         st.info(f"No results available for {student_class}.")


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

    # Calculate percentage and grade
    percentage = (total_obtained / total_max) * 100
    grade = calculate_grade(percentage)

    # Save Result Button
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

            # File for the selected class
            class_file = f"data/{student_class.lower().replace(' ', '_')}_results.csv"

            # Create the folder if it doesn't exist
            folder_path = os.path.dirname(class_file)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Load or create class-specific file
            if os.path.exists(class_file):
                df = pd.read_csv(class_file)
                df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

            else:
                df = pd.DataFrame([new_data])

            # Save to the class-specific file
            df.to_csv(class_file, index=False)
            st.success(f"Result for {name} in {student_class} saved successfully!")
        else:
            st.warning("Please enter the Student Name.")

# View All Results Page (with ranking and PDF download)
elif sidebar_option == "View All Results":
    student_class = st.selectbox("Select Class to View Results", ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7"])
    
    class_file = f"data/{student_class.lower().replace(' ', '_')}_results.csv"

    if os.path.exists(class_file):
        df = pd.read_csv(class_file)

        # Convert 'Percentage' to float
        df['Percentage'] = df['Percentage'].str.replace('%', '').astype(float)

        # Sort by percentage and assign ranks
        df = df.sort_values(by='Percentage', ascending=False).reset_index(drop=True)
        df['Rank'] = df.index + 1

        # Show the ranked table
        st.subheader(f"Results for {student_class} (Ranked)")
        st.dataframe(df)

        # Download as CSV option
        st.download_button("📥 Download as CSV", df.to_csv(index=False).encode('utf-8'), file_name=f"{student_class}_ranked_results.csv", mime='text/csv')

        # Generate PDF
        html_table = df.to_html(index=False)

        with open("temp_results.html", "w") as f:
            f.write(html_table)

        if st.button("📄 Download as PDF"):
            import pdfkit
            try:
                config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")  # Windows path
                pdfkit.from_file("temp_results.html", "ranked_results.pdf", configuration=config)
                with open("ranked_results.pdf", "rb") as pdf_file:
                    st.download_button("Click to Download PDF", pdf_file, file_name=f"{student_class}_results.pdf", mime='application/pdf')
            except Exception as e:
                st.error("PDF bananay mein masla aaya. Please ensure wkhtmltopdf is installed.")

    else:
        st.info(f"No results available for {student_class}.")

# Delete Result Page
elif sidebar_option == "Delete Result":
    student_class = st.selectbox("Select Class to Delete Results", ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7"])
    
    class_file = f"data/{student_class.lower().replace(' ', '_')}_results.csv"

    if os.path.exists(class_file):
        df = pd.read_csv(class_file)
        student_names = df["Name"].tolist()
        
        student_to_delete = st.selectbox("Select a Student to Delete", student_names)

        if st.button("Delete Result"):
            if student_to_delete:
                df = df[df["Name"] != student_to_delete]
                df.to_csv(class_file, index=False)
                st.success(f"Result for {student_to_delete} in {student_class} has been deleted.")
            else:
                st.warning("Please select a student to delete.")
    else:
        st.info(f"No results available for {student_class}.")

# Analytics Page
elif sidebar_option == "Analytics":
    student_class = st.selectbox("Select Class for Analytics", ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7"])
    class_file = f"data/{student_class.lower().replace(' ', '_')}_results.csv"

    if os.path.exists(class_file):
        df = pd.read_csv(class_file)
        total_max = sum(subjects.values())
        df['Total Marks'] = df[subjects.keys()].sum(axis=1)
        df['Percentage'] = (df['Total Marks'] / total_max) * 100

        top_3 = df.nlargest(3, 'Percentage')
        st.subheader(f"Top 3 Students in {student_class}")
        st.dataframe(top_3[['Name', 'Class', 'Total Marks', 'Percentage', 'Grade']])

        average_percentage = df['Percentage'].mean()
        st.metric("Average Percentage", f"{average_percentage:.2f}%")

    else:
        st.info(f"No results available for {student_class}.")

