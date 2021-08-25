
import streamlit as st
import numpy as np

st.title('Prime or not Prime')
num = int(st.number_input('Enter any number:'))
if num > 1:
    for i in range (2,num):
        if (num % i) == 0:
            st.text('Not Prime')
            break
    else:
        st.text('Prime')
else:
    st.text('Not Prime')
