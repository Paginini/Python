import numpy as np
from sklearn import model_selection, svm
import pandas as pd

df = pd.read_csv('./samplefiles/breast-cancer-wisconsin.txt')
df.replace('?',-9999,inplace=True) # inplace=True to replace the data but don't return the copy of object
df.drop(['id'], 1, inplace=True)

X = np.array(df.drop(['class'],1)) # select all 'features', i.e excluding the label=class
y = np.array(df['class']) # select the label
                                   
X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size=0.2)

clf = svm.SVC() # define the classifier
clf.fit(X_train,y_train) # train the classifier

accuracy = clf.score(X_test,y_test) # test the trained classifier against the test data
print('Accuracy:',accuracy)

example_measures = np.array([[4, 2, 1, 1, 1, 2, 3, 2, 1]]) # data to classify/predict
example_measures = example_measures.reshape(len(example_measures),-1)

pridiction = clf.predict(example_measures)
print("SVM Pridiction: datapoint {0} is classified as \'{1}\'".format(example_measures[0],pridiction))
