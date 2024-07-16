my_dict = {'Aleks': 1990, 'Den': 1991, 'Mike': 1992}
print('Dict: ', my_dict)
print('Existing value: ', my_dict.get('Mike'))
print('Not existing value: ', my_dict.get('Tomas'))
my_dict['Max'] = 1993
my_dict.update ({'Ivan': 1994, 'Serj': 1995})
a = my_dict.pop('Den')
print('Deleted value: ', a)
print('Modified dictionary: ', my_dict)
my_set = {1,2,3,3,2,4,5,'Set'}
print('Set:', my_set)
my_set.add((0,9,8))
my_set.add(7.56)
my_set.discard("Set")
print('Modified set: ', my_set)