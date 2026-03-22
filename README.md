📊 Content Maturity, Release Lifecycle & Playlist Rotation Analysis
🎵 Spain Top 50 Songs Analysis
📌 Project Overview

This project analyzes the Spain Top 50 music playlist to understand how songs perform over time. It focuses on:

🎯 Song lifecycle (entry → peak → decline)
🔄 Playlist rotation (churn rate)
📈 Content maturity behavior
⚡ Explicit vs clean content performance
💿 Single vs album track comparison

The goal is to help optimize release strategy, marketing, and playlist positioning.

🧠 Problem Statement

Despite having playlist data, key insights are missing:

How long do songs stay on the playlist?
Do fresh songs perform better than older ones?
How fast do songs reach peak position?
Do explicit songs behave differently?

This project solves these using data analysis + visualization.

📂 Dataset

The dataset contains daily Top 50 songs with:

date – Playlist date
position – Rank (1–50)
song – Song name
artist – Artist name
popularity – Popularity score
duration_ms – Song duration
album_type – Single / Album
is_explicit – Explicit flag
⚙️ Tech Stack
🐍 Python
📊 Pandas
📉 Matplotlib
🌐 Streamlit
🔍 Exploratory Data Analysis (EDA)

Key insights derived using:

Distribution of song positions
Top artists frequency
Explicit vs clean comparison
Song duration trends
Popularity vs ranking
🔄 Lifecycle Analysis

Each song is analyzed using:

📅 Entry Date
📅 Exit Date
⏳ Total Days on Playlist
🏆 Peak Position
⏱ Time to Peak
Lifecycle Stages:
🆕 New Entry
📈 Growth
🔝 Peak
📉 Decline
📊 Key Metrics (KPIs)
Average Days on Playlist
Time to Peak
Playlist Churn Rate
Retention Stability
Explicit Content Impact
Single vs Album Performance
🖥️ Streamlit Dashboard

Interactive dashboard includes:

📈 Lifecycle stage distribution
⚡ Explicit vs clean comparison
💿 Album type analysis
📉 Position vs popularity
📊 Song duration insights
🚀 How to Run the Project
1️⃣ Install dependencies
pip install -r requirements.txt
2️⃣ Run Streamlit app
streamlit run app.py
📁 Project Structure
project/
│── app.py
│── eda.py
│── Atlantic_Spain.csv
│── requirements.txt
│── README.md
📌 Key Insights
Spain playlist has high churn rate
Fresh releases dominate
Singles perform better than albums
Explicit songs peak faster but decline quickly
Shorter songs tend to have better retention
🎯 Conclusion

The Spain music market is fast-moving and freshness-driven.
Success depends on:

Early promotion
Frequent releases
Strong initial engagement
🔮 Future Work
🤖 ML model to predict hit songs
🌍 Cross-country analysis (Spain vs UK/US)
🎼 Genre-based insights
📊 Advanced interactive dashboards
👤 Author

Zyan Ahmed