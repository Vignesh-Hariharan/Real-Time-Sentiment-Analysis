# 🎭 Reddit Real-Time Sentiment Analysis

<div align="center">

![Reddit Logo](https://img.shields.io/badge/Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

</div>

> Dive into the emotional landscape of Reddit with our cutting-edge sentiment analysis tool! 🚀🔍

---

## 🌟 Project Overview

The Reddit Real-Time Sentiment Analysis tool is designed to provide instant insights into the emotional tone of Reddit discussions. By analyzing post titles from any chosen subreddit, this application offers a comprehensive view of sentiment trends, enabling users to gauge the overall mood and reactions within specific Reddit communities.

### 🎨 Key Features

- 🔄 **Real-Time Data Fetching**: 
  - Retrieves the latest posts from any specified subreddit.
  - Capable of fetching up to 100 posts in a single request for comprehensive analysis.

- 🧠 **Dual Sentiment Analysis**:
  - Utilizes both TextBlob and VADER (Valence Aware Dictionary and sEntiment Reasoner) for nuanced sentiment scoring.
  - TextBlob provides polarity scores ranging from -1 (very negative) to 1 (very positive).
  - VADER offers compound scores, specially tuned for social media content.

- 🏷️ **Sentiment Classification**:
  - Categorizes posts as Positive, Neutral, or Negative based on sentiment scores.
  - Offers a clear overview of sentiment distribution within the analyzed posts.

- 📊 **Interactive Visualizations**:
  - Presents sentiment distribution through dynamic pie charts and bar graphs.
  - Utilizes Matplotlib for static visualizations and Plotly for interactive charts.

- 💾 **Data Export Capability**:
  - Allows users to download sentiment analysis results in CSV format.
  - Enables further analysis and integration with other data visualization tools like Tableau.

---

## 🛠️ Technology Stack

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PRAW](https://img.shields.io/badge/PRAW-FF4500?style=for-the-badge&logo=reddit&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

</div>

- **Python**: Core programming language for the entire project.
- **PRAW (Python Reddit API Wrapper)**: Facilitates interaction with the Reddit API.
- **Streamlit**: Powers the interactive web interface for user interaction and data visualization.
- **TextBlob**: Provides sentiment analysis through natural language processing.
- **VADER**: Offers sentiment analysis specifically optimized for social media text.
- **pandas**: Enables efficient data manipulation and analysis.
- **matplotlib**: Creates static data visualizations.
- **Plotly**: Generates interactive and dynamic charts.
- **python-dotenv**: Manages environment variables for secure credential handling.
- **concurrent.futures**: Implements parallel processing for enhanced performance.

---

## 📊 Visualization Examples

<div align="center">
<img src="path_to_sample_pie_chart.png" alt="Sample Pie Chart" width="45%">
<img src="path_to_sample_bar_chart.png" alt="Sample Bar Chart" width="45%">
</div>

These visualizations demonstrate the sentiment distribution across analyzed Reddit posts, offering insights into the overall mood of the selected subreddit.

---

## 📁 Project Structure

```
reddit-sentiment-analysis/
│
├── app.py                 # Main Streamlit application
├── reddit_api.py          # Reddit API interaction module
├── sentiment_analysis.py  # Sentiment analysis algorithms
├── data_processing.py     # Data processing and manipulation utilities
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (not in version control)
└── README.md              # Project documentation
```

- **app.py**: The core of the application, integrating all components and providing the user interface through Streamlit.
- **reddit_api.py**: Handles all interactions with the Reddit API, including post fetching and data retrieval.
- **sentiment_analysis.py**: Contains the logic for sentiment analysis using TextBlob and VADER.
- **data_processing.py**: Provides utilities for processing and preparing data for analysis and visualization.

---

## 🔮 Future Enhancements

- Implementation of real-time updating for continuous sentiment analysis.
- Expansion of analysis to include comment sentiment in addition to post titles.
- Integration of machine learning models to improve sentiment prediction accuracy.
- Development of a comprehensive dashboard for tracking long-term sentiment trends.
- Addition of natural language processing techniques for more detailed text analysis.

---

<div align="center">
Empowering insights through data analysis and visualization
</div>
