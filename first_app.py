#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('toy_dataset.csv')
df_MW = df[df['City']=="Mountain View"]

st.write("Here is my first graph:")
st.dataframe(df_MW)

st.subheader("Bar chart of Income in Mountain View")
fig = px.bar(df_MW, x = "Gender", y = "Income")
st.plotly_chart(fig)


# In[ ]:





# In[ ]:




