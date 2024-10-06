import os
import logging
from typing import Optional
import praw
from dotenv import load_dotenv

__version__ = "1.0.0"

# Load the logging level from environment variables or default to INFO
log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_environment(env_file: str = '.env') -> None:
    """
    Load environment variables from a .env file if it exists, otherwise use system environment variables.

    Args:
        env_file (str): Path to the .env file. Defaults to '.env' in the current directory.
    """
    if os.path.exists(env_file):
        load_dotenv(env_file)
        logger.info(f"Loaded environment variables from {env_file}")
    else:
        logger.warning(f"Environment file {env_file} not found. Using system environment variables.")

def get_env_variable(var_name: str) -> str:
    """
    Safely retrieve an environment variable and raise an error if it's not set.

    Args:
        var_name (str): Name of the environment variable.

    Returns:
        str: Value of the environment variable.

    Raises:
        ValueError: If the environment variable is not set.
    """
    value = os.getenv(var_name)
    if value is None:
        raise ValueError(f"Environment variable '{var_name}' is not set.")
    return value

def create_reddit_instance(env_file: Optional[str] = None) -> praw.Reddit:
    """
    Create and return a Reddit instance using credentials from environment variables.

    This function initializes a connection to the Reddit API. Be aware of Reddit's API usage rules
    and rate limits when using this instance for data fetching.

    Args:
        env_file (Optional[str]): Path to a custom .env file. If None, defaults to using the '.env' in the root.

    Returns:
        praw.Reddit: An authenticated Reddit instance.

    Raises:
        ValueError: If any required environment variables are missing.
        praw.exceptions.PRAWException: If there's an error creating the Reddit instance.
    """
    if env_file:
        load_environment(env_file)
    else:
        load_environment()

    try:
        reddit_instance = praw.Reddit(
            client_id=get_env_variable('REDDIT_CLIENT_ID'),
            client_secret=get_env_variable('REDDIT_SECRET'),
            user_agent=get_env_variable('REDDIT_USER_AGENT')
        )
        logger.info("Reddit instance created successfully.")
        return reddit_instance
    except ValueError as e:
        logger.error(f"Failed to create Reddit instance due to missing environment variables: {str(e)}")
        raise
    except praw.exceptions.PRAWException as e:
        logger.error(f"PRAW exception occurred during Reddit instance creation: {str(e)}")
        raise

def test_reddit_connection(reddit_instance: praw.Reddit, subreddit_name: str = "AskReddit") -> bool:
    """
    Test the Reddit API connection by fetching a specified subreddit.

    Args:
        reddit_instance (praw.Reddit): The Reddit instance to test.
        subreddit_name (str): The name of the subreddit to test. Defaults to "AskReddit".

    Returns:
        bool: True if the connection is successful, False otherwise.
    """
    try:
        subreddit = reddit_instance.subreddit(subreddit_name)
        _ = subreddit.display_name
        logger.info(f"Reddit API connection test to '{subreddit_name}' successful.")
        return True
    except praw.exceptions.PRAWException as e:
        logger.error(f"Reddit API connection test failed for '{subreddit_name}': {str(e)}")
        return False

def fetch_subreddit_posts(reddit_instance: praw.Reddit, subreddit_name: str, limit: int = 100) -> list:
    """
    Fetch a specified number of posts from a given subreddit.

    Args:
        reddit_instance (praw.Reddit): The authenticated Reddit instance.
        subreddit_name (str): The name of the subreddit to fetch posts from.
        limit (int): The maximum number of posts to fetch. Defaults to 100.

    Returns:
        list: A list of praw.models.Submission objects representing the fetched posts.

    Raises:
        praw.exceptions.PRAWException: If there's an error fetching the posts.
    """
    try:
        subreddit = reddit_instance.subreddit(subreddit_name)
        posts = list(subreddit.hot(limit=limit))
        logger.info(f"Successfully fetched {len(posts)} posts from r/{subreddit_name}")
        return posts
    except praw.exceptions.PRAWException as e:
        logger.error(f"Failed to fetch posts from r/{subreddit_name}: {str(e)}")
        raise

if __name__ == "__main__":
    try:
        print(f"Reddit API Module Version: {__version__}")
        reddit = create_reddit_instance()
        
        subreddit_to_test = input("Enter a subreddit name to test (default is 'AskReddit'): ") or "AskReddit"
        
        if test_reddit_connection(reddit, subreddit_to_test):
            print(f"Reddit API connection to '{subreddit_to_test}' successful!")
            
            num_posts = int(input("Enter the number of posts to fetch (default is 10): ") or 10)
            posts = fetch_subreddit_posts(reddit, subreddit_to_test, limit=num_posts)
            
            print(f"\nFetched {len(posts)} posts from r/{subreddit_to_test}:")
            for i, post in enumerate(posts[:5], 1):  # Print details of first 5 posts
                print(f"{i}. {post.title[:50]}{'...' if len(post.title) > 50 else ''}")
            
            if len(posts) > 5:
                print("...")
        else:
            print(f"Failed to connect to subreddit '{subreddit_to_test}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
