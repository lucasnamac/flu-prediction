from sklearn import metrics
from sklearn.model_selection import cross_val_score, train_test_split, KFold
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
import numpy as np
import random


class NaiveBayes:

    def __init__(self, X, Y):
        
        naiveBayes = GaussianNB()
        Y =np.array(Y)
        X = np.array(X)
        print(X.shape, Y.shape)
        
        naiveBayes.fit(X, Y.reshape(-1, 1))
        #k_fold = KFold(Y.size, shuffle=True, random_state=0)
        '''
        score = cross_val_score(naiveBayes, X, Y, cv=2)
        
        print('Naive Bayes', score)
        print("Average Accuracy: %0.2f (+/- %0.2f)" % (score.mean()*100, score.std() *100))
        X_train,X_test,y_train,y_test = train_test_split(X, Y,test_size=0.3,random_state=50)
        
        naiveBayes.fit(X_train,np.ravel(y_train, order='C'))
        print('Score', naiveBayes.score(X_test,y_test))

        y_pred_ext = naiveBayes.predict(X_test)
        print('Naive Bayes R2 score:', metrics.r2_score(y_test,y_pred_ext,multioutput='variance_weighted'))
        '''
        
    def format(self, Y):
        vet = []
        for sublist in Y:
            vet.append(sum(sublist)/len(sublist))
        
        return vet
    
    def length(self, X):
        count =0
        aux=0
        for m in X:
            for b in m:
                count= count+1

            print('linha e coluna', aux, count)
            aux = aux+1
            count =0
