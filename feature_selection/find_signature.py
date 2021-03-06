#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### the words (features) and authors (labels), already largely processed
words_file = "../text_learning/your_word_data.pkl" ### like the file you made in the last mini-project 
authors_file = "../text_learning/your_email_authors.pkl"  ### this too
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (remainder go into training)
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = \
cross_validation.train_test_split(word_data, authors,
                                  test_size=0.1, random_state=42)


from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train).toarray()
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150]
labels_train   = labels_train[:150]



### your code goes here
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
acc = clf.score(features_test, labels_test)

import numpy as np
feature_importance = clf.feature_importances_
importance, number = max(feature_importance),np.where(feature_importance==max(feature_importance))

print 'Outlier is ', vectorizer.get_feature_names()[number[0]]