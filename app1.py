import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Spain Top 50 Dashboard", layout="wide")

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv(r"C:\Users\admin\Downloads\Atlantic_Spain.csv")
df['date'] = pd.to_datetime(df['date'])

# -------------------------------
# FEATURE ENGINEERING (FIX)
# -------------------------------

# Create unique song id
df['song_id'] = df['song'].astype(str) + "_" + df['artist'].astype(str)

# Entry date per song
entry_dates = df.groupby('song_id')['date'].min().reset_index()
entry_dates.columns = ['song_id', 'entry_date']

# Merge back
df = df.merge(entry_dates, on='song_id', how='left')

# Lifecycle stage
def classify_stage(row):
    days = (row['date'] - row['entry_date']).days
    
    if days <= 7:
        return "New Entry"
    elif row['position'] <= 10:
        return "Peak"
    elif row['position'] <= 25:
        return "Growth"
    else:
        return "Decline"

df['lifecycle_stage'] = df.apply(classify_stage, axis=1)

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("Filters")

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df['date'].min(), df['date'].max()]
)

explicit_filter = st.sidebar.selectbox(
    "Explicit Content",
    ["All", True, False]
)

album_filter = st.sidebar.selectbox(
    "Album Type",
    ["All"] + list(df['album_type'].dropna().unique())
)

# -------------------------------
# APPLY FILTERS
# -------------------------------
filtered_df = df.copy()

if explicit_filter != "All":
    filtered_df = filtered_df[filtered_df['is_explicit'] == explicit_filter]

if album_filter != "All":
    filtered_df = filtered_df[filtered_df['album_type'] == album_filter]

filtered_df = filtered_df[
    (filtered_df['date'] >= pd.to_datetime(date_range[0])) &
    (filtered_df['date'] <= pd.to_datetime(date_range[1]))
]

# -------------------------------
# TITLE
# -------------------------------
st.title("🎵 Spain Top 50 Playlist Analysis")

# -------------------------------
# KPI SECTION
# -------------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Avg Days on Playlist",
    round(filtered_df.groupby('song_id')['date'].nunique().mean(), 2)
)

col2.metric(
    "Avg Position",
    round(filtered_df['position'].mean(), 2)
)

col3.metric(
    "Avg Popularity",
    round(filtered_df['popularity'].mean(), 2)
)

# -------------------------------
# LIFECYCLE DISTRIBUTION
# -------------------------------
st.subheader("📈 Lifecycle Stage Distribution")

stage_counts = filtered_df['lifecycle_stage'].value_counts()

fig1, ax1 = plt.subplots()
stage_counts.plot(kind='bar', ax=ax1)
ax1.set_title("Lifecycle Stages")
st.pyplot(fig1)

# -------------------------------
# EXPLICIT VS CLEAN
# -------------------------------
st.subheader("⚡ Explicit vs Clean Songs")

explicit_counts = filtered_df['is_explicit'].value_counts()

fig2, ax2 = plt.subplots()
explicit_counts.plot(kind='bar', ax=ax2)
ax2.set_title("Explicit vs Clean")
st.pyplot(fig2)

# -------------------------------
# ALBUM TYPE
# -------------------------------
st.subheader("💿 Album Type Distribution")

album_counts = filtered_df['album_type'].value_counts()

fig3, ax3 = plt.subplots()
album_counts.plot(kind='bar', ax=ax3)
ax3.set_title("Album Types")
st.pyplot(fig3)

# -------------------------------
# POSITION VS POPULARITY
# -------------------------------
st.subheader("📉 Position vs Popularity")

fig4, ax4 = plt.subplots()
ax4.scatter(filtered_df['position'], filtered_df['popularity'])
ax4.set_xlabel("Position")
ax4.set_ylabel("Popularity")
st.pyplot(fig4)

# -------------------------------
# SONG DURATION
# -------------------------------
st.subheader("⏱ Song Duration")

filtered_df['duration_min'] = filtered_df['duration_ms'] / 60000

fig5, ax5 = plt.subplots()
filtered_df['duration_min'].plot(kind='hist', bins=20, ax=ax5)
ax5.set_title("Duration (Minutes)")
st.pyplot(fig5)

# -------------------------------
# TOP SONGS TABLE
# -------------------------------
st.subheader("📋 Top Songs Data")

st.dataframe(
    filtered_df.sort_values('position').head(50),
    use_container_width=True
)