import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



st.title('4k Alliance Chama Group 2024 Financial Analysis.')
st.write('Our vision: is to create a community where members collaborate, learn, and thrive financially. We envision a future where every member achieves their financial goals through collective effort and smart investments.')
st.caption('_financial statements as of December 2024_')
st.divider()

st.subheader('Members')

df =  pd.DataFrame({
    'Name':["Victor Kisala","Silvia Nafula","Wilson Kombwa,","Christine Sikolia","Grace Nyongesa","	Gloria ","Everly kavosa","Bromley Onzere",	"Janeti ",	"Kevin Anguche", 'Salome Atieno','Susan'
],
    'Status':['Active', 'Active','Active', 'Inactive', 'Active','Inactive', 'Active', 'Active', 'Active' , 'Active', 'Active', 'Active' ]
})
st.table(df)
st.divider()
st.subheader('Members Contributions')
st.write('Members contribute 4,000 Kenya shillings on a monthly basis.')

df2 =  pd.DataFrame(
    {'Name':["Victor Kisala","Silvia Nafula","Wilson Kombwa,","Christine Sikolia","Grace Nyongesa","	Gloria ","Everly kavosa","Bromley Onzere",	"Janeti ",	"Kevin Anguche", 'Salome Atieno', 'Susan'],
     'Amount':[ 6000,5000, 4000, 4000, 2000, 2000, 5000, 5000, 1000, 4000,2000 , 2000]

    }
)
st.table(df2)
st.divider()

st.write('Financial Statistics ')

df3 =  pd.DataFrame({
    'Name':["Victor Kisala","Silvia Nafula","Wilson Kombwa","Christine Sikolia","Grace Nyongesa","	Gloria ","Everly kavosa","Bromley Onzere",	"Janeti ",	"Kevin Anguche", 'Salome Atieno','Susan'],

    'Amount_Received': [55000, 40000, 36000,  39500,20000, 6000, 39000, 40000, 10000, 40000, 20000, 20000 ],
    'Pending Amount': [0,0, 0,500, 0,0,1000,0, 0, 0, 0,0]

})
st.table(df3)


Amount_Received = [55000, 40000, 36000,  39500, 20000, 6000, 39000, 40000, 10000, 40000, 20000, 20000 ]
colors =  plt.cm.Paired.colors[:11]
fig,ax =  plt.subplots()
ax.pie(
    Amount_Received,
    labels=[f'{amt}' for amt in Amount_Received],

    colors = colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'width': 0.2}

)
ax.set_title('Amount Received By Members')
st.pyplot(fig)

st.divider()
st.subheader('Metrics')
Total_Amount_Distributed = [55000, 40000, 36000,  39500, 20000, 6000, 39000, 40000, 10000, 40000, 20000, 20000 ]
total =  sum(Total_Amount_Distributed)
st.metric('Total Amount Distributed:', f'KES {total}',  delta=None)
percentage = "97.68%"
st.metric('Contribution Percentage: ', percentage)

st.subheader('Members contributions Percentage')

data =  {
     'Name':["Victor Kisala","Silvia Nafula","Wilson Kombwa","Christine Sikolia","Grace Nyongesa","	Gloria ","Everly kavosa","Bromley Onzere",	"Janeti ",	"Kevin Anguche", 'Salome Atieno','Susan'],

    'Amount Received': [55000, 40000, 36000,  39500,20000, 6000, 39000, 40000, 10000, 40000, 20000, 20000 ],
}

df4 =  pd.DataFrame(data)
total_contributions =  df4 ['Amount Received'].sum()

# calculate the percentage of each member and add
df4['Percenatge of The Total'] = (df4['Amount Received'] / total)* 100


st.table(df4)
st.divider()
st.write('From chairmans desk:👨‍⚖️')
st.markdown(
    """Thank you all members  for your unwavering commitment throughout the year We hope next year we will be bigger and better
    merry christmas 🎄🎄"""
)
st.write('You can download our constitution for further guidance ')
pdf_path =  '/stream/4K_ALLIANCE_CHAMA_GROUP est 2024.pdf'
with open(pdf_path, 'rb') as pdf_file:
    st.download_button(
        label='Our constitution ',
        data=pdf_file,
        file_name='4K_ALLIANCE_CHAMA_GROUP est 2024.pdf',
        mime='application/pdf'
    )