from math import sqrt

class AlphabetKeyLenError(Exception):
	def __init__(self, key):
		print('Error: Key {} must be transform to matrix'.format(key))

class HillCipher:
    def __init__(self, alphabet, key):
        key_to_matrix = sqrt(len(key))
        if(key_to_matrix - int(key_to_matrix) != 0):
            raise AlphabetKeyLenError(key = key)
        else:
            self.alphabet = alphabet
            self.key = key

    def encrypt(self):
        pass

    def decrypt(self):
        pass


cp = HillCipher(alphabet='АБВГДЕ ЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', key='12344')