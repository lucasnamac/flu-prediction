from sklearn import metrics
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.naive_bayes import GaussianNB
import numpy as np


class NaiveBayes:

    def __init__(self, X, Y):
        
        naiveBayes = GaussianNB()
        X = np.array(X)
        Y = np.array(Y)
        X = X.reshape(-1, 1)
        Y = Y.reshape(-1, 1)
        naiveBayes.fit(X, np.ravel(Y, order='C'))

        score = cross_val_score(naiveBayes, X, np.ravel(Y, order='C'), cv=2)
        print('Naive Bayes', score)
        print("Average Accuracy: %0.2f (+/- %0.2f)" % (score.mean()*100, score.std() *100))

        X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.3,random_state=50)
        
        naiveBayes.fit(X_train,np.ravel(y_train, order='C'))
        print('Score', naiveBayes.score(X_test,y_test))

        y_pred_ext = naiveBayes.predict(X_test)
        print('Naive Bayes R2 score:', metrics.r2_score(y_test,y_pred_ext,multioutput='variance_weighted'))
        