import numpy as np
from sklearn import datasets, ensemble

digits_dataset = datasets.load_digits()
X_data, y_data = digits_dataset['data'], digits_dataset['target']

split_index = int(0.25 * X_data.shape[0])
X_train, X_test = X_data[:-split_index], X_data[-split_index:]
y_train, y_test = y_data[:-split_index], y_data[-split_index:]

print(f"Размер X_train: {X_train.shape}, размер X_test: {X_test.shape}")
print(f"Размер y_train: {y_train.shape}, размер y_test: {y_test.shape}")


def find_nearest_neighbor(test_sample, X, y):
    distances = ((X - test_sample) ** 2).sum(axis=1)
    return y[np.argmin(distances)]


predicted_labels = [find_nearest_neighbor(test_sample, X_train, y_train) for test_sample in X_test]
knn_accuracy = np.mean(y_test != predicted_labels)

print(f"Точность метода ближайшего соседа: {knn_accuracy}")

random_forest_clf = ensemble.RandomForestClassifier(n_estimators=1000).fit(X_train, y_train)
rf_accuracy = np.mean(y_test != random_forest_clf.predict(X_test))

print(f"Точность случайного леса: {rf_accuracy}")
