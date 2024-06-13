import streamlit as st
import xlsxwriter
import numpy as np

st.title("Data Transformation")
uploaded_file = st.file_uploader("Choose a file",type={"csv"})
if uploaded_file is not None:
    ###### transformation #####################################
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)


    if st.button('Start Processing', help="Process Dataframe"):
        st.header('Addes Column')
        #df['new_col'] = 1
        st.dataframe(df)
        st.balloons()
        import matplotlib.pyplot as plt
        from numpy.random import rand
        fig= plt.figure(figsize=(18,10))
        sns.countplot(x='smoker',data=df,hue='smoker')
        st.pyplot(fig) 
        
        fig2= plt.figure(figsize=(18,10))
        sns.countplot(x='day',data=df, hue ='day' )
        st.pyplot(fig2)

        fig3 = sns.pairplot(df, hue = "day")
        st.pyplot(fig3)

        fig4 = sns.relplot(x="total_bill", y="tip", hue="day",
                col="time", row="sex", data=df)
        st.pyplot(fig4)

        fig5 =plt.figure(figsize=(18,10))
        sns.boxplot(x="day", y="tip", data=df)
        sns.scatterplot(x="total_bill", y="tip", hue="day", data=df)
        st.pyplot(fig5)

        fig6 = sns.jointplot(x='total_bill',y='tip',data=df,kind='reg',height=16)
        st.pyplot(fig6)





        
        import io
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            # Write each dataframe to a different worksheet.
            df.to_excel(writer, index=False)
            # Close the Pandas Excel writer and output the Excel file to the buffer
            writer.close()
            st.download_button(
                label="Download Excel Result",
                data=buffer,
                file_name="trasnformed_file.xlsx",
                mime="application/vnd.ms-excel")
            