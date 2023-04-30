import encoding_data
from Bio import SeqIO

from prediction_model.decisionTree import DecisionTree
from prediction_model.extraTrees import ExtraTrees
from prediction_model.naiveBayes import NaiveBayes
from prediction_model.randomForest import RandomForest

def main():
    #To H1N1 HA
    #file_train  = open('flu-data/H1N1/HA/H1N1-HA24-2021.fasta')
    #file_test = open('flu-data/H1N1/HA/H1N1-HA24-before2021.fasta') # Years 2019 and 2020

    #To H1N1 NA
    #file_train  = open('flu-data/H1N1/NA/H1N1-NA24-2019And2020.fasta')
    #file_test = open('flu-data/H1N1/NA/H1N1-NA24-2021.fasta')

    #To H3N2 HA
    #file_train  = open('flu-data/H3N2/HA/H3N2-HA50-2021.fasta')
    #file_test = open('flu-data/H3N2/HA/H3N2-HA50-2022.fasta')

    #To H3N2 NA    
    file_train  = open('flu-data/H3N2/NA/H3N2-NA50-2021.fasta')
    file_test = open('flu-data/H3N2/NA/H3N2-NA50-2022.fasta')

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

    
    DecisionTree(X, Y)
    print('\n')
    RandomForest(X, Y)
    print('\n')
    ExtraTrees(X, Y)
    print('\n')
    NaiveBayes(X, Y)
    
def convertData(X):
    newList = []
    for sublist in X:
        sublist.pop(0)
        sublist.pop(1)
        sublist.pop(2)
        newList.append(sublist)
    
    return newList
    
if __name__ == '__main__':
    main()