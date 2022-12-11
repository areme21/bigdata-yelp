import streamlit as st

st.title("NLP")

st.image('streamlit/bigramCloud.png')

st.write("What do reviews reveal what customers look for in a restaurant? This was the question we sought to tackle in the second part of our project, which took on more of an exploratory approach.")
st.write("Before starting, we tried to get a better feel for our data by making some plots. We see that customers most often leave 5 star reviews, and are in general more positive in the ratings they write. We also observe that the average star rating left by reviewers has been relatively stable at around 3.9 stars through the years.")
st.image("streamlit/distrubution_cust_rating.png")
st.image("streamlit/avg_monthly_cust_rating.png")
st.write("We began our review text analysis by finding the most common words (not including [stop words](https://en.wikipedia.org/wiki/Stop_word)) in all concatenated reviews. The top five words were [‘food’, ‘place’, ‘good’, ‘great’, ‘like’]. While great for getting a feel for the data, we found these to be generally unhelpful as they lacked context. In other words, we are able to understand what customers write about, but cannot confidently infer why they feel compelled to write about certain things.")
st.write("For such reasons, we next explored looking into two and three word phrases. We used scikit-learn’s packages to vectorize and find frequencies of the fifty most common bigrams and trigrams. Due to runtime issues, we were only able to run our bigram and trigram function on a one percent sample of our dataset (around 7,000 reviews).")
st.write("**50 Most Common Bigrams on 1 percent sample of the dataset**")
st.image("streamlit/common_bigrams.png")
st.write("**50 Most Common Trigrams on 1 percent sample of the dataset**")
st.image("streamlit/common_trigrams.png")
st.write("These bigrams and trigrams definitely provided us with a greater sense of what insights, advice, and overall impressions customers leave on restaurants. Yet, considering only consecutive words limits our window of observation. In reality, we utilize words in a more free-flowing manner; just because words are close to one another does not imply they build on the same idea. The nature of grammar creates natural literary breaks, filler words, and prepositions between phrases that are semantically related.")
st.write("To work around this, we explored Word2Vec, a neural network trained to reconstruct linguistics and context. By taking in words and vectoring them, Word2Vec is able to plot words of similar semantics in multidimensional plots, and calculate distance between such words. There are two ways of implementing Word2Vec: continuous-bag-of-words (CBOW) and skip-gram. Research has shown that CBOW does a better job finding frequent words, so we decided to opt for that approach.")
st.write("Before creating a model, we made two key observations and data design decisions. First, was the fact that we wanted to differentiate between what constitutes a “good” review versus a “bad” review, which we achieved by filtering by five-star reviews and one-star reviews. The assumption we made here was that nearly all opinions left in five-star reviews were positive, and nearly all opinions left in one-star reviews were negative. Manual observation from a handful of reviews confirmed our assumption. Our second decision was to run Word2Vec separately for different restaurant categories. The reason for this was the suspicion that different types of restaurants would offer different menu options, ambience, and overall experience.")
st.write("Thus, the Word2Vec running process went as follows:")
st.write("1. Find the most common words in five-star reviews for each restaurant category")
st.write("2. Use those words to run Word2Vec for five star reviews")
st.write("3. Find the most common words in one-star reviews for each restaurant category")
st.write("4. Use those words to run Word2Vec for one star reviews")
st.write("We chose to run Word2Vec on different sets of words because reviews tend to be biased positively. Thus, it made sense to treat one-star reviews and five-star reviews differently, and provide the model with unique inputs for each review type.")
st.write("Of the top 32 restaurant categories, we selected the following in the dropdown based on the diversity of reviews.")
category = st.selectbox("Choose a category", ["Bakeries", "Bars", "Cheesesteaks", "Chicken Wings", "Chinese",\
    "Coffee & Tea", "Fast Food", "Italian", "Mexican", "Sandwiches"])
st.write("**How to Interpret Results:**")
st.write("Once a restaurant category is selected, you will see three graphs and some text results. The distribution of customer ratings gives a general idea of the general sentiment of reviews. Each restaurant category has different focal points in reviews, which are captured in the two word clouds: the former are top 50 most common words on all reviews, the latter are the top 50 most common bigrams for all reviews.")
st.write("The text output shows each common word, and the top five words associated with it. The decimals represent the probability of finding the pair of words in the same context.")
if category == "Bakeries":
    st.image("streamlit/bakeries/customer_rating.png")
    st.image("streamlit/bakeries/wordCloud.png")
    st.image("streamlit/bakeries/bigramCloud.png")
    st.write("**Five Star Reviews**")
    st.write("place : [('love', 0.027094668), ('go-to', 0.011242716), ('awesome', 0.008314155), ('great', 0.0061796913), ('eat', 0.0054849065)]")
    st.write("great : [('service', 0.0036539978), ('atmosphere', 0.0030800267), ('vibe', 0.0019242186), ('spot', 0.0017979345), ('food', 0.0016875262)]")
    st.write("food : [('soul', 0.0019857867), ('quality', 0.0019079229), ('diverse', 0.001684795), ('excellent', 0.0016542719), ('court', 0.0014615428)]")
    st.write("")