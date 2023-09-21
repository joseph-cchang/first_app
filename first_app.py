#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('toy_dataset.csv')
df_MW = df[df['City']=="Mountain View"]

st.write("Here is my first graph:")
st.dataframe(df_MW)

st.subheader("Histogram of Income in Mountain View")
fig = px.scatter(
    df.query("City == Mountain View"), 
    x = "Income Value", 
    y = "Frequency")

st.plotly_chart(fig)

st.pyplot(fig)


# In[ ]:





# In[ ]:




