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

result = ins._InstanceList__get_next_token(lambda x, y: 0)
if result != 'a':
    print "There was a problem getting the next token (value: 0). Actual value: " + \
    str(result)
    print ins._get_native_types()

result = ins._InstanceList__get_next_token(lambda x, y: 1)
if result != 'a':
    print "There was a problem getting the next token (value: 1). Actual value: " + \
    str(result)
    print ins._get_native_types()

result = ins._InstanceList__get_next_token(lambda x, y: 2)
if result != 'b':
    print "There was a problem getting the next token (value: 2). Actual value: " + \
    str(result)
    print ins._get_native_types()

result = ins._InstanceList__get_next_token(lambda x, y: 3)
if result != 'b':
    print "There was a problem getting the next token (value: 3). Actual value: " + \
    str(result)
    print ins._get_native_types()

try:
    result = ins._InstanceList__get_next_token(lambda x, y: 4)
except IndexError as e:
    print "Caught Index error"
else:
    print "We didn't catch any errors, and that's a problem."

instance = mt.InstanceMatrix()

instance.load('this')

a = instance.generate()
if a != "this":
    print "There was a problem generating from the instance matrix."
    print "Result: " + a

print "Tests finished."
