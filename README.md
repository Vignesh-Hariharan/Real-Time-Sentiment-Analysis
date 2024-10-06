
# 🎭 Reddit Sentiment Analyzer

<div align="center">

![Reddit Logo](https://img.shields.io/badge/Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

</div>

Hey there! 👋 Welcome to my Reddit Sentiment Analyzer project. Ever wondered what the overall mood is like in your favorite subreddit? Well, I did, and that's why I built this tool. Let me walk you through it!

## What's This All About?

I've always been fascinated by how opinions spread on social media, especially on Reddit. This project is my attempt to capture the sentiment of Reddit discussions in real-time. It's not just about positive or negative vibes – it's about understanding the nuances of online conversations.

### Cool Features I've Packed In

- **Live Reddit Data**: The tool grabs the latest posts from any subreddit you're curious about. Want to know what's hot in r/technology or r/aww? Just type it in!
  
- **Sentiment Magic**: I've used both TextBlob and VADER for sentiment analysis. Why both? Well, sometimes one catches things the other misses. It's like having two experts instead of one!

- **Pretty Visuals**: Because who doesn't love a good chart? I've added interactive pie charts and bar graphs. They make it super easy to see sentiment trends at a glance.

- **Data to Go**: All the analysis can be downloaded as a CSV. Perfect if you want to dive deeper or create your own visualizations.

## The Tech Behind the Scenes

I had a blast working with these technologies:

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PRAW](https://img.shields.io/badge/PRAW-FF4500?style=for-the-badge&logo=reddit&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

</div>

- **Python**: The backbone of the project. I love how versatile it is!
- **PRAW**: For talking to Reddit. It's like having a direct line to Reddit's brain.
- **Streamlit**: Made the web app a breeze to build. Seriously, it's amazing for data projects.
- **TextBlob & VADER**: The dynamic duo for sentiment analysis. They're like the Watson and Crick of NLP!
- **Pandas**: For wrangling all that data. It's a data scientist's best friend.
- **Plotly**: Because static charts are so last year. Interactive visuals for the win!

## See It in Action

<div align="center">
<img src="path_to_sample_pie_chart.png" alt="Sample Pie Chart" width="45%">
<img src="path_to_sample_bar_chart.png" alt="Sample Bar Chart" width="45%">
</div>

These charts show real sentiment data from a subreddit. Pretty neat, huh? The pie chart gives you a quick overview, while the bar chart lets you compare sentiments side by side.

## How It's All Organized

Here's a quick look at how I've structured the project:

```
reddit-sentiment-analysis/
│
├── app.py                 # Where the Streamlit magic happens
├── reddit_api.py          # Handles all the Reddit communication
├── sentiment_analysis.py  # The brains of the sentiment operation
├── data_processing.py     # Data cleanup and preparation
├── requirements.txt       # All the Python goodies you need
├── .env                   # Shhh... secret stuff goes here
└── README.md              # You are here!
```

## What's Next?

I've got tons of ideas to make this even better:

- Real-time updates (because who doesn't love live data?)
- Diving into the comments for even more sentiment insights
- Maybe throw in some machine learning for extra accuracy
- A fancy dashboard for tracking long-term trends
- Exploring more advanced NLP techniques (I'm looking at you, topic modeling!)

## Let's Connect!

I had a blast building this, and I'm always happy to chat about it. Got questions, ideas, or just want to talk tech? Hit me up!

[LinkedIn](https://www.linkedin.com/in/h-vignesh) | [GitHub](#) | [Portfolio](#)

---

<div align="center">
Built with 💻 and fueled by ☕ by Vignesh
</div>

Thanks for checking out my project. Hope you find it as exciting as I do!
