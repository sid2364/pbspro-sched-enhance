import json

data_file = "accounting_log_2009_icl.sdata"

field_list = ["ctime", "qtime", "etime", "start", "resources_used.walltime", "resources_used.vmem", "resources_used.ncpus",\
		"resources_used.mem", "resources_used.cpupercent", "resources_used.cput", "Resource_List.walltime", "Resource_List.select"]

headers = field_list[:-1] + ["Resource_List.mem", "Resource_List.ncpus"]


def readLine(line):
	# format is <time;record-type;id;string>
	# time is irrelevant ?
	data = {}
	if line[1] == "E":
		lineta = {}
		jid = str(line[2]) #id
		#parse line and return only header values
		count = 0
		for part in line[3].split(" "):
			field_name = part.split('=')[0]
			field_value = ''.join(part.split('=')[1:])
			lineta[field_name] = field_value
			count += 1
		lineta['arg_count'] = count
	else:
		return None
	data[jid] = lineta
	return data

def parse(content):
	data_l = []
	for line in content:
		line = line.strip()
		parsedLine = readLine(line.split(";"))
		if parsedLine is not None:
			data_l.append(parsedLine)
	#print(json.dumps(data_l, indent=4))
	return data_l

if __name__=="__main__":
	with open(data_file, "r") as datafp:
		content = [line.rstrip('\n') for line in datafp]
		data_l = parse(content)
