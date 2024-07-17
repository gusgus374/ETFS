import streamlit as st

st.title("cold")


if st.button("snow"):
    st.write(":cold_face:")
    st.snow()


if st.button("Summer"):
    st.write(":surfer:")
    st.write(":sun_with_face:")
    st.write(":woman-swimming:")
    
if st.button("goodmorning"):
    st.write(":coffee:")
    st.write(":house_buildings:")
    st.write(":woman-lifting-weights:")
 
   
    
if st.button("eat your food"):
    st.write(":fried_egg:")
    st.write(":spaghetti:")
    st.write(":ramen:")
    st.write(":curry:")
    st.write(":rice_ball:")
   

if st.button("desserts"):
    st.write(":shaved_ice:")
    st.write(":doughnut:")
    st.write(":cookie:")
    st.write(":chocolate:")
    st.write(":icecream:")

with st.expander("Show Nevaeh's code"):
    st.code(
        body='''
import streamlit as st

st.title("cold")


if st.button("snow"):
    st.write(":cold_face:")
    st.snow()


if st.button("Summer"):
    st.write(":surfer:")
    st.write(":sun_with_face:")
    st.write(":woman-swimming:")
    
if st.button("goodmorning"):
    st.write(":coffee:")
    st.write(":house_buildings:")
    st.write(":woman-lifting-weights:")
 
   
    
if st.button("eat your food"):
    st.write(":fried_egg:")
    st.write(":spaghetti:")
    st.write(":ramen:")
    st.write(":curry:")
    st.write(":rice_ball:")
   

if st.button("desserts"):
    st.write(":shaved_ice:")
    st.write(":doughnut:")
    st.write(":cookie:")
    st.write(":chocolate:")
    st.write(":icecream:")
        ''',
        language="python",
        line_numbers=True
    )