import streamlit as st
import pandas as pd
import openpyxl as OX
import plotly as pl

@st.cache
def get_data(filename):
    tab = pd.read_csv(filename)

    return tab

header =  st.container()
dataset  = st.container()
features = st.container()
tab = get_data('./Data/DATA.csv')
tab_rowcount_QTY = pd.DataFrame(tab['INVOICED_QUANTITY'].value_counts()).head(50)
tab_rowcount = pd.DataFrame(tab['INVOICED_VALUE_NIS'].value_counts()).head(50)

with header:
    st.title('Welcome to streamlit')
    st.header('First part')
    st.subheader('5 lines')
    st.write(tab.head())
    st.subheader('to 50 sales quantity')
    st.markdown(
        """
       <style>
     .main {
     background-color: #FFFFF;

     }

    </style>

        """,
        unsafe_allow_html=True
    )
    
    QTY_NIS=st.selectbox('Quantity or NIs value',options=['Quantity','Nis value'],index=1)
    
    if QTY_NIS== 'Quantity':
        st.subheader('to 50 sales quantity')
        st.bar_chart(tab_rowcount_QTY)
    else:
        st.subheader('to 50 sales value - NIS')
        st.bar_chart(tab_rowcount)    


    st.markdown('*  My first markdown')
    st.markdown('*  My second markdown')

    st.markdown('* **first feature:** this is the explanation')
    st.markdown('* **second feature:** another explanation')

with dataset:
    st.header('Data set')
    st.text('text1')
    st.text('text1')
    


with features:
    st.header('part3')
    st.text('text1')
    st.text('text1')
    sel_col, disp_col =st.columns(2) #create columns
    sel_col.text('Columns in data:')
    sel_col.write(tab.columns)

    








