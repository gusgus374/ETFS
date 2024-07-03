import streamlit as st
import streamlit.components.v1 as components

st.title("volleyball skills")
st.header("volleyball is challenging b/c you learn new skills, its also a easy sport and become faster")
#Can you show an example?

components.iframe(src="https://www.youtube.com/embed/9YvP2-YbIFs?si=Bkpmt4wbDHfsq94H&amp;start=187", width = 300)

with st.expander("Show Aynira's code"):
    st.code(
        '''
import streamlit as st
import streamlit.components.v1 as components

st.title("volleyball skills")
st.header("volleyball is challenging b/c you learn new skills, its also a easy sport and become faster")
#Can you show an example?

components.iframe(src="https://www.youtube.com/embed/9YvP2-YbIFs?si=Bkpmt4wbDHfsq94H&amp;start=187", width = 300)
''', language='python',line_numbers=True
    )

