from __future__ import division
from random import randrange

class InstanceList(object):
    '''A dictionary-like object that remembers how many objects have been put into it. The keys should be the secondary
    items in a Markov chain, and the values should be the number of instances of that item.'''

    def __init__(self):
        '''Obviously, at this point, there are zero objects in this List.'''
        self.instances = 0
        self.output = {}

    def __getitem__(self, a):
        '''This method allows access through the [] notation'''
        return self.output[a]

    def __setitem__(self, a, b):
        '''This method allows assignment through the [] notation'''
        if a in self.output.keys():
            self.instances += b - self.output[a]
        else:
            self.instances += b

        self.output[a] = b

    def _get_native_types(self):
        '''This method is only used for testing. If it's called anywhere outside the test harness, there's something 
        wrong.'''
        return (self.instances, self.output)

    def get_next_token(self):
        return self.__get_next_token()

    def __get_next_token(self, random_generator=None):
        if random_generator == None:
            random_generator = randrange
        index = random_generator(0,self.instances)
        key_index = 0
        for key in self.output.keys():
            key_index += self.output[key]
            if key_index > index:
                return key
        raise IndexError("The random number was out of range.")

class InstanceMatrix(object):
    '''I really need to document this so that I can remember what it does later.'''

    def __init__(self):
        self.matrix = {}

    def _get_matrix(self):
        return self.matrix

    def _add_elem(self, first, second):
        if first in self.matrix:
            if second in self.matrix[first]:
                self.matrix[first][second] += 1
            else:
                self.matrix[first][second] = 1
        else:
            self.matrix[first] = InstanceList()
            self.matrix[first][second] = 1

    def load(self, iter_data):
        data_len = len(iter_data)
        for i in range(data_len):
            if i == 0:
                self._add_elem('', iter_data[i])
            else:
                self._add_elem(iter_data[i-1], iter_data[i])
        self._add_elem(iter_data[-1], '')

    def generate(self):
        result = ""
        while True:
            if result == "":
                result += self.matrix[''].get_next_token()
            else:
                tmp = self.matrix[result[-1]].get_next_token()
                if tmp == '':
                    break
                result += tmp
        return result

class MarkovChainGenerator(object):

    def __init__(self):
        self.markov_matrix = MarkovMatrix()
