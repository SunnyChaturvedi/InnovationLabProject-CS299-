import streamlit as st
from PIL import Image
st.title("--------- Denomination Detector ---------")
st.write("made as a part of CS299 by Sunny Chaturvedi(1801CS54) and Sohail Yadav(1801CS49)")
st.header("Classifies 6 types of Indian Currency Denominations\n 10, 20, 50, 100, 500, 1000")
st.text("Upload image of Indian Currency note in jpg format")

from img_classification import currency_classification

uploaded_file = st.file_uploader("upload here",type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Note', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    st.write("Just a minute")
    label = currency_classification(image, 'model.h5')
    switcher = {
             0 : "fifty", 
             1: "fivehundred",
             2: "hundred",
             3: "ten",
             4:"thousand",
             5:"twenty"
    }
    s=switcher.get(label, "Not Maching")
    st.write("Done..")
    if s=="Not Maching":
        st.write("Enter valid Image")
    else :
        st.write("This is ", s," rupees note")
    