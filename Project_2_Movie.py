import streamlit as st
import pickle
from PIL import Image
import warnings

warnings.filterwarnings('ignore')
st.set_page_config(page_title="Movie Review App", layout="wide")

# --- Page 1: Home ---
def home_page():
    st.markdown(
        """
        <h1 style='text-align: center;
                   color: #FFFFFF;
                   text-shadow: 2px 2px 4px #000000;
                   font-weight: bold;'>
            MOVIE REVIEW SENTIMENT ANALYSIS
        </h1>
        """,
        unsafe_allow_html=True
    )

    img = Image.open("film.jpg")
    st.image(img, width=500)

    st.markdown(
        """
        <h2 style='color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>🎬 Introduction</h2>
        <p style='text-align: justify; font-size: 16px; color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>
            In today’s digital age, the success of a movie is heavily influenced by public opinion shared across platforms like IMDb, 
            Google Reviews, and social media. Movie studios and producers closely monitor these reviews to understand audience sentiment, 
            which helps guide future production, marketing strategies, and even casting decisions.
        </p>
        <p style='text-align: justify; font-size: 16px; color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>
            To aid this process, I developed a machine learning-based sentiment analysis model that automatically predicts whether a movie 
            review is positive or negative. This solution is designed using Natural Language Processing (NLP) and is trained on IMDb 
            reviews collected over the past decade.
        </p>

        <h2 style='color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>🎯 Project Goal</h2>
        <ul style='font-size: 16px; color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>
            <li>Automatically classify viewer reviews as positive or negative.</li>
            <li>Analyze trends in viewer sentiment.</li>
            <li>Visualize this data using interactive graphs for better insights.</li>
            <li>Improve decision-making around a movie's success.</li>
        </ul>

        <h2 style='color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>🧹 NLP Preprocessing Steps</h2>
        <ul style='font-size: 16px; color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>
            <li>Removed special characters</li>
            <li>Converted all text to lowercase</li>
            <li>Removed common stopwords (e.g., "the", "is", "and")</li>
            <li>Applied Snowball Stemming to reduce words to their root forms</li>
        </ul>

        <h2 style='color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>📊 Models Tested</h2>
        <p style='font-size: 16px; color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>
            I tested multiple machine learning algorithms for this classification task. The results are:
        </p>
        <ul style='font-size: 16px; color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>
            <li><b>Logistic Regression:</b> 88% accuracy ✅</li>
            <li><b>Random Forest:</b> 85%</li>
            <li><b>AdaBoost:</b> 78%</li>
            <li><b>K-Nearest Neighbors:</b> 74%</li>
            <li><b>Decision Tree:</b> 71%</li>
            <li><b>Naive Bayes:</b> 64%</li>
        </ul>
        <p style='font-size: 16px; color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>
            Logistic Regression outperformed all other models, achieving the highest scores across accuracy, precision, recall, and F1-score.
        </p>

        <h2 style='color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>🚀 App Deployment</h2>
        <p style='font-size: 16px; color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>
            To make this solution accessible, I deployed the model as a web application using Streamlit. Users can input a movie review 
            and instantly receive feedback on whether the sentiment is positive or negative. This real-time capability makes it a 
            practical tool for entertainment companies and review monitoring.
        </p>
        """,
        unsafe_allow_html=True
    )


# --- Page 2: Input Features ---
def input_page():
    st.markdown(
        "<h1 style='text-align: center; color: #87CEEB;'><b>Predict the Movie Review is Negative or Positive:</b></h1>",
        unsafe_allow_html=True
    )

    review = st.text_area("Enter the Review")

    if st.button('Predict'):
        if not review.strip():  # Check for empty or whitespace-only input
            st.warning("⚠️ Please enter a review before predicting.")
        else:
            model = pickle.load(open('lg.sav', 'rb'))
            vec = pickle.load(open('vect.sav', 'rb'))
            pred = model.predict(vec.transform([review]).toarray())

            if pred == 0:
                st.error(f"❌ Negative Review")
            else:
                st.success(f"✅ Positive Review")
            # else:
            #     st.warning("⚠️ No prediction available.")

# --- Page 3: Prediction ---
def Data_Source():
    st.title("Example 1")
    st.text("Oh, *Thug Life*, where do I even start with this overcooked Tamil gangster casserole? Mani Ratnam and Kamal Haasan, the dream team behind *Nayakan*, promised us a gritty crime epic but instead served a 163-minute snoozefest that’s about as thrilling as a traffic jam in Chennai. The screenplay? A recycled mess of gangster clichés so predictable you could write it in your sleep—and trust me, you’ll want to. The first half teases some promise with Kamal’s intense brooding and Silambarasan TR’s electric swagger, but the second half crashes harder than a knockoff Vespa, dragging on like a lecture on tax law. Trisha’s role is so pointless it feels like she wandered onto the set by mistake, and don’t get me started on the half-baked romantic subplots that fizzle out faster than a damp firecracker. Sure, Ravi K. Chandran’s cinematography is gorgeous, and A.R. Rahman’s score tries to carry this sinking ship, but no amount of polish can save a story that’s basically *Scarface* meets a PowerPoint presentation gone wrong. *Thug Life* wants to be a cult classic but ends up as a cautionary tale: even legends can churn out a dud. Save your ticket money for a good biryani instead.")
    st.title("Example 2")
    st.text("A quirky comedy that has a subliminal message about gender disparity and a distorted idea of masculinity.  The film subtly yet powerfully highlights how women's needs are often overlooked or dismissed, reflecting a deeper societal conditioning that teaches women to suppress their desires and emotions. Instead of being encouraged to express their full selves, they are trained—both explicitly and implicitly—to cater to men's egos and conform to male-defined standards of behavior, value, and worth. This quiet tension underscores a broader commentary on gender dynamics. It's difficult  for people with low emotional intelligence to fully grasp the essence of this movie.")

    st.title("Data Source")
    st.write("Data Source:")
    st.link_button("Kaggle", "https://www.kaggle.com/datasets/yasserh/imdb-movie-ratings-sentiment-analysis")
    st.write('Colab Link:')
    st.link_button("Colab", "https://colab.research.google.com/drive/1ti5Q4eyTDAmsLSuqm1TJ8-cFKVIeWf0k?usp=sharing")

# --- Navigation ---
pages = [
    st.Page(home_page, title="Home"),
    st.Page(input_page, title="Input Features"),
    st.Page(Data_Source, title="Data Source")
]

with st.sidebar:
    selected = st.navigation(pages, position="sidebar", expanded=True)

selected.run()
