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
	if len(sys.argv) < 2:
		print "Usage: java.py <java_selector>"
		print ""
		print "Example: java.py Resin"
		sys.exit(1)
	print sys.argv
	print [get_pid(p) for p in get_java_processes() if p['args'].find(sys.argv[1]) != -1]