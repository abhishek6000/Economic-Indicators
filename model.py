from sklearn.metrics import accuracy_score
from sklearn import tree
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn import svm
from sklearn.utils import shuffle
def model():
	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(train_mat, train_Y)
	test_score = accuracy_score(clf.predict(test_mat), test_Y)
	train_score = accuracy_score(clf.predict(train_mat), train_Y)
	print(train_score)
	print(test_score)



