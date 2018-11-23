# In[]
import arff
import scipy.io.arff as sarff
import os
import pandas as pd
import numpy as np

print('working dir is: ' + os.getcwd())
file = open('Edumy/q4/spam_train_2000.arff', 'r')
dataset = arff.load(file)
X = dataset["data"]
Y = []
for letter in X:
    y_label = 1 if letter.pop() == 'spam' else 0
    Y.append(y_label)

# bag of words
X = np.array(X)
# label 0 or 1
Y = np.array(Y)
n = len(X)
print('dataset size is: ' + str(n))

