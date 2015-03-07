#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below

outlier = [person for person in data_dict.keys() if
 data_dict[person]['salary'] == 26704229. ]
 
data_dict.pop(outlier[0],None) 
data = featureFormat(data_dict, features)

#Two people made bonuses around 6-8 million dollars, 
#and a salary of over 1 million dollars; in other words, 
#they made out like bandits. What are the names associated with those points?
outlier2 = [person for person in data_dict.keys() 
    if  data_dict[person]['bonus']!='NaN' and 
    data_dict[person]['salary']!='NaN' and   
    data_dict[person]['bonus'] > 5e6 and
    data_dict[person]['salary'] > 1e6 ]

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )


