import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import praw
from dotenv import load_dotenv
import os
from reddit_api import create_reddit_instance, fetch_subreddit_posts
from sentiment_analysis import analyze_sentiment_textblob, analyze_sentiment_vader, classify_sentiment
from data_processing import process_posts_to_dataframe

import os
from dotenv import load_dotenv

# Load environment variables
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Debug: Print to check if the variables are loaded
print("REDDIT_CLIENT_ID:", os.getenv("REDDIT_CLIENT_ID"))
print("REDDIT_SECRET:", os.getenv("REDDIT_SECRET"))
print("REDDIT_USER_AGENT:", os.getenv("REDDIT_USER_AGENT"))
print("REDDIT_USERNAME:", os.getenv("REDDIT_USERNAME"))
print("REDDIT_PASSWORD:", os.getenv("REDDIT_PASSWORD"))



# Function to get environment variable or raise an error if it's not set
def get_env_variable(var_name):
    value = os.getenv(var_name)
    if value is None:
        raise ValueError(f"Environment variable '{var_name}' is not set")
    return value

# Initialize Reddit instance
@st.cache_resource
def get_reddit_instance():
    try:
        return praw.Reddit(
            client_id=get_env_variable('REDDIT_CLIENT_ID'),
            client_secret=get_env_variable('REDDIT_SECRET'),
            user_agent=get_env_variable('REDDIT_USER_AGENT')
        )
    except ValueError as e:
        st.error(f"Error: {str(e)}")
        st.stop()

def plot_sentiment_distribution(df: pd.DataFrame, chart_types: list):
    """
    Plot sentiment distribution based on selected chart types.
    """
    sentiments = df['Classified_Sentiment'].value_counts()
    if "Pie Chart" in chart_types:
        st.subheader("Sentiment Distribution (Pie Chart)")
        fig, ax = plt.subplots(figsize=(7, 7))
        ax.pie(sentiments, labels=sentiments.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)
    if "Bar Chart" in chart_types:
        st.subheader("Sentiment Distribution (Bar Chart)")
        sentiment_counts = sentiments.reset_index()
        sentiment_counts.columns = ['Sentiment', 'Count']
        fig = px.bar(sentiment_counts, x='Sentiment', y='Count', title='Sentiment Analysis Bar Chart')
        st.plotly_chart(fig)

def main():
    st.title("Reddit Real-Time Sentiment Analysis")
    st.sidebar.header("Configuration")

    # Input fields for subreddit and number of posts
    subreddit_name = st.sidebar.text_input("Enter Subreddit Name", "technology")
    post_limit = st.sidebar.slider("Number of Posts to Analyze", 10, 100, 50)
    
    # Visualization options
    chart_type = st.sidebar.multiselect(
        "Select Chart Types",
        ["Pie Chart", "Bar Chart"],
        default=["Pie Chart", "Bar Chart"]
    )

    # Button to trigger sentiment analysis
    if st.sidebar.button("Fetch and Analyze"):
        try:
            # Create Reddit instance
            reddit = get_reddit_instance()

            # Fetch posts from the specified subreddit
            with st.spinner(f"Fetching {post_limit} posts from r/{subreddit_name}..."):
                posts = fetch_subreddit_posts(reddit, subreddit_name, post_limit)

            # Process posts and perform sentiment analysis
            df = process_posts_to_dataframe(posts)

            # Display the data frame with sentiment analysis
            st.subheader("Sentiment Analysis Results:")
            st.dataframe(df)

            # Plot sentiment distribution
            plot_sentiment_distribution(df, chart_type)

            # Display raw sentiment scores
            st.subheader("Raw Sentiment Scores")
            st.write("TextBlob scores range from -1 (very negative) to 1 (very positive)")
            st.write("VADER scores range from -1 (very negative) to 1 (very positive)")
            st.dataframe(df[['Title', 'TextBlob_Sentiment', 'Vader_Sentiment']])

            # Option to download the data as CSV for Tableau visualization
            csv = df.to_csv(index=False)
            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name=f'reddit_sentiment_analysis_{subreddit_name}.csv',
                mime='text/csv'
            )

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
