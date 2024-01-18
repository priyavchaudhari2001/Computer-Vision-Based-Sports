import streamlit as st
import numpy as np
import tempfile
import time

# VIDEO_1 = 'E:/Data Analyst Journey/5. Streamlits Web Apps/8. BE Final Year Project/Datasets/Cric_.mp4'

st.set_page_config(page_title="SPARK - The Beginning", page_icon=":bar_chart:",
layout="wide")

st.title('Video Analytics 🏀')
st.write('---')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------------------------
col1, col2 = st.columns(2)

video_pose = col1.selectbox('Select Input Video',['Cricket','Badminton','Exercise','Basketball'])

if video_pose == "Cricket":
    # Allow the user to upload a file in the second column
    option = col1.radio("Select Video Type", ("Cricket Side Posture", "Cricket Front Posture"),horizontal = True)
    uploaded_file = col2.file_uploader("Upload your custom video")

    if uploaded_file is not None:

        run = st.button('Run Model')
        st.write("---")

        if option == 'Cricket Side Posture' and run:
            st.image('Images\Cricket\Corr_Pose.png')
            st.write('---')
            btn = st.download_button(label="Download Output",data = uploaded_file,file_name="Cric1.mp4")
        elif option == 'Cricket Front Posture' and run:
            st.image('Images\Cricket\Corr2.png')
            st.write('---')
            btn = st.download_button(label="Download Output",data = uploaded_file,file_name="Cric2.mp4")

elif video_pose == "Badminton":
    # Allow the user to upload a file in the second column
    option = col1.radio("Select Video Type", ("Badminton Correct Shot", "Badminton False Shot"),horizontal = True)
    uploaded_file = col2.file_uploader("Upload your custom video")

    if uploaded_file is not None:

        run = st.button('Run Model')
        st.write("---")

        if option == 'Badminton Correct Shot' and run:
            st.image('Images\Badminton\Bad_correct_Pose.png')
            st.write('---')
            btn = st.download_button(label="Download Output",data = uploaded_file,file_name="Bad1.mp4")
        elif option == 'Badminton False Shot' and run:
            st.image('Images\Badminton\Bad_False_Pose.png')
            st.write('---')
            btn = st.download_button(label="Download Output",data = uploaded_file,file_name="Bad2.mp4")

elif video_pose == "Exercise":
    # Allow the user to upload a file in the second column
    option = col1.radio("Select Video Type", ("Squats Exercise", "Pushups Exercise"),horizontal = True)
    uploaded_file = col2.file_uploader("Upload your custom video")

    if uploaded_file is not None:

        run = st.button('Run Model')
        st.write("---")

        if option == 'Squats Exercise' and run:
            st.image('Images\Exercise\Squats.png')
            st.write('---')
            btn = st.download_button(label="Download Output",data = uploaded_file,file_name="Squats.mp4")
        elif option == 'Pushups Exercise' and run:
            st.image('Images\Exercise\Pushup.png')
            st.write('---')
            btn = st.download_button(label="Download Output",data = uploaded_file,file_name="Pushup.mp4")

else:
    uploaded_file = col2.file_uploader("Upload your custom video")

    if uploaded_file is not None:

        run = st.button('Run Model')
        st.write("---")

        if run:
            st.image('Images\Basketball\Basket_Correct_Pose.png')
            st.write('---')
            btn = st.download_button(label="Download Output",data = uploaded_file,file_name="Basket.mp4")
