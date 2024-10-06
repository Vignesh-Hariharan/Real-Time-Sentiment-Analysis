from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import logging
import nltk


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Download VADER lexicon if not already present
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

# Initialize VADER Sentiment Intensity Analyzer
vader_analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment_textblob(text: str) -> float:
    """
    Analyze sentiment using TextBlob, returning a polarity score between -1 and 1.
    Args:
        text (str): The text to analyze.
    Returns:
        float: Sentiment polarity score (-1 to 1).
    """
    try:
        blob = TextBlob(text)
        score = blob.sentiment.polarity
        logger.info(f"TextBlob sentiment analysis complete: {score}")
        return score
    except Exception as e:
        logger.error(f"Error in TextBlob sentiment analysis: {str(e)}")
        return 0.0  # Return a neutral score on error

def analyze_sentiment_vader(text: str) -> float:
    """
    Analyze sentiment using VADER, returning a compound score between -1 and 1.
    Args:
        text (str): The text to analyze.
    Returns:
        float: Sentiment compound score (-1 to 1).
    """
    try:
        sentiment = vader_analyzer.polarity_scores(text)
        compound_score = sentiment['compound']
        logger.info(f"VADER sentiment analysis complete: {compound_score}")
        return compound_score
    except Exception as e:
        logger.error(f"Error in VADER sentiment analysis: {str(e)}")
        return 0.0  # Return a neutral score on error

def classify_sentiment(vader_score: float) -> str:
    """
    Classify sentiment based on the VADER compound score.
    Args:
        vader_score (float): VADER compound score (-1 to 1).
    Returns:
        str: Classified sentiment ('Positive', 'Neutral', or 'Negative').
    """
    try:
        if vader_score >= 0.05:
            sentiment = "Positive"
        elif vader_score <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        
        logger.info(f"Sentiment classified as: {sentiment}")
        return sentiment
    except Exception as e:
        logger.error(f"Error in sentiment classification: {str(e)}")
        return "Neutral"  # Default to neutral sentiment on error

if __name__ == "__main__":
    # Example usage for testing
    test_text = "I love programming, but sometimes it can be frustrating."
    
    textblob_score = analyze_sentiment_textblob(test_text)
    vader_score = analyze_sentiment_vader(test_text)
    classified_sentiment = classify_sentiment(vader_score)
    
    print(f"Text: {test_text}")
    print(f"TextBlob Score: {textblob_score}")
    print(f"VADER Score: {vader_score}")
    print(f"Classified Sentiment: {classified_sentiment}")
