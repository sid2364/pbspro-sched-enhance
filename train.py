from sklearn import svm, ensemble, neighbors
from sklearn.metrics import accuracy_score
import parse_data as parse
import segment as seg

data = parse.getData()
features_data, labels_data = seg.split_features(data)
features_train, features_test = seg.segment_data(features_data)
labels_train, labels_test = seg.segment_data(labels_data)

#classifier = ensemble.RandomForestClassifier(n_estimators=500,max_features=3,min_samples_split=5,oob_score=True)
classifier = svm.SVC(kernel='linear', cache_size=20, verbose=True)
#classifier = neighbors.KNeighborsClassifier(algorithm="auto", weights="distance", n_neighbors=15)
#classifier = ensemble.AdaBoostClassifier(n_estimators=50, learning_rate=0.5)

print("Going to fit " + str(len(features_train)) + " training rows with " + str(len(labels_train)) + " labels.")

print("Training...")
classifier.fit(features_train, labels_train)
print("Finished training.")

print("Predicting...")
prediction = classifier.predict_proba(features_test)
print("Finished predicting.")

ccuracy = accuracy_score(prediction, labels_test)
print "Accuracy: ", str(round(accuracy*100, 3))

