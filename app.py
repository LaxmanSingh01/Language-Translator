import textblob
import streamlit as st

# f1 = 'TextBlob is a great tool for developers'

# blob = textblob.TextBlob(f1)
# # print(blob.translate(to='hi'))

st.title('Language Translator')

user_menu=st.selectbox('Select the language',('Hindi','English','French','Spanish','German','Telugu','Marathi','Italian','Punjabi','Bangla','Russian'))

input=st.text_area('Please enter the text')


if user_menu == 'Hindi':
    blob_hi= textblob.TextBlob(input)
    if st.button('Convert'):
        st.subheader(blob_hi.translate(to='hi'))

if user_menu == 'English':
    blob_hi= textblob.TextBlob(input)
    if st.button('Convert'):
        st.subheader(blob_hi.translate(to='en'))

if user_menu == 'French':
    blob_hi= textblob.TextBlob(input)
    if st.button('Convert'):
        st.subheader(blob_hi.translate(to='fr'))

if user_menu == 'Spanish':
    blob_hi= textblob.TextBlob(input)
    if st.button('Convert'):
        st.subheader(blob_hi.translate(to='es'))

if user_menu == 'German':
    blob_hi= textblob.TextBlob(input)
    if st.button('Convert'):
        st.subheader(blob_hi.translate(to='de'))

if user_menu == 'Telugu':
    blob_hi= textblob.TextBlob(input)
    if st.button('Convert'):
        st.subheader(blob_hi.translate(to='te'))

if user_menu == 'Marathi':
    blob_hi= textblob.TextBlob(input)
    if st.button('Convert'):
        st.subheader(blob_hi.translate(to='mr'))

if user_menu == 'Bangla':
    blob_hi= textblob.TextBlob(input)
    if st.button('Convert'):
        st.subheader(blob_hi.translate(to='bn'))

if user_menu == 'Russian':
    blob_hi= textblob.TextBlob(input)
    if st.button('Convert'):
        st.subheader(blob_hi.translate(to='ru'))

if user_menu == 'Italian':
    blob_hi= textblob.TextBlob(input)
    if st.button('Convert'):
        st.subheader(blob_hi.translate(to='it'))

if user_menu == 'Punjabi':
    blob_hi= textblob.TextBlob(input)
    if st.button('Convert'):
        st.subheader(blob_hi.translate(to='pa'))

# if user_menu == 'Sanskrit':
#     blob_hi= textblob.TextBlob(input)
#     if st.button('Convert'):
#         st.subheader(blob_hi.translate(to='san'))



