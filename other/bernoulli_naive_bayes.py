import numpy1 as np
from sklearn.naive_bayes import BernoulliNB


rng = np.random.RandomState()
X = rng.randint(5, size=(6, 2))
T = rng.randint(5, size=(1, 2))
print(X)
print()
print(T)
Y = np.array([1, 0, 0, 1, 1, 0])
clf = BernoulliNB(force_alpha=False)
clf.fit(X, Y)

total = []
for i in range(len(X)):
    my_sum = np.sum(X[i:i + 1] == T[0:1])
    print("count for record", i, ":", np.sum(X[i:i+1] == T[0:1]), "(", Y[i], ")")
    total.append([my_sum, i])


def using_first(item):
    return item[0]


print(total)
total = sorted(total,key=using_first)
print(total)
print("index:", total[-1][1])
expected = Y[total[-1][1]]
print("Expected:", expected)
print("Got:", clf.predict(T[0:1]))
