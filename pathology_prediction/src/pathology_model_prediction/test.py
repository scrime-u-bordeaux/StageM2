#!/usr/bin/env python3

import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
import sklearn.metrics as sklm

import warnings
warnings.filterwarnings("ignore")

input_total = "./pathology_prediction/data/csv/complete/complete_pathologies.csv"

with open(input_total) as f3:
    line3 = f3.readline()
    data3 = line3.split(',')
    print(data3)
    nbcols_total = len(data3)
    print(nbcols_total)

total_dataset = np.loadtxt(input_total, delimiter=",", skiprows=1, usecols=range(1,nbcols_total))

pathologies_train = total_dataset[:,0:1]
classification = total_dataset[:,1:2]
features = total_dataset[:,2:]

nb_lines = len(total_dataset)

seed = 1
test_size_ratio = 0.33
asthma = LRTI = pneumonia = bronchioectasis = bronchiolitis = URTI = COPD = healthy = total = 0
print("init ok !")
# features_train, features_test, pathologies_train, pathologies_test = train_test_split(features, pathologies, test_size = test_size_ratio, random_state = seed)
print("split ok !")
for i in range(0,len(pathologies_train)):
    if(pathologies_train[i] == 1):
        asthma += 1
        total += 1
    if(pathologies_train[i] == 2):
        LRTI += 1
        total += 1
    if(pathologies_train[i] == 3):
        pneumonia += 1
        total += 1
    if(pathologies_train[i] == 4):
        bronchioectasis += 1
        total += 1
    if(pathologies_train[i] == 5):
        bronchiolitis += 1
        total += 1
    if(pathologies_train[i] == 6):
        URTI += 1
        total += 1
    if(pathologies_train[i] == 7):
        COPD += 1
        total += 1
    if(pathologies_train[i] == 8):
        healthy += 1
        total += 1
print(asthma)
print(LRTI)
print(pneumonia)
print(bronchioectasis)
print(bronchiolitis)
print(URTI)
print(COPD)
print(healthy)
print(total)
print("computation ratios")
ratio_asthma = (total-asthma) / asthma
ratio_LRTI = (total-LRTI) / LRTI
ratio_pneumonia = (total-pneumonia) / pneumonia
ratio_bronchioectasis = (total-bronchioectasis) / bronchioectasis
ratio_bronchiolitis = (total-bronchiolitis) / bronchioectasis
ratio_URTI = (total-URTI) / URTI
ratio_COPD = (total-COPD) / COPD
ratio_healthy = (total-healthy) / healthy
