# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?

# import random

# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()


import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

# преобразуем DataFrame в one-hot
one_hot = pd.get_dummies(data['whoAmI'], sparse=True)

# объединяем исходный DataFrame и one-hot
data_one_hot = pd.concat([data, one_hot], axis=1)

# удаляем исходный столбец 'whoAmI'
data_one_hot = data_one_hot.drop('whoAmI', axis=1)

# выводим результат
print(data_one_hot.head())