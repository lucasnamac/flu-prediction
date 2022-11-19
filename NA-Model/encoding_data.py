#This class serve to encode the data in integer values

class EncodingData:

    def encoding(self, sequence):
        data_encoded = []
        new_sequence = []

        for i in sequence:
            if i == 'A' :
                data_encoded.append('1')
            elif i =='T' :
                data_encoded.append('2')
            
            elif i =='G':
                data_encoded.append('3')
            
            elif i == 'C':
                data_encoded.append('4')

        for i in range(len(data_encoded)):
            if i%15==0:
                aux = data_encoded[i:i+15]
                aux = ''.join(aux)
                aux = float(aux)
                new_sequence.append(aux)
        
        return (new_sequence)