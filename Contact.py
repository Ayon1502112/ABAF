import streamlit as st
import pandas as pd

# Title of the app
st.title("Contact Information")

# Hardcoded contact details in a dictionary
data = {
    "নাম": ["অয়ন", "আসিফ", "অয়ন আম্মা", "আসিফ আম্মা","মাসুদ","হিমেল","উল্লাস"],
    "মোবাইল নাম্বার": ["01678-863041// +880 1996-716061", "01835-272538 // +8801533090060", "01720578534 // +880 1948-636595", "01301496460","016-788-63651","017-147-12194","+880 1987-196753"]
}

# Convert dictionary to DataFrame
contacts_df = pd.DataFrame(data)

# Display the table
st.dataframe(contacts_df)
