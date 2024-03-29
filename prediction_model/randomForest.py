
from sklearn import ensemble, metrics
from sklearn.model_selection import cross_val_score, train_test_split

class RandomForest:

    def __init__(self, X, Y):
        
        randomForest = ensemble.RandomForestRegressor(n_estimators=23)
        randomForest.fit(X, Y)
        score = cross_val_score(randomForest, X, Y, cv=2)

        print('Random Forest', score)
        print("Average Accuracy: %0.2f (+/- %0.2f)" % (score.mean()*100, score.std() *100))

        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=50)

        randomForest.fit(X_train,Y_train)
        print('Score ', randomForest.score(X_test,Y_test))

        y_pred_rfr = randomForest.predict(X_test)
        
        print('----- Metrics to Random Forest-----')
        print('R2 score:', metrics.r2_score(Y_test,y_pred_rfr,multioutput='variance_weighted'))
        print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, y_pred_rfr))
        print('Mean Squared Error:', metrics.mean_squared_error(Y_test,y_pred_rfr))

