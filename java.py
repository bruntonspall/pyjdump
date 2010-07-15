import subprocess
import sys

def map_process(process):
	return {
	'user': process[0],
	'pid': process[1],
	'cmd': process[10],
	'args': ' '.join(process[11:]),	
	}
	
def get_processlist():
	return [map_process(l.split()) for l in subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).stdout.readlines()]
	
def get_java_processes():
	ps = get_processlist()
	return [l for l in ps if l['cmd'].endswith('java')]
	
def get_pid(process):
	return process['pid']
	
if __name__ == '__main__':
	processlist = get_java_processes()
	if len(processlist) > 1:
		print "Pick one"
		print ""
		print "OPTION\tPID\tCMD\tARGS"
		for index,process in enumerate(processlist):
			print "%d\t%s\t%s\t%s" % (index,process['pid'],process['cmd'],process['args'])
		process = raw_input('Pick One: ')
		if process:
			print get_pid(processlist[int(process)])
			
	else:
		print get_pid(processlist[0])