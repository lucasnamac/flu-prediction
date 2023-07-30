from sklearn import tree
from sklearn import metrics
from sklearn.model_selection import cross_val_score, train_test_split


class DecisionTree:

    def __init__(self, X, Y):
        
        decisionTree = tree.DecisionTreeRegressor()
        decisionTree.fit(X, Y)
        score = cross_val_score(decisionTree, X, Y, cv=2)

        print('Decision Tree score: ', score)
        print('Average Accuracy:  %0.2f (+/- %0.2f)' % (score.mean()*100, score.std()*100))

        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=50)

        decisionTree.fit(X_train,Y_train)
        print('Score ', decisionTree.score(X_test,Y_test))

        y_pred_dtr = decisionTree.predict(X_test)

        print('----- Metrics to Decision Trees-----')
        print('R2 score:', metrics.r2_score(Y_test,y_pred_dtr,multioutput='variance_weighted'))
        print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, y_pred_dtr))
        print('Mean Squared Error:', metrics.mean_squared_error(Y_test,y_pred_dtr))
        

