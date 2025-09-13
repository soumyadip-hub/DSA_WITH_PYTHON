# Dictionary - a dictionary is a collection which is unordered,changeable and indexed

# create a dictioanry
mydict = dict()
print(mydict)
mydict2 = {}
print(mydict2)

# method-1   my_dict = dict(key1='value1',key2='value2',key3='value3')
eng_sp = dict(one="uno", two="dos", three="tres")
print(eng_sp)

# method-2   This rule:    my_dict = {'key1':'value1','key2':'value2','key3':'value3'}

eng_sp2 = {"one": "uno", "two": "dos", "three": "tres"}
print(eng_sp2)

# method-3   my_list_of_tuples = [('key1','value1'),('key2','value2'),('key3','value3')]
#                   my_dict =dict(my_list_of_tuples)

eng_sp_list = [("one", "uno"), ("two", "dos"), ("three", "tres")]
eng_sp3 = dict(eng_sp_list)
print(eng_sp3)
