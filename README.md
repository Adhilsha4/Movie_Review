# 🎬 Movie Review Sentiment Analysis Using NLP and Logistic Regression

In today’s digital era, the success of a movie is deeply influenced by public reviews on platforms like **IMDb**, **Google Reviews**, and social media. Movie studios closely monitor these reviews to understand audience sentiment, enabling better decisions for production, marketing, and future projects.

This project involves building a **Machine Learning-based Sentiment Analysis model** using **Natural Language Processing (NLP)** to automatically classify movie reviews as **positive** or **negative**. The model is trained on IMDb reviews collected over the past decade and deployed as a web application using **Streamlit**.

---

## 💡 Project Objective

This project helps movie officials and analysts to:

- Automatically **classify movie reviews** as positive or negative
- **Analyze sentiment trends** over time
- **Visualize data** using graphs and charts
- Make **data-driven decisions** regarding movie success

---

## 🧹 NLP Preprocessing Steps

To ensure clean and effective data input, the following preprocessing steps were applied:

- Removal of special characters  
- Conversion of text to lowercase  
- Elimination of stopwords (e.g., *the*, *is*, *and*)  
- Word stemming using **SnowballStemmer** to reduce words to their root form  

---

## 🤖 Machine Learning Models Tested

| Algorithm              | Accuracy |
|------------------------|----------|
| ✅ Logistic Regression | **88%**   |
| Random Forest          | 85%       |
| AdaBoost               | 78%       |
| K-Nearest Neighbors    | 74%       |
| Decision Tree          | 71%       |
| Naive Bayes            | 64%       |

> **Logistic Regression** performed the best with the highest accuracy, precision, recall, and F1-score.

---

## 🚀 App Deployment

The model has been deployed as an interactive web app using **Streamlit**.

### 🔧 App Features:
- Users can enter any movie review
- The model instantly predicts sentiment: **Positive** or **Negative**
- Visual analytics for overall sentiment distribution

---

## 🛠️ Tech Stack

- **Language**: Python  
- **Libraries**: Scikit-learn, NLTK, Pandas, NumPy  
- **NLP Tools**: SnowballStemmer, Stopwords, Regex  
- **Deployment**: Streamlit  

---

## 📁 Project Structure

 ├── app.py # Streamlit application
 ├── model.pkl # Trained Logistic Regression model
 ├── vectorizer.pkl # TF-IDF Vectorizer
 ├── sentiment_analysis.ipynb # Model development and training
 ├── requirements.txt # Dependencies
 └── README.md # Project overview
