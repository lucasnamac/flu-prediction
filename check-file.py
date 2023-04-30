from Bio import SeqIO
import encoding_data

#file = open('flu-data/dataset/NA/H1N1-NA2021.fasta')
#file = open('flu-data/dataset/NA/H1N1-NA2021.fasta')
#file = open('flu-data/H1N1/NA/H1N1-NA24-2021.fasta')
file = open('flu-data/H1N1/HA/H1N1-HA24-2021.fasta')
#file = open('flu-data/H1N1/HA/H1N1-HA24-before2021.fasta')
data = list(SeqIO.parse(file, 'fasta'))

vet = []

for i in range(len(data)):
    vet.append(data[i].seq)


encode = encoding_data.EncodingData()
X = []

for k in range(len(vet)):
        encoded_train = encode.encoding(vet[k])
        X.append(encoded_train)

a = []
b = []
print(len(X))
qtd=1

for i in X:
    print(len(i), qtd)
    qtd = qtd+1

print('--------------------')
print('Final Statistic')
for i in X:
    a.append(len(i))
b = set(a)
for j in b:
    print(j, a.count(j))

