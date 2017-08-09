import json

data_file = "accounting_log_2009_icl.sdata"

field_list = ["ctime", "qtime", "etime", "start", "resources_used.walltime", "resources_used.vmem", "resources_used.ncpus",\
		"resources_used.mem", "resources_used.cpupercent", "resources_used.cput", "Resource_List.walltime", "Resource_List.select"]

headers = field_list[:-1] + ["Resource_List.mem", "Resource_List.ncpus"]

time_fields = ["Resource_List.walltime", "resources_used.cput", "resources_used.walltime"]
number_fields = ["session", "etime", "start", "Resource_List.ncpus", "end", "ctime", "qtime",\
			"resources_used.ncpus", "resources_used.ncpus", "Resource_List.nodect"]
mem_fields = ["Resource_List.mem", "resources_used.mem", "resources_used.vmem"]

def convertToGMKb(memory_string, target='kb'):
	gmk_d = {'kb': 1, 'mb': 2, 'gb': 3}
	gmk = memory_string[-2:].lower()
	size = float(memory_string[:-2])
	shift = gmk_d[target] - gmk_d[gmk]
	if shift != 0:
		size /= 1024**shift
	return size

def convertTimeToSeconds(time_string, ftr=[3600,60,1]):
	return sum([a*b for a,b in zip(ftr, map(int,time_string.split(':')))])

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
			if field_name in time_fields:
				field_value_i = convertTimeToSeconds(field_value)
			elif field_name in number_fields:
				field_value_i = int(field_value)
			elif field_name in mem_fields:
				field_value_i = convertToGMKb(field_value)
			else:
				field_value_i = field_value
			lineta[field_name] = field_value_i
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
	print(json.dumps(data_l, indent=4))
	return data_l

if __name__=="__main__":
	with open(data_file, "r") as datafp:
		content = [line.rstrip('\n') for line in datafp]
		data_l = parse(content)
	
