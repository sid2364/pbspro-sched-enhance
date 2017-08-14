from sklearn import svm, ensemble, neighbors
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import parse_data as parse
import segment as seg


default_train_ft=["Resource_List.walltime"]

default_target_ft="resources_used.walltime"

data = parse.getData()
features_data, labels_data = seg.split_features(data)
features_train, features_test = seg.segment_data(features_data)
labels_train, labels_test = seg.segment_data(labels_data)

#print(features_train)
#print(labels_train)
#print(features_test)
#print(labels_test)

#classifier = ensemble.RandomForestClassifier(n_estimators=500,max_features=3,min_samples_split=5,oob_score=True)
#classifier = svm.SVC(kernel='linear', cache_size=10, verbose=True)
#classifier = neighbors.KNeighborsClassifier(algorithm="auto", weights="distance", n_neighbors=15)
#classifier = ensemble.AdaBoostClassifier(n_estimators=50, learning_rate=0.5)
#classifier = GaussianNB()
classifier = svm.SVC()

print("Going to fit " + str(len(features_train)) + " training rows with " + str(len(labels_train)) + " labels.")

print("Training...")
classifier.fit(features_train, labels_train)
print("Finished training.")

print("Predicting...")
prediction = classifier.predict(features_test)
print("Finished predicting.")

print(prediction)

accuracy = accuracy_score(prediction, labels_test)
print "Accuracy: ", str(round(accuracy*100, 3))
