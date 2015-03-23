#!/usr/bin/python


"""
    starter code for the validation mini-project
    the first step toward building your POI identifier!

    start by loading/formatting the data

    after that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### it's all yours from here forward!  
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(features,labels)
clf.predict(features)
print ('Accuracy is %.2f') %(clf.score(features,labels))

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(
     features, labels, test_size=0.30, random_state=42)
clf = DecisionTreeClassifier()
clf.fit(features_train,labels_train)
clf.predict(features_test)
print ('Accuracy of test data is %.2f') %(clf.score(features_test,labels_test))
<<<<<<< HEAD
=======


>>>>>>> 3f5b16c8f4a0794ac03080e8d9bea032fd886abf

