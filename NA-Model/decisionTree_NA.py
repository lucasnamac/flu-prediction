from sklearn import tree
from sklearn import metrics
from sklearn.model_selection import  cross_val_score, train_test_split
import numpy as np
from sklearn.preprocessing import StandardScaler

class DecisionTree:

    def __init__(self, X, Y):
        decisionTree = tree.DecisionTreeRegressor()
        maxLen = max(map(len, X))
        for row in X:
            if len(row) < maxLen:
                row.extend(self.add(maxLen-len(row), row))

        decisionTree.fit(X, Y)
        
        score = cross_val_score(decisionTree, X, Y, cv=2)

        print('Decision Tree score: ', score)
        print('Average Accuracy:  %0.2f (+/- %0.2f)' % (score.mean()*100, score.std()*100))

        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=50)

        decisionTree.fit(X_train,Y_train)
        print('Score ', decisionTree.score(X_test,Y_test))

        y_pred_dtr = decisionTree.predict(X_test)
        print('Decision Trees R2 score:', metrics.r2_score(Y_test,y_pred_dtr,multioutput='variance_weighted'))
        

    def add(self, length, row):
        result =0
        X = []
        result = result + sum(row)
        result = result/len(row)
        for i in range(length):
            X.append(result)
        
        return X