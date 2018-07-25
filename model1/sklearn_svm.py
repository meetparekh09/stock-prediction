from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import csv
from random import shuffle
import numpy as np

data_file = csv.reader(open('data.csv', 'r'))
X = []

for row in data_file:
    if row[0] == 'date':
        continue
    X.append([int(x) for x in row[1:]])

shuffle(X)
X = np.array(X)

y = X[:, -1]
X = X[:, :-1]

# scaler = StandardScaler()
# X = scaler.fit_transform(X)
# print(X)

thres = int(round(X.shape[0]*0.7))

X_train = X[:thres]
y_train = y[:thres]
X_test = X[thres:]
y_test = y[thres:]



clf = svm.SVC()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print(accuracy_score(y_test, y_pred))
