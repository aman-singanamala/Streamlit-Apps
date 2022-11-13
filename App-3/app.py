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
        st.image("./Images/Dhanurasana.png")
        
with c2:
    st.subheader("Bhujangasana")
    with st.expander("Bhujangasana"):
        st.image("./Images/Bhujangasana.png")       
with c3:
    st.subheader("Padmasana")
    with st.expander("Padmasana"):
        st.image("./Images/Padmasana.png")
        
# Row-2
with d1:
    st.subheader("Utthita Parsvakonasana")
    with st.expander("Utthita Parsvakonasana"):
        st.image("./Images/Utthita Parsvakonasana.png")
with d2:
    st.subheader("Surya Namaskar")
    with st.expander("Surya Namaskar"):
        st.image("./Images/Surya Namaskar.png")
with d3:
    st.subheader("Siddhasana")
    with st.expander("Siddhasana"):
        st.image("./Images/Siddhasana.png")

# Row-3
with e1:
    st.subheader("Vrikshasana (Tree Pose)")
    with st.expander("Vrikshasana (Tree Pose)"):
        st.image("./Images/Vrikshasana.png") 
with e2:
    st.subheader("Baddha Konasana")
    with st.expander("Baddha Konasana"):
        st.image("./Images/Baddha Konasana.png")    
with e3:
    st.subheader("Utkatasana")
    with st.expander("Utkatasana"):
        st.image("./Images/Utkatasana.png")