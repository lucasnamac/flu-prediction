from sklearn import metrics
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn import ensemble

class ExtraTrees:

    def __init__(self, X, Y):
        extraTrees = ensemble.ExtraTreesRegressor(n_estimators=3)
        maxLen = max(map(len, X))
        X1=[]
        for row in X:
            if len(row) < maxLen:
                row.extend(self.add(maxLen-len(row), row))
                X1.append(row)
        extraTrees.fit(X, Y)
        score = cross_val_score(extraTrees, X, Y, cv=2)
        print('Extra Trees', score)
        print("Average Accuracy: %0.2f (+/- %0.2f)" % (score.mean()*100, score.std() *100))

        X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.3,random_state=50)

        extraTrees.fit(X_train,y_train)
        print('Score', extraTrees.score(X_test,y_test))

        y_pred_ext = extraTrees.predict(X_test)
        print('Extra Trees R2 score:', metrics.r2_score(y_test,y_pred_ext,multioutput='variance_weighted'))

    def add(self, length, row):
        result =0
        X = []
        result = result + sum(row)
        result = result/len(row)
        for i in range(length):
            X.append(result)
        
        return X