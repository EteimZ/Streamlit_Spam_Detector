#Streamlit GUI for Spam Detector.
import streamlit as st
import joblib
from model import vect, text_process #Importing vect,text_process from model module

loaded_model = joblib.load("spam.sav")

def check(text):
    clean_text = text_process(text)
    in_text = [clean_text]
    text_dtm = vect.transform(in_text)
    result = loaded_model.predict(text_dtm)
    
    return result;

st.title("Spam Detector")

"""
Detect if a message is spam or not.
"""

txt = st.text_area("Enter message:")


mesg = check(txt)

if st.button("Check"):
    if mesg  == 1:
        st.write("**Spam!**")
    else:
        st.write("Not Spam!")
