import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style = 'darkgrid')
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(page_title="SPARK - The Beginning", page_icon=":bar_chart:",
layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title('Team Performance 🏸')
st.write('---')

## ------------------------------------------------------------------------------

# Use st.columns to layout the selectbox and radio buttons side-by-side
col1, col2 = st.columns(2)

# Add a selectbox to the first column for selecting the sport
sport = col1.selectbox("Select a sport", ("Cricket", "Badminton", "Basketball"))

# Check if the user selected cricket
if sport == "Cricket":
    # Allow the user to upload a file in the second column
    uploaded_file = col2.file_uploader("Upload your custom dataset", type="csv")

    if uploaded_file is not None:
        # Load the custom dataset provided by the user
        custom_dataset = pd.read_csv(uploaded_file)

        # Add radio buttons after the file uploader for selecting innings
        innings = col1.radio("Select innings", ("First innings", "Second innings"),horizontal = True)
        st.write("---")

        # Filter the dataset to get the selected innings data
        if innings == "First innings":
            innings_data = custom_dataset[custom_dataset["Innings_number"] == 1]
        else:
            innings_data = custom_dataset[custom_dataset["Innings_number"] == 2]

        # Create a visualization of the selected innings
        with st.expander("View runs scored by each batsman"):
            # Create a bar chart of runs scored by each batsman
            batsman_runs = innings_data.groupby("Batsman")["Runs_off_bat"].sum().reset_index()
            fig, ax = plt.subplots()
            ax.bar(batsman_runs["Batsman"], batsman_runs["Runs_off_bat"], color=["#0057e7", "#d62d20", "#ffa700", "#008744", "#6a00ff", "#f012be", "#7f7f7f", "#001f3f", "#ff851b", "#3d9970"])
            ax.set_xlabel("Batsman")
            ax.set_ylabel("Runs")
            ax.set_title("Runs scored by each batsman")
            st.pyplot(fig)

        with st.expander("View types of dismissals"):
            # Create a pie chart of types of dismissals
            dismissals = innings_data["Kind_of_wicket"].value_counts()
            fig, ax = plt.subplots()
            colors = ["#d62d20", "#008744", "#6a00ff", "#ffa700", "#001f3f", "#7f7f7f", "#f012be", "#3d9970"]
            ax.pie(dismissals, labels=dismissals.index, autopct="%1.1f%%", colors=colors)
            ax.set_title("Types of dismissals")
            st.pyplot(fig)

        with st.expander("View total runs scored by each over"):
            # Create a line chart of total runs scored by each over
            over_runs = innings_data.groupby("Over")["Total"].sum().reset_index()
            fig, ax = plt.subplots()
            ax.plot(over_runs["Over"], over_runs["Total"], color="#008744")
            ax.set_xlabel("Over")
            ax.set_ylabel("Runs")
            ax.set_title("Total runs scored by each over")
            st.pyplot(fig)
elif sport == "Basketball":
    # Allow the user to upload a file in the second column
    uploaded_file = col2.file_uploader("Upload your custom dataset", type="csv")

    if uploaded_file is not None:
        # Load the custom dataset provided by the user
        custom_dataset = pd.read_csv(uploaded_file)

        # Add radio buttons after the file uploader for selecting innings
        match = col1.radio("Select Match", ("Match 1", "Match 2",'Match 3'),horizontal = True)
        st.write("---")

        if match == "Match 1":
            match_data = custom_dataset[custom_dataset["Match ID"] == match]
        elif match == 'Match 2':
            match_data = custom_dataset[custom_dataset["Match ID"] == match]
        else:
            match_data = custom_dataset[custom_dataset["Match ID"] == match]

        with st.expander("Total Points Scored by Teams in {}".format(match)):
            # Create a bar plot for the total points scored by each team in the match
            fig, ax = plt.subplots()
            colors = ['#457b9d', '#fca311'] # blue and orange colors
            ax.bar(match_data['Teams'], match_data['Total Pts'], color=colors)
            ax.set_xlabel('Teams')
            ax.set_ylabel('Total Points')
            ax.set_title('Total Points Scored by Teams in {}'.format(match))
            st.pyplot(fig)
        with st.expander("Distribution of Field Goal Attempts by Type in {}".format(match)):
            # Create a stacked bar chart for the distribution of field goal attempts by type for each team in the match
            fig, ax = plt.subplots()
            match_data[['2PtsA', '3PtsA']].plot(kind='bar', stacked=True, ax=ax)
            ax.set_xlabel('Teams')
            ax.set_ylabel('Number of Attempts')
            ax.set_title('Distribution of Field Goal Attempts by Type in {}'.format(match))
            ax.legend(["2-Point Attempts", "3-Point Attempts"])
            ax.set_xticklabels(match_data['Teams'])
            st.pyplot(fig)
        with st.expander("Boxplot of Free Throw Percentages"):
            # Create a boxplot of free throw percentages
            fig, ax = plt.subplots()
            sns.boxplot(x="FT%", y="Teams", data=custom_dataset, palette="rocket", orient="h", ax=ax)
            ax.set_xlabel('Free Throw Percentage')
            ax.set_ylabel('Teams')
            ax.set_title('Distribution of Free Throw Percentages')
            st.pyplot(fig)
        with st.expander("Stacked Bar Chart of Rebounds"):
            # Create a stacked bar chart of rebounds
            fig, ax = plt.subplots()
            custom_dataset.plot(kind='barh', x='Teams', y=['OFF REB', 'DEF REB'], stacked=True, color=['#7f6d5f', '#557f2d'], ax=ax)
            ax.set_xlabel('Number of Rebounds')
            ax.set_ylabel('Teams')
            ax.set_title('Number of Offensive and Defensive Rebounds')
            st.pyplot(fig)
        with st.expander("Steals and Blocks by Teams"):
            # Create a stacked bar chart of steals and blocks
            fig, ax = plt.subplots()
            custom_dataset.plot(kind='barh', x='Teams', y=['Steals', 'Blocks'], stacked=True, color=['#1f77b4', '#ff7f0e'], ax=ax)
            ax.set_xlabel('Number of Plays')
            ax.set_ylabel('Teams')
            ax.set_title('Number of Steals and Blocks by Teams')
            st.pyplot(fig)
else:
    uploaded_file = col2.file_uploader("Upload your custom dataset", type="csv")

    if uploaded_file is not None:
        # Load the custom dataset provided by the user
        custom_dataset = pd.read_csv(uploaded_file)

        # Add radio buttons after the file uploader for selecting innings
        # match = col1.radio("Select Match", ("Match 1", "Match 2",'Match 3'),horizontal = True)
        st.write("---")
        #
        # if match == "Match 1":
        #     match_data = custom_dataset[custom_dataset["Match ID"] == match]
        # elif match == 'Match 2':
        #     match_data = custom_dataset[custom_dataset["Match ID"] == match]
        # else:
        #     match_data = custom_dataset[custom_dataset["Match ID"] == match]

        with st.expander("Distribution of Points Won by Player in each Match"):
            match_data = custom_dataset.groupby(["Match ID", "Player 1"]).agg({"Points Won": "sum"}).reset_index()
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.barplot(x="Match ID", y="Points Won", hue="Player 1", data=match_data, palette="Set2")
            ax.set_xlabel("Match ID")
            ax.set_ylabel("Points Won")
            ax.set_title("Distribution of Points Won by Player in each Match")
            ax.legend(title="Player", loc="best")
            st.pyplot(fig)

        with st.expander("Comparison of Shots Attempted by each Player in each Match"):
            match_data = custom_dataset.groupby(["Match ID", "Player 1"]).agg({"Smashes": "sum", "Net Shots": "sum", "Drop Shots": "sum"}).reset_index()
            match_data = pd.melt(match_data, id_vars=["Match ID", "Player 1"], value_vars=["Smashes", "Net Shots", "Drop Shots"], var_name="Shot Type", value_name="Shots Attempted")
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.barplot(x="Match ID", y="Shots Attempted", hue="Player 1", data=match_data, palette="Set2", hue_order=["John", "Peter", "Mary", "Lisa", "David", "James",'Sarah','Emma','Kevin','Mark'])
            ax.set_xlabel("Match ID")
            ax.set_ylabel("Shots Attempted")
            ax.set_title("Comparison of Shots Attempted by each Player in each Match")
            ax.legend(title="Player", loc="best")
            st.pyplot(fig)

        with st.expander("Distribution of Faults by Player in each Match"):
            match_data = custom_dataset.groupby(["Match ID", "Player 1"]).agg({"Faults": "sum"}).reset_index()
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.barplot(x="Match ID", y="Faults", hue="Player 1", data=match_data, palette="Set2")
            ax.set_xlabel("Match ID")
            ax.set_ylabel("Number of Faults")
            ax.set_title("Distribution of Faults by Player in each Match")
            ax.legend(title="Player", loc="best")
            st.pyplot(fig)
