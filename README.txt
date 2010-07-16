This is pyjava.

It looks at currently running processes, hunting for java processes, and gives you an option to do a java memory dump of one of them.

Potential upgrades:
use subprocess.call shorcut instead of subprocess.Popen
when there is only 1 java process running, it doesn't make a dump file, it should
It should check the uid or gid of the current user. (os.getuid might be worth a look)
It should check which version of java is installed and use the correct options.
It should give you the option of a stack dump as well as a heap dump.
