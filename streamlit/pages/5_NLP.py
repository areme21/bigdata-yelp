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
    st.write("""**Five Star Reviews**

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


**One Star Reviews**

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
elif category == "Bars":
    st.image("streamlit/bars/customer_rating.png")
    st.image("streamlit/bars/wordCloud.png")
    st.image("streamlit/bars/bigramCloud.png")
    st.write("""**Five Star Reviews**

great : [('service', 0.01614107), ('atmosphere', 0.00960041), ('experience', 0.00745694), ('job', 0.0053773285), ('prices', 0.0050195362)]


food : [('comfort', 0.06937321), ('coma', 0.031890407), ('network', 0.019258725), ('truck', 0.008404063), ('excellent', 0.0063490467)]


place : [('go-to', 0.020195113), ('hopping', 0.011893098), ('love', 0.0069533964), ('chill', 0.006542906), ('underrated', 0.0055680866)]


good : [('pretty', 0.0975689), ('sooo', 0.05367818), ('soooo', 0.022716505), ('damn', 0.013250977), ('sooooo', 0.010583609)]


one : [('places', 0.4155759), ('spots', 0.10862216), ('favorites', 0.06726071), ('restaurants', 0.030519115), ('reasons', 0.015550526)]


service : [('impeccable', 0.63713074), ('prompt', 0.13601708), ('customer', 0.12682226), ('fast', 0.022472367), ('top-notch', 0.019960955)]


best : [('ever', 0.97118974), ('hands', 0.0060233567), ('city', 0.004262487), ('hands-down', 0.0036473344), ('worlds', 0.003135527)]


like : [('felt', 0.3708922), ('feels', 0.31887853), ('feel', 0.27869344), ('looks', 0.024042696), ('seems', 0.0011321987)]


really : [('enjoyed', 0.28149968), ('liked', 0.14083296), ('appreciated', 0.0589167), ('cool', 0.012097801), ('impressed', 0.009765238)]


also : [('sell', 0.0059543117), ('enjoyed', 0.005356416), ('liked', 0.003997857), ('byob', 0.002410277), ('shared', 0.0023474535)]


time : [('next', 0.64383763), ('every', 0.19527905), ('first', 0.08929824), ('second', 0.032329343), ('long', 0.01495797)]


go : [('wrong', 0.9297954), ('everytime', 0.009923753), ('back', 0.004514048), ('decided', 0.0015014652), ('wanna', 0.0012511053)]


back : [('laid', 0.94101506), ('come', 0.017280947), ('coming', 0.008021913), ('soon', 0.0071240724), ('sometime', 0.0039067348)]


delicious : [('absolutely', 0.07039238), ('equally', 0.027500354), ('everything', 0.0071650734), ('filling', 0.005180209), ('amazingly', 0.004622835)]


get : [('seat', 0.14400576), ('chance', 0.09659505), ('rid', 0.037957963), ('able', 0.03290533), ('crowded', 0.025884107)]


love : [('fell', 0.018718071), ('absolutely', 0.0014000309), ('fallen', 0.00092265074), ('concept', 0.000917263), ('fall', 0.00090680085)]


definitely : [('returning', 0.02412515), ('recommend', 0.010521861), ('return', 0.008283286), ('back', 0.0031303037), ('worth', 0.0027512)]


bar : [('dive', 0.0987996), ('stools', 0.027719375), ('sports', 0.027109312), ('tenders', 0.02266774), ('behind', 0.019013943)]


amazing : [('absolutely', 0.0013824116), ('freaking', 0.0006684735), ('simply', 0.0006544533), ('view', 0.00040733686), ('equally', 0.00040306273)]


menu : [('items', 0.034979396), ('extensive', 0.023686513), ('tasting', 0.020768393), ('changes', 0.019274507), ('listed', 0.009110999)]


i've : [('melts', 8.795947e-05), ('melted', 8.438658e-05), ('melt', 8.428106e-05), ('watering', 8.401059e-05), ('mouth', 7.2184586e-05)]


would : [('suggest', 0.037356257), ('recommend', 0.03729516), ('advise', 0.0041872454), ('worried', 0.003984533), ('heartbeat', 0.003637553)]


restaurant : [('week', 0.048933323), ('starr', 0.0070840726), ('mexican', 0.003501824), ('japanese', 0.0017580523), ('indian', 0.0017116201)]


got : [('boyfriend', 0.0015839254), ('partner', 0.0012467589), ('friend', 0.0011715513), ('finally', 0.0011629063), ('fianc', 0.0009468195)]


always : [('consistent', 0.0034744476), ('changing', 0.0015868074), ('remembers', 0.0014032795), ('smiling', 0.0011995893), ('packed', 0.000995559)]


us : [('gave', 0.1146997), ('helped', 0.023008581), ('allowed', 0.012046434), ('chatted', 0.008405289), ('brought', 0.008092311)]


ordered : [('takeout', 0.00473981), ('delivery', 0.0041117487), ('boyfriend', 0.0022351223), ('grubhub', 0.0019850056), ('friend', 0.0018353385)]


well : [('executed', 0.090848476), ('balanced', 0.023112986), ('seasoned', 0.01650744), ('done', 0.014225654), ('priced', 0.013504114)]


nice : [('touch', 0.026007896), ('weather', 0.0029238258), ('gesture', 0.0021472727), ('balance', 0.00097190944), ('atmosphere', 0.0009276837)]


try : [('must', 0.020854775), ('dying', 0.011688187), ('wanting', 0.010962013), ('eager', 0.00880489), ('excited', 0.008408732)]


philly : [('south', 0.24492559), ('west', 0.024452914), ('visiting', 0.012670601), ('conference', 0.008502385), ('scene', 0.0056227166)]


came : [('quickly', 0.012399234), ('whim', 0.007368415), ('across', 0.00462869), ('promptly', 0.0036426405), ('timely', 0.003114537)]


staff : [('friendly', 0.1802759), ('members', 0.02281492), ('member', 0.020425525), ('wait', 0.01990158), ('helpful', 0.01091137)]


beer : [('selection', 0.26424855), ('list', 0.09486556), ('craft', 0.08892718), ('garden', 0.04280161), ('bible', 0.018930359)]


everything : [('else', 0.44732296), ('tasted', 0.0010160522), ('ate', 0.0008854799), ('including', 0.00070307986), ('sounded', 0.000649884)]


even : [('though', 0.110157035), ('better', 0.03262527), ('describe', 0.004208379), ('begin', 0.0026785908), ('existed', 0.0025244479)]


i'm : [('especially', 0.00010142512), ('awesome', 9.579326e-05), ('well', 8.5947e-05), ('excellent', 8.539845e-05), ('fantastic', 8.484453e-05)]


night : [('friday', 0.18749687), ('last', 0.087110184), ('late', 0.08496368), ('saturday', 0.08285121), ('thursday', 0.028535502)]


favorite : [('personal', 0.15024638), ('absolute', 0.04286481), ('all-time', 0.037986565), ('spots', 0.008758709), ('become', 0.007162363)]


come : [('back', 0.008977935), ('across', 0.0036050626), ('everytime', 0.003105479), ('often', 0.0020907207), ('anytime', 0.001265889)]


friendly : [('staff', 0.10399928), ('super', 0.0090348255), ('waitstaff', 0.0070780152), ('employees', 0.0050844504), ('staffs', 0.0040392135)]


recommend : [('highly', 0.9997577), ('strongly', 0.00022469845), ('anyone', 5.7837997e-06), ('would', 5.869016e-07), ('heartily', 3.683575e-07)]


made : [('freshly', 0.30059642), ('scratch', 0.10833046), ('reservations', 0.013815716), ('effort', 0.012997616), ('sure', 0.01286564)]


cheese : [('mac', 0.76098186), ('goat', 0.16530217), ('curds', 0.042452052), ('board', 0.010669356), ('blue', 0.00620114)]


went : [('beyond', 0.0061126603), ('yesterday', 0.0045603653), ('whim', 0.003591602), ('birthday', 0.002838503), ('recently', 0.0022036403)]


first : [('timers', 0.12900071), ('glance', 0.122979805), ('foremost', 0.10263839), ('timer', 0.088544354), ('time', 0.039705526)]


drinks : [('mixed', 0.092978954), ('specialty', 0.010584331), ('strong', 0.0067944895), ('stiff', 0.0056103556), ('alcoholic', 0.0052413857)]


sushi : [('sashimi', 0.01669782), ('freshest', 0.0119686695), ('koto', 0.008368372), ('nigiri', 0.008297458), ('lovers', 0.007894193)]


happy : [('hour', 0.99999994), ('camper', 5.2194153e-08), ('hr', 1.2692581e-08), ('hours', 9.03228e-09), ('report', 4.1938897e-09)]


experience : [('dining', 0.74155694), ('dinning', 0.038348332), ('positive', 0.004323145), ('culinary', 0.0041789142), ('enhanced', 0.0022121076)]


**One Star Reviews**

food : [('poisoning', 0.47550294), ('mediocre', 0.08221698), ('quality', 0.049902204), ('average', 0.0133601595), ('subpar', 0.01142097)]


us : [('gave', 0.35528582), ('tell', 0.037694816), ('give', 0.028109215), ('serve', 0.021511486), ('greet', 0.018067058)]


place : [('crowded', 0.037717182), ('empty', 0.023215143), ('recommend', 0.022104064), ('packed', 0.020989552), ('avoid', 0.016754016)]


one : [('star', 0.007687509), ('person', 0.004016108), ('else', 0.0023547926), ('thing', 0.0020399308), ('bite', 0.0009041243)]


like : [('tasted', 0.10150173), ('feel', 0.048024688), ('felt', 0.046176527), ('looked', 0.035678387), ('looks', 0.023542862)]


service : [('customer', 0.06221856), ('poor', 0.0508366), ('slow', 0.046341315), ('horrendous', 0.017532522), ('terrible', 0.01255761)]


would : [('recommend', 0.021467708), ('think', 0.0049542976), ('thought', 0.002406663), ('figured', 0.002359661), ('wish', 0.0021811496)]


get : [('attention', 0.0056115766), ('together', 0.0027066078), ('rid', 0.0020221812), ('trying', 0.0019730665), ('home', 0.0013566235)]


back : [('sent', 0.111873), ('send', 0.06874197), ('coming', 0.019915776), ('come', 0.01033381), ('forth', 0.009356536)]


never : [('return', 0.012153715), ('seen', 0.011629758), ('received', 0.0066317474), ('returning', 0.0054690703), ('experienced', 0.0048181466)]


time : [('waste', 0.06567082), ('every', 0.06308981), ('second', 0.030886913), ('first', 0.027609235), ('last', 0.013645408)]


even : [('though', 0.4634287), ('worse', 0.0027922804), ('bother', 0.0016309632), ('busy', 0.0012194654), ('finish', 0.0011215209)]


ordered : [('beer', 0.0039088666), ('beers', 0.0029902486), ('appetizer', 0.0026409246), ('delivery', 0.0025737358), ('friend', 0.0022980182)]


came : [('back', 0.0030799918), ('finally', 0.0028088656), ('never', 0.0019937872), ('manager', 0.0016944164), ('downhill', 0.0016260325)]


go : [('elsewhere', 0.007760279), ('back', 0.0037275755), ('decided', 0.0020290187), ('never', 0.0018744185), ('want', 0.0017952613)]


order : [('placed', 0.15482968), ('take', 0.014257075), ('taking', 0.013333529), ('messed', 0.009212061), ('delivery', 0.0065284427)]


bar : [('sports', 0.023643557), ('tender', 0.020894276), ('behind', 0.009456687), ('dive', 0.0071573146), ('sat', 0.006299231)]


good : [('pretty', 0.0168572), ('thing', 0.0033690426), ('luck', 0.0027383557), ('reviews', 0.0017359671), ('ambiance', 0.0013383896)]


asked : [('politely', 0.013212717), ('wanted', 0.00585032), ('waitress', 0.0047775134), ('specifically', 0.004715067), ('server', 0.003954689)]


minutes : [('later', 0.3171758), ('ago', 0.11404763), ('waited', 0.09955056), ('took', 0.034835074), ('ten', 0.014123904)]


got : [('finally', 0.0046935077), ('sick', 0.0035246985), ('home', 0.0028005294), ('poisoning', 0.002267394), ('attention', 0.0022544137)]


restaurant : [('week', 0.018209834), ('empty', 0.009552529), ('chain', 0.0021282856), ('italian', 0.002022215), ('full', 0.0020099557)]


table : [('next', 0.008545072), ('reserved', 0.004984277), ('cleared', 0.004069851), ('sit', 0.0034861336), ('dirty', 0.0034091698)]


said : [('yes', 0.0077084107), ('oh', 0.0032987641), ('sorry', 0.003176316), ('ok', 0.0026736688), ('rudely', 0.0024868553)]


told : [('rudely', 0.002654598), ('called', 0.0024508059), ('hostess', 0.0023895756), ('sit', 0.002182796), ('us', 0.0019251257)]


could : [('wish', 0.011942907), ('hear', 0.005431039), ('see', 0.004270894), ('easily', 0.003596727), ('eat', 0.003088391)]


went : [('downhill', 0.010287303), ('hill', 0.0029641762), ('friends', 0.002776097), ('today', 0.0027190747), ('back', 0.002366062)]


people : [('many', 0.039195213), ('group', 0.004610122), ('several', 0.004007097), ('three', 0.003960702), ('treat', 0.0024667138)]


drinks : [('watered', 0.017142072), ('overpriced', 0.0057988726), ('weak', 0.005365533), ('priced', 0.0042616953), ('round', 0.004172811)]


waitress : [('friendly', 0.006787258), ('attentive', 0.0052299565), ('nice', 0.004839896), ('disappeared', 0.0044492423), ('inattentive', 0.0032034449)]


really : [('wanted', 0.0047756582), ('disappointed', 0.0021559515), ('nice', 0.0014550594), ('excited', 0.0013430633), ('bad', 0.0012807159)]


took : [('forever', 0.8988005), ('long', 0.0076676942), ('bite', 0.00491076), ('mins', 0.003138106), ('minutes', 0.0022738285)]


come : [('back', 0.010080398), ('never', 0.0013366307), ('first', 0.0010853315), ('together', 0.0010140397), ('ever', 0.0010108365)]


experience : [('dining', 0.09305818), ('ruined', 0.013944904), ('recent', 0.012283978), ('bad', 0.011721475), ('unpleasant', 0.009310233)]


first : [('time', 0.03389905), ('visit', 0.006671758), ('opened', 0.0032477472), ('round', 0.0025299625), ('thing', 0.0022126115)]


i'm : [('red', 0.00031648288), ('brown', 0.00029896141), ('green', 0.000295142), ('cold', 0.00027369865), ('flavor', 0.00027298174)]


bad : [('experience', 0.0129215885), ('reviews', 0.005178395), ('service', 0.005168705), ('review', 0.0044034994), ('feel', 0.003345829)]


two : [('times', 0.034579955), ('bites', 0.0057242373), ('occasions', 0.0045817965), ('hours', 0.0044964324), ('pieces', 0.0036449824)]


manager : [('spoke', 0.044971704), ('speak', 0.02512086), ('general', 0.0073746555), ('duty', 0.0052657686), ('speaking', 0.0040015737)]


another : [('give', 0.006406006), ('round', 0.004519996), ('person', 0.0027745895), ('minutes', 0.0027620024), ('offered', 0.0021222786)]


drink : [('watered', 0.010028772), ('buy', 0.0055364347), ('spilled', 0.0051469114), ('specials', 0.003603714), ('bottled', 0.0033529887)]


ever : [('worst', 0.91844094), ('seen', 0.0017308749), ('rudest', 0.0015234055), ('experienced', 0.0013821967), ('encountered', 0.001340363)]


night : [('friday', 0.44465205), ('saturday', 0.20065206), ('last', 0.115200244), ('thursday', 0.015055216), ('tuesday', 0.010402384)]


server : [('disappeared', 0.004909404), ('attentive', 0.004774867), ('friendly', 0.004333316), ('flag', 0.004202361), ('inattentive', 0.0034625365)]


going : [('back', 0.005743668), ('recommend', 0.0017247353), ('keep', 0.0016554743), ('ended', 0.0012377648), ('downhill', 0.00123311)]


know : [('let', 0.65542877), ('dont', 0.004985705), ('letting', 0.0028262315), ('industry', 0.0009849484), ('cook', 0.00079482433)]


staff : [('wait', 0.1360391), ('member', 0.03157378), ('members', 0.02392543), ('friendly', 0.02198225), ('rude', 0.011872126)]


also : [('ordered', 0.000538463), ('sauce', 0.0005042322), ('mixed', 0.00049309235), ('added', 0.00044267703), ('add', 0.00040750604)]


made : [('reservation', 0.2899686), ('mistake', 0.07535335), ('reservations', 0.06640873), ('sense', 0.035849188), ('feel', 0.013905417)]


make : [('sense', 0.22637133), ('sure', 0.11125764), ('matters', 0.10608849), ('effort', 0.02837124), ('mistake', 0.015500463)]


""")
elif category == "Cheesesteaks":
    st.image("streamlit/cheesesteaks/customer_rating.png")
    st.image("streamlit/cheesesteaks/wordCloud.png")
    st.image("streamlit/cheesesteaks/bigramCloud.png")
    st.write("""**Five Star Reviews**

cheesesteak : [('favorite', 0.018000733), ('philadelphia', 0.015728619), ('ever', 0.010519282), ('authentic', 0.010067194), ('ordered', 0.00888597)]


philly : [('south', 0.5277006), ('visiting', 0.027793577), ('authentic', 0.013409564), ('favorite', 0.00727207), ('native', 0.007264157)]


cheese : [('steak', 0.33188295), ('wiz', 0.099544674), ('steaks', 0.08986137), ('american', 0.06681622), ('whiz', 0.03790568)]


place : [('favorite', 0.012488508), ('love', 0.012359324), ('recommend', 0.0061469288), ('go', 0.0036024307), ('try', 0.0035559116)]


best : [('city', 0.3528858), ('ever', 0.21877684), ('hands', 0.04102559), ('absolute', 0.022801267), ('far', 0.020185938)]


steak : [('cheese', 0.009399382), ('chopped', 0.0033711912), ('cheez', 0.0025329753), ('chicken', 0.0018393124), ('real', 0.0016134096)]


good : [('pretty', 0.0028776543), ('really', 0.0019649006), ('fries', 0.0014732226), ('damn', 0.0012660899), ('everything', 0.0012260751)]


great : [('service', 0.0063034664), ('staff', 0.0026721396), ('atmosphere', 0.0022446236), ('price', 0.0017221441), ('prices', 0.0016774413)]


get : [('want', 0.0014700698), ('usually', 0.0010645005), ('ahead', 0.0010279414), ('favor', 0.00086071517), ('wait', 0.00085964636)]


one : [('two', 0.0018931271), ('half', 0.0016203712), ('eaten', 0.0015556096), ('easily', 0.0015398699), ('probably', 0.0015021657)]


sandwich : [('half', 0.001236512), ('huge', 0.0010984904), ('chicken', 0.0010549158), ('make', 0.0010314761), ('pork', 0.001020741)]


go : [('back', 0.0036969115), ('wrong', 0.002887829), ('want', 0.0026233187), ('gotta', 0.0017418524), ('locals', 0.0016314663)]


food : [('service', 0.0029947686), ('great', 0.0026090518), ('excellent', 0.0025690913), ('amazing', 0.0022545403), ('awesome', 0.001825947)]


like : [('places', 0.0024018195), ('feel', 0.002234666), ('taste', 0.0013581075), ('use', 0.0012700469), ('chopped', 0.0011281824)]


time : [('next', 0.24181738), ('every', 0.10811787), ('first', 0.041610334), ('long', 0.005718676), ('second', 0.0027397708)]


i've : [('went', 0.000262097), ('came', 0.00024818274), ('friend', 0.0002455227), ('us', 0.00024098203), ('said', 0.00023911126)]


order : [('ahead', 0.010382803), ('window', 0.0085517345), ('ready', 0.007646338), ('placed', 0.004254815), ('pick', 0.003919181)]


cheesesteaks : [('city', 0.0019124893), ('philadelphia', 0.0015794279), ('chicken', 0.0013983264), ('favorite', 0.0012892213), ('tried', 0.0012642175)]


got : [('boyfriend', 0.0031462838), ('husband', 0.0027866387), ('mine', 0.0021237314), ('friend', 0.0019611528), ('finally', 0.0019569432)]


meat : [('chopped', 0.021552453), ('tender', 0.016086103), ('sliced', 0.014718179), ('quality', 0.008141427), ('texture', 0.0077443123)]


fries : [('french', 0.027067067), ('waffle', 0.0195575), ('side', 0.009884757), ('drinks', 0.008300192), ('rings', 0.0071367365)]


back : [('come', 0.016704), ('coming', 0.010563394), ('definitely', 0.008604878), ('wait', 0.0060263015), ('home', 0.003822359)]


also : [('selection', 0.0026859187), ('beer', 0.0022177983), ('options', 0.0016437962), ('drinks', 0.0016372089), ('fries', 0.0012172417)]


really : [('really', 0.0021066298), ('nice', 0.0018785093), ('good', 0.0015236846), ('enjoyed', 0.0011437776), ('friendly', 0.0010236494)]


i'm : [('nice', 0.00039461363), ('super', 0.0003621062), ('lots', 0.00035677128), ('little', 0.0003567342), ('served', 0.00035328115)]


definitely : [('recommend', 0.044964362), ('worth', 0.025710851), ('return', 0.006541618), ('back', 0.005839126), ('returning', 0.0024088984)]


try : [('must', 0.0066788145), ('decided', 0.004659998), ('give', 0.0032485104), ('items', 0.0023714767), ('wrong', 0.002237395)]


delicious : [('everything', 0.0019242258), ('absolutely', 0.001532552), ('food', 0.0013230874), ('wings', 0.0012323679), ('fresh', 0.0010635925)]


always : [('always', 0.0014401395), ('fresh', 0.0011490604), ('service', 0.0009501716), ('fast', 0.0007899738), ('point', 0.00077350443)]


love : [('love', 0.0017770355), ('pizza', 0.0013817718), ('place', 0.0012559182), ('absolutely', 0.0011955412), ('spot', 0.0009910653)]


steaks : [('king', 0.005137178), ('prince', 0.0030034939), ('cheese', 0.002865204), ('steve', 0.002489318), ('jim', 0.0017590517)]


would : [('recommend', 0.11018199), ('say', 0.0026790726), ('suggest', 0.0025286083), ('wish', 0.0020698986), ('stars', 0.0020130735)]


first : [('time', 0.08476832), ('bite', 0.050786424), ('experience', 0.004102985), ('went', 0.004049779), ('visit', 0.0036307853)]


chicken : [('buffalo', 0.028704625), ('maroosh', 0.022512702), ('chicken', 0.015616922), ('cutlet', 0.013033357), ('parm', 0.0103547815)]


onions : [('fried', 0.051915426), ('peppers', 0.049873084), ('grilled', 0.009596645), ('american', 0.0051044254), ('provolone', 0.00483621)]


line : [('long', 0.28701743), ('door', 0.011867323), ('quickly', 0.010301988), ('moves', 0.009519475), ('waiting', 0.008080035)]


pork : [('roast', 0.99910367), ('roasted', 5.2751464e-05), ('broccoli', 2.585575e-05), ('pulled', 2.3629103e-05), ('rabe', 1.3200655e-05)]


bread : [('soft', 0.013796633), ('fresh', 0.0105601875), ('perfect', 0.0052482192), ('chewy', 0.005166195), ('fluffy', 0.0037916612)]


service : [('friendly', 0.108253844), ('customer', 0.076796904), ('fast', 0.02634129), ('quick', 0.016667545), ('excellent', 0.006515563)]


well : [('worth', 0.008506474), ('seasoned', 0.0022368468), ('cooked', 0.0015633774), ('price', 0.0012095688), ('fries', 0.0010810839)]


worth : [('wait', 0.22865129), ('totally', 0.068436995), ('well', 0.04041069), ('definitely', 0.03496144), ('trip', 0.025612434)]


ever : [('best', 0.010171062), ('eaten', 0.006849004), ('life', 0.0055141775), ('tasted', 0.004132743), ('hands', 0.0033910517)]


better : [('much', 0.009478363), ('even', 0.007270919), ('pats', 0.00496488), ('pat', 0.0048617357), ('better', 0.004001657)]


ordered : [('boyfriend', 0.005147565), ('husband', 0.0033793587), ('mine', 0.003237154), ('wife', 0.0026084718), ('mushroom', 0.0024577111)]


even : [('better', 0.005982264), ('though', 0.003953759), ('finish', 0.0012563539), ('pretty', 0.0012327302), ('ate', 0.0011348885)]


wait : [('worth', 0.3361843), ('long', 0.0309862), ('prepared', 0.004422206), ('minutes', 0.003450325), ('mins', 0.0029228984)]


make : [('sure', 0.24761473), ('trip', 0.0062427134), ('point', 0.004001177), ('home', 0.0025833503), ('way', 0.0025121653)]


eat : [('sit', 0.0039828476), ('could', 0.0036997693), ('area', 0.0026830758), ('able', 0.0024388088), ('seating', 0.0021617445)]


amazing : [('everything', 0.0017080717), ('absolutely', 0.0015195634), ('food', 0.0013699146), ('sandwiches', 0.0013147177), ('fries', 0.0011709898)]


pat's : [('night', 0.00042824645), ('little', 0.00041174327), ('took', 0.00040035328), ('take', 0.00039945322), ('went', 0.00039010437)]


**One Star Reviews**

place : [('recommend', 0.0012750104), ('many', 0.0011335528), ('anyone', 0.0010623124), ('review', 0.0010609606), ('going', 0.001002594)]


cheese : [('provolone', 0.0050225793), ('whiz', 0.004330126), ('cheese', 0.0041796304), ('wiz', 0.0041578724), ('onions', 0.004152288)]


food : [('service', 0.001874536), ('customer', 0.0018229426), ('staff', 0.0014035564), ('rude', 0.0014012777), ('horrible', 0.0010324308)]


cheesesteak : [('best', 0.0020677925), ('philly', 0.0019298547), ('real', 0.0017046948), ('cheese', 0.0015483246), ('steaks', 0.0014223191)]


steak : [('cheese', 0.0038720963), ('chicken', 0.0024722898), ('whiz', 0.002196678), ('wiz', 0.0021239356), ('steak', 0.0021071034)]


order : [('minutes', 0.005767193), ('waited', 0.005224565), ('hour', 0.004496896), ('called', 0.0038166654), ('told', 0.0037616172)]


like : [('flavor', 0.0009986941), ('much', 0.0009901413), ('taste', 0.00097316876), ('bread', 0.00096918107), ('quality', 0.00092066027)]


philly : [('south', 0.0044243257), ('tony', 0.0039636083), ('luke', 0.003463581), ('places', 0.0032423467), ('try', 0.0031712917)]


sandwich : [('onions', 0.0009773357), ('whiz', 0.00091727293), ('wiz', 0.00089276896), ('soggy', 0.00088370626), ('provolone', 0.0008695237)]


get : [('went', 0.0006529915), ('try', 0.0006441432), ('wanted', 0.0006426465), ('another', 0.00062818045), ('going', 0.0006098285)]


one : [('give', 0.00069641863), ('try', 0.00068651856), ('wanted', 0.00067423884), ('one', 0.0006472667), ('ever', 0.0006443045)]


go : [('street', 0.0026822824), ('across', 0.002236526), ('tony', 0.00201597), ('pats', 0.0020053186), ('south', 0.0019185526)]


meat : [('dry', 0.010042229), ('bread', 0.0075084902), ('flavor', 0.006871201), ('meat', 0.0064804866), ('chewy', 0.0061439425)]


even : [('also', 0.00062044343), ('cold', 0.0006183985), ('put', 0.00060274854), ('hot', 0.00056229334), ('well', 0.00056014996)]


would : [('give', 0.004042414), ('stars', 0.0027120104), ('could', 0.0023046115), ('would', 0.0022813403), ('star', 0.0015717312)]


good : [('much', 0.0010718559), ('quality', 0.0010272837), ('great', 0.000915607), ('taste', 0.0008763268), ('pretty', 0.0008689264)]


better : [('better', 0.0034383212), ('south', 0.0032984656), ('places', 0.003185238), ('much', 0.00297409), ('pat', 0.0029524215)]


time : [('waste', 0.0039434866), ('time', 0.0039411364), ('first', 0.00320003), ('last', 0.0025211973), ('money', 0.00218478)]


ordered : [('ordered', 0.00470769), ('onions', 0.0023823527), ('fries', 0.0023046583), ('half', 0.0021594772), ('got', 0.0020983182)]


never : [('never', 0.0012603273), ('going', 0.0010783983), ('back', 0.0010516212), ('come', 0.0010411454), ('give', 0.0009752928)]


back : [('back', 0.0029861124), ('called', 0.0023824463), ('told', 0.0022816113), ('going', 0.0019432041), ('another', 0.0017832818)]


service : [('service', 0.06412298), ('customer', 0.06122317), ('horrible', 0.016147012), ('terrible', 0.012845593), ('poor', 0.011180144)]


got : [('ordered', 0.0017110406), ('half', 0.0013691698), ('asked', 0.0012758847), ('got', 0.0011914442), ('fries', 0.0011293517)]


people : [('english', 0.0013316317), ('customer', 0.0012944766), ('business', 0.0012942929), ('customers', 0.0012830975), ('speak', 0.0011909135)]


i'm : [('dry', 0.0013692442), ('bread', 0.0012877493), ('flavor', 0.0011880973), ('soggy', 0.0011286868), ('tasteless', 0.0010655895)]


fries : [('onions', 0.004817452), ('ordered', 0.0037446185), ('peppers', 0.0034431757), ('provolone', 0.003312016), ('chicken', 0.0028383124)]


geno's : [('onions', 0.0021027215), ('provolone', 0.001887488), ('chicken', 0.0015714112), ('whiz', 0.0015237976), ('wiz', 0.001521779)]


said : [('told', 0.0027323463), ('said', 0.002616361), ('guy', 0.002379554), ('asked', 0.0023664145), ('called', 0.0023041635)]


ever : [('worst', 0.022616897), ('ever', 0.010788852), ('life', 0.004524492), ('eaten', 0.0033196583), ('experience', 0.0030861313)]


cheesesteaks : [('places', 0.0026575574), ('south', 0.0025981427), ('best', 0.0025230022), ('worst', 0.002442266), ('philadelphia', 0.0023085158)]


i've : [('pizza', 0.00059928873), ('nothing', 0.0005961341), ('sandwiches', 0.0005638454), ('well', 0.00055753655), ('also', 0.0005559128)]


bread : [('dry', 0.010601071), ('bread', 0.007467334), ('chewy', 0.0070462795), ('flavor', 0.006623506), ('soggy', 0.006411615)]


pat's : [('much', 0.00071222696), ('nothing', 0.0006607015), ('way', 0.0006368243), ('pizza', 0.00063337607), ('thing', 0.00062047056)]


really : [('much', 0.00095260923), ('think', 0.0008998103), ('bad', 0.0008796739), ('quality', 0.00085193914), ('great', 0.00082227465)]


pizza : [('pizza', 0.0009653914), ('chicken', 0.00095124246), ('whiz', 0.00081879593), ('sandwiches', 0.00079971243), ('ordered', 0.0007923079)]


know : [('going', 0.0010406082), ('business', 0.00087005424), ('recommend', 0.00084427657), ('give', 0.00083451305), ('else', 0.0008340699)]


first : [('time', 0.0026115547), ('first', 0.0017027408), ('last', 0.0014946348), ('money', 0.0013508475), ('went', 0.0011792443)]


went : [('went', 0.0018533106), ('try', 0.0016868149), ('last', 0.001452118), ('first', 0.0013963239), ('time', 0.0012565668)]


eat : [('try', 0.0008101844), ('else', 0.00077744486), ('going', 0.00077016075), ('wanted', 0.00075969676), ('eat', 0.0007266786)]


could : [('give', 0.008498476), ('could', 0.0078088804), ('stars', 0.0049971603), ('zero', 0.0029096864), ('star', 0.0023066725)]


worst : [('worst', 0.046246316), ('ever', 0.026473353), ('life', 0.008290367), ('eaten', 0.0048824036), ('experience', 0.004203032)]


asked : [('asked', 0.0071956497), ('said', 0.004206305), ('guy', 0.0037497766), ('minutes', 0.003203031), ('told', 0.0031353948)]


way : [('much', 0.0011360022), ('great', 0.00083387305), ('steaks', 0.0008306541), ('way', 0.00080687436), ('places', 0.00080085715)]


told : [('told', 0.003969605), ('minutes', 0.0036885142), ('called', 0.0035096277), ('waited', 0.0032748368), ('hour', 0.0030317614)]


steaks : [('best', 0.001780806), ('pat', 0.001648529), ('south', 0.001636962), ('real', 0.0015701172), ('steaks', 0.001544282)]


rude : [('rude', 0.017681815), ('staff', 0.01052432), ('service', 0.008473453), ('customer', 0.008103034), ('extremely', 0.0033723235)]


make : [('made', 0.0005984653), ('could', 0.0005980676), ('well', 0.0005930436), ('say', 0.00058191095), ('told', 0.00057993946)]


want : [('else', 0.0007979692), ('think', 0.00072646345), ('want', 0.00071983057), ('say', 0.00070850103), ('eat', 0.0007073572)]


give : [('give', 0.017900161), ('stars', 0.01297708), ('could', 0.0105625605), ('would', 0.0044576162), ('star', 0.0040181745)]


try : [('try', 0.004041756), ('tony', 0.002764381), ('pats', 0.0025771223), ('south', 0.002516536), ('street', 0.0023052597)]

""")
elif category == "Chicken Wings":
    st.image("streamlit/wings/customer_rating.png")
    st.image("streamlit/wings/wordCloud.png")
    st.image("streamlit/wings/bigramCloud.png")
    st.write("""**Five Star Reviews**

chicken : [('fried', 0.0655027), ('korean', 0.02410782), ('ever', 0.01587783), ('sandwich', 0.014048549), ('chicken', 0.012594945)]


place : [('area', 0.002625527), ('neighborhood', 0.0019318718), ('city', 0.001832031), ('philadelphia', 0.0015636376), ('new', 0.0015510257)]


great : [('service', 0.002524553), ('staff', 0.0020162885), ('selection', 0.0019207995), ('beer', 0.0019070008), ('prices', 0.0016685834)]


good : [('beer', 0.00086751784), ('selection', 0.0007500457), ('really', 0.00074574514), ('service', 0.00073898), ('prices', 0.00067752233)]


food : [('friendly', 0.003037377), ('staff', 0.0022553853), ('customer', 0.0019819809), ('atmosphere', 0.0019402074), ('clean', 0.0019369868)]


wings : [('garlic', 0.0017033404), ('soy', 0.001480685), ('honey', 0.0014802803), ('korean', 0.0013696767), ('favorite', 0.0012313656)]


fried : [('korean', 0.0063092927), ('fried', 0.0053857225), ('chicken', 0.005191846), ('ever', 0.0041704336), ('best', 0.002867447)]


best : [('ever', 0.0140568735), ('best', 0.009573693), ('city', 0.009478659), ('hands', 0.006757669), ('korean', 0.005489887)]


donuts : [('hot', 0.001412284), ('tried', 0.0011378512), ('fresh', 0.0010797553), ('donuts', 0.0010780585), ('federal', 0.0010596934)]


get : [('wait', 0.0010391661), ('next', 0.0009741176), ('come', 0.0009522377), ('would', 0.0009358579), ('definitely', 0.0009302557)]


like : [('still', 0.00053846295), ('perfect', 0.000515768), ('flavor', 0.0005053127), ('little', 0.00050406397), ('taste', 0.0004931703)]


also : [('sweet', 0.0010850753), ('tasty', 0.00094635715), ('salad', 0.0009145947), ('bread', 0.0008836044), ('also', 0.0008722746)]


love : [('korean', 0.0010141312), ('place', 0.00096705963), ('spot', 0.00095858803), ('love', 0.0009204456), ('area', 0.00084240665)]


go : [('definitely', 0.0017433546), ('would', 0.0016044946), ('try', 0.0012848743), ('coming', 0.00126942), ('come', 0.0012489223)]


time : [('first', 0.004921232), ('every', 0.0034528396), ('last', 0.0033136583), ('time', 0.0033079835), ('next', 0.0026802225)]


order : [('wait', 0.002172015), ('every', 0.001720877), ('made', 0.0016790401), ('order', 0.0016683883), ('make', 0.00153271)]


really : [('beer', 0.001017159), ('awesome', 0.0010103607), ('super', 0.0009923299), ('selection', 0.0009715831), ('excellent', 0.00096679205)]


one : [('city', 0.0020210834), ('philly', 0.0019301334), ('favorite', 0.0017859422), ('places', 0.0017647978), ('one', 0.0016847397)]


i've : [('bread', 0.00057734374), ('salad', 0.0005746084), ('sweet', 0.0005713386), ('seasoned', 0.0005562437), ('flavor', 0.0005546024)]


pizza : [('best', 0.0012785901), ('ever', 0.0012456815), ('cheesesteak', 0.0012410413), ('favorite', 0.00114953), ('city', 0.0010550368)]


delicious : [('crispy', 0.0014542656), ('fresh', 0.001357907), ('tasty', 0.0012359237), ('juicy', 0.001170691), ('super', 0.0011432801)]


back : [('definitely', 0.003601946), ('wait', 0.0034316925), ('come', 0.0031355612), ('back', 0.0029464194), ('would', 0.002675707)]


try : [('definitely', 0.0037442488), ('try', 0.0029878956), ('would', 0.0026775736), ('back', 0.0026647819), ('must', 0.0024104794)]


always : [('friendly', 0.0023256147), ('staff', 0.002077816), ('clean', 0.001490128), ('attentive', 0.0014345568), ('atmosphere', 0.0013886694)]


definitely : [('recommend', 0.007835147), ('definitely', 0.0032794205), ('back', 0.002721502), ('come', 0.0025291592), ('would', 0.0025241554)]


got : [('ordered', 0.0014329455), ('half', 0.0014069333), ('got', 0.0012853565), ('came', 0.0011437135), ('tried', 0.0010501887)]


service : [('friendly', 0.023250716), ('customer', 0.008599777), ('staff', 0.008564888), ('clean', 0.007223588), ('atmosphere', 0.0067123175)]


i'm : [('came', 0.0005278107), ('perfect', 0.0005184192), ('still', 0.0004913454), ('little', 0.00048498463), ('flavor', 0.00047219562)]


hot : [('hot', 0.0043771053), ('fresh', 0.0036655427), ('lavender', 0.0021356216), ('sugar', 0.0020190468), ('cinnamon', 0.0019339423)]


ordered : [('ordered', 0.0015469639), ('got', 0.0013224679), ('half', 0.001313189), ('tried', 0.0011371066), ('came', 0.0010886522)]


amazing : [('absolutely', 0.00065384764), ('korean', 0.0006378379), ('awesome', 0.00062818), ('spot', 0.00062329735), ('pretty', 0.0006001678)]


would : [('recommend', 0.03582657), ('would', 0.004152426), ('definitely', 0.0038312138), ('highly', 0.0031889814), ('recommended', 0.0024733616)]


fresh : [('fresh', 0.0072468366), ('hot', 0.0037826574), ('made', 0.0029255438), ('crispy', 0.0026453333), ('cooked', 0.0022436182)]


well : [('super', 0.0019869627), ('nice', 0.0014005948), ('staff', 0.0013307163), ('tasty', 0.0012981344), ('excellent', 0.0012297552)]


philly : [('philly', 0.006947221), ('city', 0.006088504), ('philadelphia', 0.0047797924), ('area', 0.0041695894), ('places', 0.0029060529)]


nice : [('super', 0.008011049), ('staff', 0.0055451333), ('nice', 0.004302761), ('friendly', 0.003992198), ('inside', 0.0030384124)]


cheese : [('cheese', 0.045663144), ('mac', 0.02162861), ('steak', 0.01066842), ('fries', 0.005620476), ('salad', 0.0055877073)]


spicy : [('garlic', 0.024877135), ('soy', 0.021578202), ('spicy', 0.009563869), ('half', 0.00858049), ('honey', 0.006004738)]


ever : [('best', 0.013722443), ('ever', 0.008327915), ('korean', 0.0050335145), ('city', 0.005030802), ('hands', 0.0047837757)]


donut : [('lavender', 0.0020981182), ('strawberry', 0.0020062434), ('sugar', 0.0017694824), ('donut', 0.0016967289), ('tried', 0.0016518005)]


even : [('came', 0.00072562945), ('make', 0.00072016177), ('even', 0.00070026354), ('made', 0.0006978274), ('us', 0.00069455773)]


friendly : [('staff', 0.023840548), ('friendly', 0.010391778), ('super', 0.007351755), ('attentive', 0.0062832665), ('atmosphere', 0.0060706716)]


sauce : [('garlic', 0.00658198), ('soy', 0.006026048), ('ranch', 0.0047713537), ('chili', 0.004713577), ('seasoned', 0.0044026724)]


come : [('wait', 0.001870554), ('come', 0.0015942256), ('definitely', 0.0014981467), ('try', 0.001440006), ('worth', 0.0014371806)]


staff : [('friendly', 0.01914228), ('super', 0.005192311), ('nice', 0.0045838505), ('staff', 0.0043651713), ('attentive', 0.0038317582)]


made : [('fresh', 0.0024643065), ('made', 0.0024588394), ('came', 0.0013405916), ('super', 0.0012361736), ('hot', 0.0012127066)]


came : [('came', 0.0013403643), ('last', 0.0011965527), ('night', 0.001170041), ('us', 0.001124555), ('first', 0.0010908311)]


first : [('time', 0.0048449747), ('last', 0.0040391525), ('first', 0.0038893698), ('night', 0.0038601507), ('day', 0.0028778424)]


favorite : [('favorite', 0.0026776541), ('ever', 0.002112483), ('korean', 0.0019542577), ('places', 0.0015749214), ('far', 0.0015728996)]


& : [('next', 0.001115541), ('try', 0.0010907834), ('come', 0.0010646209), ('visit', 0.0010386436), ('since', 0.0010160201)]


**One Star Reviews**

order : [('hour', 0.002239005), ('minutes', 0.0020536801), ('hours', 0.0018983784), ('took', 0.00189718), ('waiting', 0.0018320731)]


food : [('ever', 0.0006798234), ('bad', 0.0006647193), ('rude', 0.00066016323), ('experience', 0.0006492504), ('last', 0.00064671965)]


place : [('worst', 0.0018090406), ('ever', 0.0017000233), ('experience', 0.0016905182), ('bad', 0.0015763902), ('horrible', 0.0015760391)]


ordered : [('cheese', 0.0019770488), ('fries', 0.0018712836), ('sauce', 0.0017180433), ('cold', 0.0014192322), ('chicken', 0.0012594059)]


pizza : [('fries', 0.0008940697), ('cold', 0.000887207), ('sandwich', 0.00078733946), ('cheese', 0.0007720076), ('sauce', 0.0007659105)]


chicken : [('cheese', 0.00991339), ('sauce', 0.005259615), ('fries', 0.00505977), ('chicken', 0.004819025), ('fried', 0.004778251)]


get : [('took', 0.0008996419), ('wait', 0.00088153593), ('phone', 0.000859885), ('waiting', 0.00084878755), ('another', 0.00083495316)]


time : [('phone', 0.0008321487), ('going', 0.00081491005), ('wait', 0.00079660566), ('long', 0.0007902068), ('take', 0.00078845606)]


never : [('rude', 0.00090454984), ('going', 0.0008679754), ('location', 0.00084961305), ('money', 0.0008208498), ('people', 0.00078881014)]


like : [('cheese', 0.0022266398), ('fried', 0.0017962453), ('fries', 0.0016715014), ('sauce', 0.0016472847), ('taste', 0.0015181956)]


one : [('going', 0.0006896693), ('want', 0.00068951247), ('make', 0.00067017885), ('see', 0.0006655882), ('sure', 0.00066028745)]


service : [('worst', 0.012219847), ('service', 0.01068273), ('customer', 0.010607122), ('horrible', 0.009515551), ('ever', 0.00945097)]


back : [('phone', 0.0018819855), ('call', 0.0017530393), ('called', 0.0017025904), ('manager', 0.0015915197), ('driver', 0.0014863095)]


would : [('give', 0.001423516), ('could', 0.0013210396), ('would', 0.001250139), ('stars', 0.0012184575), ('phone', 0.0011370775)]


got : [('half', 0.0012522864), ('cold', 0.001167809), ('fries', 0.0011432208), ('two', 0.001102161), ('took', 0.0010580217)]


said : [('called', 0.0021175747), ('phone', 0.0020303675), ('minutes', 0.002000239), ('waiting', 0.0019739354), ('took', 0.0019659428)]


wings : [('cheese', 0.0033442832), ('fries', 0.002621865), ('sauce', 0.00254105), ('chicken', 0.0019547122), ('fried', 0.0019496034)]


even : [('want', 0.0006689015), ('going', 0.0006560047), ('eat', 0.00064413866), ('people', 0.0006434984), ('make', 0.00064295734)]


called : [('called', 0.003458042), ('minutes', 0.0033792453), ('hour', 0.0033576414), ('phone', 0.0029394159), ('waiting', 0.0029168983)]


told : [('called', 0.0018605208), ('phone', 0.0018281089), ('hour', 0.0018232084), ('minutes', 0.0018189265), ('took', 0.001812583)]


go : [('rude', 0.00093591027), ('going', 0.0009003743), ('location', 0.0008870195), ('money', 0.0008659891), ('people', 0.00084149576)]


good : [('bad', 0.00125345), ('experience', 0.001203666), ('worst', 0.0011390756), ('ever', 0.001110473), ('horrible', 0.0010878828)]


minutes : [('hour', 0.00643126), ('minutes', 0.0052655926), ('took', 0.004727157), ('hours', 0.0046531423), ('waited', 0.004451086)]


asked : [('took', 0.0014320306), ('waiting', 0.0013711818), ('hour', 0.0012913095), ('pm', 0.0012700385), ('asked', 0.0012587822)]


us : [('took', 0.001464494), ('waiting', 0.0014156151), ('wait', 0.0013752913), ('phone', 0.0013428035), ('another', 0.0012878258)]


came : [('took', 0.0011719246), ('pm', 0.001068339), ('half', 0.0010568541), ('waiting', 0.001052093), ('two', 0.0010477048)]


give : [('stars', 0.0024209712), ('give', 0.0022685379), ('could', 0.0019344407), ('would', 0.0014523211), ('money', 0.0011744393)]


customer : [('service', 0.01421256), ('worst', 0.013234766), ('ever', 0.011168287), ('experience', 0.0106024835), ('horrible', 0.010342449)]


delivery : [('took', 0.001582994), ('hour', 0.0015697586), ('hours', 0.0015574612), ('wait', 0.0014514767), ('waiting', 0.0014439473)]


i'm : [('want', 0.0007230376), ('eat', 0.00071415026), ('last', 0.0007043465), ('going', 0.0007019878), ('people', 0.00070159585)]


manager : [('phone', 0.0017233525), ('call', 0.0015209358), ('manager', 0.0014810323), ('called', 0.0012755824), ('driver', 0.001273305)]


hour : [('hour', 0.0063214027), ('minutes', 0.0047127986), ('took', 0.0046795933), ('hours', 0.004550283), ('waited', 0.0044075027)]


could : [('give', 0.0015971955), ('could', 0.0015913311), ('stars', 0.001280609), ('would', 0.001207223), ('phone', 0.0010646313)]


went : [('took', 0.0013442392), ('wait', 0.0012736965), ('waiting', 0.0012595311), ('phone', 0.0012521294), ('pm', 0.0012188535)]


ever : [('worst', 0.004674337), ('ever', 0.004280405), ('experience', 0.0035149923), ('horrible', 0.00312627), ('customer', 0.0029275522)]


2 : [('eat', 0.0007356849), ('want', 0.0007162248), ('really', 0.0007121245), ('better', 0.00069899904), ('sure', 0.0006955963)]


still : [('took', 0.0018057191), ('hour', 0.001726725), ('waiting', 0.0016220813), ('hours', 0.0015845889), ('waited', 0.0015265525)]


cheese : [('cheese', 0.027205972), ('sauce', 0.0119258305), ('fries', 0.011332561), ('chicken', 0.009579307), ('fried', 0.009358772)]


people : [('bad', 0.0010324478), ('rude', 0.0009699453), ('location', 0.0009250459), ('experience', 0.00090677885), ('people', 0.00089881517)]


bad : [('worst', 0.003243113), ('experience', 0.0030830451), ('ever', 0.0030041945), ('horrible', 0.0028573694), ('bad', 0.0027110525)]


first : [('sandwich', 0.0008423876), ('fries', 0.00078743097), ('eat', 0.00076444534), ('taste', 0.0007450413), ('also', 0.0007415031)]


know : [('bad', 0.000987571), ('really', 0.000882907), ('rude', 0.0008743186), ('better', 0.0008652944), ('want', 0.0008583711)]


another : [('took', 0.0020510177), ('hour', 0.002008586), ('waiting', 0.0019172715), ('hours', 0.0018339802), ('wait', 0.0018022688)]


worst : [('worst', 0.008724994), ('ever', 0.008195718), ('experience', 0.006374783), ('service', 0.006140994), ('horrible', 0.0056910333)]


come : [('phone', 0.0011643558), ('call', 0.0010468302), ('wait', 0.0010384299), ('take', 0.0010061808), ('going', 0.0009905136)]


i've : [('phone', 0.0016464416), ('called', 0.0015907771), ('call', 0.0015139808), ('took', 0.0014167774), ('waiting', 0.0014134893)]


location : [('ever', 0.0014650053), ('bad', 0.0014228013), ('experience', 0.0014089292), ('worst', 0.0013465969), ('horrible', 0.001230949)]


call : [('phone', 0.0023166663), ('call', 0.0021244602), ('called', 0.0018816659), ('driver', 0.0018119457), ('manager', 0.0018004529)]


sauce : [('cheese', 0.026567983), ('sauce', 0.013242763), ('fries', 0.01201994), ('chicken', 0.0094983615), ('fried', 0.008429895)]


want : [('going', 0.0008637214), ('rude', 0.00083550176), ('want', 0.00081823673), ('people', 0.0007924503), ('money', 0.00078647427)]
""")
elif category == "Chinese":
    st.image("streamlit/chinese/customer_rating.png")
    st.image("streamlit/chinese/wordCloud.png")
    st.image("streamlit/chinese/bigramCloud.png")
    st.write("""**Five Star Reviews**
    
food : [('asian', 0.042030394), ('comfort', 0.035984512), ('chinese', 0.019288078), ('quality', 0.013652301), ('vietnamese', 0.008605243)]


place : [('go-to', 0.025097474), ('love', 0.017515555), ('hit', 0.009781518), ('awesome', 0.006843312), ('cool', 0.0046721483)]


great : [('service', 0.061928574), ('experience', 0.046939682), ('prices', 0.018858999), ('atmosphere', 0.018044842), ('environment', 0.014177087)]


good : [('pretty', 0.3256817), ('really', 0.046682186), ('soooo', 0.013778503), ('damn', 0.0101011405), ('sooo', 0.0053710197)]


best : [('ever', 0.10935535), ('city', 0.028062958), ('hands', 0.020095235), ('town', 0.0094008045), ('absolute', 0.006876326)]


get : [('usually', 0.002086804), ('early', 0.0015553307), ('want', 0.0011898002), ('hard', 0.0011128606), ('sure', 0.0010716113)]


one : [('places', 0.009786914), ('restaurants', 0.0040223594), ('favorite', 0.003182022), ('spots', 0.0030221876), ('thing', 0.0026549436)]


like : [('feel', 0.010572163), ('looks', 0.006010825), ('felt', 0.0045537096), ('feels', 0.002830671), ('something', 0.0023227239)]


go : [('wrong', 0.036154334), ('back', 0.0035143804), ('whenever', 0.0033393744), ('wait', 0.002907445), ('want', 0.0023699878)]


also : [('enjoyed', 0.0014054812), ('tried', 0.00087744364), ('ordered', 0.0008506433), ('got', 0.0008183879), ('byob', 0.00071915716)]


soup : [('noodle', 0.09228011), ('wonton', 0.073716655), ('miso', 0.027222112), ('base', 0.021564508), ('dumplings', 0.019764032)]


time : [('next', 0.20693293), ('every', 0.07895443), ('first', 0.07396559), ('long', 0.013786363), ('last', 0.010269826)]


love : [('absolutely', 0.0038830603), ('love', 0.0019034412), ('place', 0.0015702953), ('much', 0.0011104601), ('coming', 0.0010815179)]


chinese : [('authentic', 0.018800806), ('american', 0.01845869), ('restaurants', 0.018091252), ('traditional', 0.014100924), ('americanized', 0.012221187)]


service : [('customer', 0.018800482), ('quick', 0.015637135), ('excellent', 0.012529271), ('impeccable', 0.01097454), ('speedy', 0.009573321)]


really : [('enjoyed', 0.014004213), ('liked', 0.0051972144), ('good', 0.002716519), ('cool', 0.0021782736), ('nice', 0.0012681222)]


delicious : [('absolutely', 0.0032996815), ('everything', 0.0015596463), ('fresh', 0.0010541904), ('cheap', 0.00076231116), ('equally', 0.0007036587)]


restaurant : [('week', 0.0038939032), ('asian', 0.0030498554), ('starr', 0.002499938), ('clean', 0.002465651), ('chinese', 0.0023914343)]


definitely : [('recommend', 0.025698), ('worth', 0.013120607), ('return', 0.009824882), ('returning', 0.0054594465), ('back', 0.004332712)]


pork : [('belly', 0.2796108), ('roast', 0.20628902), ('buns', 0.015456935), ('minced', 0.012054228), ('roasted', 0.009382956)]


chicken : [('general', 0.049623434), ('kung', 0.013165266), ('wings', 0.012486634), ('pao', 0.011824352), ('broccoli', 0.010575835)]


i've : [('especially', 0.00026022355), ('awesome', 0.00025942456), ('loved', 0.00024749368), ('wonderful', 0.00023996136), ('oh', 0.00023738279)]


always : [('packed', 0.0017289608), ('point', 0.0017199632), ('consistent', 0.0014696186), ('almost', 0.0013289895), ('consistently', 0.0012329093)]


noodles : [('shaved', 0.06662321), ('hand', 0.06559676), ('dan', 0.033827055), ('drawn', 0.02347307), ('dandan', 0.010241721)]


back : [('come', 0.033490166), ('coming', 0.02015848), ('soon', 0.009109281), ('wait', 0.006934682), ('definitely', 0.005083491)]


dumplings : [('edamame', 0.29380447), ('soup', 0.033992406), ('pork', 0.00854146), ('steamed', 0.005516159), ('chive', 0.0046398933)]


try : [('must', 0.045998197), ('items', 0.007220203), ('wanted', 0.0071631763), ('things', 0.0066743204), ('decided', 0.006581034)]


would : [('recommend', 0.19742537), ('suggest', 0.0097470805), ('say', 0.003034833), ('recommended', 0.0022230195), ('probably', 0.001511593)]


everything : [('else', 0.06483755), ('menu', 0.003866374), ('ate', 0.0030671917), ('tried', 0.002911354), ('ordered', 0.0025374203)]


ordered : [('friend', 0.010873228), ('boyfriend', 0.004830234), ('girlfriend', 0.0037615946), ('entrees', 0.0032884728), ('everything', 0.0030988397)]


amazing : [('absolutely', 0.0023963337), ('cocktails', 0.0010949554), ('simply', 0.0010361791), ('service', 0.0008867507), ('everything', 0.000879431)]


fried : [('rice', 0.8037783), ('pan', 0.1016812), ('stir', 0.025505353), ('deep', 0.0025259245), ('kim', 0.0007092687)]


spicy : [('cucumbers', 0.019349186), ('spicy', 0.0105415825), ('medium', 0.0076572294), ('handle', 0.006563173), ('numbing', 0.006266683)]


philly : [('visiting', 0.021091966), ('south', 0.011153604), ('visit', 0.006589318), ('must', 0.0042527597), ('west', 0.0040558516)]


hot : [('pot', 0.98101324), ('sour', 0.012000818), ('piping', 0.0013636479), ('pots', 0.000783287), ('pepper', 0.00019324344)]


order : [('online', 0.0066844695), ('placed', 0.0034113661), ('grubhub', 0.0029157521), ('ready', 0.0026975323), ('take', 0.0026860193)]


come : [('back', 0.045634214), ('often', 0.0034809795), ('hungry', 0.00325963), ('would', 0.0026671058), ('whenever', 0.0023726933)]


favorite : [('personal', 0.022308301), ('absolute', 0.020740654), ('spots', 0.004730493), ('one', 0.004703336), ('far', 0.003801045)]


beef : [('wagyu', 0.07197815), ('brisket', 0.042575702), ('tendon', 0.019585239), ('braised', 0.01215658), ('satay', 0.011759384)]


menu : [('extensive', 0.14855884), ('items', 0.07747449), ('tasting', 0.048184093), ('item', 0.0064235283), ('knowledgeable', 0.0043548564)]


got : [('friend', 0.00834348), ('boyfriend', 0.004173341), ('mom', 0.002468325), ('girlfriend', 0.0022008258), ('finally', 0.0019268739)]


fresh : [('produce', 0.017185282), ('ingredients', 0.00966498), ('made', 0.008581217), ('seafood', 0.006993542), ('fruits', 0.0069140736)]


eat : [('could', 0.0092847375), ('want', 0.0030514237), ('able', 0.0015583979), ('wanted', 0.0014330194), ('hard', 0.0014087677)]


i'm : [('found', 0.00032538452), ('city', 0.00028752236), ('original', 0.00028668705), ('makes', 0.000279196), ('similar', 0.00027572844)]


recommend : [('highly', 0.9996778), ('strongly', 6.966912e-05), ('anyone', 3.3718217e-05), ('would', 3.015131e-05), ('checking', 5.8243163e-06)]


sauce : [('soy', 0.09538876), ('dipping', 0.08826188), ('chili', 0.04651354), ('garlic', 0.042907674), ('bar', 0.013839915)]


well : [('cooked', 0.010973654), ('worth', 0.0070781265), ('seasoned', 0.0062274), ('done', 0.004708298), ('prepared', 0.00359087)]


even : [('though', 0.18314245), ('better', 0.102220185), ('packed', 0.0010840796), ('close', 0.0010688698), ('begin', 0.0010351542)]


rice : [('fried', 0.9068394), ('white', 0.016028976), ('brown', 0.007694223), ('sticky', 0.0076873805), ('fry', 0.0020864226)]


nice : [('staff', 0.00981329), ('touch', 0.0046574855), ('servers', 0.0044071088), ('super', 0.0032846252), ('environment', 0.0029398855)]


**One Star Reviews**

food : [('terrible', 0.004615983), ('horrible', 0.0046133823), ('good', 0.003992501), ('great', 0.0032822045), ('mediocre', 0.0030564545)]


place : [('reviews', 0.002357206), ('recommend', 0.0017876345), ('philly', 0.001444709), ('chinatown', 0.0014146357), ('dynasty', 0.0014115752)]


order : [('called', 0.003436234), ('delivery', 0.0031654716), ('order', 0.0021194874), ('hour', 0.002039324), ('grubhub', 0.001911233)]


us : [('table', 0.0049810545), ('waiter', 0.0044507287), ('waitress', 0.0041320627), ('bill', 0.004052773), ('tip', 0.0032776305)]


like : [('tasted', 0.0026748667), ('taste', 0.0026158772), ('like', 0.001432089), ('everything', 0.0011374218), ('sauce', 0.001136032)]


ordered : [('ordered', 0.004363429), ('rolls', 0.002446049), ('shrimp', 0.0022101111), ('roll', 0.0021553272), ('lunch', 0.0021042337)]


service : [('terrible', 0.023654202), ('horrible', 0.019100882), ('customer', 0.018546198), ('poor', 0.011998278), ('bad', 0.006473008)]


one : [('one', 0.0015951291), ('star', 0.0014717212), ('give', 0.0012486526), ('could', 0.0008567393), ('stars', 0.0007962679)]


never : [('ever', 0.0059312712), ('never', 0.0033546132), ('worst', 0.0025412887), ('come', 0.0017899441), ('back', 0.0017562893)]


restaurant : [('years', 0.0011152027), ('dining', 0.0009795275), ('worst', 0.0009556062), ('restaurant', 0.00095505116), ('philadelphia', 0.0008938654)]


would : [('give', 0.0030748108), ('would', 0.0029345707), ('stars', 0.0020546273), ('could', 0.0019906866), ('recommend', 0.0017549319)]


time : [('last', 0.008529552), ('first', 0.004897663), ('night', 0.0030182921), ('time', 0.002085923), ('today', 0.0020251274)]


even : [('water', 0.0009336062), ('enough', 0.00075078156), ('everything', 0.0006900037), ('waitress', 0.0006809397), ('gave', 0.0006379932)]


back : [('come', 0.004139503), ('go', 0.003520902), ('back', 0.0033828206), ('never', 0.0031048576), ('going', 0.0027776177)]


get : [('money', 0.0009842966), ('want', 0.0008987816), ('get', 0.00088265433), ('else', 0.00083193934), ('take', 0.0008282994)]


good : [('quality', 0.0020570613), ('reviews', 0.0018790911), ('service', 0.0018320275), ('experience', 0.0017310699), ('pretty', 0.0016339041)]


chicken : [('tso', 0.006983493), ('general', 0.0056812647), ('broccoli', 0.005003154), ('chicken', 0.0047441674), ('shrimp', 0.003932068)]


got : [('arrived', 0.00082338677), ('two', 0.0007930291), ('ordered', 0.00078595127), ('hours', 0.000741421), ('half', 0.00073778845)]


go : [('go', 0.004153529), ('recommend', 0.0032534373), ('back', 0.0032261377), ('going', 0.0021802671), ('eat', 0.0020194326)]


came : [('sat', 0.0012836787), ('finally', 0.0012354965), ('brought', 0.001226164), ('table', 0.001180601), ('minutes', 0.0011228209)]


said : [('said', 0.0024800915), ('called', 0.00226531), ('told', 0.0019698304), ('card', 0.0019360089), ('phone', 0.0019095455)]


chinese : [('better', 0.0042908713), ('restaurants', 0.0042625004), ('places', 0.0042443494), ('chinese', 0.004102234), ('chinatown', 0.0036258006)]


told : [('asked', 0.001892586), ('told', 0.0017731127), ('check', 0.0016061041), ('said', 0.0015901382), ('called', 0.0015490346)]


asked : [('asked', 0.0037128683), ('charged', 0.0029638123), ('waitress', 0.0024599864), ('bill', 0.0024312881), ('waiter', 0.0023306755)]


rice : [('fried', 0.008275524), ('rice', 0.005306543), ('white', 0.0040939315), ('shrimp', 0.003527944), ('roll', 0.0031546894)]


bad : [('service', 0.0027987156), ('extremely', 0.0019740073), ('taste', 0.0018907413), ('experience', 0.001830633), ('absolutely', 0.0016778581)]


eat : [('eat', 0.0014178394), ('else', 0.0013588276), ('go', 0.0011076225), ('better', 0.00096281193), ('bbq', 0.00091841)]


give : [('give', 0.019889014), ('star', 0.017413039), ('stars', 0.0148084415), ('could', 0.00774967), ('zero', 0.0068812794)]


table : [('table', 0.009090185), ('seated', 0.0040743425), ('tables', 0.0039792163), ('water', 0.0037176036), ('sat', 0.003566717)]


soup : [('soup', 0.012189431), ('dumplings', 0.0055967895), ('noodle', 0.0043630158), ('wonton', 0.0038738432), ('pork', 0.0029508178)]


could : [('give', 0.0056443834), ('could', 0.0040141866), ('star', 0.0033288044), ('stars', 0.0033129319), ('zero', 0.0021670454)]


minutes : [('waited', 0.014376339), ('hour', 0.011800029), ('minutes', 0.011112291), ('later', 0.007925303), ('wait', 0.007074023)]


ever : [('worst', 0.0845347), ('ever', 0.021545542), ('never', 0.0062877215), ('life', 0.0055018715), ('delivery', 0.0026631078)]


really : [('reviews', 0.0018796077), ('quality', 0.0015718935), ('really', 0.0014903542), ('bad', 0.001476569), ('great', 0.0013474778)]


i'm : [('years', 0.00084437395), ('chinatown', 0.0007547447), ('many', 0.0007502155), ('philly', 0.00072446396), ('last', 0.00071744673)]


people : [('people', 0.0019485314), ('many', 0.0014032518), ('customers', 0.0013793348), ('tables', 0.0013522743), ('around', 0.0012855245)]


first : [('time', 0.006059466), ('last', 0.0047866427), ('night', 0.004204762), ('first', 0.0022303737), ('today', 0.0020376774)]


come : [('back', 0.003053908), ('never', 0.0021348617), ('come', 0.0015992573), ('going', 0.0014322734), ('coming', 0.0012421986)]


went : [('last', 0.0052391603), ('night', 0.003887859), ('went', 0.0038266573), ('pm', 0.003720789), ('dinner', 0.0033284815)]


take : [('told', 0.0010921855), ('hour', 0.0010578089), ('call', 0.0010535668), ('called', 0.0010279625), ('another', 0.0009778042)]


know : [('want', 0.0017078904), ('know', 0.0017005745), ('going', 0.0014823283), ('money', 0.0013662074), ('let', 0.0012972688)]


fried : [('rice', 0.010639065), ('fried', 0.0068034395), ('shrimp', 0.005511773), ('pork', 0.0042330995), ('roll', 0.003804557)]


also : [('also', 0.0006808806), ('small', 0.0006588229), ('two', 0.00061849045), ('served', 0.0005911481), ('cold', 0.00058836676)]


sauce : [('sauce', 0.011427627), ('sweet', 0.004304653), ('garlic', 0.00427694), ('soy', 0.00381736), ('meat', 0.003779353)]


called : [('called', 0.009324399), ('phone', 0.0060835346), ('delivery', 0.005339578), ('driver', 0.00505632), ('call', 0.004696254)]


worst : [('ever', 0.14228265), ('worst', 0.03701578), ('experience', 0.011642799), ('life', 0.010907205), ('part', 0.0055439635)]


i've : [('tasted', 0.0018658714), ('taste', 0.0016699957), ('bland', 0.0014601557), ('flavor', 0.0014452869), ('salty', 0.0013256934)]


took : [('hour', 0.011975353), ('minutes', 0.010690021), ('waited', 0.008871414), ('mins', 0.0056907404), ('took', 0.005149892)]


two : [('two', 0.005719436), ('tables', 0.0026079332), ('pm', 0.0023968702), ('three', 0.0022568156), ('seated', 0.0021441611)]


shrimp : [('shrimp', 0.0064023295), ('fried', 0.0060339), ('roll', 0.005068082), ('broccoli', 0.0040547056), ('egg', 0.0038188512)]

""")
elif category == "Coffee & Tea":
    st.image("streamlit/coffeetea/customer_rating.png")
    st.image("streamlit/coffeetea/wordCloud.png")
    st.image("streamlit/coffeetea/bigramCloud.png")
    st.write("""**Five Star Reviews**

place : [('go-to', 0.030420424), ('awesome', 0.0065581813), ('rocks', 0.0056213266), ('study', 0.0048703398), ('chill', 0.004637225)]


great : [('service', 0.03349244), ('experience', 0.024182344), ('atmosphere', 0.015979476), ('selection', 0.015091176), ('vibes', 0.00936472)]


coffee : [('shop', 0.6307964), ('drip', 0.12704208), ('iced', 0.123800576), ('shops', 0.033437103), ('cup', 0.027045907)]


food : [('ethiopian', 0.040192023), ('comfort', 0.034624007), ('fantastic', 0.017029975), ('delicious', 0.012111408), ('excellent', 0.011850035)]


good : [('pretty', 0.0038569544), ('really', 0.0020488221), ('karma', 0.0014393358), ('soooo', 0.0013492557), ('sooooo', 0.0012762968)]


one : [('places', 0.005328969), ('favorites', 0.003191244), ('favorite', 0.0030703512), ('shot', 0.002526308), ('spots', 0.0019797909)]


get : [('usually', 0.0022501356), ('anything', 0.0017022347), ('hard', 0.0016483911), ('chance', 0.001538733), ('early', 0.0014289233)]


love : [('fell', 0.002916307), ('absolutely', 0.0023230067), ('much', 0.0012666227), ('coming', 0.0011405246), ('love', 0.0010839326)]


like : [('feel', 0.06080316), ('felt', 0.02871709), ('looks', 0.02708152), ('feels', 0.019283459), ('tastes', 0.0056942003)]


also : [('got', 0.0013393313), ('enjoyed', 0.0008321254), ('tried', 0.0007883879), ('ordered', 0.0007579052), ('liked', 0.00068952487)]


delicious : [('absolutely', 0.0067433775), ('equally', 0.0011031291), ('crepes', 0.0010467166), ('food', 0.0010042302), ('amazingly', 0.0009158968)]


go : [('wrong', 0.07249286), ('back', 0.002659566), ('want', 0.0019116418), ('wait', 0.0018785617), ('grab', 0.0017334957)]


best : [('ever', 0.17715767), ('city', 0.018870657), ('part', 0.010566096), ('hands', 0.010268615), ('possibly', 0.007387255)]


really : [('enjoyed', 0.0073139276), ('liked', 0.0068313195), ('nice', 0.0022210802), ('impressed', 0.0020818007), ('appreciate', 0.0018745138)]


time : [('next', 0.4236693), ('every', 0.040652998), ('first', 0.036607366), ('last', 0.010989564), ('long', 0.0070223343)]


back : [('come', 0.02556014), ('coming', 0.025360096), ('laid', 0.014298213), ('definitely', 0.0068054516), ('soon', 0.0049056998)]


i've : [('blue', 0.00015570965), ('awesome', 0.00014981326), ('especially', 0.00014693798), ('oh', 0.00014644333), ('win', 0.00014488099)]


definitely : [('worth', 0.01693892), ('recommend', 0.014941506), ('return', 0.011136273), ('back', 0.006511672), ('returning', 0.0051538497)]


try : [('must', 0.026586447), ('give', 0.013695983), ('gotta', 0.012415809), ('chance', 0.012100733), ('excited', 0.009563612)]


amazing : [('simply', 0.0012863757), ('absolutely', 0.001284663), ('food', 0.0012079588), ('experience', 0.00095283176), ('donuts', 0.0007360059)]


always : [('smile', 0.0020081108), ('busy', 0.0018543869), ('point', 0.0013974465), ('fan', 0.001274761), ('times', 0.0010583269)]


friendly : [('staff', 0.31901067), ('baristas', 0.032811996), ('employees', 0.014885037), ('super', 0.012332864), ('workers', 0.007246485)]


service : [('customer', 0.12636136), ('quick', 0.054400668), ('impeccable', 0.023075908), ('fast', 0.02045351), ('prompt', 0.014073375)]


i'm : [('sauce', 0.00025534836), ('top', 0.00023904328), ('white', 0.00023814305), ('red', 0.00022575253), ('sprinkled', 0.00022555633)]


got : [('friend', 0.006174283), ('boyfriend', 0.0046861195), ('sister', 0.0024375303), ('bf', 0.0019651365), ('recently', 0.0017483366)]


would : [('recommend', 0.3849802), ('suggest', 0.005303168), ('say', 0.0030539904), ('lived', 0.002722946), ('thought', 0.0020031775)]


fresh : [('ingredients', 0.0354963), ('squeezed', 0.027772043), ('produce', 0.019062694), ('juice', 0.017807337), ('fruit', 0.015101148)]


staff : [('friendly', 0.43747705), ('attentive', 0.0062133204), ('helpful', 0.0048878333), ('polite', 0.0034462991), ('courteous', 0.0033332515)]


philly : [('south', 0.59392756), ('west', 0.043726336), ('visiting', 0.01707294), ('trip', 0.0054374724), ('cheesesteak', 0.0031261295)]


nice : [('touch', 0.0024570285), ('super', 0.0023400297), ('really', 0.002023848), ('employees', 0.0016535283), ('baristas', 0.0015049289)]


breakfast : [('burrito', 0.10730207), ('sandwiches', 0.04483445), ('sandwich', 0.0355317), ('lunch', 0.031572543), ('burritos', 0.004728645)]


everything : [('else', 0.056452073), ('menu', 0.008134646), ('looks', 0.0022615178), ('fresh', 0.0016847185), ('looked', 0.0016498887)]


well : [('done', 0.03212103), ('worth', 0.012491548), ('priced', 0.0062281294), ('cooked', 0.0046191197), ('seasoned', 0.004511792)]


little : [('pricey', 0.037876822), ('bit', 0.0207967), ('spoon', 0.017955115), ('cute', 0.015498008), ('gem', 0.009616723)]


come : [('back', 0.024011217), ('often', 0.003221184), ('would', 0.0027298168), ('hungry', 0.0025387104), ('wrong', 0.0024171898)]


even : [('though', 0.29922974), ('better', 0.07773778), ('maybe', 0.0013096603), ('close', 0.0009835564), ('gave', 0.00095710345)]


favorite : [('personal', 0.08724553), ('absolute', 0.033784807), ('new', 0.015718805), ('far', 0.014337067), ('become', 0.0061861323)]


chicken : [('fried', 0.95268375), ('wings', 0.0026359498), ('ranch', 0.0026010098), ('popcorn', 0.0015004241), ('korean', 0.0014241216)]


menu : [('extensive', 0.2171531), ('items', 0.05317322), ('tasting', 0.014993809), ('specials', 0.009374612), ('changes', 0.0093107335)]


cafe : [('la', 0.045647543), ('rim', 0.018688736), ('ole', 0.014087551), ('soho', 0.01335227), ('mood', 0.013044122)]


make : [('sure', 0.44487184), ('reservation', 0.010725706), ('scratch', 0.008065912), ('decision', 0.0066415532), ('freshly', 0.0063812006)]


made : [('freshly', 0.4827885), ('scratch', 0.019336777), ('home', 0.00907462), ('perfectly', 0.007119849), ('house', 0.005947078)]


every : [('single', 0.610828), ('bite', 0.070002586), ('penny', 0.019500531), ('day', 0.014963816), ('month', 0.01267909)]


ordered : [('friend', 0.008113415), ('boyfriend', 0.0057427227), ('bf', 0.00463552), ('huevos', 0.003463262), ('shakshuka', 0.00326081)]


ever : [('best', 0.20593171), ('eaten', 0.016352123), ('tasted', 0.010233145), ('hands', 0.008397217), ('seen', 0.0063020643)]


spot : [('hit', 0.016964208), ('go-to', 0.016576923), ('brunch', 0.013761803), ('study', 0.009492676), ('new', 0.0048196632)]


people : [('watching', 0.21381174), ('many', 0.013740574), ('work', 0.009601207), ('watch', 0.008839377), ('working', 0.008637143)]


recommend : [('highly', 0.99999845), ('strongly', 9.260714e-07), ('would', 1.7911209e-07), ('anyone', 1.0611165e-07), ('getting', 1.5044385e-08)]


sandwich : [('egg', 0.032934453), ('breakfast', 0.030993752), ('turkey', 0.012087075), ('chicken', 0.009466627), ('bagel', 0.005308391)]


super : [('friendly', 0.0072554005), ('busy', 0.0064891865), ('cute', 0.005221159), ('fast', 0.0027690572), ('nice', 0.0024782878)]


**One Star Reviews**

food : [('food', 0.0015353285), ('service', 0.001503654), ('horrible', 0.0010388843), ('terrible', 0.00097456324), ('customer', 0.0009522369)]


place : [('recommend', 0.0014382323), ('reviews', 0.0014315454), ('better', 0.0013363777), ('love', 0.0012323437), ('city', 0.0012041111)]


order : [('waited', 0.0022674287), ('min', 0.0022582938), ('took', 0.0021882069), ('mins', 0.0021555477), ('hour', 0.0021380645)]


like : [('tasted', 0.00276984), ('taste', 0.002305856), ('like', 0.0018471447), ('really', 0.0015677836), ('old', 0.0011707575)]


one : [('one', 0.00058096554), ('ever', 0.0005105255), ('another', 0.000469202), ('two', 0.00046837), ('around', 0.00045732295)]


get : [('another', 0.0007681114), ('took', 0.0007659434), ('half', 0.0007205233), ('hour', 0.0007140483), ('get', 0.00071082753)]


coffee : [('tea', 0.0033750003), ('coffee', 0.003164435), ('iced', 0.0021084729), ('cup', 0.002011594), ('milk', 0.0016623187)]


time : [('last', 0.004245705), ('time', 0.0039463937), ('first', 0.0036891855), ('every', 0.0036646228), ('waste', 0.0022522195)]


service : [('customer', 0.013460766), ('terrible', 0.007049875), ('horrible', 0.006758975), ('poor', 0.0061442913), ('slow', 0.005966592)]


would : [('give', 0.0054754233), ('would', 0.0031530343), ('could', 0.0029867955), ('stars', 0.0028562602), ('else', 0.0017294756)]


back : [('go', 0.0032788902), ('come', 0.0028854106), ('going', 0.0027533874), ('back', 0.0020850142), ('went', 0.0020202065)]


even : [('could', 0.0005450695), ('manager', 0.00054096343), ('wait', 0.0005340731), ('customers', 0.00053366594), ('make', 0.0005204626)]


go : [('back', 0.003093976), ('go', 0.0025325937), ('waste', 0.002205756), ('recommend', 0.002082107), ('never', 0.0020679678)]


ordered : [('egg', 0.0047084983), ('bacon', 0.004484593), ('cheese', 0.0038917665), ('eggs', 0.0031676076), ('turkey', 0.0029216132)]


never : [('ever', 0.0027289453), ('never', 0.0021837507), ('go', 0.002169798), ('come', 0.0020023833), ('going', 0.0019488097)]


got : [('half', 0.0014744811), ('sandwich', 0.00132711), ('egg', 0.0013266956), ('bacon', 0.0013109554), ('finally', 0.0012785143)]


us : [('us', 0.00487793), ('table', 0.004102402), ('counter', 0.0029642584), ('waitress', 0.0029320985), ('behind', 0.0027205409)]


asked : [('asked', 0.0072042444), ('said', 0.0034231185), ('told', 0.0029656023), ('gave', 0.0028719185), ('us', 0.00268138)]


people : [('rude', 0.0026396487), ('customers', 0.0026133375), ('staff', 0.0021627191), ('employees', 0.0021492166), ('working', 0.0019900678)]


minutes : [('waited', 0.02165775), ('waiting', 0.010157416), ('took', 0.009669202), ('hour', 0.008451837), ('minutes', 0.006978301)]


said : [('said', 0.0040286384), ('asked', 0.003496353), ('told', 0.002980155), ('ask', 0.0025606856), ('card', 0.0025065711)]


good : [('taste', 0.0022937541), ('quality', 0.002092963), ('good', 0.001704371), ('tasted', 0.0016657303), ('better', 0.0016576555)]


went : [('went', 0.0021188178), ('last', 0.0020603323), ('back', 0.0019405438), ('today', 0.0018529105), ('breakfast', 0.0017698576)]


came : [('finally', 0.0019830319), ('later', 0.0017396335), ('hour', 0.0015231686), ('came', 0.0014444301), ('friend', 0.0013893291)]


told : [('told', 0.0026378417), ('asked', 0.0023921346), ('said', 0.002347388), ('ask', 0.0022306414), ('card', 0.0021776308)]


i'm : [('customer', 0.0008447809), ('rude', 0.0008361719), ('staff', 0.00080688513), ('friendly', 0.00069912017), ('employees', 0.0006862684)]


could : [('give', 0.00345712), ('could', 0.003067474), ('would', 0.0013937699), ('wanted', 0.0012724452), ('asked', 0.0010752174)]


really : [('taste', 0.002406457), ('really', 0.0023644352), ('better', 0.0020519635), ('quality', 0.0016609009), ('great', 0.0016600733)]


customer : [('service', 0.025348108), ('customer', 0.010163506), ('rude', 0.008921268), ('staff', 0.0068684034), ('poor', 0.0045666946)]


i've : [('quality', 0.0006860633), ('experience', 0.0006843709), ('better', 0.0006659568), ('love', 0.00063663535), ('great', 0.00063255744)]


make : [('could', 0.0009264503), ('much', 0.0009003393), ('want', 0.0008786084), ('know', 0.000814992), ('give', 0.0008141424)]


ever : [('worst', 0.07118418), ('ever', 0.036091644), ('mcdonald', 0.0055625294), ('dunkin', 0.005386994), ('life', 0.0050001238)]


staff : [('rude', 0.008341159), ('staff', 0.0043174704), ('customer', 0.00385771), ('friendly', 0.0033044901), ('slow', 0.002818119)]


first : [('time', 0.0031713678), ('last', 0.0021225486), ('first', 0.00171743), ('went', 0.0014560522), ('today', 0.0014435255)]


sandwich : [('egg', 0.009124306), ('cheese', 0.009024076), ('bacon', 0.008055304), ('cream', 0.005373915), ('chicken', 0.0050044907)]


bad : [('quality', 0.0028903391), ('experience', 0.0027622085), ('reviews', 0.0023299537), ('overall', 0.002213224), ('great', 0.0017639425)]


two : [('two', 0.0025623196), ('waited', 0.0023964185), ('hour', 0.0017938211), ('finally', 0.0015571157), ('took', 0.0015525526)]


know : [('know', 0.0009310358), ('much', 0.00085458776), ('really', 0.0008130811), ('want', 0.000810769), ('owner', 0.0007899985)]


going : [('going', 0.001214201), ('else', 0.001172896), ('back', 0.0011691479), ('say', 0.0011214336), ('want', 0.0010570766)]


give : [('give', 0.020058108), ('stars', 0.01092365), ('could', 0.008700298), ('would', 0.0061678276), ('zero', 0.0046643345)]


rude : [('rude', 0.011568112), ('staff', 0.007311522), ('customer', 0.0042859237), ('friendly', 0.0036938929), ('employees', 0.0035757027)]


come : [('back', 0.0030483683), ('never', 0.0017211264), ('come', 0.0015326474), ('every', 0.0014339121), ('money', 0.0012485143)]


took : [('minutes', 0.004372428), ('hour', 0.003997889), ('waited', 0.0027665307), ('took', 0.002460951), ('mins', 0.0023718246)]


also : [('bread', 0.0007709754), ('tasted', 0.0007586062), ('chicken', 0.0007478945), ('also', 0.00072070654), ('small', 0.00069932826)]


worst : [('ever', 0.0956428), ('worst', 0.0800366), ('experience', 0.007331612), ('mcdonald', 0.0067664534), ('life', 0.0056351763)]


way : [('better', 0.00088859), ('much', 0.0008312825), ('want', 0.0006945384), ('way', 0.00068549445), ('really', 0.0006164913)]


another : [('another', 0.0020674102), ('give', 0.0016010555), ('come', 0.0014414401), ('decided', 0.0013573435), ('take', 0.0013399951)]


take : [('another', 0.0016342986), ('check', 0.001535477), ('money', 0.0014439507), ('take', 0.0014204582), ('come', 0.0013667919)]


made : [('put', 0.0006702572), ('menu', 0.00062320894), ('also', 0.00059500063), ('gave', 0.00058744685), ('made', 0.0005873089)]


wait : [('minutes', 0.006793642), ('wait', 0.006704785), ('waiting', 0.005717512), ('line', 0.0051632808), ('long', 0.0048937313)]

""")
elif category == "Fast Food":
    st.image("streamlit/fastfood/customer_rating.png")
    st.image("streamlit/fastfood/wordCloud.png")
    st.image("streamlit/fastfood/bigramCloud.png")
    st.write("""**Five Star Reviews**

place : [('great', 0.0018938953), ('favorite', 0.0017740297), ('love', 0.0015648132), ('amazing', 0.0012179207), ('best', 0.0011955078)]


food : [('great', 0.0019793215), ('fast', 0.0017573794), ('amazing', 0.0016311792), ('customer', 0.0015033638), ('quality', 0.0013987409)]


great : [('service', 0.003364621), ('prices', 0.0019600189), ('experience', 0.0019372449), ('spot', 0.0018659849), ('place', 0.0017887256)]


get : [('sure', 0.0015201297), ('want', 0.0012928745), ('could', 0.0010206562), ('get', 0.0008943528), ('way', 0.00083250995)]


good : [('service', 0.002016878), ('pretty', 0.0015899313), ('really', 0.0012949471), ('everything', 0.0012490015), ('fries', 0.0012351105)]


one : [('favorite', 0.001989315), ('places', 0.0017340137), ('many', 0.0012463637), ('city', 0.0011327205), ('spots', 0.0010769394)]


go : [('back', 0.0015679275), ('want', 0.0012994015), ('stop', 0.001253794), ('come', 0.0011061095), ('wrong', 0.0010432557)]


love : [('absolutely', 0.0034660865), ('market', 0.0016414901), ('love', 0.0015205285), ('reading', 0.0014724663), ('place', 0.0013353846)]


philly : [('visit', 0.006341995), ('must', 0.0051969127), ('visiting', 0.0047401176), ('stop', 0.0037018233), ('philadelphia', 0.0024923072)]


best : [('ever', 0.015163605), ('city', 0.010727693), ('hands', 0.0036110333), ('far', 0.0035261202), ('philadelphia', 0.0028805821)]


like : [('anything', 0.000824132), ('things', 0.00076846045), ('could', 0.0006842069), ('everything', 0.00067893177), ('much', 0.0006724955)]


market : [('reading', 0.015226702), ('terminal', 0.013898671), ('market', 0.0065344726), ('indoor', 0.004848745), ('farmer', 0.0030183364)]


time : [('every', 0.03694834), ('first', 0.026266353), ('next', 0.006766118), ('last', 0.004498251), ('went', 0.0023342436)]


fresh : [('produce', 0.021741712), ('fresh', 0.010692877), ('meats', 0.009419551), ('seafood', 0.0065936353), ('fruits', 0.0062026163)]


cheese : [('whiz', 0.014034488), ('steak', 0.014020144), ('cheese', 0.008129176), ('wiz', 0.007858105), ('onions', 0.0073543224)]


also : [('sweet', 0.0008423943), ('nice', 0.0007913272), ('homemade', 0.0007791917), ('baked', 0.000775706), ('soft', 0.0007399334)]


always : [('friendly', 0.002095176), ('always', 0.0012333059), ('super', 0.0011814651), ('make', 0.0010679826), ('nice', 0.0010523369)]


really : [('good', 0.0014291396), ('pretty', 0.0010247084), ('never', 0.0010151785), ('awesome', 0.0010143083), ('nice', 0.0010091919)]


try : [('try', 0.0059710937), ('must', 0.004230783), ('things', 0.0025939762), ('different', 0.0024286988), ('come', 0.001946213)]


back : [('come', 0.006150748), ('definitely', 0.004297485), ('wait', 0.0038854205), ('coming', 0.0035012348), ('going', 0.003034494)]


chicken : [('chicken', 0.012075493), ('paneer', 0.0117840115), ('fried', 0.011464881), ('kati', 0.008807896), ('roll', 0.007172217)]


delicious : [('everything', 0.0012052631), ('food', 0.0010721358), ('filling', 0.0009180084), ('sauces', 0.0008296057), ('burgers', 0.0008268979)]


definitely : [('recommend', 0.04724764), ('worth', 0.004404753), ('back', 0.0033546335), ('recommended', 0.0022455882), ('try', 0.0021294155)]


i've : [('sweet', 0.000418918), ('awesome', 0.00039929917), ('amish', 0.00039656606), ('huge', 0.00038515928), ('top', 0.00037914916)]


eat : [('could', 0.003848944), ('eat', 0.003356869), ('want', 0.002799697), ('different', 0.0026697223), ('something', 0.002510616)]


reading : [('terminal', 0.88058853), ('market', 0.0014847787), ('love', 0.0004044794), ('railroad', 0.00036870706), ('pike', 0.0003585259)]


i'm : [('could', 0.00055249594), ('take', 0.0005381506), ('find', 0.00048269815), ('around', 0.00047707802), ('walk', 0.0004629665)]


many : [('options', 0.020168489), ('different', 0.01549249), ('many', 0.011031936), ('places', 0.008682441), ('choices', 0.0084944675)]


everything : [('could', 0.0022572288), ('want', 0.0021617808), ('everything', 0.0021321718), ('anything', 0.0018575963), ('fresh', 0.0014456959)]


terminal : [('reading', 0.92493886), ('market', 0.0022297455), ('indoor', 0.00036884402), ('redding', 0.0003041691), ('farmer', 0.00023100985)]


got : [('half', 0.0015785076), ('went', 0.0014799236), ('came', 0.0013392469), ('got', 0.0010541274), ('ordered', 0.0010525684)]


would : [('recommend', 0.017399441), ('would', 0.0026822009), ('come', 0.0016078311), ('anyone', 0.0015778738), ('give', 0.0015751604)]


amazing : [('experience', 0.0011881941), ('food', 0.0011542978), ('place', 0.0010097335), ('everything', 0.0009310494), ('absolutely', 0.00092282624)]


sandwich : [('pork', 0.013434907), ('roast', 0.005756951), ('dinic', 0.0037645323), ('sandwich', 0.0032198776), ('beef', 0.0029163603)]


lunch : [('lunch', 0.013704759), ('dinner', 0.008132176), ('breakfast', 0.0066011106), ('quick', 0.004183299), ('grab', 0.0029235173)]


even : [('better', 0.0010203326), ('produce', 0.00093963), ('pretty', 0.0008335845), ('buy', 0.00081150926), ('even', 0.00077507854)]


every : [('time', 0.01982991), ('day', 0.005933636), ('bite', 0.0056948964), ('could', 0.0027101606), ('type', 0.0020272636)]


service : [('friendly', 0.1841391), ('customer', 0.04912601), ('excellent', 0.014158609), ('great', 0.011437518), ('fast', 0.009788855)]


order : [('ready', 0.0031317999), ('extra', 0.003079202), ('minutes', 0.0027052085), ('order', 0.002662838), ('window', 0.0025260744)]


places : [('favorite', 0.010570762), ('many', 0.007760554), ('different', 0.002772098), ('amish', 0.0024874718), ('shops', 0.002352399)]


come : [('back', 0.005348215), ('come', 0.003844489), ('soon', 0.002552284), ('would', 0.0024378328), ('going', 0.002377046)]


much : [('much', 0.0037001683), ('anything', 0.0020171844), ('better', 0.0020084174), ('could', 0.0018187243), ('pretty', 0.0017190814)]


favorite : [('places', 0.0063106897), ('city', 0.0054410514), ('spot', 0.004346629), ('spots', 0.003744889), ('cheesesteaks', 0.0026298242)]


make : [('sure', 0.037970465), ('want', 0.0025718058), ('home', 0.0025064312), ('make', 0.002239546), ('ready', 0.0015083654)]


well : [('cooked', 0.0010387644), ('filling', 0.0009762922), ('portions', 0.00094273186), ('juicy', 0.00093258015), ('super', 0.00091386103)]


want : [('want', 0.008079098), ('everything', 0.0066565047), ('anything', 0.006227786), ('could', 0.003926197), ('find', 0.0033509654)]


find : [('something', 0.007462889), ('find', 0.006992623), ('anything', 0.0034866624), ('hard', 0.0026820414), ('could', 0.0026039693)]


around : [('parking', 0.011423452), ('seating', 0.010384122), ('crowded', 0.008160255), ('walk', 0.007113304), ('hours', 0.005839532)]


first : [('time', 0.028827457), ('day', 0.0047959574), ('visit', 0.0035724463), ('went', 0.0031815388), ('night', 0.002509848)]


people : [('crowded', 0.0034220286), ('around', 0.0025405954), ('friendly', 0.0019688746), ('busy', 0.0019508713), ('walk', 0.0018645858)]


**One Star Reviews**

food : [('slow', 0.001159376), ('service', 0.001150265), ('fast', 0.0010243292), ('customer', 0.001004257), ('horrible', 0.0009399149)]


order : [('window', 0.003546222), ('waited', 0.0032318265), ('minutes', 0.0030082685), ('waiting', 0.0024005473), ('wait', 0.0023999456)]


place : [('experience', 0.0017703661), ('star', 0.0017394988), ('stars', 0.0015788914), ('mcdonald', 0.0015421854), ('recommend', 0.0015133293)]


like : [('meat', 0.0011788183), ('taste', 0.0010658365), ('steak', 0.0010139722), ('bread', 0.0008840057), ('dry', 0.0008470589)]


one : [('come', 0.0005774462), ('going', 0.0005476508), ('around', 0.00053748477), ('first', 0.0005332302), ('went', 0.0005328225)]


get : [('window', 0.00072911516), ('wait', 0.0007033869), ('took', 0.00070024974), ('went', 0.0006924456), ('long', 0.0006797766)]


time : [('time', 0.00389151), ('last', 0.0028887824), ('waste', 0.0026913905), ('every', 0.0025870297), ('drive', 0.002470507)]


service : [('customer', 0.014465706), ('service', 0.008657144), ('poor', 0.0075811944), ('slow', 0.006945039), ('horrible', 0.0064080525)]


go : [('never', 0.0018426391), ('money', 0.0018287242), ('back', 0.0017430487), ('go', 0.0017156556), ('going', 0.0017082735)]


even : [('attitude', 0.00052009214), ('well', 0.0004895595), ('also', 0.00048512412), ('nothing', 0.0004745929), ('rude', 0.000468367)]


back : [('back', 0.0035146165), ('money', 0.0024178086), ('come', 0.0017489907), ('told', 0.0016368829), ('going', 0.0014994837)]


never : [('going', 0.001468182), ('money', 0.0014255312), ('never', 0.0014250377), ('mcdonald', 0.0013785531), ('recommend', 0.0013204338)]


ordered : [('cold', 0.002500903), ('ordered', 0.0022539229), ('fries', 0.0022407454), ('nuggets', 0.0021029608), ('piece', 0.002024576)]


would : [('stars', 0.0041823587), ('give', 0.003866224), ('would', 0.003179438), ('could', 0.0026869772), ('star', 0.002347677)]


got : [('extra', 0.0019107375), ('ordered', 0.0018382745), ('asked', 0.001790066), ('nuggets', 0.001776214), ('piece', 0.0017587118)]


chicken : [('cheese', 0.012078769), ('dry', 0.009819674), ('steak', 0.008317086), ('bread', 0.008186469), ('meat', 0.007934834)]


people : [('rude', 0.0018679897), ('employees', 0.0017780254), ('staff', 0.0015058813), ('people', 0.0014969199), ('slow', 0.0013610779)]


said : [('asked', 0.0055496516), ('told', 0.0034876827), ('said', 0.0034344767), ('us', 0.003064325), ('ask', 0.0023812915)]


asked : [('asked', 0.00889257), ('said', 0.004264451), ('told', 0.0042392216), ('us', 0.0038232503), ('ask', 0.0028342442)]


minutes : [('waited', 0.013788466), ('minutes', 0.009946921), ('thru', 0.009458878), ('window', 0.008679829), ('wait', 0.008386756)]


i'm : [('say', 0.0005185361), ('still', 0.0005166497), ('around', 0.000514385), ('attitude', 0.0005097169), ('want', 0.0005010251)]


worst : [('worst', 0.023473632), ('ever', 0.016625293), ('experience', 0.0069283913), ('far', 0.0052845734), ('bell', 0.0050979913)]


ever : [('worst', 0.024958644), ('ever', 0.013711449), ('philly', 0.007831895), ('experience', 0.0059264274), ('mcdonald', 0.0055659493)]


cheese : [('cheese', 0.0246752), ('steak', 0.020194018), ('dry', 0.010604583), ('meat', 0.009393498), ('bread', 0.00903865)]


good : [('philly', 0.001621754), ('cheesesteak', 0.0015284937), ('better', 0.0013415709), ('pat', 0.001208571), ('great', 0.0011330099)]


location : [('experience', 0.0022516784), ('mcdonald', 0.0019068498), ('philly', 0.0017475174), ('worst', 0.0017288061), ('mcdonalds', 0.001704641)]


give : [('give', 0.014430958), ('stars', 0.010098056), ('could', 0.009323104), ('would', 0.006130892), ('wish', 0.003650248)]


sandwich : [('cheese', 0.00357642), ('steak', 0.0030872151), ('onions', 0.002493333), ('dry', 0.00244559), ('cold', 0.0024396828)]


customer : [('service', 0.019813126), ('customer', 0.005984789), ('poor', 0.0052219396), ('experience', 0.004566441), ('slow', 0.0044548917)]


i've : [('great', 0.0006918754), ('think', 0.0006885983), ('pat', 0.000680584), ('experience', 0.0006774751), ('philly', 0.0006719349)]


went : [('went', 0.001485195), ('last', 0.0012738949), ('first', 0.0011745372), ('came', 0.0011436774), ('window', 0.001099035)]


fries : [('cheese', 0.005325446), ('steak', 0.004697083), ('dry', 0.004530319), ('meat', 0.004466664), ('cold', 0.0043441076)]


could : [('give', 0.0076534185), ('could', 0.0054254886), ('stars', 0.0045473445), ('would', 0.0032823368), ('wish', 0.0022044575)]


told : [('asked', 0.005512602), ('told', 0.004752419), ('us', 0.003864592), ('said', 0.003575693), ('window', 0.0027495576)]


staff : [('rude', 0.0042179595), ('employees', 0.0027458887), ('staff', 0.0026372962), ('slow', 0.0019881614), ('customer', 0.0018153085)]


rude : [('rude', 0.0051757577), ('staff', 0.0027529972), ('employees', 0.0026052475), ('extremely', 0.0017454802), ('attitude', 0.0014994164)]


know : [('cheesesteak', 0.0009182045), ('philly', 0.00084648695), ('pat', 0.0008326944), ('steak', 0.0008281638), ('much', 0.0008051743)]


better : [('philly', 0.0057267393), ('better', 0.004870086), ('cheesesteak', 0.0038122756), ('pat', 0.0032364165), ('places', 0.0030876426)]


going : [('going', 0.0010368676), ('money', 0.0010140988), ('philly', 0.0009511501), ('pat', 0.0009129584), ('try', 0.0008860489)]


want : [('money', 0.0010343777), ('would', 0.0009340052), ('know', 0.0009025871), ('say', 0.0008787855), ('want', 0.0008712094)]


really : [('better', 0.0012212697), ('philly', 0.0012172668), ('experience', 0.0011182479), ('pat', 0.0010941628), ('really', 0.0010858903)]


bad : [('experience', 0.0020695373), ('service', 0.00164323), ('quality', 0.0016159117), ('fast', 0.0015768358), ('poor', 0.0015317076)]


drive : [('thru', 0.15647294), ('drive', 0.016243186), ('line', 0.007410022), ('waited', 0.0072014336), ('wait', 0.006473777)]


eat : [('philly', 0.0013591747), ('cheesesteak', 0.0012923105), ('pat', 0.0011407204), ('try', 0.00096635206), ('geno', 0.0009333213)]


first : [('money', 0.0011379697), ('first', 0.0011195429), ('last', 0.0011015328), ('time', 0.0010898587), ('went', 0.0009845871)]


make : [('want', 0.0007648584), ('say', 0.00075541285), ('money', 0.00074311014), ('try', 0.00071801076), ('make', 0.000716788)]


manager : [('manager', 0.0039286534), ('us', 0.002424336), ('rude', 0.0023276554), ('told', 0.0022896272), ('asked', 0.002228998)]


line : [('drive', 0.0031810608), ('line', 0.0030438346), ('thru', 0.003035898), ('wait', 0.002755716), ('waiting', 0.0026881613)]


come : [('back', 0.0022589052), ('money', 0.0020296809), ('come', 0.0015499963), ('going', 0.0014516995), ('never', 0.0013336904)]


came : [('window', 0.0018073651), ('told', 0.0015833807), ('took', 0.0014880047), ('us', 0.0014590147), ('finally', 0.0013611648)]
""")
elif category == "Italian":
    st.image("streamlit/italian/customer_rating.png")
    st.image("streamlit/italian/wordCloud.png")
    st.image("streamlit/italian/bigramCloud.png")
    st.write("""**Five Star Reviews**

great : [('atmosphere', 0.041506782), ('service', 0.022592405), ('experience', 0.015146322), ('value', 0.011496417), ('job', 0.009930586)]


food : [('comfort', 0.040885914), ('spectacular', 0.011703442), ('italian', 0.011129635), ('incredible', 0.009625537), ('excellent', 0.009594631)]


pizza : [('margherita', 0.42990154), ('margarita', 0.14814977), ('neapolitan', 0.036036912), ('square', 0.027100341), ('pepperoni', 0.017022794)]


place : [('go-to', 0.022607595), ('love', 0.0066152816), ('trendy', 0.0062578656), ('hit', 0.005580452), ('small', 0.004819516)]


good : [('pretty', 0.389236), ('sooo', 0.036850788), ('damn', 0.029185837), ('soooo', 0.021204878), ('really', 0.018769488)]


best : [('ever', 0.093528256), ('part', 0.008790265), ('city', 0.008571361), ('hands', 0.0075890897), ('absolute', 0.0057282075)]


one : [('places', 0.008744656), ('favorites', 0.003629533), ('restaurants', 0.00247897), ('favorite', 0.0021711523), ('thing', 0.0019086312)]


service : [('impeccable', 0.04584358), ('customer', 0.031321302), ('excellent', 0.0093938485), ('exceptional', 0.0091905575), ('attentive', 0.0074590156)]


delicious : [('absolutely', 0.0067022988), ('equally', 0.0010535996), ('everything', 0.001048904), ('fresh', 0.0009821857), ('amazingly', 0.00094623066)]


like : [('felt', 0.13327624), ('feel', 0.09261873), ('feels', 0.06813852), ('looks', 0.012183034), ('seems', 0.007278804)]


restaurant : [('week', 0.041473016), ('italian', 0.0034641838), ('history', 0.0025959313), ('favorite', 0.0023143622), ('adorable', 0.0018097854)]


go : [('wrong', 0.10086073), ('back', 0.0062477025), ('wait', 0.0047196024), ('everytime', 0.0024985662), ('favor', 0.0020306846)]


also : [('tried', 0.0010311981), ('byob', 0.0006677009), ('enjoyed', 0.0006271921), ('offer', 0.000549859), ('fries', 0.00054895726)]


time : [('every', 0.10076743), ('next', 0.04423287), ('first', 0.040002286), ('long', 0.018643318), ('second', 0.01371324)]


back : [('come', 0.031051062), ('coming', 0.022102863), ('laid', 0.01635048), ('soon', 0.0102979615), ('definitely', 0.005408278)]


get : [('hard', 0.0021639161), ('usually', 0.0018850671), ('favor', 0.00162799), ('chance', 0.0015809636), ('enough', 0.0014747597)]


italian : [('market', 0.10101586), ('authentic', 0.087161995), ('cuisine', 0.040216736), ('southern', 0.014777571), ('classic', 0.009669954)]


really : [('enjoyed', 0.010339498), ('liked', 0.00671082), ('good', 0.0024839514), ('cool', 0.002111979), ('nice', 0.0020075624)]


amazing : [('absolutely', 0.0028070393), ('simply', 0.0007644891), ('food', 0.0007367421), ('everything', 0.0007006764), ('freaking', 0.00069953786)]


i've : [('especially', 0.00013675929), ('etc', 0.00013104935), ('super', 0.00013001965), ('la', 0.00012890734), ('always', 0.0001274921)]


definitely : [('recommend', 0.011637316), ('worth', 0.008936803), ('return', 0.008456892), ('back', 0.008103727), ('returning', 0.007765078)]


would : [('recommend', 0.06672298), ('suggest', 0.01574797), ('thought', 0.0062900884), ('anyone', 0.0035067438), ('imagine', 0.0031552524)]


us : [('gave', 0.14291379), ('brought', 0.022634843), ('told', 0.0136160115), ('checked', 0.007954641), ('helped', 0.0069079213)]


love : [('love', 0.0020619824), ('fell', 0.0019845844), ('absolutely', 0.0011524181), ('much', 0.0009663789), ('fact', 0.00094039115)]


menu : [('tasting', 0.09297618), ('items', 0.04666926), ('extensive', 0.036012553), ('item', 0.020665303), ('changes', 0.019872462)]


cheese : [('goat', 0.43805438), ('mac', 0.06162384), ('steak', 0.03088531), ('board', 0.0235675), ('blue', 0.016159402)]


philly : [('south', 0.77828974), ('visiting', 0.007868708), ('cheesesteak', 0.0030196812), ('trip', 0.0015193898), ('west', 0.0013696661)]


got : [('friend', 0.003531088), ('glad', 0.0022722469), ('finally', 0.0018786669), ('girlfriend', 0.0018404812), ('boyfriend', 0.0015229438)]


ordered : [('friend', 0.0029041686), ('husband', 0.0026869338), ('delivery', 0.0026371933), ('takeout', 0.002145545), ('grubhub', 0.0020587456)]


always : [('go-to', 0.002567216), ('smile', 0.001955514), ('consistent', 0.0019028807), ('hit', 0.0017807517), ('delivery', 0.0012798114)]


try : [('excited', 0.029655213), ('must', 0.024582151), ('give', 0.018593999), ('decided', 0.015891762), ('chance', 0.014864182)]


pasta : [('dishes', 0.05312738), ('homemade', 0.025483456), ('ink', 0.020943634), ('dish', 0.009272541), ('handmade', 0.008709974)]


well : [('done', 0.045493487), ('cooked', 0.021775817), ('worth', 0.015250164), ('seasoned', 0.012119947), ('prepared', 0.010538923)]


nice : [('touch', 0.020103838), ('super', 0.0042221737), ('atmosphere', 0.0028515286), ('staff', 0.0019743273), ('weather', 0.0018627151)]


staff : [('friendly', 0.21970797), ('wait', 0.06005974), ('attentive', 0.011784139), ('knowledgeable', 0.011247389), ('helpful', 0.007012885)]


everything : [('else', 0.16812767), ('tried', 0.004683042), ('menu', 0.0016460234), ('ate', 0.0015587007), ('hoped', 0.0015198052)]


made : [('freshly', 0.121476814), ('scratch', 0.07256681), ('reservations', 0.057913262), ('in-house', 0.03723671), ('house', 0.030494913)]


sauce : [('tomato', 0.5411184), ('cream', 0.07698247), ('red', 0.06466255), ('blush', 0.037176587), ('dipping', 0.013031286)]


dinner : [('birthday', 0.010947675), ('rehearsal', 0.010020363), ('lunch', 0.004519029), ('anniversary', 0.0023981237), ('celebration', 0.0023007127)]


even : [('though', 0.6760809), ('better', 0.054381225), ('fan', 0.00043285338), ('describe', 0.00040636183), ('close', 0.00034797765)]


i'm : [('la', 0.00021567488), ('opera', 0.0001567871), ('thank', 0.00015485687), ('delight', 0.00015323563), ('absolute', 0.00015192611)]


meal : [('end', 0.02077133), ('throughout', 0.009495038), ('memorable', 0.0049927407), ('finish', 0.0048325052), ('entire', 0.0046728114)]


little : [('nonna', 0.09828727), ('pricey', 0.014517247), ('bit', 0.011967764), ('gem', 0.008060893), ('cramped', 0.006309625)]


perfect : [('amount', 0.04947559), ('balance', 0.010946412), ('ratio', 0.003662319), ('temperature', 0.0028343794), ('combination', 0.002490924)]


favorite : [('personal', 0.046027973), ('absolute', 0.035754964), ('new', 0.009603951), ('all-time', 0.006947081), ('far', 0.0067732525)]


night : [('last', 0.42071927), ('saturday', 0.1279913), ('friday', 0.11816688), ('late', 0.10429901), ('date', 0.020762846)]


ever : [('best', 0.12818947), ('eaten', 0.065742515), ('tasted', 0.018764509), ('seen', 0.009041709), ('life', 0.008711901)]


fresh : [('ingredients', 0.12641324), ('mozzarella', 0.021939356), ('tortillas', 0.011169688), ('basil', 0.0080070915), ('baked', 0.0046808654)]


came : [('quickly', 0.0121307485), ('across', 0.008911884), ('whim', 0.0038102607), ('shortly', 0.0030549474), ('girlfriend', 0.0028995809)]


recommend : [('highly', 0.9998517), ('anyone', 6.8483074e-05), ('strongly', 2.899251e-05), ('would', 4.9259447e-06), ('anybody', 6.3266714e-07)]


**One Star Reviews**

food : [('good', 0.004403311), ('mediocre', 0.0033748911), ('quality', 0.0029256076), ('great', 0.0024545973), ('terrible', 0.0022904288)]


place : [('business', 0.0012737123), ('yelp', 0.0012354054), ('recommend', 0.0011591132), ('reviews', 0.0011467434), ('negative', 0.0011234863)]


pizza : [('hut', 0.003611083), ('pepperoni', 0.0020525868), ('ordered', 0.001992126), ('slice', 0.0014829183), ('cold', 0.0014381137)]


us : [('seated', 0.0024528748), ('seat', 0.002438494), ('table', 0.0024265863), ('sat', 0.0020291288), ('approached', 0.0019620277)]


order : [('delivery', 0.0062969294), ('driver', 0.005142661), ('grubhub', 0.0027425815), ('placed', 0.002713032), ('call', 0.0027040718)]


would : [('recommend', 0.0014748675), ('give', 0.0012691708), ('wish', 0.0011663518), ('think', 0.0011529914), ('make', 0.0011441957)]


like : [('tasted', 0.01523789), ('looked', 0.0050606285), ('feel', 0.0043757707), ('tastes', 0.0030449938), ('felt', 0.0025169228)]


one : [('star', 0.0021069439), ('one', 0.0017151079), ('ever', 0.0011119009), ('give', 0.0011094388), ('two', 0.0010133763)]


ordered : [('wings', 0.006208146), ('salad', 0.005950364), ('chicken', 0.005921103), ('caesar', 0.004398525), ('medium', 0.003143248)]


never : [('return', 0.0036307669), ('life', 0.003486561), ('ever', 0.002635043), ('recommend', 0.001947073), ('seen', 0.0019461719)]


time : [('last', 0.021145571), ('first', 0.015275153), ('waste', 0.0133962585), ('long', 0.0065646037), ('every', 0.004330899)]


get : [('money', 0.0020596532), ('want', 0.0014439874), ('drink', 0.0012336388), ('else', 0.001177437), ('line', 0.0010711332)]


restaurant : [('week', 0.0013794882), ('dining', 0.0013540672), ('philadelphia', 0.0011171527), ('italian', 0.0010755401), ('empty', 0.0009911612)]


service : [('horrible', 0.030252755), ('customer', 0.025237408), ('terrible', 0.024817817), ('poor', 0.021724647), ('slow', 0.01381939)]


back : [('go', 0.013655957), ('going', 0.00858147), ('come', 0.007415172), ('sent', 0.0069127376), ('send', 0.0052909083)]


even : [('though', 0.001001976), ('give', 0.0009329534), ('even', 0.0007047197), ('bread', 0.000651594), ('star', 0.00062265864)]


good : [('food', 0.0026428201), ('really', 0.002199274), ('pretty', 0.0020973086), ('reviews', 0.0017403765), ('taste', 0.0013938651)]


go : [('back', 0.022163007), ('else', 0.005830857), ('somewhere', 0.0038119482), ('elsewhere', 0.0025231654), ('philly', 0.002108201)]


said : [('said', 0.0020936632), ('manager', 0.0019486338), ('called', 0.0017897793), ('something', 0.0016152363), ('speak', 0.0015012918)]


came : [('back', 0.013963539), ('meal', 0.0022494905), ('finally', 0.0020717927), ('server', 0.002005376), ('waiter', 0.0018358234)]


told : [('manager', 0.0026397952), ('called', 0.002437812), ('could', 0.0020745408), ('reservation', 0.0020228955), ('would', 0.0019568482)]


got : [('finally', 0.0010011448), ('wings', 0.00096047693), ('home', 0.00090836943), ('wrong', 0.0008955506), ('fries', 0.00087307714)]


asked : [('waiter', 0.0033386701), ('wanted', 0.0032866008), ('waitress', 0.0032131341), ('manager', 0.0026413973), ('server', 0.002619505)]


table : [('tables', 0.004894297), ('seated', 0.004885557), ('sat', 0.0046594664), ('glasses', 0.004558914), ('table', 0.0035881537)]


minutes : [('waited', 0.075142704), ('later', 0.04736426), ('took', 0.03550357), ('waiting', 0.020665744), ('wait', 0.019414518)]


could : [('give', 0.0038205134), ('asked', 0.0020809667), ('make', 0.0016663332), ('wish', 0.0014831754), ('free', 0.0011742065)]


cheese : [('cheese', 0.04004661), ('steak', 0.021491457), ('onions', 0.009760826), ('fries', 0.0049272235), ('peppers', 0.0044479356)]


people : [('tables', 0.0021644107), ('people', 0.0017603119), ('area', 0.001734068), ('empty', 0.0015170531), ('customers', 0.0015115043)]


went : [('back', 0.00575482), ('birthday', 0.0047865794), ('night', 0.0035520566), ('friend', 0.003258935), ('friends', 0.002905618)]


ever : [('worst', 0.3919099), ('life', 0.054872893), ('ever', 0.03236056), ('seen', 0.005474575), ('experienced', 0.0045857974)]


called : [('phone', 0.023701893), ('driver', 0.014899742), ('delivery', 0.0142253935), ('called', 0.009568425), ('call', 0.0076410593)]


experience : [('worst', 0.010335927), ('horrible', 0.008202693), ('terrible', 0.006411888), ('bad', 0.0040767007), ('disappointing', 0.0032662817)]


i'm : [('make', 0.00052426726), ('made', 0.0005110042), ('way', 0.00044820167), ('think', 0.00041837347), ('much', 0.000414083)]


two : [('two', 0.0053285914), ('four', 0.0025032677), ('large', 0.0024227756), ('three', 0.002206353), ('hours', 0.0017192407)]


bad : [('experience', 0.0056381486), ('reviews', 0.0053135976), ('really', 0.004397856), ('service', 0.0043656584), ('review', 0.0023445268)]


first : [('time', 0.044654887), ('night', 0.005510863), ('experience', 0.0027806524), ('visit', 0.0025910388), ('first', 0.0021284376)]


took : [('hour', 0.030160401), ('minutes', 0.029263774), ('long', 0.011725518), ('forever', 0.009447044), ('mins', 0.00570217)]


better : [('much', 0.0077103865), ('places', 0.0072222236), ('olive', 0.0047894293), ('garden', 0.00430685), ('better', 0.0039971825)]


really : [('really', 0.0038231874), ('bad', 0.0029105623), ('reviews', 0.001815769), ('nice', 0.0017906354), ('good', 0.0017417204)]


another : [('give', 0.002776708), ('another', 0.0023300375), ('chance', 0.0013899845), ('leave', 0.0011723432), ('come', 0.0010982325)]


made : [('reservation', 0.019096276), ('reservations', 0.00720404), ('mistake', 0.0045943493), ('made', 0.002680131), ('sure', 0.0021597007)]


eat : [('else', 0.0021167474), ('home', 0.0015314686), ('decided', 0.0014716699), ('cheesesteak', 0.0014324891), ('wanted', 0.0013176783)]


make : [('sure', 0.004581187), ('mistake', 0.0044776886), ('reservation', 0.0031726824), ('feel', 0.0023047018), ('make', 0.0018552113)]


know : [('let', 0.0028806468), ('know', 0.0026260966), ('want', 0.001363345), ('need', 0.0012310842), ('business', 0.001170941)]


going : [('back', 0.0059361607), ('elsewhere', 0.0015693253), ('street', 0.0013029636), ('philly', 0.0011109965), ('let', 0.001034117)]


give : [('star', 0.08535649), ('stars', 0.06138703), ('give', 0.039988212), ('chance', 0.013758414), ('zero', 0.009615711)]


way : [('better', 0.0009734421), ('way', 0.000930833), ('much', 0.0008658329), ('customers', 0.0006599997), ('make', 0.0006052333)]


i've : [('quality', 0.00060854445), ('definitely', 0.00046788054), ('really', 0.0004509667), ('taste', 0.00044407646), ('way', 0.00044227688)]


also : [('sauce', 0.0011404038), ('extremely', 0.0009561614), ('sweet', 0.0009214861), ('also', 0.000876861), ('completely', 0.0008172417)]


take : [('money', 0.0032866884), ('long', 0.0014304408), ('order', 0.0013824804), ('want', 0.0012576623), ('away', 0.0012244077)]
""")
elif category == "Mexican":
    st.image("streamlit/mexican/customer_rating.png")
    st.image("streamlit/mexican/wordCloud.png")
    st.image("streamlit/mexican/bigramCloud.png")
    st.write("""**Five Star Reviews**

food : [('authentic', 0.028633121), ('quality', 0.024208123), ('mexican', 0.01771746), ('outstanding', 0.017498557), ('excellent', 0.011168757)]


great : [('atmosphere', 0.048357747), ('service', 0.034865733), ('vibe', 0.022569025), ('experience', 0.018642187), ('prices', 0.011086301)]


place : [('go-to', 0.015122457), ('love', 0.009662998), ('hit', 0.008883869), ('favorite', 0.0071071405), ('hits', 0.0050443034)]


tacos : [('fish', 0.23645304), ('chicken', 0.05767901), ('shrimp', 0.04540543), ('carnitas', 0.036908492), ('mahi', 0.030715132)]


good : [('pretty', 0.0036242462), ('really', 0.002596326), ('prices', 0.0015948479), ('sooo', 0.0014087657), ('damn', 0.0013408436)]


mexican : [('authentic', 0.03364698), ('cuisine', 0.027811078), ('restaurants', 0.009187515), ('fare', 0.005068718), ('upscale', 0.004621902)]


delicious : [('absolutely', 0.003257053), ('fresh', 0.0019931798), ('everything', 0.001963422), ('margaritas', 0.0018088731), ('drinks', 0.0011477954)]


best : [('ever', 0.12005831), ('city', 0.027132673), ('hands', 0.017728405), ('philadelphia', 0.014611705), ('part', 0.013517368)]


get : [('usually', 0.0029925026), ('pay', 0.0014921566), ('money', 0.0012998013), ('sometimes', 0.0011914998), ('able', 0.0011774013)]


also : [('got', 0.0008495511), ('ordered', 0.0007961494), ('tasty', 0.00067554327), ('enjoyed', 0.0005994212), ('selection', 0.0005907981)]


one : [('favorite', 0.0036373644), ('places', 0.0016966645), ('favorites', 0.0012376581), ('thing', 0.0011987862), ('best', 0.0011915133)]


go : [('wrong', 0.013587355), ('back', 0.0074529764), ('wait', 0.0053359917), ('want', 0.0040010912), ('decided', 0.003379826)]


really : [('enjoyed', 0.002893828), ('good', 0.0023891395), ('liked', 0.0017982466), ('nice', 0.0016816279), ('cool', 0.0015481514)]


love : [('love', 0.0025918232), ('absolutely', 0.0017298332), ('place', 0.0016331816), ('margaritas', 0.0009264014), ('spot', 0.000815075)]


i've : [('atmosphere', 0.00026623017), ('lovely', 0.0002635521), ('staff', 0.00026187385), ('bar', 0.00025213585), ('decor', 0.00024978872)]


time : [('every', 0.49403685), ('next', 0.03959189), ('first', 0.021852296), ('last', 0.008019308), ('long', 0.0033829634)]


like : [('feel', 0.012118995), ('felt', 0.0048079193), ('looks', 0.0038064104), ('feels', 0.0022511072), ('tastes', 0.0019429575)]


service : [('friendly', 0.018798362), ('excellent', 0.018471714), ('fast', 0.0098954225), ('attentive', 0.008123658), ('customer', 0.0065937187)]


back : [('come', 0.05102969), ('coming', 0.026466835), ('wait', 0.012091338), ('going', 0.008117107), ('soon', 0.0077065807)]


definitely : [('worth', 0.044669136), ('recommend', 0.026560266), ('back', 0.0102547), ('return', 0.006823041), ('returning', 0.0046216426)]


amazing : [('absolutely', 0.001970737), ('everything', 0.0012128211), ('experience', 0.0012064952), ('margaritas', 0.0011483133), ('food', 0.00092678407)]


got : [('friend', 0.0044951886), ('boyfriend', 0.0034473063), ('wife', 0.0021380014), ('girlfriend', 0.0019821892), ('husband', 0.001953996)]


always : [('always', 0.0042973724), ('delivery', 0.002259051), ('order', 0.001882124), ('times', 0.0015661817), ('consistent', 0.0014070721)]


restaurant : [('mexican', 0.0031892254), ('clean', 0.0026220381), ('small', 0.0022841014), ('beautiful', 0.0017053733), ('cozy', 0.0016610936)]


chicken : [('burrito', 0.008190822), ('enchiladas', 0.0055183424), ('quesadilla', 0.0050312895), ('tinga', 0.0029481477), ('steak', 0.0029062447)]


ordered : [('enchiladas', 0.0042675687), ('friend', 0.003883673), ('boyfriend', 0.0037050827), ('entrees', 0.003007162), ('delivery', 0.0029786024)]


try : [('wait', 0.015404553), ('must', 0.013232872), ('decided', 0.010492601), ('give', 0.0069751088), ('items', 0.004836142)]


would : [('recommend', 0.24521567), ('suggest', 0.0069966144), ('say', 0.003038775), ('wish', 0.0019447099), ('eat', 0.001843705)]


fresh : [('ingredients', 0.025946954), ('made', 0.0059276926), ('super', 0.0045115603), ('flavorful', 0.0044224258), ('everything', 0.0037731596)]


i'm : [('spot', 0.00042507958), ('happy', 0.00036102242), ('restaurant', 0.00036074824), ('addition', 0.00035147948), ('cafe', 0.00034564335)]


menu : [('items', 0.07111558), ('extensive', 0.03181856), ('item', 0.0053451685), ('vegan', 0.004500252), ('options', 0.0044337334)]


taco : [('bell', 0.013341898), ('fish', 0.005238094), ('riendo', 0.0041193897), ('revolution', 0.0036106845), ('joint', 0.003518308)]


well : [('worth', 0.004926698), ('seasoned', 0.0028385925), ('done', 0.0016665432), ('prepared', 0.0013833273), ('cooked', 0.0012339004)]


everything : [('menu', 0.007810785), ('else', 0.0035465404), ('fresh', 0.0024201246), ('tried', 0.002275965), ('tasted', 0.0019292801)]


order : [('wait', 0.0028434843), ('ahead', 0.0027458523), ('always', 0.002400659), ('orders', 0.0023403622), ('delivery', 0.002284021)]


favorite : [('city', 0.008222503), ('spot', 0.0066412175), ('one', 0.0047439886), ('new', 0.004621249), ('spots', 0.004413301)]


chips : [('salsa', 0.77119535), ('tortilla', 0.07494223), ('salsas', 0.00808013), ('guac', 0.0071941484), ('complimentary', 0.0052305465)]


burrito : [('veggie', 0.0067592757), ('chicken', 0.0062186695), ('breakfast', 0.0056157615), ('steak', 0.0038289372), ('bowl', 0.0028079634)]


philly : [('south', 0.14486217), ('best', 0.008725509), ('west', 0.0074478975), ('center', 0.0028989452), ('find', 0.0024588367)]


nice : [('staff', 0.0041250614), ('super', 0.0039355317), ('people', 0.003228433), ('vibe', 0.003066291), ('touch', 0.0027856885)]


friendly : [('staff', 0.1996493), ('servers', 0.009446523), ('helpful', 0.008467278), ('server', 0.008249679), ('super', 0.007278739)]


even : [('better', 0.029951815), ('though', 0.026940715), ('us', 0.0013483977), ('care', 0.0011976343), ('made', 0.0011486316)]


recommend : [('highly', 0.99975157), ('anyone', 2.6224823e-05), ('would', 1.0735396e-05), ('strongly', 5.6327044e-06), ('checking', 2.673767e-06)]


made : [('freshly', 0.026228558), ('home', 0.020029267), ('sure', 0.012378181), ('house', 0.012259579), ('feel', 0.009948448)]


came : [('quickly', 0.003838599), ('friend', 0.0033725568), ('across', 0.0029482318), ('back', 0.0028064272), ('lunch', 0.0022955993)]


come : [('back', 0.024977315), ('wait', 0.0014388125), ('would', 0.001416191), ('often', 0.0013488182), ('week', 0.00132281)]


staff : [('friendly', 0.34314567), ('wait', 0.013104264), ('attentive', 0.008698148), ('pleasant', 0.008118219), ('helpful', 0.007800195)]


little : [('bit', 0.015730813), ('little', 0.009364583), ('pricey', 0.0064234724), ('cute', 0.002451693), ('spice', 0.002241269)]


us : [('gave', 0.026114449), ('us', 0.02608367), ('brought', 0.0171261), ('asked', 0.009232181), ('greeted', 0.009223983)]


wait : [('worth', 0.09465172), ('long', 0.024180394), ('minutes', 0.022266202), ('line', 0.0072509833), ('minute', 0.006878995)]


**One Star Reviews**

food : [('service', 0.0012137673), ('terrible', 0.0010403458), ('horrible', 0.0009997421), ('poor', 0.0009197562), ('customer', 0.0008723579)]


place : [('reviews', 0.0017653144), ('better', 0.001600347), ('review', 0.0015414949), ('stars', 0.0015392194), ('places', 0.001466416)]


order : [('minutes', 0.002332554), ('waited', 0.002172719), ('hour', 0.002167759), ('took', 0.0018210592), ('later', 0.001721081)]


like : [('tasted', 0.0010387369), ('taste', 0.0010300868), ('flavor', 0.0010077307), ('sauce', 0.0009626738), ('rice', 0.0008566109)]


us : [('seated', 0.005582803), ('table', 0.0048655937), ('told', 0.0041456074), ('waited', 0.0039004367), ('minutes', 0.0038605125)]


one : [('eat', 0.0005555621), ('come', 0.00053412927), ('taco', 0.0005292328), ('give', 0.00051777804), ('made', 0.0005001426)]


would : [('give', 0.0023325845), ('stars', 0.0017219634), ('would', 0.0016243573), ('going', 0.0015750657), ('could', 0.0013923206)]


ordered : [('chicken', 0.0031528214), ('ordered', 0.0028805328), ('cold', 0.0020715888), ('tacos', 0.0020533116), ('cheese', 0.0020507185)]


service : [('customer', 0.00821725), ('service', 0.0060830796), ('poor', 0.005941867), ('terrible', 0.005307713), ('horrible', 0.005123109)]


back : [('back', 0.0045406064), ('never', 0.00279897), ('going', 0.0026509927), ('go', 0.0023285002), ('coming', 0.0019599032)]


get : [('another', 0.00071552215), ('wait', 0.0007032979), ('take', 0.00065569836), ('told', 0.00061353244), ('took', 0.000612713)]


even : [('drinks', 0.00055150903), ('made', 0.0005477742), ('menu', 0.00053200143), ('gave', 0.0005170286), ('though', 0.0005146611)]


time : [('last', 0.0044317045), ('night', 0.003250775), ('time', 0.0024666106), ('went', 0.0022601136), ('first', 0.0019303549)]


never : [('back', 0.0020588643), ('going', 0.0017296058), ('never', 0.00166063), ('ever', 0.0015423307), ('coming', 0.0014457204)]


go : [('going', 0.0020520438), ('back', 0.0020420398), ('go', 0.0020096658), ('money', 0.001823262), ('never', 0.0016431148)]


got : [('ordered', 0.0010809927), ('cold', 0.0010504613), ('chicken', 0.0010332412), ('half', 0.0009933951), ('two', 0.00094946544)]


restaurant : [('experience', 0.001423833), ('customer', 0.0012875601), ('going', 0.0012650047), ('staff', 0.0012400904), ('location', 0.0011730137)]


good : [('mexican', 0.0020020655), ('quality', 0.001962202), ('authentic', 0.0018884356), ('better', 0.0016823297), ('terrible', 0.0016198766)]


tacos : [('chicken', 0.006510667), ('beans', 0.0046819686), ('rice', 0.004164534), ('fish', 0.00409341), ('tortilla', 0.003988233)]


came : [('minutes', 0.0017675351), ('waited', 0.0016543642), ('took', 0.001427909), ('hour', 0.0013932646), ('later', 0.0013794522)]


asked : [('asked', 0.0023881502), ('told', 0.0018918507), ('ask', 0.0018422039), ('said', 0.00171035), ('table', 0.0016328854)]


minutes : [('waited', 0.008864463), ('minutes', 0.00788396), ('hour', 0.0065946477), ('seated', 0.005799135), ('waiting', 0.005260783)]


mexican : [('bell', 0.005229168), ('mexican', 0.00516114), ('better', 0.0050948784), ('authentic', 0.0047306223), ('worst', 0.0046377084)]


said : [('asked', 0.0018993338), ('told', 0.001816041), ('table', 0.0016090369), ('ask', 0.0015640592), ('said', 0.0014987258)]


could : [('give', 0.0019216385), ('could', 0.0016113963), ('would', 0.0010047731), ('wanted', 0.0009937376), ('said', 0.0009398261)]


told : [('told', 0.00200482), ('another', 0.0019635363), ('wait', 0.0019147724), ('hostess', 0.0019061149), ('table', 0.0018792987)]


table : [('seated', 0.005026941), ('table', 0.004595754), ('waited', 0.004227869), ('minutes', 0.0039567812), ('sat', 0.0036583573)]


chicken : [('chicken', 0.0086101685), ('beans', 0.007451688), ('rice', 0.006652734), ('fish', 0.0061594965), ('tortilla', 0.0057239467)]


i'm : [('wait', 0.0007692717), ('another', 0.0007465975), ('told', 0.0007313074), ('took', 0.0007287792), ('table', 0.00071298)]


really : [('bad', 0.0010562314), ('great', 0.0010527966), ('good', 0.0010026919), ('terrible', 0.0009880203), ('really', 0.0009717602)]


went : [('last', 0.0016017988), ('night', 0.0014415472), ('went', 0.0014083313), ('first', 0.0011808515), ('two', 0.0009420004)]


people : [('rude', 0.0021814087), ('staff', 0.0021420699), ('wait', 0.001555929), ('manager', 0.0013242794), ('people', 0.0013111393)]


burrito : [('chicken', 0.0028129963), ('rice', 0.0023199609), ('beans', 0.0022677889), ('cheese', 0.0021865587), ('fish', 0.0020502876)]


taco : [('bell', 0.008822576), ('taco', 0.0061127027), ('worst', 0.0032772068), ('fish', 0.0030676054), ('flavor', 0.002404598)]


first : [('night', 0.0009454331), ('last', 0.00092969934), ('first', 0.00086430804), ('went', 0.0008571939), ('times', 0.0007562137)]


ever : [('worst', 0.019033315), ('ever', 0.013116321), ('taco', 0.0030000594), ('bell', 0.002839453), ('life', 0.0025982638)]


i've : [('made', 0.000547098), ('drinks', 0.0005139698), ('margaritas', 0.0005107969), ('menu', 0.0005091291), ('everything', 0.0005038287)]


two : [('half', 0.001767493), ('two', 0.0016758943), ('waited', 0.001635631), ('hour', 0.0015387994), ('minutes', 0.0014263503)]


bad : [('terrible', 0.0014522967), ('service', 0.0014017934), ('poor', 0.0012566199), ('horrible', 0.0012562685), ('great', 0.0011889104)]


make : [('give', 0.0010588467), ('want', 0.00094384124), ('know', 0.0009311864), ('going', 0.0009032266), ('staff', 0.00089524145)]


know : [('staff', 0.0014326737), ('rude', 0.0013090089), ('going', 0.0011823257), ('give', 0.0011210728), ('know', 0.0010750203)]


come : [('come', 0.00090265204), ('back', 0.0008546379), ('take', 0.0007272675), ('another', 0.00069564267), ('still', 0.0006752075)]


took : [('minutes', 0.0048004906), ('waited', 0.004195466), ('hour', 0.0041358103), ('took', 0.0030127205), ('later', 0.002900429)]


give : [('give', 0.0069087953), ('stars', 0.0051632635), ('could', 0.003239992), ('would', 0.00252387), ('try', 0.0024057447)]


drinks : [('drinks', 0.0013949464), ('wait', 0.00095862), ('rude', 0.00083973096), ('took', 0.00083247665), ('hour', 0.0008283306)]


also : [('gave', 0.00084831205), ('water', 0.0008002148), ('two', 0.000790803), ('put', 0.0007886308), ('drinks', 0.0007787556)]


going : [('going', 0.002394829), ('money', 0.0019966064), ('back', 0.0019955705), ('go', 0.0018258936), ('recommend', 0.0017667809)]


made : [('made', 0.00060161395), ('want', 0.0005960688), ('something', 0.00058559637), ('wanted', 0.00056799233), ('give', 0.0005580604)]


take : [('another', 0.0011981449), ('back', 0.0011645316), ('going', 0.0011121174), ('take', 0.0010647965), ('called', 0.0010479572)]


chips : [('chips', 0.008271576), ('salsa', 0.0077763437), ('cheese', 0.004019106), ('beans', 0.0037843504), ('rice', 0.0034200184)]

""")
elif category == "Sandwiches":
    st.image("streamlit/sandwiches/customer_rating.png")
    st.image("streamlit/sandwiches/wordCloud.png")
    st.image("streamlit/sandwiches/bigramCloud.png")
    st.write("""**Five Star Reviews**

place : [('cute', 0.011040691), ('favorite', 0.007916263), ('popular', 0.0074711572), ('love', 0.0063675293), ('found', 0.004712843)]


great : [('service', 0.0860747), ('prices', 0.018922534), ('experience', 0.01864647), ('job', 0.012417941), ('atmosphere', 0.011340352)]


good : [('pretty', 0.09871167), ('damn', 0.053996347), ('sooo', 0.041887075), ('sooooo', 0.024887864), ('really', 0.022751268)]


food : [('comfort', 0.24943851), ('network', 0.049305685), ('coma', 0.04268635), ('prepared', 0.028617293), ('quality', 0.013588177)]


best : [('ever', 0.7295074), ('absolute', 0.06634199), ('hands', 0.039666954), ('city', 0.018293897), ('far', 0.011988902)]


sandwich : [('meatball', 0.14277476), ('breakfast', 0.13578777), ('brisket', 0.035839163), ('turkey', 0.019318584), ('pastrami', 0.017687133)]


get : [('usually', 0.036876477), ('seat', 0.014659661), ('early', 0.011662337), ('easy', 0.010116808), ('gotta', 0.008453163)]


cheese : [('cream', 0.54208624), ('mac', 0.45142245), ('goat', 0.0039501945), ('grilled', 0.0005528103), ('steak', 0.0005470644)]


one : [('places', 0.006434783), ('favorites', 0.0045782733), ('spots', 0.004448294), ('favorite', 0.0018608957), ('thing', 0.0013044991)]


philly : [('south', 0.16028371), ('west', 0.0063737873), ('institution', 0.005836689), ('visiting', 0.005731286), ('native', 0.004450693)]


go : [('wrong', 0.038996093), ('back', 0.0026469836), ('everytime', 0.001675405), ('want', 0.0016501371), ('wait', 0.0015754781)]


like : [('feel', 0.060175747), ('feels', 0.048225928), ('felt', 0.047847435), ('looks', 0.024703119), ('seems', 0.013672896)]


also : [('tried', 0.0013937135), ('sell', 0.0013715083), ('fries', 0.0008413938), ('ordered', 0.00068843324), ('offer', 0.0006637153)]


time : [('every', 0.22996452), ('next', 0.12472069), ('first', 0.047176275), ('long', 0.007818943), ('last', 0.005219366)]


delicious : [('absolutely', 0.007047356), ('equally', 0.0010945377), ('everything', 0.0009819053), ('fresh', 0.0009157337), ('consistently', 0.00085317285)]


i've : [('especially', 0.00012813738), ('e', 0.00012444415), ('--', 0.000120152436), ('nofa', 0.00011912861), ('eden', 0.00011771957)]


really : [('enjoyed', 0.00527039), ('liked', 0.0051905694), ('cool', 0.0014372228), ('appreciate', 0.0012606429), ('good', 0.0011455741)]


cheesesteak : [('authentic', 0.004954468), ('philly', 0.0037763852), ('invented', 0.0030042876), ('philadelphia', 0.0022439966), ('cleavers', 0.0015984172)]


love : [('fell', 0.004530474), ('honey', 0.0022954121), ('absolutely', 0.0021732764), ('love', 0.0013101017), ('much', 0.001133793)]


back : [('laid', 0.12229335), ('coming', 0.029374989), ('come', 0.018787304), ('soon', 0.0073796078), ('brought', 0.0069977576)]


always : [('consistent', 0.002242221), ('smile', 0.0020705564), ('almost', 0.0016549045), ('specials', 0.0012957517), ('point', 0.0010682485)]


got : [('boyfriend', 0.005527132), ('husband', 0.0022663546), ('bf', 0.0021167975), ('friend', 0.0020466198), ('finally', 0.001760099)]


definitely : [('recommend', 0.019085998), ('returning', 0.0076202443), ('return', 0.007099819), ('worth', 0.0061942013), ('back', 0.0054793595)]


service : [('customer', 0.34912843), ('quick', 0.021915866), ('impeccable', 0.017957516), ('prompt', 0.0130622275), ('excellent', 0.010479142)]


i'm : [('brunch', 0.00016619907), ('coffee', 0.00016544542), ('thanks', 0.00014497347), ('e', 0.0001406951), ('went', 0.00013641735)]


try : [('give', 0.022521319), ('excited', 0.016770678), ('must', 0.01667351), ('decided', 0.009247196), ('gotta', 0.007338439)]


chicken : [('fried', 0.6625118), ('cutlet', 0.037195794), ('parm', 0.031103957), ('tenders', 0.025726052), ('buffalo', 0.022695933)]


order : [('online', 0.015772868), ('placed', 0.01537153), ('grubhub', 0.007659358), ('pickup', 0.0068687596), ('ready', 0.0065609096)]


would : [('recommend', 0.09179075), ('suggest', 0.024080873), ('thought', 0.007568091), ('say', 0.0037908778), ('lived', 0.0028001834)]


friendly : [('staff', 0.59215873), ('employees', 0.013426576), ('super', 0.008873573), ('workers', 0.004486228), ('extremely', 0.0037631853)]


amazing : [('absolutely', 0.0023887516), ('simply', 0.000999117), ('freaking', 0.0007934822), ('experience', 0.0007182606), ('donuts', 0.0006510924)]


well : [('seasoned', 0.04986145), ('done', 0.022651784), ('priced', 0.02166138), ('executed', 0.010852597), ('cooked', 0.00986854)]


fresh : [('ingredients', 0.14113411), ('squeezed', 0.015607142), ('produce', 0.0081545), ('rolls', 0.006839316), ('veggies', 0.005669237)]


steak : [('cheese', 0.13747539), ('chopped', 0.008587904), ('cheez', 0.0060759126), ('chop', 0.002282728), ('king', 0.0021997679)]


staff : [('friendly', 0.53434855), ('attentive', 0.0062148524), ('pleasant', 0.0047914907), ('helpful', 0.0041923677), ('courteous', 0.004149604)]


ordered : [('boyfriend', 0.006864647), ('online', 0.0057335165), ('grubhub', 0.0046833614), ('friend', 0.0024239616), ('delivery', 0.0022879266)]


sandwiches : [('breakfast', 0.014761684), ('salads', 0.0040886244), ('meatball', 0.0030749163), ('soups', 0.002491136), ('specialty', 0.0018598549)]


nice : [('touch', 0.012314975), ('employees', 0.004755571), ('staff', 0.002928497), ('really', 0.0022869157), ('super', 0.0019072145)]


even : [('though', 0.5941827), ('better', 0.018867653), ('close', 0.0010871063), ('begin', 0.00087721326), ('remotely', 0.0008032506)]


ever : [('eaten', 0.065553434), ('best', 0.050538637), ('tasted', 0.01813667), ('life', 0.0065754107), ('tastiest', 0.0056195455)]


little : [('pricey', 0.06344429), ('bit', 0.015978431), ('cute', 0.007888169), ('gem', 0.005644694), ('italy', 0.004652546)]


wait : [('minutes', 0.13928606), ('worth', 0.06095676), ('long', 0.05800412), ('cannot', 0.038721636), ('minute', 0.022019062)]


first : [('time', 0.086302556), ('timers', 0.05141045), ('bite', 0.035250973), ('glance', 0.032032557), ('timer', 0.025341855)]


pizza : [('pepperoni', 0.022466065), ('margherita', 0.021715103), ('sicilian', 0.01541191), ('slice', 0.015379507), ('pizza', 0.013927145)]


make : [('sure', 0.40629068), ('reservation', 0.017462073), ('effort', 0.013691515), ('trek', 0.012745359), ('sense', 0.011191507)]


everything : [('else', 0.34841454), ('menu', 0.0043092724), ('tried', 0.0013633616), ('sounded', 0.0011834871), ('looked', 0.0010516277)]


made : [('freshly', 0.29639605), ('scratch', 0.020755198), ('home', 0.011058756), ('house', 0.007749356), ('decision', 0.007398829)]


come : [('back', 0.017711306), ('would', 0.001996963), ('everytime', 0.0019852337), ('often', 0.0014891714), ('wrong', 0.0013536017)]


favorite : [('personal', 0.14738433), ('absolute', 0.09335907), ('new', 0.046838176), ('all-time', 0.009309173), ('become', 0.008371574)]


eat : [('could', 0.014932423), ('able', 0.0043227314), ('sit', 0.002842889), ('gotta', 0.0017727807), ('everyday', 0.0017499301)]



**<ins>One Star Reviews</ins>**

food : [('horrible', 0.0024749981), ('terrible', 0.0023322108), ('good', 0.0022887667), ('overpriced', 0.0019557786), ('great', 0.0016098414)]


place : [('try', 0.0010589939), ('great', 0.0010543432), ('bad', 0.0010479222), ('good', 0.0009977329), ('love', 0.0009947835)]


order : [('took', 0.006595372), ('placed', 0.004526003), ('wrong', 0.004021456), ('delivery', 0.0037725135), ('messed', 0.0030317674)]


like : [('tasted', 0.024894439), ('looked', 0.008126187), ('looks', 0.006313144), ('feel', 0.005793398), ('tastes', 0.0049444847)]


one : [('star', 0.004197028), ('two', 0.0015223456), ('worst', 0.0012271829), ('stars', 0.00090842124), ('another', 0.0008654478)]


get : [('money', 0.0033461647), ('line', 0.0013290371), ('home', 0.0011480155), ('drink', 0.0011130822), ('mins', 0.0010483343)]


ordered : [('salad', 0.004867927), ('pizza', 0.0045082485), ('sausage', 0.0042898227), ('fries', 0.003953598), ('wings', 0.0038361275)]


would : [('recommend', 0.003462185), ('better', 0.0033290703), ('stars', 0.002060809), ('wish', 0.001677638), ('give', 0.001576843)]


time : [('waste', 0.05755697), ('last', 0.03596659), ('first', 0.028335761), ('every', 0.01903672), ('next', 0.0143130245)]


cheese : [('steak', 0.075892285), ('whiz', 0.011595241), ('melted', 0.010462553), ('steaks', 0.008593983), ('mac', 0.006685317)]


never : [('life', 0.0052603153), ('ever', 0.004438151), ('return', 0.003049533), ('recommend', 0.0025801195), ('seen', 0.0024315375)]


back : [('money', 0.014538055), ('coming', 0.010148545), ('going', 0.010082862), ('went', 0.008493758), ('go', 0.0054764827)]


go : [('back', 0.015626114), ('else', 0.004693504), ('elsewhere', 0.0040233675), ('never', 0.0027780898), ('favor', 0.0018809539)]


even : [('though', 0.003407572), ('eat', 0.001091459), ('finish', 0.0009394298), ('worse', 0.0008412411), ('put', 0.0007822245)]


service : [('customer', 0.543238), ('poor', 0.033787306), ('terrible', 0.019455316), ('horrible', 0.019182213), ('slow', 0.015422664)]


sandwich : [('roast', 0.0014062878), ('pork', 0.0013850173), ('make', 0.0012663883), ('got', 0.0011290455), ('egg', 0.001048206)]


good : [('pretty', 0.0032348672), ('really', 0.0029228416), ('reviews', 0.0027462677), ('experience', 0.0020482838), ('thing', 0.0017970935)]


got : [('home', 0.0019950434), ('wrong', 0.0016121153), ('finally', 0.0014076066), ('burger', 0.0012677594), ('today', 0.0011300062)]


said : [('says', 0.0030847464), ('wanted', 0.002946075), ('called', 0.0025253003), ('said', 0.0024918835), ('receipt', 0.0020594378)]


us : [('us', 0.009164639), ('table', 0.008755386), ('waitress', 0.00875343), ('server', 0.0059420858), ('hostess', 0.0049534366)]


asked : [('waitress', 0.0035829877), ('server', 0.0032149502), ('lady', 0.0030564268), ('politely', 0.002890952), ('waiter', 0.0027924506)]


pizza : [('pizza', 0.0046889824), ('delivered', 0.003736755), ('ordered', 0.0021461009), ('delivery', 0.0021368547), ('wings', 0.0019913157)]


minutes : [('waited', 0.15159993), ('took', 0.116127394), ('wait', 0.05863448), ('waiting', 0.05216991), ('later', 0.037226774)]


people : [('many', 0.0022391446), ('working', 0.0018280228), ('rude', 0.001469082), ('know', 0.0013991792), ('treat', 0.0013848341)]


told : [('would', 0.0032913457), ('called', 0.0031854594), ('refund', 0.0021290365), ('manager', 0.0020430384), ('could', 0.0019757901)]


i'm : [('want', 0.00027561167), ('also', 0.00026739843), ('ok', 0.0002624752), ('much', 0.00026241277), ('small', 0.0002588076)]


cheesesteak : [('philly', 0.02071837), ('best', 0.0034567586), ('famous', 0.0023794149), ('ever', 0.0023629847), ('real', 0.0021010598)]


could : [('give', 0.0067089363), ('stars', 0.0035292793), ('asked', 0.0024634807), ('told', 0.0023575777), ('see', 0.002221474)]


better : [('places', 0.01708399), ('much', 0.01253974), ('steaks', 0.0065577324), ('cheesesteaks', 0.0054656053), ('city', 0.005172859)]


came : [('back', 0.004633876), ('friend', 0.002997486), ('boyfriend', 0.002783367), ('burger', 0.0020095806), ('finally', 0.0020049624)]


went : [('back', 0.0076262574), ('today', 0.0050592986), ('friend', 0.0036378254), ('boyfriend', 0.0035153623), ('husband', 0.0026587974)]


philly : [('south', 0.028277248), ('cheesesteak', 0.022303607), ('best', 0.008031026), ('cheesesteaks', 0.006579625), ('visiting', 0.005903058)]


really : [('bad', 0.0031855498), ('really', 0.0025899657), ('good', 0.0025678913), ('pretty', 0.0016101776), ('disappointed', 0.0015357422)]


ever : [('worst', 0.679624), ('life', 0.00753928), ('seen', 0.0041714367), ('experienced', 0.0027083703), ('rudest', 0.001216306)]


steak : [('cheese', 0.18588184), ('philly', 0.0031096197), ('onions', 0.002904858), ('whiz', 0.0028403106), ('dry', 0.0025383625)]


chicken : [('chicken', 0.039074734), ('salad', 0.0145758465), ('buffalo', 0.010985188), ('fried', 0.00777161), ('wrap', 0.004469836)]


i've : [('dirty', 0.000480423), ('high', 0.00043182142), ('old', 0.00038682393), ('little', 0.00035268842), ('disgusting', 0.00033840648)]


know : [('know', 0.0031022), ('let', 0.0024820103), ('people', 0.0019899562), ('dont', 0.0015997548), ('english', 0.0015467944)]


first : [('time', 0.059743043), ('day', 0.0040063695), ('night', 0.0036258462), ('experience', 0.003194474), ('visit', 0.002857345)]


meat : [('chewy', 0.010626862), ('bread', 0.008642972), ('meat', 0.0074234377), ('tough', 0.0069348365), ('dry', 0.006611586)]


customer : [('service', 0.52176553), ('skills', 0.003906973), ('loyal', 0.0026397877), ('lost', 0.0023421233), ('management', 0.001883223)]


give : [('stars', 0.05153318), ('star', 0.042060774), ('chance', 0.006444772), ('could', 0.0059960037), ('zero', 0.00591891)]


make : [('sure', 0.007075388), ('mistake', 0.0030212116), ('sense', 0.0017800077), ('could', 0.001537458), ('better', 0.0014677857)]


going : [('back', 0.008591163), ('elsewhere', 0.0019693892), ('recommend', 0.0016052336), ('say', 0.0011617618), ('sure', 0.0009868235)]


bad : [('experience', 0.0068557994), ('reviews', 0.0046187476), ('really', 0.004436694), ('service', 0.00392274), ('bad', 0.0022137826)]


called : [('phone', 0.023705631), ('manager', 0.020957172), ('answered', 0.017073533), ('back', 0.015471981), ('driver', 0.0123777)]


eat : [('else', 0.0018672452), ('never', 0.0017937891), ('want', 0.0013184745), ('somewhere', 0.0011673935), ('would', 0.0011318377)]


way : [('better', 0.0018835354), ('way', 0.0018052257), ('much', 0.0014549653), ('overpriced', 0.0010461668), ('quality', 0.0010326335)]


two : [('two', 0.01263015), ('three', 0.0068886783), ('times', 0.006507641), ('tables', 0.0029197715), ('couple', 0.002520927)]


worst : [('ever', 0.48002487), ('life', 0.05669544), ('experience', 0.017672904), ('part', 0.016129917), ('far', 0.0073112207)]


""")