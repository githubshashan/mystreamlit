import streamlit as st
st.set_page_config(page_title='mystreamlit',page_icon='random')
mymenu=st.sidebar.selectbox('My menu',('Home','FillForm','Downloads'))
st.image('https://onleitechnologies.com/wp-content/uploads/2021/12/Untitled_design__6_-removebg-preview-1-150x84.png')
st.title('onlie technologies')
st.header('by xyz')
st.text('this is a tu torial on streamlit library')
if(mymenu=='Home'):
    st.markdown('<center><h1>welcome</h1></center>',unsafe_allow_html=True)
    st.video('https://www.youtube.com/watch?v=9tYXyhLnqI0')
elif(mymenu=='FillForm'):
    with st.form('my form'):
        name=st.text_input('enter name')
        dob=st.date_input("choose date of birth")
        marks=st.slider('Marks')
        k=st.form_submit_button("submit form")
        if k:
            st.write('Name=',name,'DOB:',dob,'Marks:',marks)

elif(mymenu=='Downloads'):
    st.header("Downloads")
    st.download_button('download now','hello this is the downloaded data','onlei.txt')
    
