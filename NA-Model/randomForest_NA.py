
from sklearn import ensemble, metrics
from sklearn.model_selection import cross_val_score, train_test_split

class RandomForest:

    def __init__(self, X, Y):
        
        randomForest = ensemble.RandomForestRegressor(n_estimators=23)
        maxLen = max(map(len, X))
        X1=[]
        for row in X:
            if len(row) < maxLen:
                row.extend(self.add(maxLen-len(row), row))
                X1.append(row)
        randomForest.fit(X, Y)
        score = cross_val_score(randomForest, X, Y, cv=2)

        print('Random Forest', score)
        print("Average Accuracy: %0.2f (+/- %0.2f)" % (score.mean()*100, score.std() *100))

        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=50)

        randomForest.fit(X_train,Y_train)
        print('Score ', randomForest.score(X_test,Y_test))

        y_pred_rfr = randomForest.predict(X_test)
        print('Random Forests R2 score:', metrics.r2_score(Y_test,y_pred_rfr,multioutput='variance_weighted'))
        print('Random Forests MSE:', metrics.mean_squared_error(Y_test,y_pred_rfr))

    def add(self, length, row):
        result =0
        X = []
        result = result + sum(row)
        result = result/len(row)
        for i in range(length):
            X.append(result)
        
        return X