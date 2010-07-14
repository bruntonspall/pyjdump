import subprocess

def get_processlist():
	return subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).stdout.readlines()
	
def get_java_processes():
	ps = get_processlist()
	return [l.split() for l in ps if l.split()[10].endswith('java')]
	
def get_pid(process):
	return process[1]
		
def dump_stack(pid, filename):
	subprocess.Popen(['jmap', '-dump:file=%s' % filename, pid])
	
if __name__ == '__main__':
	print [get_pid(p) for p in get_java_processes()]