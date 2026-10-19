# 🎬 Movie Recommendation System

An end-to-end Machine Learning web application built using Python, Scikit-Learn, and Streamlit. This app utilizes content-based filtering and Cosine Similarity to recommend similar movies based on textual tags and metadata.

---

## 🚀 Live Demo
🔗 **[Click Here to Access Live Web App]([https://tamari-movie-app-link.streamlit.app](https://tkjobmv5hznzhzglplneg8.streamlit.app/))**

---

## 📌 Project Features
- **Content-Based Filtering**: Recommends movies by analyzing metadata and textual tags.
- **Text Vectorization**: Applied Natural Language Processing (NLP) techniques via `CountVectorizer` to convert text data into numerical feature vectors.
- **Similarity Metrics**: Calculated pairwise similarity scores using **Cosine Similarity**.
- **Interactive UI**: Real-time user input interface designed with Streamlit.
- **Cloud Deployment**: Deployed live on Streamlit Community Cloud.

---

## 🛠️ Tech Stack & Libraries
- **Language**: Python
- **Machine Learning**: Scikit-Learn
- **Data Processing**: Pandas, NumPy
- **Web Framework**: Streamlit
- **Deployment**: Streamlit Cloud, GitHub

---

## 📂 Project Structure
```text
├── app.py                  # Streamlit web interface application
├── movie_dict.pkl          # Pickled movie dataset and titles
├── similarity.pkl          # Pre-computed cosine similarity matrix
├── requirements.txt        # Project dependencies and libraries
└── README.md               # Project documentation
