from sklearn import svm, ensemble, neighbors
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import parse_data as parse
import segment as seg
import numpy as np 


default_train_ft=["Resource_List.walltime", "Resource_List.ncpus", "Resource_List.mem"]

default_target_ft="resources_used.walltime"

data = parse.getData()
features_data, labels_data = seg.split_features(data, trainers=default_train_ft)
features_train, features_test = seg.segment_data(features_data)
labels_train, labels_test = seg.segment_data(labels_data)

#print(features_data)
#print("*" * 40)
#print(labels_data)

features_train = np.array(features_train)
labels_train = np.array(labels_train)
features_test = np.array(features_test)
labels_test = np.array(labels_test)

#classifier = ensemble.RandomForestClassifier(n_estimators=500,max_features=3,min_samples_split=5,oob_score=True)
#classifier = svm.SVC(kernel='linear', cache_size=10, verbose=True)
#classifier = neighbors.KNeighborsClassifier(algorithm="auto", weights="distance", n_neighbors=15)
#classifier = ensemble.AdaBoostClassifier(n_estimators=50, learning_rate=0.5)
#classifier = GaussianNB()
#classifier = svm.SVC()
classifier = LinearRegression(n_jobs=-1)

print("Going to fit " + str(len(features_train)) + " training rows with " + str(len(labels_train)) + " labels.")

print("Training...")
classifier.fit(features_train, labels_train)
print("Finished training.")

print("Predicting...")
prediction = classifier.predict(features_test)
print("Finished predicting.")

print(len(prediction), len(labels_test))
print(np.shape(prediction), np.shape(labels_test))

print(prediction)
print(labels_test)


rsq = classifier.score(features_test, labels_test)
print("R-squared: ", rsq)
