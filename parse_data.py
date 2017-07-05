
data_file = "accounting_log_2009_icl.sdata"

def readLine(line):
	# format is <time;record-type;id;string>
	# time is irrelevant ?
	parsed = []
	if line[1] == "E":
		parsed.append(line[2]) #id
		return line[3].split(" ")
	else:
		return None

def parse(content):
	data_l = []
	for line in content:
		line = line.strip()
		parsedLine = readLine(line.split(";"))
		print(parsedLine)
		if parsedLine is not None:
			data_l.append(parsedLine)
	print(data_l)

if __name__=="__main__":
	with open(data_file, "r") as datafp:
		content = [line.rstrip('\n') for line in datafp]
		data_l = parse(content)
		print data_l
