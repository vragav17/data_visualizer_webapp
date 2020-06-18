import os
import streamlit as st

# EDA Pkgs
import pandas as pd
import numpy as np

# Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns

def data_app():
    """ Data Processer and Visualizer  """
    st.title("Data Stories")
    st.subheader("A to Z about Data Analysis")

    file = ['./dataset/Ac1',[0,1]]
    def file_selector():
        filename = st.file_uploader("Upload Excel File", type=['xls','xlsx'])
        if filename is not None:
            sheetnames = pd.ExcelFile(filename).sheet_names
            sheet = st.selectbox("Sheet Sheet", sheetnames)
            return [filename, sheet]

    file = file_selector()




    # Read Data
    try :
        df = pd.read_excel(file[0], sheet_name = file[1])
    except Exception as e:
        st.info("Please upload Excel file")

    # Show Datas

    if st.checkbox("Show Dataset"):
        number = st.number_input("Number of Rows to View",5,10)
        st.dataframe(df.head(number))

# Show Columns
    if st.button("Column Names"):
        st.write(df.columns)

# Show Shape
    if st.checkbox("Shape of Dataset"):
        st.write(df.shape)

# Select Columns
    if st.checkbox("Select Columns To Show"):
        all_columns = df.columns.tolist()
        selected_columns = st.multiselect("Select",all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)

# Show Values
    if st.button("Value Counts"):
        st.text("Value Counts By Target/Class")
        st.write(df.iloc[:,-1].value_counts())


# Show Datatypes
    if st.button("Data Types"):
        st.write(df.dtypes)



# Show Summary
    if st.checkbox("Summary"):
        st.write(df.describe().T)

## Plot and Visualization

    st.subheader("Data Visualization")
# Correlation
# Seaborn Plot
    if st.checkbox("Correlation Plot[Seaborn]"):
        st.write(sns.heatmap(df.corr(),annot=True))
        st.pyplot()


# Pie Chart
    if st.checkbox("Pie Plot"):
        all_columns_names = df.columns.tolist()
        if st.button("Generate Pie Plot"):
            st.success("Generating A Pie Plot")
            st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
            st.pyplot()

# Count Plot
    if st.checkbox("Plot of Value Counts"):
        st.text("Value Counts By Target")
        all_columns_names = df.columns.tolist()
        primary_col = st.selectbox("Primary Columm to GroupBy",all_columns_names)
        selected_columns_names = st.multiselect("Select Columns",all_columns_names)

        if st.button("Plot"):
            st.text("Generate Plot")
            if selected_columns_names:
                vc_plot = df.groupby(primary_col)[selected_columns_names].count()
            else:
                vc_plot = df.iloc[:,-1].value_counts()
            st.write(vc_plot.plot(kind="bar"))
            st.pyplot()

#Contour Plot
    if st.checkbox("Contour Plot "):
        st.text("3D Contour Plot")
        all_columns_names = df.columns.tolist()
        X = st.selectbox("Select X axis",all_columns_names)
        Y = st.selectbox("Select Y axis",all_columns_names)
        VS = st.selectbox("Select Z axis",all_columns_names)


        Z_F = df.pivot_table(index=X, columns=Y, values=VS).T.values

        X_unique = np.sort(df[X].unique())
        Y_unique = np.sort(df[Y].unique())
        X_F, Y_F = np.meshgrid(X_unique, Y_unique)
        pd.DataFrame(Z_F).round(3)
        pd.DataFrame(X_F).round(3)
        pd.DataFrame(Y_F).round(3)

        fig,ax=plt.subplots(1,1)
        cp = ax.contourf(X_F, Y_F, Z_F)
        fig.colorbar(cp) # Add a colorbar to a plot
        st.pyplot(fig=fig)

# Customizable Plot
    try:
        st.subheader("Customizable Plot")
        all_columns_names = df.columns.tolist()
        type_of_plot = st.selectbox("Select Type of Plot",["area","bar","line","hist","box","kde"])
        selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)

        if st.button("Generate Plot"):
            st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

    # Plot By Streamlit
        if type_of_plot == 'area':
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)

        elif type_of_plot == 'bar':
            cust_data = df[selected_columns_names]
            st.bar_chart(cust_data)

        elif type_of_plot == 'line':
            cust_data = df[selected_columns_names]
            st.line_chart(cust_data)

    # Custom Plot
        elif type_of_plot:
            cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
            st.write(cust_plot)
            st.pyplot()

        if st.button("Thanks"):
            st.balloons()
    except:
        st.write("Please upload Excel file")
    st.sidebar.header("Data Stories")
    st.sidebar.info("A to Z about Data Analysis")




    st.sidebar.info("Built by Veera Ragavan")
    

if __name__ == '__main__':
    data_app()
