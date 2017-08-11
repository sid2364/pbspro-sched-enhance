import parse_data

# take data and segment into (RL_ncpus, RL_mem, RL_walltime, RU_ncpus, RU_mem) and target (RU_walltime)

default_train_ft=["Resource_List.mem", "Resource_List.ncpus", \
				"resources_used.mem", "Resource_List.walltime", "resources_used.ncpus"]

default_target_ft="resources_used.walltime"

def split_features(data, trainers=default_train_ft, target=default_target_ft):
	training_features = []
	target_features = []
	for row in data:
		for jid in row:
			temp_d = row[jid]
			training_ = []
			try:
				for trainer in trainers:
					training_.append(temp_d[trainer])
				training_features.append(training_)
				target_features.append(temp_d[target])
			except KeyError:
				print("Skipping, since ", temp_d, "doesn't have valid keys.")
	return training_features, target_features

def segment_data(data, tr_s=0.75):
	te_s = 1 - tr_s
	l = len(data)
	return data[:int(tr_s*l)], data[int(tr_s*l)+1:]

if __name__=="__main__":
	data = parse_data.getData()
	train_features, target_features = split_features(data)
	train_data, test_data = segment_data(train_features)
	
