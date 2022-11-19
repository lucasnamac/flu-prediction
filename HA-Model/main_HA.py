
import encoding_data
from Bio import SeqIO
from decisionTree_HA import DecisionTree
from extraTrees_HA import ExtraTrees
from naiveBayes_HA import NaiveBayes
import numpy as np
from randomForest_HA import RandomForest 



def main():
    
    file  = open('../flu-data/H3N2/H3N2-HA50.fasta')

    data = list(SeqIO.parse(file, 'fasta'))

    train0 = []
    test0 = []
    train =[]
    test = []

    for i in range(0, len(data)-1):
        train0.append(data[i].seq)
    
    for j in range(1, len(data)):
        test0.append(data[i].seq)

    # 2 Step: encoding letters to numbers
    
    encode = encoding_data.EncodingData()

    for k in range(len(train0)):
        encoded_train = encode.encoding(train0[k])
        train.append(encoded_train)
    
    for l in range(len(test0)):
        encoded_test = encode.encoding(test0[l])
        test.append(encoded_test)

    
    DecisionTree(train, test) 
    print('\n')
    RandomForest(train, test)
    print('\n')
    ExtraTrees(train, test)
    print('\n')
    NaiveBayes(train, test)
    

if __name__ == '__main__':
    main()