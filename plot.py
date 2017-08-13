import matplotlib.pyplot as plt
import parse_data as parse
import segment as seg

train_ft=["Resource_List.walltime"]

target_ft="resources_used.walltime"

data = parse.getData()
RL_walltime, RU_walltime = seg.split_features(data, train_ft, target_ft)

print(len(RL_walltime), len(RU_walltime))

plt.plot(RL_walltime, RU_walltime, 'ro')
plt.show()
