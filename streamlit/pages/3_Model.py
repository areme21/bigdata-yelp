import streamlit as st
import randomforest as rf
import numpy as np
import pandas as pd
import folium
import streamlit_folium as sf

st.set_page_config(
    page_title="Big Data Final Project - Yelp"
)

st.title("Big Data Final Project - Yelp")
days_open = st.slider("How many days a week will you be open?", 0, 7)
# avg_hours_open = st.number_input("What is the average number of hours you are open each day?", max_value=24.0)
zip_code = st.selectbox("In what Philadelphia zip code will you be located?", (19107, 19106, 19147, 19127, 19123, 19104, 19130, 19124, 19139, 19115,
 19146, 19103, 19126, 19131, 19114, 19121, 19154, 19143, 19134, 19102,
 19128, 19111, 19118, 19153, 19141, 19129, 19148, 19120, 19151, 19119,
 19122, 19149, 19176, 19136, 19135, 19145, 19152, 19125, 19138, 19116,
 19144, 19112, 19137, 19132, 19133, 19140, 19142, 19150, 19195, 19155,
 19113, 19454, 19019, 19092))

zip_income = pd.read_csv('streamlit/zip_to_med_income.csv')
median_income = zip_income.loc[zip_income['postal_code'] == zip_code, 'median_income'].iloc[0]

attributes = st.multiselect("Select restaurant attributes", \
    ['Delivery', 'Takeout', 'Accept Credit Cards', 'Outdoor Seating', 'Reservations',\
        'Good for Groups', 'Has TV', 'Alcohol', 'Good for Kids'])

wifi = st.radio("WiFi?", ['Free WiFi', 'No WiFi', 'Paid WiFi'])

attire = st.radio("Attire?", ['Casual', 'Dressy', 'Formal', 'Other'])

categories = st.multiselect("Restaurant Categories", ['Nightlife', 'Bars', 'Sandwiches', 'Pizza',\
    'American (New)', 'Breakfast & Brunch', 'American (Traditional)', 'Coffee & Tea', \
        'Italian', 'Chinese', "Fast Food", "Burgers", "Seafood", "Cafes", "Mexican", \
            "Delis", "Event Planning & Services", "Salad", "Specialty Food", "Chicken Wings",\
                 "Bakeries", "Japanese", "Asian Fusion", "Vegetarian", "Caterers", "Desserts",\
                     "Sushi Bar", "Mediterranean", "Cheesesteaks", "Pubs"])

ambience = st.multiselect("Restaurant Ambience", ['Touristy', 'Hipster', 'Romantic', 'Divey',\
    'Intimate', 'Trendy', 'Upscale', 'Classy', 'Casual'])

parking = st.multiselect("Parking", ['Garage', 'Street', 'Validated', 'Lot', 'Valet'])

price_range = st.radio("Price Range?", ['$', '$$', '$$$', '$$$$'])



takeout = 1 if "Takeout" in attributes else 0
delivery = 1 if "Delivery" in attributes else 0
accepts_credit = 1 if "Accept Credit Cards" in attributes else 0
high_price_range = 1 if price_range == '$$$' or price_range == '$$$$' else 0
outdoor_seating = 1 if "Outdoor Seating" in attributes else 0
reservations = 1 if "Reservations" in attributes else 0
good_groups = 1 if 'Good for Groups' in attributes else 0
has_tv = 1 if 'Has TV' in attributes else 0
alcohol = 1 if 'Alcohol' in attributes else 0
good_kids = 1 if 'Good for Kids' in attributes else 0
restaurants = 1
food = 1
nightlife = 1 if 'Nightlife' in categories else 0
bars = 1 if 'Bars' in categories else 0
sandwiches = 1 if 'Sandwiches' in categories else 0
pizza = 1 if 'Pizza' in categories else 0
american_new = 1 if 'American (New)' in categories else 0
breakfast_brunch = 1 if 'Breakfast & Brunch' in categories else 0
american_traditional = 1 if 'American (Traditional)' in categories else 0
coffee_tea = 1 if 'Coffee & Tea' in categories else 0
italian = 1 if 'Italian' in categories else 0
chinese = 1 if 'Chinese' in categories else 0
fast_food = 1 if 'Fast Food' in categories else 0
burgers = 1 if 'Burgers' in categories else 0
seafood = 1 if 'Seafood' in categories else 0
cafes = 1 if 'Cafes' in categories else 0
mexican = 1 if 'Mexican' in categories else 0
delis = 1 if 'Delis' in categories else 0
event_planning = 1 if 'Event Planning & Services' in categories else 0
salad = 1 if 'Salad' in categories else 0
specialty_food = 1 if 'Specialty Food' in categories else 0
chicken_wings = 1 if 'Chicken Wings' in categories else 0
bakeries = 1 if 'Bakeries' in categories else 0
japanese = 1 if 'Japanese' in categories else 0
asian_fusion = 1 if 'Asian Fusion' in categories else 0
vegetarian = 1 if 'Vegetarian' in categories else 0
caterers = 1 if 'Caterers' in categories else 0
desserts = 1 if 'Desserts' in categories else 0
sushi_bars = 1 if 'Sushi Bar' in categories else 0
mediterranean = 1 if 'Mediterranean' in categories else 0
cheesesteaks = 1 if 'Cheesesteaks' in categories else 0
pubs = 1 if 'Pubs' in categories else 0
touristy = 1 if 'Touristy' in ambience else 0
hipster = 1 if 'Hipster' in ambience else 0
romantic = 1 if 'Romantic' in ambience else 0
divey = 1 if 'Divey' in ambience else 0
intimate = 1 if 'Intimate' in ambience else 0
trendy = 1 if 'Trendy' in ambience else 0
upscale = 1 if 'Upscale' in ambience else 0
classy = 1 if 'Classy' in ambience else 0
casual = 1 if 'Casual' in ambience else 0
garage = 1 if 'Garage' in parking else 0
street = 1 if 'Street' in parking else 0
validated = 1 if 'Validated' in parking else 0
lot = 1 if 'Lot' in parking else 0
valet = 1 if 'Valet' in parking else 0
days_open = days_open# days_open is set
median_income = median_income# need to get median_income
mean_income = 0# need to get mean_income
attire_casual = 1 if attire == "Casual" else 0
attire_dressy = 1 if attire == "Dressy" else 0
attire_formal = 1 if attire == "Formal" else 0
attire_other = 1 if attire == "Other" else 0
wifi_free = 1 if wifi == "Free WiFi" else 0
wifi_no = 1 if wifi == "No WiFi" else 0
wifi_paid = 1 if wifi == "Paid WiFi" else 0
high_median_income = 1
postal_code_0 = 0
postal_code_19019 = 1 if zip_code == 19019 else 0
postal_code_19092 = 1 if zip_code == 19092 else 0
postal_code_19102 = 1 if zip_code == 19102 else 0
postal_code_19103 = 1 if zip_code == 19103 else 0
postal_code_19104 = 1 if zip_code == 19104 else 0
postal_code_19106 = 1 if zip_code == 19106 else 0
postal_code_19107 = 1 if zip_code == 19107 else 0
postal_code_19111 = 1 if zip_code == 19111 else 0
postal_code_19112 = 1 if zip_code == 19112 else 0
postal_code_19113 = 1 if zip_code == 19113 else 0
postal_code_19114 = 1 if zip_code == 19114 else 0
postal_code_19115 = 1 if zip_code == 19115 else 0
postal_code_19116 = 1 if zip_code == 19116 else 0
postal_code_19118 = 1 if zip_code == 19118 else 0
postal_code_19119 = 1 if zip_code == 19119 else 0
postal_code_19120 = 1 if zip_code == 19120 else 0
postal_code_19121 = 1 if zip_code == 19121 else 0
postal_code_19122 = 1 if zip_code == 19122 else 0
postal_code_19123 = 1 if zip_code == 19123 else 0
postal_code_19124 = 1 if zip_code == 19124 else 0
postal_code_19125 = 1 if zip_code == 19125 else 0
postal_code_19126 = 1 if zip_code == 19126 else 0
postal_code_19127 = 1 if zip_code == 19127 else 0
postal_code_19128 = 1 if zip_code == 19128 else 0
postal_code_19129 = 1 if zip_code == 19129 else 0
postal_code_19130 = 1 if zip_code == 19130 else 0
postal_code_19131 = 1 if zip_code == 19131 else 0
postal_code_19132 = 1 if zip_code == 19132 else 0
postal_code_19133 = 1 if zip_code == 19133 else 0
postal_code_19134 = 1 if zip_code == 19134 else 0
postal_code_19135 = 1 if zip_code == 19135 else 0
postal_code_19136 = 1 if zip_code == 19136 else 0
postal_code_19137 = 1 if zip_code == 19137 else 0
postal_code_19138 = 1 if zip_code == 19138 else 0
postal_code_19139 = 1 if zip_code == 19139 else 0
postal_code_19140 = 1 if zip_code == 19140 else 0
postal_code_19141 = 1 if zip_code == 19141 else 0
postal_code_19142 = 1 if zip_code == 19142 else 0
postal_code_19143 = 1 if zip_code == 19143 else 0
postal_code_19144 = 1 if zip_code == 19144 else 0
postal_code_19145 = 1 if zip_code == 19145 else 0
postal_code_19146 = 1 if zip_code == 19146 else 0
postal_code_19147 = 1 if zip_code == 19147 else 0
postal_code_19148 = 1 if zip_code == 19148 else 0
postal_code_19149 = 1 if zip_code == 19149 else 0
postal_code_19150 = 1 if zip_code == 19150 else 0
postal_code_19151 = 1 if zip_code == 19151 else 0
postal_code_19152 = 1 if zip_code == 19152 else 0
postal_code_19153 = 1 if zip_code == 19153 else 0
postal_code_19154 = 1 if zip_code == 19154 else 0
postal_code_19155 = 1 if zip_code == 19155 else 0
postal_code_19176 = 1 if zip_code == 19176 else 0
postal_code_19195 = 1 if zip_code == 19195 else 0
postal_code_19454 = 1 if zip_code == 19454 else 0

sample = np.array([takeout, delivery, accepts_credit, high_price_range, outdoor_seating, reservations,\
    good_groups, has_tv, alcohol, good_kids, restaurants, food, nightlife, bars, \
        sandwiches, pizza, american_new, breakfast_brunch, american_traditional, coffee_tea, \
            italian, chinese, fast_food, burgers, seafood, cafes, mexican, delis, event_planning, \
                salad, specialty_food, chicken_wings, bakeries, japanese, asian_fusion, vegetarian, \
                    caterers, desserts, sushi_bars, mediterranean, cheesesteaks, pubs, \
                        touristy, hipster, romantic, divey, intimate, trendy, upscale, \
                            classy, casual, garage, street, validated, lot, valet, days_open, median_income,\
                                attire_casual, attire_dressy, attire_formal, attire_other, wifi_free,\
                                    wifi_no, wifi_paid, postal_code_0, postal_code_19019, postal_code_19092, \
                                        postal_code_19102, postal_code_19103, postal_code_19104, postal_code_19106, postal_code_19107,\
                                            postal_code_19111, postal_code_19112, postal_code_19113, postal_code_19114, postal_code_19115, \
                                                postal_code_19116, postal_code_19118, postal_code_19119, postal_code_19120, postal_code_19121, \
                                                    postal_code_19122, postal_code_19123, postal_code_19124, postal_code_19125, postal_code_19126, postal_code_19127, postal_code_19128, postal_code_19129,\
                                                        postal_code_19130, postal_code_19131, postal_code_19132, postal_code_19133, postal_code_19134, postal_code_19135, postal_code_19136, postal_code_19137, postal_code_19138, postal_code_19139,\
                                                            postal_code_19140, postal_code_19141, postal_code_19142, postal_code_19143, postal_code_19144, postal_code_19145, postal_code_19146, postal_code_19147, postal_code_19148, postal_code_19149, \
                                                                postal_code_19150, postal_code_19151, postal_code_19152, postal_code_19153, postal_code_19154, postal_code_19155, postal_code_19176, postal_code_19195, postal_code_19454])
pred = rf.randomforest.predict(sample.reshape(1, -1))

clean_csv = pd.read_csv('streamlit/final_clean.csv')

def plot_cat_in_zip(cat: list, zip):
    # cat input must be a list of names of category columns
    filter_cat = False
    for category in cat:
        filter_cat = filter_cat | (clean_csv[category] == 1)
    data = clean_csv[(clean_csv['postal_code'] == zip) & filter_cat]

    if (len(data) == 0):
        print("no {} in {}".format(cat, zip))
        return

    data_map = folium.Map(location=[data.latitude.mean(), data.longitude.mean()],
                    zoom_start=14,
                    control_scale=True)

    for i, row in data.iterrows():
        iframe = folium.IFrame(str(row["name"]), "50%", ratio="30%")
        popup = folium.Popup(iframe, min_width=300, max_width=300)
        folium.Marker(location=[row['latitude'],row['longitude']],
                  popup = popup, c=row['postal_code']).add_to(data_map)

    return data_map
if len(categories) != 0:
    button = st.button("Find Yelp Score!")
    if button:
        st.subheader("Your predicted Yelp Score: " + str(round(pred[0], 2)))
    map = plot_cat_in_zip(categories, zip_code)
    st.write("**Restaurants in your zip code with at least 1 of the same categories:**")
    st_map = sf.st_folium(map, width=700, height=500)
else:
    button = st.button("Find Yelp Score!")
    if button:
        st.subheader("Your predicted Yelp Score: " + str(round(pred[0], 2)))

# this csv needs to be the final clean csv that still has latitude, longitude columns

# example:
# plot_cat_in_zip(['Coffee & Tea', "Pizza"], 19115)

# example that doesn't work
# plot_cat_in_zip(['Coffee & Tea', "Pizza"], 80000)
