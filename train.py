from sklearn import svm, ensemble, neighbors
from sklearn.metrics import accuracy_score
import parse_data as parse
import segment as seg

data = parse.getData()
features_data, labels_data = seg.split_features(data)
features_train, features_test = seg.segment_data(features_data)
labels_train, labels_test = seg.segment_data(labels_data)

classifier = ensemble.RandomForestClassifier(n_estimators=500,max_features=3,min_samples_split=5,oob_score=True)

print("Training...")
classifier.fit(features_train, labels_train)
print("Finished training.")

print("Predicting...")
prediction = classifier.predict_proba(features_test)
print("Finished predicting.")

ccuracy = accuracy_score(prediction, labels_test)
print "Accuracy: ", str(round(accuracy*100, 3))

