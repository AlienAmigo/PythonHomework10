import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot_data = pd.get_dummies(data['whoAmI'])
data_one_hot = pd.concat([data, one_hot_data], axis=1)

print(data_one_hot)

# ===================================================
# Решение без get_dummies
print('\nРешение без get_dummies:')

data_one_hot = pd.DataFrame(
    {'whoAmI': lst, 'human': map(lambda el: int(el == 'human'), lst), 'robot': map(lambda el: int(el == 'robot'), lst)})

print(data_one_hot)
