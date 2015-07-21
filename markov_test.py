import markov_tool as mt

ins = mt.InstanceList()

if ins._get_native_types() != (0, {}):
    print "There was a problem instantiating the InstanceList."
    print ins._get_native_types()

ins['a'] = 1
if ins['a'] != 1 or ins._get_native_types() != (1, {'a': 1}):
    print "There was a problem setting/getting an item."
    print ins._get_native_types()

ins['a'] += 1
if ins['a'] != 2 or ins._get_native_types() != (2, {'a': 2}):
    print "There was a problem setting/getting an item."
    print ins._get_native_types()

ins['b'] = 2

if ins._InstanceList__get_next_token(lambda x, y: 0) != 'a':
    print "There was a problem getting the next token (value: 0). Actual value: " + \
    str(ins._InstanceList__get_next_token(lambda x, y: 0))
    print ins._get_native_types()    

instance = mt.InstanceMatrix()

instance._add_char('a', 'b')
if {'a': {'b': 1}} != instance._get_matrix():
    print "There was a problem adding a new top-level element."
    print instance._get_matrix()

instance._add_char('a', 'c')
if {'a': {'b': 1, 'c': 1}} != instance._get_matrix():
    print "There was a problem adding a new second-level element."
    print instance._get_matrix()

instance._add_char('a', 'c')
if {'a': {'b': 1, 'c': 2}} != instance._get_matrix():
    print "There was a problem updating a second-level element."
    print instance._get_matrix()

instance = mt.InstanceMatrix()

instance.load('this')
if {'': {'t': 1}, 't': {'h': 1}, 'h': {'i': 1}, 'i': {'s': 1}, 's': {'': 1}} != instance._get_matrix():
    print "There was a problem loading a string into the Instance Matrix."

print "Tests finished."

