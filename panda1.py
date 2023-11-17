import pandas as pd

print("item1 = pd.DataFrame({ 'id': [0, 1, 2, 3], 'name': ['name1', 'name2', 'name3', 'name4'], 'age': [20, 22, 24, 30] })")
item1 = pd.DataFrame({ 'id': [0, 1, 2, 3], 'name': ['name1', 'name2', 'name3', 'name4'], 'age': [20, 22, 24, 30] })
print("item1:\n", item1)
print()

print("item1.head(1):\n", item1.head(1))
print()

print("item1.tail(1):\n", item1.tail(1))
print()

print("item2 = pd.DataFrame({ 'id': [0, 1, 2, 3], 'name': ['name1', 'name2', 'name3', 'name4'], 'age': [20, 22, 24, 30] })")
item2 = pd.DataFrame({ 'id': [0, 5, 6, 7], 'name': ['name1', 'name5', 'name6', 'name7'], 'age': [20, 32, 34, 40] })
print("item2:\n", item2)
print()

print("item3 = pd.DataFrame({ 'city': ['city1', 'city2', 'city3', 'city3'] })")
item3 = pd.DataFrame({ 'city': ['city1', 'city2', 'city3', 'city3'] })
print("item3:\n", item3)
print()

print("pd.merge(item1, item2):\n", pd.merge(item1, item2))
print()

print("item1.join(item3):\n", item1.join(item3))
print()

print("item1.to_csv('item1.csv')")
item1.to_csv("item1.csv")
print()

print("pd.read_csv('item1.csv'):\n", pd.read_csv("item1.csv"))
