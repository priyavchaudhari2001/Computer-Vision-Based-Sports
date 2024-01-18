import streamlit as st

st.set_page_config(page_title="SPARK - The Beginning", page_icon=":bar_chart:",
layout="wide")

st.title('Sports Performance Analytics - Computer Vision :dart:')
st.markdown('Bringing **_Data Science_** onto the field.')
st.write('---')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.image('Images\home2.png')
st.write('---')

st.subheader('Application Description ✅')
st.write('##')
st.markdown("""

●  ***Player Statistics Analysis:*** - It will consist of the player's overall statistics with
multiple graphs showcasing his skills/records. This will
be also useful to get the overall skill/performance of Players.

● ***Team Performance Dashboard:*** - This will contain overall Visualizations for different
modules we will be implementing.

● ***Video Posture Analysis:*** - This shows a video analysis of a particular player using
the help of OpenCV to give an in-depth analysis of a player. """)
