import pandas as pd
import random

# Ваш исходный код
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразование в one-hot кодировку
one_hot_encoded = pd.get_dummies(data['whoAmI'], prefix='whoAmI')
result = pd.concat([data, one_hot_encoded], axis=1)
result.drop('whoAmI', axis=1, inplace=True)

print(result.head())