import streamlit as st
import pandas as pd

df= pd.read_excel("C:\\Users\\Carl\\Housing\\flats_within_wales.xlsx")
st.table(df)