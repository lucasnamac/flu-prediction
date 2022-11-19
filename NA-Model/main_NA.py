from decisionTree_NA import DecisionTree
import encoding_data
from Bio import SeqIO
from extraTrees_NA import ExtraTrees
from naiveBayes_NA import NaiveBayes
import numpy as np
from randomForest_NA import RandomForest 



def main():
    
    file_train  = open('../flu-data/H3N2/teste.fasta')
    file_test = open('../flu-data/H3N2/teste.fasta')
    data_train = list(SeqIO.parse(file_train, 'fasta'))
    data_test = list(SeqIO.parse(file_test, 'fasta'))

    train = []
    test = []
    X = []
    Y = []
    for i in range(len(data_train)):
        train.append(data_train[i].seq)
    
    for j in range(len(data_test)):
        test.append(data_test[i].seq)

    # 2 Step: encoding letters to numbers
    
    encode = encoding_data.EncodingData()

    for k in range(len(train)):
        encoded_train = encode.encoding(train[k])
        X.append(encoded_train)

    
    for l in range(len(test)):
        encoded_test = encode.encoding(test[l])
        Y.append(encoded_test)
    

    #DecisionTree(train, test)
    #print('\n')
    #RandomForest(train, test)
    #print('\n')
    #ExtraTrees(train, test)
    #NaiveBayes(train, test)
    


if __name__ == '__main__':
    main()