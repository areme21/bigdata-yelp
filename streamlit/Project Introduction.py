import streamlit as st

st.set_page_config(
    page_title="Big Data Final Project - Yelp"
)

st.title("Big Data Final Project - Yelp")

st.write("Our group was interested in examining what aspects of a business lead to business success and what customers value in a business. Many business owners want to know what is important to their customers, because customer experience drives their success. Online platforms, such as Yelp, allow customers to provide feedback to a business and share their sentiment with other potential customers. As such, Yelp reviews provide up-to-date and nearly automatic feedback from current customers. Although the traditional use of Yelp is to allow prospective customers to learn about a business from other customers, we believe that Yelp can provide valuable information for businesses too.")
st.write("We will be focusing specifically on restaurants in Philadelphia, using Yelp reviews and characteristics of the business for our analysis.")
st.write("For the first part of this project, we will be predicting how successful a restaurant is based on characteristics of the restaurant. For example, a coffee shop may be more successful in one zip code compared to another, or perhaps features like offering free wifi are important to restaurant success. The end goal of this part is to create a model with an interface in which prospective restaurants can enter in characteristics of their proposed restaurant (such as the number of days they are open, where they are located, and so on) and see how successful they will be. We are measuring success as a yelp score ranging from 1 to 5 which is calculated based on number of reviews and star ratings, which is explained in more detail later on. Ideally, this tool will be used by prospective businesses or investors to predict how successful opening a business will be, and how they could increase success by adjusting certain characteristics (like location or other features).")
st.write("For the second part of this project, we are curious about what the customer feedback from a site like Yelp can tell us about what customers value. By analyzing reviews from Yelp users with natural language processing, we hope to gain insights into customer values.")
st.write("We recognize there are limitations in the dataset, and that inherently assumptions are made when analyzing this prepared dataset. We discuss these considerations in the conclusion section.")
