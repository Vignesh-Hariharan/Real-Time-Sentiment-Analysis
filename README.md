
# 🎭 Reddit Real-Time Sentiment Analysis

<div align="center">

![Reddit Logo](https://img.shields.io/badge/Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

</div>

> Unlock the power of real-time sentiment analysis on Reddit with this powerful tool built to understand the emotional pulse of any subreddit! 🚀🔍

---

## 🌟 Project Overview

This **Reddit Real-Time Sentiment Analysis** project is part of Vignesh's portfolio, showcasing advanced data science and natural language processing capabilities. It’s designed to provide actionable insights into the sentiment of Reddit discussions, allowing users to monitor how people feel about specific topics in real time.

### 🎨 Key Features

- 🔄 **Real-Time Reddit Data Fetching**: 
  - Retrieves live post titles from any subreddit, up to 100 posts in a single request.
  - Perfect for tracking sentiment changes in fast-paced discussions.

- 🧠 **Comprehensive Sentiment Analysis**:
  - Dual approach using **TextBlob** and **VADER** for accurate sentiment detection.
  - Sentiment is quantified as Positive, Neutral, or Negative, making it easy to interpret.

- 📊 **Interactive Visualizations**:
  - Generates dynamic pie charts, bar charts, and histograms to help visualize sentiment trends.
  - Built with Matplotlib and Plotly for both static and interactive visualization options.

- 💾 **Downloadable Results**:
  - Allows exporting the sentiment analysis as a CSV file for further analysis.
  - Integration-ready with external tools like Tableau for advanced reporting.

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

- **Python**: Programming language for the entire project.
- **PRAW**: Python Reddit API Wrapper to interact with the Reddit API.
- **Streamlit**: Framework used to build the interactive web app interface.
- **TextBlob & VADER**: Natural language processing libraries for sentiment analysis.
- **pandas**: For data manipulation and analysis.
- **matplotlib & Plotly**: For data visualization, both static and interactive.
- **python-dotenv**: To manage secure environment variables.

---

## 📊 Visualization Examples

<div align="center">
<img src="path_to_sample_pie_chart.png" alt="Sample Pie Chart" width="45%">
<img src="path_to_sample_bar_chart.png" alt="Sample Bar Chart" width="45%">
</div>

These visualizations show the sentiment distribution of Reddit posts, helping users understand the overall mood of the subreddit.

---

## 📁 Project Structure

```
reddit-sentiment-analysis/
│
├── app.py                 # Main Streamlit app file
├── reddit_api.py          # Reddit API interaction script
├── sentiment_analysis.py  # Sentiment analysis logic
├── data_processing.py     # Data processing utilities
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (kept out of version control)
└── README.md              # Project documentation
```

- **app.py**: The core application logic that integrates the Reddit API and sentiment analysis with Streamlit.
- **reddit_api.py**: Handles Reddit data fetching.
- **sentiment_analysis.py**: Applies TextBlob and VADER to classify sentiment.
- **data_processing.py**: Processes fetched data for visualization.

---

## 🔮 Future Enhancements

- Continuous real-time updates for ongoing sentiment tracking.
- Analyze Reddit comments in addition to post titles for a deeper understanding of user sentiment.
- Integrate machine learning models to improve sentiment accuracy.
- Expand visualizations with a more comprehensive dashboard for long-term trend analysis.
- Explore advanced NLP techniques for more granular text insights.

---

<div align="center">
Empowering Reddit insights through real-time data analysis and visualization
</div>

---

This project is part of Vignesh's personal portfolio, reflecting a hands-on approach to sentiment analysis, data visualization, and real-time data handling. For further details and updates, check out the GitHub repository!
