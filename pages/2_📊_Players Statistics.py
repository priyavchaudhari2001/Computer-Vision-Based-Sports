import streamlit as st
import pandas as pd

st.set_page_config(page_title="SPARK", page_icon=":bar_chart:", layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def load_data(uploaded_file):
    file_extension = uploaded_file.name.split('.')[-1]
    if file_extension == 'csv':
        df = pd.read_csv(uploaded_file)
    elif file_extension in ['xls', 'xlsx']:
        df = pd.read_excel(uploaded_file)
    return df


## ------------------------------------------------------------------------------
st.title('Players Statistics 🏏')
st.write('---')

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        sport = st.selectbox('Select Your Sport', ('Cricket', 'Badminton', 'Basketball'))

    with right_column:
        uploaded_file = st.file_uploader('Upload a CSV/Excel file', type=['csv', 'xls', 'xlsx'])

    st.write('---')

    if uploaded_file is not None:
        if sport == 'Cricket':
            df = load_data(uploaded_file)
            if sport == df['Sport'].unique()[0]:
                st.table(df[['Name', 'Role', 'Runs', 'Balls', 'Strike Rate', 'Fours', 'Sixes', 'Boundary % Runs']])
            else:
                st.info(f'Please upload only {sport} sport data.', icon="ℹ️")
        elif sport == 'Badminton':
            df = load_data(uploaded_file)
            if sport == df['Sport'].unique()[0]:
                st.table(df[['Name', 'Age', 'Country', 'Rank', 'Singles Win','Singles Loss', 'Doubles Win', 'Doubles Loss', 'Smash Speed','Serve Accuracy', 'Return Accuracy', 'Net Play Success Rate']])
            else:
                st.info(f'Please upload only {sport} sport data.', icon="ℹ️")
        elif sport == 'Basketball':
            df = load_data(uploaded_file)
            if sport == df['Sport'].unique()[0]:
                st.table(df[['Name', 'Age', 'Position', 'Points', 'Rebounds', 'Assists','Steals', 'Blocks', 'Turnovers', 'FG%', '3P%', 'FT%']])
            else:
                st.info(f'Please upload only {sport} sport data.', icon="ℹ️")
        else:
            st.info('Please select a valid sport.', icon="ℹ️")
    else:
        st.info('Please upload a CSV/Excel file to see the output......', icon="ℹ️")
