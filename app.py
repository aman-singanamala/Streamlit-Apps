import streamlit as st

st.set_page_config(layout='wide')
st.header("Reference for Yoga Poses")

c1 , c2 , c3= st.columns(3)
d1 , d2 , d3= st.columns(3)
e1, e2, e3 = st.columns(3)

# Row-1
with c1:
    st.subheader("Dhanurasana")
    with st.expander("Dhanurasana"):
        #st.image("./Images/Dhanurasana.png")
        st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://raw.githubusercontent.com/aman-singanamala/Streamlit-Apps/main/Yoga-Poses-App/Images/Dhanurasana.png" />
    </a>''',
    unsafe_allow_html=True)
        
with c2:
    st.subheader("Bhujangasana")
    with st.expander("Bhujangasana"):
        st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://raw.githubusercontent.com/aman-singanamala/Streamlit-Apps/main/Yoga-Poses-App/Images/Baddha%20Konasana.png" />
    </a>''',
    unsafe_allow_html=True)
    
         
with c3:
    st.subheader("Padmasana")
    with st.expander("Padmasana"):
        st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://raw.githubusercontent.com/aman-singanamala/Streamlit-Apps/main/Yoga-Poses-App/Images/Padmasana.png" />
    </a>''',
    unsafe_allow_html=True)
        
        
# Row-2
with d1:
    st.subheader("Utthita Parsvakonasana")
    with st.expander("Utthita Parsvakonasana"):
        st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://raw.githubusercontent.com/aman-singanamala/Streamlit-Apps/main/Yoga-Poses-App/Images/Utthita%20Parsvakonasana.png" />
    </a>''',
    unsafe_allow_html=True)
        
        
with d2:
    st.subheader("Surya Namaskar")
    with st.expander("Surya Namaskar"):
        st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://raw.githubusercontent.com/aman-singanamala/Streamlit-Apps/main/Yoga-Poses-App/Images/Surya%20Namaskar.png" />
    </a>''',
    unsafe_allow_html=True)
       
with d3:
    st.subheader("Siddhasana")
    with st.expander("Siddhasana"):
        st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://raw.githubusercontent.com/aman-singanamala/Streamlit-Apps/main/Yoga-Poses-App/Images/Siddhasana.png" />
    </a>''',
    unsafe_allow_html=True)
        

# Row-3
with e1:
    st.subheader("Vrikshasana (Tree Pose)")
    with st.expander("Vrikshasana (Tree Pose)"):
        st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://raw.githubusercontent.com/aman-singanamala/Streamlit-Apps/main/Yoga-Poses-App/Images/Vrikshasana.png" />
    </a>''',
    unsafe_allow_html=True)
        
with e2:
    st.subheader("Baddha Konasana")
    with st.expander("Baddha Konasana"):
        st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://raw.githubusercontent.com/aman-singanamala/Streamlit-Apps/main/Yoga-Poses-App/Images/Baddha%20Konasana.png" />
    </a>''',
    unsafe_allow_html=True)
        
with e3:
    st.subheader("Utkatasana")
    with st.expander("Utkatasana"):
        st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://raw.githubusercontent.com/aman-singanamala/Streamlit-Apps/main/Yoga-Poses-App/Images/Utkatasana.png" />
    </a>''',
    unsafe_allow_html=True)
       