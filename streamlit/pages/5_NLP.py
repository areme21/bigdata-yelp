import streamlit as st

st.title("NLP")

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
    st.write("good : [('really', 0.00503906), ('pretty', 0.0029145924), ('baked', 0.0015816826), ('tasted', 0.0015099634), ('damn', 0.001278953)]")
    st.write("one : [('places', 0.003898391), ('favorite', 0.0020543486), ('probably', 0.001434693), ('eaten', 0.0012591118), ('thing', 0.001134365)]")
    st.write("best : [('ever', 0.07968066), ('city', 0.030001892), ('philadelphia', 0.011668629), ('hands', 0.007379711), ('part', 0.005066734)]")
    st.write("get : [('early', 0.0044759973), ('usually', 0.002103638), ('hard', 0.0015536383), ('sure', 0.0014974619), ('donuts', 0.0012729755)]")
    st.write("go : [('wrong', 0.015347903), ('back', 0.006945573), ('must', 0.0049468554), ('want', 0.0037998431), ('hungry', 0.0032136156)]")
    st.write("love : [('love', 0.0023175804), ('place', 0.0020493055), ('absolutely', 0.0018938545), ('much', 0.0015932196), ('coming', 0.0012987027)]")
    st.write("like : [('feel', 0.0046502724), ('feels', 0.002451075), ('tastes', 0.0023518845), ('looks', 0.0021489055), ('felt', 0.002002553)]")
    st.write("delicious : [('absolutely', 0.002210935), ('everything', 0.002147205), ('pastries', 0.0011553373), ('food', 0.0010118), ('cappuccino', 0.0009094204)]")
    st.write("also : [('ordered', 0.0012056866), ('got', 0.0011174349), ('tea', 0.0008944834), ('tried', 0.00089245546), ('enjoyed', 0.0008690088)]")
    st.write("coffee : [('tea', 0.04069004), ('iced', 0.0257961), ('cup', 0.01660676), ('bubble', 0.016455833), ('shop', 0.011431669)]")
    st.write("time : [('next', 0.3164644), ('every', 0.17941159), ('first', 0.047879897), ('last', 0.008741783), ('long', 0.00720109)]")
    st.write("really : [('good', 0.0038235816), ('enjoyed', 0.0020579093), ('liked', 0.0020171397), ('really', 0.0016268702), ('nice', 0.0014443098)]")
    st.write("i've : [('awesome', 0.00024741585), ('right', 0.00023378228), ('loved', 0.00023177378), ('real', 0.0002272466), ('top', 0.00022221783)]")
    st.write("philly : [('south', 0.04097974), ('visiting', 0.011180897), ('visit', 0.0077669225), ('staple', 0.0042876084), ('cheesesteak', 0.004151255)]")
    st.write("cake : [('birthday', 0.07972915), ('wedding', 0.041719366), ('carrot', 0.033406556), ('pound', 0.022022776), ('shower', 0.0076979417)]")
    st.write("back : [('coming', 0.040458266), ('come', 0.03060994), ('soon', 0.0113789765), ('going', 0.010935964), ('definitely', 0.0060010892)]")
    st.write("try : [('must', 0.041357372), ('wait', 0.015863337), ('decided', 0.005830778), ('next', 0.0033726443), ('gotta', 0.003267857)]")
    st.write("chocolate : [('chip', 0.3028401), ('dark', 0.0075482945), ('peanut', 0.0070995893), ('raspberry', 0.0062835673), ('hot', 0.005186766)]")
    st.write("amazing : [('absolutely', 0.0027742004), ('service', 0.0015455857), ('donuts', 0.0013749914), ('doughnuts', 0.0011423195), ('cookies', 0.0010793519)]")
    st.write("fresh : [('baked', 0.04711717), ('produce', 0.019741543), ('meats', 0.009093244), ('made', 0.008048557), ('vegetables', 0.0070396354)]")
    st.write("always : [('fresh', 0.0019323332), ('always', 0.0016338282), ('bring', 0.0011487448), ('something', 0.0011309828), ('come', 0.0009114414)]")
    st.write("everything : [('else', 0.01100552), ('want', 0.0035851083), ('loved', 0.0030805964), ('tried', 0.0027742963), ('delicious', 0.002654554)]")
    st.write("i'm : [('large', 0.00030787216), ('small', 0.00030763456), ('nice', 0.00030592608), ('awesome', 0.00028400385), ('huge', 0.0002785396)]")
    st.write("definitely : [('worth', 0.048529662), ('recommend', 0.026786227), ('back', 0.0062088855), ('return', 0.0040910654), ('would', 0.0026375933)]")
    st.write("would : [('recommend', 0.34312433), ('suggest', 0.0034157562), ('say', 0.003012439), ('recommended', 0.0023352876), ('lived', 0.0013559879)]")
    st.write("market : [('reading', 0.010302861), ('farmer', 0.007434261), ('market', 0.0069332705), ('indoor', 0.0062715784), ('farmers', 0.005821264)]")
    st.write("got : [('friend', 0.0024943405), ('boyfriend', 0.0018437811), ('husband', 0.0017051573), ('home', 0.0015093216), ('recently', 0.0014267205)]")
    st.write("ever : [('best', 0.061967175), ('eaten', 0.015069834), ('tasted', 0.011711623), ('hands', 0.003933155), ('life', 0.0037491836)]")
    st.write("even : [('better', 0.008045791), ('though', 0.0049175317), ('made', 0.0011212305), ('free', 0.0010074452), ('pretty', 0.0009404546)]")
    st.write("make : [('sure', 0.21025419), ('home', 0.0040311953), ('trip', 0.0035773446), ('point', 0.0026565706), ('freshly', 0.0020292427)]")
    st.write("little : [('bit', 0.011599147), ('little', 0.0046085506), ('pricey', 0.00298932), ('cute', 0.0028557654), ('tiny', 0.0017235418)]")
    st.write("favorite : [('places', 0.007256956), ('philadelphia', 0.00651746), ('absolute', 0.0061408365), ('city', 0.0054711807), ('spots', 0.005242178)]")
    st.write("many : [('options', 0.054804735), ('choices', 0.019492693), ('places', 0.015908055), ('different', 0.0103797885), ('times', 0.008540983)]")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("""Five Star Reviews
place : [('love', 0.027094668), ('go-to', 0.011242716), ('awesome', 0.008314155), ('great', 0.0061796913), ('eat', 0.0054849065)]


great : [('service', 0.0036539978), ('atmosphere', 0.0030800267), ('vibe', 0.0019242186), ('spot', 0.0017979345), ('food', 0.0016875262)]


food : [('soul', 0.0019857867), ('quality', 0.0019079229), ('diverse', 0.001684795), ('excellent', 0.0016542719), ('court', 0.0014615428)]


good : [('really', 0.00503906), ('pretty', 0.0029145924), ('baked', 0.0015816826), ('tasted', 0.0015099634), ('damn', 0.001278953)]


one : [('places', 0.003898391), ('favorite', 0.0020543486), ('probably', 0.001434693), ('eaten', 0.0012591118), ('thing', 0.001134365)]


best : [('ever', 0.07968066), ('city', 0.030001892), ('philadelphia', 0.011668629), ('hands', 0.007379711), ('part', 0.005066734)]


get : [('early', 0.0044759973), ('usually', 0.002103638), ('hard', 0.0015536383), ('sure', 0.0014974619), ('donuts', 0.0012729755)]


go : [('wrong', 0.015347903), ('back', 0.006945573), ('must', 0.0049468554), ('want', 0.0037998431), ('hungry', 0.0032136156)]


love : [('love', 0.0023175804), ('place', 0.0020493055), ('absolutely', 0.0018938545), ('much', 0.0015932196), ('coming', 0.0012987027)]


like : [('feel', 0.0046502724), ('feels', 0.002451075), ('tastes', 0.0023518845), ('looks', 0.0021489055), ('felt', 0.002002553)]


delicious : [('absolutely', 0.002210935), ('everything', 0.002147205), ('pastries', 0.0011553373), ('food', 0.0010118), ('cappuccino', 0.0009094204)]


also : [('ordered', 0.0012056866), ('got', 0.0011174349), ('tea', 0.0008944834), ('tried', 0.00089245546), ('enjoyed', 0.0008690088)]


coffee : [('tea', 0.04069004), ('iced', 0.0257961), ('cup', 0.01660676), ('bubble', 0.016455833), ('shop', 0.011431669)]


time : [('next', 0.3164644), ('every', 0.17941159), ('first', 0.047879897), ('last', 0.008741783), ('long', 0.00720109)]


really : [('good', 0.0038235816), ('enjoyed', 0.0020579093), ('liked', 0.0020171397), ('really', 0.0016268702), ('nice', 0.0014443098)]


i've : [('awesome', 0.00024741585), ('right', 0.00023378228), ('loved', 0.00023177378), ('real', 0.0002272466), ('top', 0.00022221783)]


philly : [('south', 0.04097974), ('visiting', 0.011180897), ('visit', 0.0077669225), ('staple', 0.0042876084), ('cheesesteak', 0.004151255)]


cake : [('birthday', 0.07972915), ('wedding', 0.041719366), ('carrot', 0.033406556), ('pound', 0.022022776), ('shower', 0.0076979417)]


back : [('coming', 0.040458266), ('come', 0.03060994), ('soon', 0.0113789765), ('going', 0.010935964), ('definitely', 0.0060010892)]


try : [('must', 0.041357372), ('wait', 0.015863337), ('decided', 0.005830778), ('next', 0.0033726443), ('gotta', 0.003267857)]


chocolate : [('chip', 0.3028401), ('dark', 0.0075482945), ('peanut', 0.0070995893), ('raspberry', 0.0062835673), ('hot', 0.005186766)]


amazing : [('absolutely', 0.0027742004), ('service', 0.0015455857), ('donuts', 0.0013749914), ('doughnuts', 0.0011423195), ('cookies', 0.0010793519)]


fresh : [('baked', 0.04711717), ('produce', 0.019741543), ('meats', 0.009093244), ('made', 0.008048557), ('vegetables', 0.0070396354)]


always : [('fresh', 0.0019323332), ('always', 0.0016338282), ('bring', 0.0011487448), ('something', 0.0011309828), ('come', 0.0009114414)]


everything : [('else', 0.01100552), ('want', 0.0035851083), ('loved', 0.0030805964), ('tried', 0.0027742963), ('delicious', 0.002654554)]


i'm : [('large', 0.00030787216), ('small', 0.00030763456), ('nice', 0.00030592608), ('awesome', 0.00028400385), ('huge', 0.0002785396)]


definitely : [('worth', 0.048529662), ('recommend', 0.026786227), ('back', 0.0062088855), ('return', 0.0040910654), ('would', 0.0026375933)]


would : [('recommend', 0.34312433), ('suggest', 0.0034157562), ('say', 0.003012439), ('recommended', 0.0023352876), ('lived', 0.0013559879)]


market : [('reading', 0.010302861), ('farmer', 0.007434261), ('market', 0.0069332705), ('indoor', 0.0062715784), ('farmers', 0.005821264)]


got : [('friend', 0.0024943405), ('boyfriend', 0.0018437811), ('husband', 0.0017051573), ('home', 0.0015093216), ('recently', 0.0014267205)]


ever : [('best', 0.061967175), ('eaten', 0.015069834), ('tasted', 0.011711623), ('hands', 0.003933155), ('life', 0.0037491836)]


even : [('better', 0.008045791), ('though', 0.0049175317), ('made', 0.0011212305), ('free', 0.0010074452), ('pretty', 0.0009404546)]


make : [('sure', 0.21025419), ('home', 0.0040311953), ('trip', 0.0035773446), ('point', 0.0026565706), ('freshly', 0.0020292427)]


little : [('bit', 0.011599147), ('little', 0.0046085506), ('pricey', 0.00298932), ('cute', 0.0028557654), ('tiny', 0.0017235418)]


favorite : [('places', 0.007256956), ('philadelphia', 0.00651746), ('absolute', 0.0061408365), ('city', 0.0054711807), ('spots', 0.005242178)]


many : [('options', 0.054804735), ('choices', 0.019492693), ('places', 0.015908055), ('different', 0.0103797885), ('times', 0.008540983)]


well : [('worth', 0.0052085794), ('pretty', 0.00078328507), ('done', 0.00068376923), ('tasty', 0.0006108911), ('enjoyed', 0.0005666934)]


bakery : [('metropolitan', 0.005410576), ('termini', 0.003430796), ('beiler', 0.002841488), ('italian', 0.0024648295), ('bros', 0.0023045752)]


every : [('bite', 0.12620664), ('time', 0.110776186), ('single', 0.06667391), ('day', 0.030277086), ('year', 0.02083974)]


come : [('back', 0.0664589), ('would', 0.004147967), ('hungry', 0.0036508176), ('definitely', 0.0023728139), ('often', 0.0023523248)]


sweet : [('tooth', 0.30886117), ('overly', 0.044512585), ('freedom', 0.021762153), ('savory', 0.00952176), ('box', 0.0041646087)]


service : [('customer', 0.10948675), ('friendly', 0.06628387), ('excellent', 0.01723558), ('attentive', 0.009046504), ('outstanding', 0.007570859)]


friendly : [('staff', 0.6175941), ('super', 0.00764483), ('service', 0.005099757), ('employees', 0.003649045), ('servers', 0.0033045406)]


eat : [('could', 0.015423839), ('want', 0.0055681234), ('hard', 0.005324483), ('sit', 0.0028734726), ('places', 0.0027832824)]


made : [('freshly', 0.06470083), ('home', 0.013721489), ('fresh', 0.013476724), ('goods', 0.003939609), ('sure', 0.0033414117)]


day : [('every', 0.11922549), ('next', 0.040121462), ('last', 0.011654562), ('day', 0.0036158166), ('first', 0.0034207879)]


reading : [('terminal', 0.9999859), ('market', 9.88822e-07), ('reviews', 1.4441932e-07), ('railroad', 1.4060781e-07), ('review', 4.670211e-08)]


can't : [('vegan', 0.00043280076), ('free', 0.00038287533), ('local', 0.0003243359), ('use', 0.00032322967), ('deli', 0.00028912557)]


staff : [('friendly', 0.866692), ('nice', 0.0033864635), ('attentive', 0.0031509195), ('helpful', 0.003001106), ('pleasant', 0.0022367067)]


nice : [('staff', 0.011782849), ('super', 0.0063091065), ('really', 0.0029586388), ('people', 0.0028570679), ('vibe', 0.0025335867)]


One Star Reviews
food : [('experience', 0.0006857641), ('ever', 0.000630791), ('day', 0.0006256662), ('great', 0.00061990076), ('wait', 0.0006189283)]


like : [('experience', 0.00065366644), ('day', 0.00062459905), ('give', 0.00061033166), ('wait', 0.00061028486), ('great', 0.0006092154)]


place : [('experience', 0.00070171355), ('ever', 0.0006451572), ('day', 0.00063664926), ('great', 0.0006314828), ('give', 0.00063110964)]


one : [('experience', 0.00068950147), ('day', 0.0006818566), ('wait', 0.0006769429), ('give', 0.0006642453), ('another', 0.00065531215)]


cake : [('day', 0.0007007534), ('wait', 0.00068748835), ('experience', 0.0006814209), ('give', 0.0006734151), ('another', 0.000664974)]


would : [('experience', 0.0006671904), ('day', 0.00065842585), ('wait', 0.00065389875), ('give', 0.0006518205), ('another', 0.0006353323)]


back : [('wait', 0.00066290924), ('day', 0.0006580459), ('another', 0.00064820214), ('give', 0.0006436591), ('take', 0.0006429037)]


order : [('wait', 0.0007005483), ('day', 0.00069185527), ('another', 0.00068888714), ('counter', 0.0006842681), ('take', 0.0006814001)]


get : [('day', 0.00066336), ('wait', 0.0006600847), ('experience', 0.00065085955), ('give', 0.0006440442), ('another', 0.00064109825)]


time : [('experience', 0.00070407067), ('day', 0.0006961337), ('wait', 0.00069060654), ('give', 0.0006743059), ('another', 0.0006667713)]


service : [('experience', 0.0009534169), ('ever', 0.00089626276), ('worst', 0.00087271), ('horrible', 0.00078460964), ('bad', 0.00076485367)]


even : [('experience', 0.0006921791), ('day', 0.0006851611), ('wait', 0.0006800847), ('give', 0.00066931127), ('another', 0.0006577698)]


go : [('experience', 0.0007453627), ('day', 0.0007118285), ('wait', 0.00070337846), ('give', 0.00069499173), ('great', 0.0006825535)]


never : [('experience', 0.0007261452), ('day', 0.00068135286), ('wait', 0.00067512365), ('give', 0.0006701221), ('ever', 0.00067001913)]


ordered : [('day', 0.0007604936), ('wait', 0.00074901816), ('experience', 0.000732164), ('sandwich', 0.00072755996), ('give', 0.0007221219)]


asked : [('wait', 0.0007552487), ('day', 0.00075056625), ('another', 0.00073768036), ('counter', 0.0007359575), ('take', 0.0007287509)]


said : [('wait', 0.0007551745), ('day', 0.0007500973), ('another', 0.0007374579), ('take', 0.000736878), ('counter', 0.0007345564)]


us : [('wait', 0.00073097204), ('another', 0.0007199426), ('day', 0.0007167096), ('counter', 0.00071658887), ('take', 0.00071018067)]


good : [('experience', 0.00079833367), ('ever', 0.00071497186), ('day', 0.0007006595), ('great', 0.00069961796), ('better', 0.000698557)]


got : [('day', 0.00074401364), ('wait', 0.0007360699), ('experience', 0.00072848983), ('give', 0.00071467715), ('another', 0.00071054377)]


told : [('wait', 0.00077164086), ('day', 0.00076378457), ('another', 0.0007547044), ('counter', 0.0007503459), ('take', 0.0007453002)]


could : [('day', 0.0007455374), ('wait', 0.00073990924), ('experience', 0.00073749735), ('give', 0.0007323982), ('another', 0.00071544584)]


people : [('experience', 0.0008166057), ('day', 0.0007869618), ('wait', 0.0007791111), ('give', 0.00076400134), ('another', 0.00074614526)]


went : [('day', 0.0007625412), ('wait', 0.0007566505), ('experience', 0.00074203697), ('another', 0.0007314224), ('give', 0.0007304268)]


customer : [('experience', 0.00091965677), ('ever', 0.0008451723), ('worst', 0.00081798574), ('horrible', 0.0007383505), ('rude', 0.00073783996)]


came : [('wait', 0.0007634557), ('day', 0.00076312415), ('another', 0.00074155733), ('counter', 0.00073849177), ('give', 0.0007306954)]


i'm : [('experience', 0.0006993109), ('day', 0.00066778593), ('wait', 0.0006583329), ('give', 0.0006530579), ('great', 0.0006453921)]


minutes : [('wait', 0.00075844117), ('another', 0.0007471396), ('counter', 0.0007421906), ('day', 0.0007413947), ('take', 0.0007348893)]


really : [('experience', 0.0008436203), ('day', 0.00076071196), ('ever', 0.00075137155), ('great', 0.000746999), ('give', 0.0007466367)]


make : [('day', 0.00078017433), ('experience', 0.0007771831), ('wait', 0.00077248795), ('give', 0.0007554958), ('another', 0.00074287766)]


coffee : [('experience', 0.000823031), ('day', 0.0007871767), ('wait', 0.00077354966), ('give', 0.00075845805), ('great', 0.0007524256)]


going : [('experience', 0.00081958005), ('day', 0.0008040318), ('wait', 0.000798997), ('give', 0.0007816507), ('another', 0.0007669124)]


take : [('wait', 0.000799363), ('take', 0.00079920614), ('day', 0.0007888992), ('another', 0.000784518), ('counter', 0.00077815255)]


bad : [('experience', 0.0008676525), ('ever', 0.0007810086), ('worst', 0.0007448774), ('great', 0.0007381236), ('better', 0.00073611544)]


first : [('experience', 0.0008059337), ('day', 0.0007974853), ('wait', 0.00079027825), ('give', 0.0007673035), ('another', 0.00075866026)]


two : [('day', 0.00083658594), ('wait', 0.0008329362), ('another', 0.00080234185), ('counter', 0.0008018235), ('give', 0.0007966498)]


also : [('experience', 0.0008631358), ('day', 0.000851065), ('wait', 0.00083737436), ('give', 0.0008165998), ('another', 0.00079907186)]


know : [('experience', 0.00084874826), ('day', 0.00082183135), ('wait', 0.00081417983), ('give', 0.0007982206), ('another', 0.0007789695)]


sandwich : [('day', 0.0007884797), ('wait', 0.0007791894), ('experience', 0.00076328876), ('sandwich', 0.000753748), ('give', 0.0007525858)]


i've : [('experience', 0.00083383796), ('day', 0.00083113066), ('wait', 0.00081815623), ('give', 0.00079785933), ('another', 0.00078222645)]


give : [('experience', 0.0007998617), ('day', 0.0007851302), ('wait', 0.00077955675), ('give', 0.0007756896), ('another', 0.0007520143)]


made : [('experience', 0.0008500676), ('day', 0.00081900466), ('wait', 0.0008057819), ('give', 0.00079061725), ('great', 0.00077408797)]


want : [('experience', 0.0008430996), ('day', 0.00078547065), ('wait', 0.0007741816), ('give', 0.0007666842), ('great', 0.00075550383)]


way : [('experience', 0.00095594954), ('day', 0.00088869565), ('wait', 0.0008713681), ('give', 0.0008602378), ('great', 0.00084877637)]


come : [('experience', 0.0007737824), ('day', 0.0007733234), ('wait', 0.00076821557), ('give', 0.0007499685), ('another', 0.00074028765)]


ever : [('experience', 0.0010015819), ('ever', 0.00090709486), ('worst', 0.0008652754), ('great', 0.0008241239), ('day', 0.000818701)]


table : [('wait', 0.0008593298), ('day', 0.0008522469), ('another', 0.0008332269), ('counter', 0.0008304861), ('take', 0.00081478705)]


rude : [('experience', 0.0008501017), ('day', 0.0007995708), ('wait', 0.0007950028), ('give', 0.0007785639), ('rude', 0.0007639138)]


took : [('wait', 0.0007665491), ('day', 0.00076605513), ('experience', 0.00074388826), ('another', 0.00074138795), ('give', 0.0007383122)]


another : [('wait', 0.00082947966), ('day', 0.0008241882), ('another', 0.00080324424), ('counter', 0.00079758227), ('give', 0.0007922009)]

""")