import streamlit as st

st.title("Interpretation")

st.write("The model to predict Yelp Score based on a variety of features was built using a random forest algorithm. We thought it would be a good model to use considering the many features we had (120). Before creating the random forest, we calculated and added Yelp Score to our data. Yelp Score was calculated as a function of star rating and number of reviews using a Bayesian average. The formula was (stars * review count + (mean stars * 25th percentile of review counts)) / (review count + 25th percentile of review counts). We settled on this method of a Yelp Score because a restaurant’s star rating does not paint a complete picture. We wanted to ensure a restaurant with a 4.7 star rating and 1000 reviews would have a higher Yelp Score than a restaurant with a 5 star rating and only 1 review.")
st.write("For our random forest model, we used 1000 trees and decided to bootstrap our data to encourage diverse trees and reduce overfitting. To decide the maximum depth of each tree in the forest, we plotted mean squared error as maximum depth increased:")
st.image("streamlit/mse_v_treedepth.png")
st.write("We minimize MSE at a maximum depth of 17, which we use. Above that, there appears to be some overfitting.")
st.write("Using these parameters, we return a final mean squared error of about .177. We believe this is a good error value for our model, as this small squared error would not, on average, change the meaning of a restaurant’s Yelp Score.")