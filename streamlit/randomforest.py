import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree, export_graphviz
import graphviz


df = pd.read_csv('for_tree.csv')
df1 = pd.get_dummies(df, columns=['postal_code'])
clean_df = pd.read_csv('final_clean.csv')
# data2 = data1.fillna(0)
data = df1.drop(['is_open', 'Unnamed: 0', 'zip'], axis='columns')
# data.to_csv('Final Project/data.csv')

X_train, X_test, y_train, y_test = \
    train_test_split(data.drop(['yelp_score', 'HighMeanIncome', 'avg_hours_open'], axis='columns'), data['yelp_score'], test_size=.2, random_state=1)
randomforest = RandomForestRegressor(n_estimators=1000, bootstrap=True, max_depth=12)
randomforest.fit(X_train, y_train)

y_pred = randomforest.predict(X_test)
print(mean_squared_error(y_test, y_pred))
print(randomforest.score(X_test, y_test))
# sample = np.array([1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1,\
#     0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0,\
#         0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 7, 85000, 85000, 0, 1, 0, 0,\
#             1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
#                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
#                     0, 0, 0, 0, 0, 0, 0, 0])
# pred = randomforest.predict(sample.reshape(1, -1))
# print(pred)
# plot_tree(randomforest.estimators_[0])
data0 = data.drop(['yelp_score', 'HighMeanIncome', 'avg_hours_open'], axis='columns')
cols = data0.columns
# g = export_graphviz(randomforest.estimators_[0], feature_names=cols)
# graph = graphviz.Source(g)
# graph.render('Final Project/graph.pdf')