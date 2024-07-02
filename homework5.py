immutable_var=13, 'text', True #кортеж
print('immutable_var:', immutable_var)
#immutable_var[0]=True # нельзя изменить значение. Кортеж не поддерживает обращение по элементам.

mutable_list=[12, 'dog',True]
print(mutable_list) # изначалный список
mutable_list[0]='door' # поменял 12 на door
mutable_list.append(False) # добавил к списку False
mutable_list.extend(['mouse','bear']) #добавил еще списком
print('mutable_list: ', mutable_list) # add to Git