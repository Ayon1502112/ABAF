import streamlit as st
import pandas as pd

# URL Buttons
st.columns(2)[0].link_button("🌐 Appsheet", "https://www.appsheet.com/start/1e3ec32d-a687-4a57-af21-cc8524d2f421")
st.columns(2)[1].link_button("🤖 Google Sheet", "https://docs.google.com/spreadsheets/d/19ZHtmylVV4FkXgdePpJAJOjQSb45aiK2Mb6fsqjVjtU/edit?usp=sharing")

# Title
st.title("📞 যোগাযোগের তথ্য")

# Contact info (easily editable)
contacts = [
    {"নাম": "অয়ন", "মোবাইল নাম্বার": "01678-863041 // +880 1996-716061"},
    {"নাম": "আসিফ", "মোবাইল নাম্বার": "01835-272538 // +8801533090060"},
    {"নাম": "অয়ন আম্মা", "মোবাইল নাম্বার": "01720578534 // +880 1948-636595"},
    {"নাম": "আসিফ আম্মা", "মোবাইল নাম্বার": "01301496460"},
    {"নাম": "মাসুদ", "মোবাইল নাম্বার": "016-788-63651"},
    {"নাম": "হিমেল", "মোবাইল নাম্বার": "017-147-12194"},
    {"নাম": "উল্লাস", "মোবাইল নাম্বার": "+880 1987-196753"},
]

# Show contacts as table
df = pd.DataFrame(contacts)
st.dataframe(df, use_container_width=True)
