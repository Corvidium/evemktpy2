import mktconfig, datetime

def uniLog(some_data):
	with open(mktconfig.genlog, "a") as file:
		file.write('\n')
		file.write('['+str(datetime.datetime.now())+'] ')
		file.write(str(type(some_data)))
		if(type(some_data) == str):
			file.write(some_data)
		file.close()
	return 1