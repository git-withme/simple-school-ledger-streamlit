import streamlit as st
import pandas as pd

# Initial dummy data
data = {
    "Roll No.": [1, 2, 3],
    "Student Name": ["Aditi Sharma", "Rohan Verma", "Priya Singh"],
    "Class": ["5th", "6th", "5th"],
    "Total Fees": [10000, 12000, 10000],
    "Fees Paid": [6000, 12000, 5000],
    "Balance Due": [4000, 0, 5000],
    "Payment Date": ["01-Apr-2025", "02-Apr-2025", "03-Apr-2025"]
}

# Convert to DataFrame
ledger_df = pd.DataFrame(data)

# Streamlit UI
st.title("🏫 Simple School Ledger")

st.subheader("📋 Student Fee Details")
st.dataframe(ledger_df, use_container_width=True)

st.subheader("➕ Add New Student Entry")

with st.form(key="add_form"):
    roll_no = st.number_input("Roll No.", min_value=1, step=1)
    name = st.text_input("Student Name")
    student_class = st.text_input("Class")
    total_fees = st.number_input("Total Fees", min_value=0, step=500)
    fees_paid = st.number_input("Fees Paid", min_value=0, step=500)
    payment_date = st.date_input("Payment Date")
    
    submit_button = st.form_submit_button(label="Add Entry")
    
    if submit_button:
        balance_due = total_fees - fees_paid
        
        new_row = {
            "Roll No.": roll_no,
            "Student Name": name,
            "Class": student_class,
            "Total Fees": total_fees,
            "Fees Paid": fees_paid,
            "Balance Due": balance_due,
            "Payment Date": payment_date.strftime("%d-%b-%Y")
        }
        
        ledger_df = pd.concat([ledger_df, pd.DataFrame([new_row])], ignore_index=True)
        
        st.success(f"Added entry for {name} successfully!")
        st.dataframe(ledger_df, use_container_width=True)
