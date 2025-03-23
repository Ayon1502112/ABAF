import streamlit as st
import pandas as pd

# Title of the app
st.title("Contact Information")

# Hardcoded contact details in a dictionary
data = {
    "Name": ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown"],
    "Phone Number": ["+1-123-456-7890", "+1-987-654-3210", "+1-555-666-7777", "+1-888-999-0000"],
    "Email": ["john.doe@example.com", "jane.smith@example.com", "alice.johnson@example.com", "bob.brown@example.com"]
}

# Convert dictionary to DataFrame
contacts_df = pd.DataFrame(data)

# Display the table
st.dataframe(contacts_df)
