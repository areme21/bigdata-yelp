import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree, export_graphviz
import graphviz

# ONLY MEEDIAN INCOME

df = pd.read_csv('streamlit/for_tree.csv') # pd.read_csv('streamlit/for_tree.csv')
df1 = pd.get_dummies(df, columns=['postal_code'])
clean_df = pd.read_csv('streamlit/final_clean.csv') # pd.read_csv('streamlit/final_clean.csv')
# data2 = data1.fillna(0)
# data = df1.drop(['is_open', 'Unnamed: 0', 'zip', 'mean_income', 'HighMedianIncome','HighMeanIncome'], axis='columns')
data = df1.drop(['is_open', 'Unnamed: 0', 'zip'], axis='columns')
# data.to_csv('Final Project/data.csv')

X_train, X_test, y_train, y_test = \
    train_test_split(data.drop(['yelp_score', 'avg_hours_open', 'HighMedianIncome', 'mean_income', 'HighMeanIncome'], axis='columns'), data['yelp_score'], test_size=.2, random_state=1)
randomforest = RandomForestRegressor(n_estimators=1000, bootstrap=True, max_depth=12)
randomforest.fit(X_train, y_train)

y_pred = randomforest.predict(X_test)
print(mean_squared_error(y_test, y_pred))
print(randomforest.score(X_test, y_test))
# plot_tree(randomforest.estimators_[900])
data0 = data.drop(['yelp_score', 'avg_hours_open'], axis='columns')
cols = data0.columns
# g = export_graphviz(randomforest.estimators_[0], feature_names=cols)
# graph = graphviz.Source(g)
# graph.render('Final Project/graph.pdf')