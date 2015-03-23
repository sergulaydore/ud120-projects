#!/usr/bin/python


"""
    starter code for the evaluation mini-project
    start by copying your trained/tested POI identifier from
    that you built in the validation mini-project

    the second step toward building your POI identifier!

    start by loading/formatting the data

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



### your code goes here 
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
predict_test = clf.predict(features_test)
print ('Accuracy of test data is %.2f') %(clf.score(features_test,labels_test))
from sklearn.metrics import accuracy_score
import numpy as np
print ('Accuracy of test data if everything is predicted 0: %.2f') %(accuracy_score(labels_test, 
                                            np.zeros((len(predict_test)))))

from sklearn.metrics import precision_score                                            
precision_score(labels_test, predict_test, average=None) 
from sklearn.metrics import recall_score                                            
recall_score(labels_test, predict_test, average=None) 


predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
precision_score(true_labels,predictions)
recall_score(true_labels,predictions)
