import streamlit as st
import folium
from folium import plugins
import streamlit_folium as sf
import pandas as pd
import streamlit.components.v1 as com

st.title("Data")

st.header("Data Cleaning")
st.write("For this project, we used a [dataset](https://www.yelp.com/dataset/documentation/main) provided directly from Yelp. This dataset has multiple json files, including a file for all businesses and another file for reviews. Exploring the dataset in its entirety, we found which states, cities, and zip codes were most represented. We wanted our analysis to balance capturing idiosyncrasies among geographic locations with some level of generalizability. Thus, we decided to constrain our analysis to cities. The most represented cities in the business.json dataset were as follows:")
st.write("{'Philadelphia': 14569, 'Tucson': 9250, 'Tampa': 9050, 'Indianapolis': 7540, 'Nashville': 6971, 'New Orleans': 6209, 'Reno': 5935, 'Edmonton': 5054, 'Saint Louis': 4827, 'Santa Barbara': 3829}")
st.write("We were intrigued with the number of observations within Philadelphia, and felt as though it would be a great, diverse, and historically rich option to begin our analysis on.")
st.write("Preprocessing this data to get it into a format that was usable for our model was a long, multi-step process. For our random forest model that will be used to predict a restaurant’s success based on certain characteristics of the restaurant, we primarily used the business dataset from Yelp as well as data on income at the zip code level for every zip code in Philadelphia from the Census’ [American Community Survey](https://www.census.gov/programs-surveys/acs/data.html).")
st.write("The business json from Yelp has multiple fields such as business id, name, zip code, average star rating, number of reviews, an extensive json of business attributes, a list of categories, and hours. First we filtered this json of all businesses in Philadelphia to only look at businesses that are restaurants. This left us with 5,852 restaurants. ")
st.write("There were 53 restaurants that had no attributes listed, and 23 restaurants that had no categories listed. We decided to drop these rows since we felt they didn’t have enough information to be included in our model. After dropping these restaurants, we were left with 5,776 restaurants.")
st.write("We then parsed through the attributes section of the json to turn each attribute into a column with the value of that attribute. We capped the percentage of missing values at 30 percent, so if an attribute was not listed in more than 30 percent of the restaurants, we did not include this attribute. In the end, we were left with 14 of the top-listed attributes :")
st.write("{'RestaurantsTakeOut',  'RestaurantsDelivery', 'BusinessAcceptsCreditCards',   'BusinessParking',  'RestaurantsPriceRange2', 'OutdoorSeating', 'RestaurantsReservations', 'RestaurantsGoodForGroups', 'HasTV',  'Alcohol', 'GoodForKids', 'Ambience', 'RestaurantsAttire', 'WiFi'}")
st.write("Most of these attributes have values that are booleans, but 'BusinessParking' and 'Ambience' were further broken down into columns based on their subcategories.")
st.write("If an attribute was not listed in a restaurant’s json of attributes, we first labeled the value for this attribute as ‘missing’. If a restaurant was missing more than half of the attributes listed above, then that restaurant was dropped from the dataset. 760 restaurants met this condition (13 percent of the dataset), and they were dropped. After this processing, we were left with a dataset containing 5,016 restaurants.")
st.write("If a restaurant listed at least half of the attributes but didn’t list a certain attribute, this attribute was assumed to not apply to this business, and the ‘missing’ value was replaced with False. We think this is a fair assumption because if a restaurant has listed certain attributes about itself, but did not include a particular one, it is likely that they don’t have that attribute and didn’t take the time to select it just to say False.")
st.write("A similar process was done to get the categories field into a usable format. First, we found the top 30 categories shared across the restaurants, and converted these into columns. In the original json, the categories field looked like ‘categories’: [ ‘Mexican’, ‘Burgers’, ‘Gastropubs’ ], so if the category was listed in this list, the restaurant received a True value in this category, if not, the restaurant was assumed to not fall into this category and was labeled as False.")
st.write("Preprocessing was also done on the hours column to determine how many days a week a business was open and the average hours open per day. Missing days open and average hours were replaced with the mean. The only other column with missing data at this point was the price range column, in which prices were labeled from ($ to $$$$). Missing entries were replaced with the mode, which was $$ but this was a negligible part of the dataset. At this point, the data from the Yelp business dataset was complete.")
st.write("Data was downloaded from the Census with median household income from each zip code in Philadelphia and combined with the dataset above using the zip code of the business. If a zipcode’s income was missing, it was replaced with the average of the median income column.")
st.write("A yelp score was calculated for each restaurant based on a function of the restaurant's average star rating and the number of reviews a restaurant has. The details on how this was calculated are in the Tree Model section, and this yelp score is how we are measuring the success of a business. A **yelp score** of 5 is the best, and 1 is the worst.")
st.write("The final dataset includes columns for business identifiers and location, 15 columns for the main attributes as well as additional columns for the ambiance attribute, the top 30 categories of restaurants, and median household income. This file can be viewed [here](https://drive.google.com/file/d/155P7hELF5FEt9nwqFArbZFKrUuRL9HZg/view?usp=sharing).")

st.header("Data Exploration")
st.write("Looking at the distribution of the data, we can see that the star ratings are approximately normally distributed, although they are skewed more to the high-end, and most restaurants have between 0 and 500 reviews, with some outliers as high as 5,000 reviews.  ")
st.image("streamlit/stars_reviews.png")
st.write("After using stars and review counts to create the yelp scores, we can see that the yelp scores are approximately evenly distributed, peaking around a score of 3.4 and ranging from around 1.5 to 5.")
st.image("streamlit/yelpscore.png")
st.write("Below is a heat map of the locations of the restaurants in the dataset. We can see that the restaurants are spread all throughout Philadelphia with the largest cluster in the center city / south. This cluster aligns with the most popular zip code in our dataset: 19107.")
def make_heatmap():
   all_csv = pd.read_csv('streamlit/final_clean.csv')
 
   location_data = list(zip(all_csv['latitude'], all_csv['longitude']))
 
   map2 = folium.Map(location=[all_csv.latitude.mean(), all_csv.longitude.mean()],
                   zoom_start=9,
                   control_scale=True,
                   tiles="OpenStreetMap")
 
   # plot heatmap
   map2.add_child(plugins.HeatMap(location_data, radius=15))
   map2.save('heatmap.html')
   map2
 
   hm_layer = plugins.HeatMap(location_data,
                   min_opacity=0.4,
                   radius=8,
                   blur=6,
                   )
   map2.add_child(hm_layer)
   return map2
 
# sf.st_folium(make_heatmap())
st.write("Looking closer at the attributes data, we can see the following chart that shows the distribution of several of the top attributes that have boolean values. We can see that for some attributes, like offering takeout, a vast majority offer takeout compared to only about 9% who don’t. However for another attribute, like offering reservations, only about 35 percent of restaurants in Philly offer reservations. ")
st.image("streamlit/top_rest_attributes.png")
st.write("As for categories, the top category that restaurants shared was Nightlife at 19.5% of restaurants. Other top categories include Bars, Sandwiches, Pizza, American (New), and Breakfast & Brunch. See the wordcloud below for more of the top categories.")
com.html("""<div class='tableauPlaceholder' id='viz1670789136667' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;RestaurantCategories&#47;Sheet1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='RestaurantCategories&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;RestaurantCategories&#47;Sheet1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1670789136667');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>""", height=1000)
st.write("Overall, our dataset includes a wide variety of restaurants with different locations, attributes, and categories. Next we will move onto using this data to create a model to predict a business’s Yelp Score.")