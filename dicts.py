User = {'Sergey': 89013005304, 'Marina': 89817831120}
print(User['Marina']) # посмотрели значение Marina
User['Sergey']=True # Поменяли значение у Sergey
print(User['Sergey'])
print(User.get('ф', 'нет такого')) # get значение по ключу (без ошибок)
User["Sfomin"] = 89112277250 # добавил нового
del User['Sergey'] # удалил Sergey!!!
User.update({'John' : 89119283308,
             'Vadim' : 89119187882,
             'Gena' : 8904444433}) #Добавил списком
print(User)
print(User.get('Gena')) # достали Gena
User.pop('Marina') # метод удалил Марина!!!
print(User)
print(User.keys()) # ключи
print(User.values()) # значения
print(User.items()) # ключ и значение
free = {1,2,4,5,1,5, 'text', False} # множество
print(free) # add to Git