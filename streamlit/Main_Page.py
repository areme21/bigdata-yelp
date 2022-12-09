import streamlit as st

st.set_page_config(
    page_title="Big Data Final Project - Yelp"
)

st.title("Big Data Final Project - Yelp")
st.sidebar.success("Select page")
st.slider("How many days a week are you open?", 0, 7)
st.number_input("What is the average number of hours you are open each day?", max_value=24.0)
st.selectbox("In what Philadelphia zip code are you located?", (19107, 19106, 19147, 19127, 19123, 19104, 19130, 19124, 19139, 19115,
 19146, 19103, 19126, 19131, 19114, 19121, 19154, 19143, 19134, 19102,
 19128, 19111, 19118, 19153, 19141, 19129, 19148, 19120, 19151, 19119,
 19122, 19149, 19176, 19136, 19135, 19145, 19152, 19125, 19138, 19116,
 19144, 19112, 19137, 19132, 19133, 19140, 19142, 19150, 19195, 19155,
 19113, 19454, 19019, 19092))

st.multiselect("Select restaurant attributes", \
    ['Delivery', 'Takeout', 'Accept Credit Cards', 'Outdoor Seating', 'Reservations',\
        'Good for Groups', 'Has TV', 'Alcohol', 'Good for Kids'])

st.radio("WiFi?", ['Free WiFi', 'No WiFi', 'Paid WiFi'])

st.radio("Attire?", ['Casual', 'Dressy', 'Formal', 'Other'])

st.multiselect("Restaurant Categories", ['Nightlife', 'Bars', 'Sandwiches', 'Pizza',\
    'American (New)', 'Breakfast & Brunch', 'American (Traditional)', 'Coffee & Tea', \
        'Italian', 'Chinese', "Fast Food", "Burgers", "Seafood", "Cafes", "Mexican", \
            "Delis", "Event Planning & Services", "Salad", "Specialty Food", "Chicken Wings",\
                 "Bakeries", "Japanese", "Asian Fusion", "Vegetarian", "Caterers", "Desserts",\
                     "Sushi Bar", "Mediterranean", "Cheesesteaks", "Pubs"])

st.multiselect("Restaurant Ambience", ['Touristy', 'Hipster', 'Romantic', 'Divey',\
    'Intimate', 'Trendy', 'Upscale', 'Classy', 'Casual'])

st.multiselect("Parking", ['Garage', 'Street', 'Validated', 'Lot', 'Valet'])