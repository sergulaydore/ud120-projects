#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
for key in enron_data.keys():
    print len(enron_data[key])


pois = [enron_data[key]['poi'] for key in enron_data.keys()]
print sum(pois)

salary = [enron_data[key]['salary'] for key in enron_data.keys()
 if enron_data[key]['salary']!='NaN']
     
emails = [enron_data[key]['email_address'] for key in enron_data.keys()
 if enron_data[key]['email_address']!='NaN']


text_data = open('../final_project/poi_names.txt','r')
names_data = text_data.readlines()

pois_names = [enron_data[name]['poi'] for name in wtf if name in enron_data.keys()]    