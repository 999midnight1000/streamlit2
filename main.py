import streamlit as st

#Title
st.title("App")

#add text
st.write("memento mori")

#Text input
name = st.text_input("Enter your name: ")
#num input
age = st.number_input("Age: ")

#Display a message when button is clicked
if st.button("Submit"):
    st.write("hello {name}, welcome to app 1")

