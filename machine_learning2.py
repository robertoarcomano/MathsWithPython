import seaborn as sb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

def rndint(item):
    return np.intc(np.round(item))


person = {
    "finance": rndint(np.random.rand(40) * 10),
    "management": rndint(np.random.rand(40) * 10),
    "logistic": rndint(np.random.rand(40) * 10),
    "get_work": rndint(np.random.rand(40))
}
Data = pd.DataFrame(person, columns=["finance", "management", "logistic", "get_work"])

x = Data[["finance", "management", "logistic"]]
y = Data["get_work"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

logistic_regression = LogisticRegression()
logistic_regression.fit(x_train, y_train)
y_prediction = logistic_regression.predict(x_test)

confusion_matrix = pd.crosstab(y_test, y_prediction, rownames=["True"], colnames=["Prevision"])

sb.heatmap(confusion_matrix)

print("Accuracy:", metrics.accuracy_score(y_test, y_prediction))
plot.show()
