import streamlit as st

st.title("Yelp Review Conclusions")

st.write("There is great value for businesses to go through and see a quantifiable metric on what properties customers care enough to report. While each restaurant category has its own idiosyncrasies, there are a few conclusions that can be drawn across all observations.")
st.subheader("1. Comparing menu items in five star vs. one star reviews can be valuable")
st.write("A reason we chose to include so many common words (50) was to be able to capture some of the more unique yet not as common words in each restaurant category. Finding one menu item or restaurant feature on the collection of common five star words, but not on the collection of common one star words, should catch the attention of restaurant owners. For example, the word 'korean' is associated with 8 of the top 50 positive words in five-star reviewed Chicken Wing restaurants. However, there are no references to 'korean' in any of the one-star reviews, implying that korean chicken wings are a well-liked menu item.")
st.subheader("2. There is a strong emphasis on service quality ")
st.write("Service usually cracks the top 10 in both 1 star and 5 star reviews for all categories, implying that it is a feature customers value. Further analysis on whether this prioritization of service has been affected by the pandemic would be an interesting avenue of continued research.")
st.subheader("3. Philadelphia-specific characteristics are consistently captured by both Word Clouds and Word2Vec")
st.write("Bars commonly reference geographic location, suggesting a relationship between bars and future plans for the evening. There are also frequent references to 'Reading Terminal', which is Philly’s famous indoor farmers market. The fact that there existed enough observations to generate insights about Cheesesteak restaurants is also indicative of Philadelphia’s food culture.")
st.subheader("4. Word2Vec results on 5 star reviews may be more insightful")
st.write("One star reviews tend to revert almost exclusively common descriptors such as 'bad', 'terrible', and 'poor' to describe their experience. On the other hand, five star reviews tend to capture more nuances about what made the restaurant so great. For example, 'authentic' is the most likely word to be associated with 'food' for Mexican restaurants. A hypothesis for this is that five star reviews are generally more well-thought out.")