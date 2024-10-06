import pandas as pd
from sentiment_analysis import analyze_sentiment_textblob, analyze_sentiment_vader, classify_sentiment
from typing import List, Dict, Any
from praw.models import Submission
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def process_post(post: Submission) -> Dict[str, Any]:
    """
    Process a single Reddit post and perform sentiment analysis.

    Args:
        post (praw.models.Submission): A Reddit post object.

    Returns:
        Dict[str, Any]: A dictionary containing post data and sentiment analysis results.
    """
    try:
        title = post.title
        textblob_score = analyze_sentiment_textblob(title)
        vader_score = analyze_sentiment_vader(title)
        sentiment = classify_sentiment(vader_score)

        return {
            'Title': title,
            'Author': str(post.author),
            'Score': post.score,
            'Num_Comments': post.num_comments,
            'Created_UTC': pd.to_datetime(post.created_utc, unit='s'),
            'TextBlob_Sentiment': textblob_score,
            'Vader_Sentiment': vader_score,
            'Classified_Sentiment': sentiment
        }
    except Exception as e:
        logger.error(f"Error processing post {post.id}: {str(e)}. Post title: {post.title}")
        return None

def process_posts_to_dataframe(posts: List[Submission], max_workers: int = 5) -> pd.DataFrame:
    """
    Process Reddit posts and perform sentiment analysis on each post using parallel processing.

    Args:
        posts (List[praw.models.Submission]): A list of Reddit posts fetched using PRAW.
        max_workers (int): Maximum number of threads for parallel processing.

    Returns:
        pd.DataFrame: A DataFrame containing post data and sentiment analysis results.
    """
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_post = {executor.submit(process_post, post): post for post in posts}
        for future in as_completed(future_to_post):
            result = future.result()
            if result:
                results.append(result)

    if not results:
        logger.warning("No posts were successfully processed.")
        return pd.DataFrame()

    df = pd.DataFrame(results)
    
    # Calculate additional metrics
    df['Sentiment_Difference'] = df['TextBlob_Sentiment'] - df['Vader_Sentiment']
    df['Engagement_Score'] = df['Score'] + df['Num_Comments']

    # Sort by engagement score
    df = df.sort_values('Engagement_Score', ascending=False)

    logger.info(f"Successfully processed {len(df)} posts.")
    return df

def generate_summary_stats(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Generate summary statistics from the processed data.

    Args:
        df (pd.DataFrame): The DataFrame containing processed post data.

    Returns:
        Dict[str, Any]: A dictionary containing summary statistics.
    """
    return {
        'Total_Posts': len(df),
        'Average_Score': df['Score'].mean(),
        'Average_Comments': df['Num_Comments'].mean(),
        'Sentiment_Distribution': df['Classified_Sentiment'].value_counts().to_dict(),
        'Average_TextBlob_Sentiment': df['TextBlob_Sentiment'].mean(),
        'Average_Vader_Sentiment': df['Vader_Sentiment'].mean(),
        'Most_Positive_Post': df.loc[df['Vader_Sentiment'].idxmax(), 'Title'],
        'Most_Negative_Post': df.loc[df['Vader_Sentiment'].idxmin(), 'Title'],
        'Most_Engaging_Post': df.loc[df['Engagement_Score'].idxmax(), 'Title']
    }

if __name__ == "__main__":
    from reddit_api import create_reddit_instance, fetch_subreddit_posts

    reddit = create_reddit_instance()
    posts = fetch_subreddit_posts(reddit, "python", limit=10)
    
    df = process_posts_to_dataframe(posts)
    print(df.head())
    
    summary = generate_summary_stats(df)
    print("\nSummary Statistics:")
    for key, value in summary.items():
        print(f"{key}: {value}")
