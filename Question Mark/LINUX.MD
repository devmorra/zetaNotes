##Linux L11 - v1

###Question 1 of 7
All are primary methods of managing software in Linux operating systems EXCEPT:

 	Blue Hat method
 	Compile from source code
 	Debian method
 	Red Hat method

###Question 2 of 7
What is the file extension for Red Hat software packages?

 	.com
 	.deb
 	.net
 	.rpm

*Answer: The file extension for Red Hat software packages is .rpm.nswer*

###Question 3 of 7
Which are attributes for managing software by compiling from source code? Select three responses.

 	Common in Linux but not in Windows or macOS
 	Has a .deb file extension
 	Turns human-readable code into machine-readable code
 	Uses GCC compiler

*Answer: Has a .deb file extension is not an attribute for managing software by compiling from source code.*

###Question 4 of 7
What do packages contain for software installation? Select three responses.

 	Documentation
 	Discounts on future software purchases
 	Installation instructions
 	Pre-compiled code

*Answer:All of these are contained in packages for software installation.*

###Question 5 of 7
Which command can be combined with yum to display specific installed software packages?

 	grep
 	kill
 	regedit
 	whoami

*Answer: The command grep can be combined with yum to display specific installed software packages.*

###Question 6 of 7
You want to see a list of all the ssh packages that have been installed on your Red Hat distribution. 
What command would you use?

 	grep yum ssh
 	yum list installed | grep ssh
 	yum remove ssh
 	yum zsh

*Answer: The command yum list installed | grep ssh should be used.*

###Question 7 of 7
You are using a RedHat distribution and need to use yum to install a package update for zsh. 
What command would you use?

 	yum update zsh
 	zsh install
 	yum remove zsh
 	zsh yum

*Answer:  The command to use would be yum update zsh.*
 
##Linux L2

###Question 1 of 7
What is the command syntax of Linux is composed of?
 Select three responses.
 
 	Argument
 	Command
 	Configuration
 	Option

*Answer: The command syntax of Linux is composed of an argument, command, and option.*

###Question 2 of 7
What is the default shell called that provides command prompt?

 	Bat
 	Bash
 	Hash
 	Prompt

*Answer: The default shell is called the Bash.*

###Question 3 of 7
Which key automatically completes commands and file/directory names in Bash?

 	CTRL
 	ENTER
 	SHIFT
 	TAB

*Answer: TAB is the key that automatically completes commands and file/directory names in Bash.*

###Question 4 of 7
Which command will display the account you are logged in as?

 	date
 	uptime
 	wc
 	whoami

*Answer: The command whoami will display the account you are logged in.*

###Question 5 of 7
Which command will display the previous commands if you make a mistake in a command prompt?

 	cal
 	history
 	hostname
 	who

*Answer: The history command will display previous comments in the case of a mistake in command prompts.*

###Question 6 of 7
You need to remove a sensitive password that was used as a command argument from the history file in bash. 

Where is the history file typically located?

 	/history/<username>/.bash
 	home/.bash_history
 	/home/<username>/.bash_history
 	<username>/history/home.bash

*Answer: The history file is typically located as /home/<username>/.bash_history.*

###Question 7 of 7
You are going to add data from a file called addresses.csv and need to know how many lines are present in the file. 
What command should you use?

 	addresses.csv -l cat
 	addresses.csv -l wc
 	cat -l  addresses.csv
 	wc -l addresses.csv

*Answer: The command you should use is wc -l addresses.csv.
 
##Linux L3

###Question 1 of 6
What is everything in Linux composed of?

 	Documents
 	Files
 	Hardware
 	System configurations

*Answer: Files are what Linux is comprised.*

###Question 2 of 6
Which attributes apply to Linux file names and extensions?
 Select three responses.
 
 	Is case sensitive
 	Extensions are optional and not necessarily mapped to applications
 	Must be unique within the directory
 	Must contain a / or spaces

*Answer: Those attributes apply to Linux file names and extensions.*

###Question 3 of 6
What is the function of the /etc directory?

 	Configuration files
 	Log files, print spool, network services
 	Removable media
 	Root of the file system

*Answer: Configuration files are the function of the /etc directory.*

###Question 4 of 6
Which command displays the absolute path to your current location in the file system?

 	cat
 	cp
 	pwd
 	tail

*Answer: The command pwd displays the absolute path to you current location in the file system.*

###Question 5 of 6
Which command changes your current working directory to another directory?

 	cd
 	head
 	more
 	rm

*Answer: The command cd changes the current working directory to another directory.*

###Question 6 of 6
You need to see a complete list of the log file names. What command would you use?

 	list -names /var/log
 	/log/ -la - ls
 	ls -la /var/log
 	/var/log -la -ls

*Answer: The command to see a complete list of log file names is ls -la /var/log.
 
##Linux L4
###Question 1 of 7
What is a value enclosed in to force Bash to recognize a space?

 	double commas
 	double hyphens
 	double periods
 	double quotes

*Answer: Double quotes is the value enclosed in that forces Bash to recognize a space.*

###Question 2 of 7
What three types of wild card characters does Bash recognize?
 Select three responses.
 
 	?
 	&
 	*
 	[ ]

*Answer: The three types of wild card characteristics that Bash recognizes is ?
, &, and [ ].*

###Question 3 of 7
Which command filters out repeated lines in a file?

 	awk
 	grep
 	tr
 	uniq

*Answer: The command uniq filters out repeated lines in a file.*

###Question 4 of 7
Which redirector overwrites existing file content with no warning?

 	<
 	>
 	|
 	2>

*Answer: The redirector > overwrites existing file content without warning.*

###Question 5 of 7
What variable can be set to prevent the output redirector to overwrite an existing file with no warning?

 	pipefail
 	noclobber
 	nooverwrite
 	tee

*Answer: The variable noclobber can be set to prevent the output redirector to overwrite an existing file without warning.*

###Question 6 of 7
You are troubleshooting an issue and want to check the log files for any failures. Which command syntax would display any secure log files containing the word "fail" for you?

 	grep fail /var/log/secure
 	find -f /*.csv
 	find */var/log/secure
 	fail whoami

*Answer: The command syntax is grep fail /var/log/secure that would display any secure log files containing the word "fail" for you.*

###Question 7 of 7
As you review the log files, you notice several duplicate entries. It would be helpful if you could remove or filter out the duplicates.
Which commands could help you accomplish this task?
 Select two responses.
 
 	echo "duplicates" | sed
 	sort -u file.txt
 	usermod -c "duplicates"
 	uniq /var/log/secure

*Answer: The commands you would use are sort -u file.txt and uniq /var/log/secure.
 
##Linux L5

###Question 1 of 7
What is the best practice for number of users per account?

 	1
 	2
 	3
 	4

*Answer: The best practice for number of users per account is one.*

###Question 2 of 7
Which statements apply to setting user passwords?
 Select three responses.
 
 	Passwords must be entered twice.
 	Passwords are set with the passwd command.
 	The root user only has access to reset their own password.
 	Users can reset their own passwords.

*Answer: Those statements apply to setting user passwords.*

###Question 3 of 7
All are data included in the / etc / group file EXCEPT:

 	GID
 	Group members
 	Group password field
 	Unencrypted password

*Answer: Unencrypted password is not included in the / etc / group.*

###Question 4 of 7
Which access levels are granted to a standard user?
 Select three responses.
 
 	Access any files given the right permissions are active
 	Control any files the user owns
 	Limited access to manage the system
 	Manage any account

*Answer:  Those are the correct access levels that are granted to a standard user.*

###Question 5 of 7
Which command allows full administrative privileges?

 	pseudo
 	root
 	su
 	sudo

*Answer: The su command allows full administrative privileges.*

###Question 6 of 7
You have been tasked with updating some user accounts. For this next account, you need to add a full name comment on a the Julia Martinez user and also specify an expiration date of Dec 31, 2021.
Which commands could you use to accomplish these tasks?
 Select two responses.

 	jmartinez -e 2021-12-31
 	root -c julia martinez
 	usermod -c "julia martinez" jmartinez
 	usermod -e 2021-12-31 jmartinez
 	None of the above

*Answer: The commands are usermod -c "julia martinez" jmartinez and usermod -e 2021-12-31 jmartinez.*

###Question 7 of 7
A few weeks later, you find out a user named Julia Martinez has moved on to another company and her account needs to be deleted.
Which command would you use to complete this task?

 	delete user julia martinez
 	deluser jm
 	hide jmartinez
 	userdel jmartinez

*Answer: The command would be userdel jmartinez.*
 
##Linux L6
###Question 1 of 7
What modes does Linux use to configure permissions?
 Select two responses.
 
 	Absolute
 	Basic
 	Infinite
 	Symbolic

*Answer: Absolute and symbolic are the modes ##Linux uses to configure permissions.*

###Question 2 of 7
Which three permissions does the ls-l command output?
 Select three responses.
 
 	group
 	other
 	system
 	user

*Answer: Group, other, and user are the three permissions that ls-l command outputs.*

###Question 3 of 7
What command is used to set permissions on files and directories?

 	awk
 	chmod
 	less
 	more

*Answer: The command to set permissions on files and directories is chmod.*

###Question 4 of 7
Which command is used to change the owner or group for a file or directory?

 	chown
 	regedit
 	sort
 	umask

*Answer: The command to change the owner or group for a file or director is chown.*

###Question 5 of 7
Which are best practices for permissions?
 Select three responses.
 
 	Do not use chmod777, which grants read, write and execute permissions to all users
 	Principle of least permissions
 	Principle of most permissions
 	Limit file names to alphanumeric characters, dots, and dashes.

*Answer: One of those are not a best practice for permissions.*

###Question 6 of 7
You have been asked to add group write permissions to file 1. 
What command would allow you to do this in symbolic mode?

 	chmod g+w file 1
 	file 1 chmod gw
 	root file 1 write
 	sort g+w file 1

*Answer: The chmod g+w file 1 command would allow you to do this in symbolic mode.*

###Question 7 of 7
You have also been asked to change the owner of a file, named file 1, to a user named Julia Martinez. What command allows you to do this?

 	chg file 1 jmartinez
 	chown jmartinez file 1
 	file 1 jmartinez change
 	own jmartinez file 1

*Answer: The command chown jmartinez file 1 to change the file owner.*
 
##Linux L8

###Question 1 of 7
Which are system programs?
 Select three responses.

 	Operating system commands
 	The primal computer functions
 	Utility program
 	Word processor

*Answer:  A word processor is not a system program.*

###Question 2 of 7
What do daemons, services, and programs consist of?

 	command
 	kernal
 	process
 	option

*Answer: These all consist of process.*

###Question 3 of 7
What command displays current processes?

 	nice
 	pidof
 	ps
 	renice

*Answer: The command that displays current processes is ps.*

###Question 4 of 7
Which command displays processes in a tree structure to easily identify parent and child processes?

 	child
 	kill
 	pstree
 	tree

*Answer: The command that displays processes in a tree structure to easily identify parent and child processes is pstree.*

###Question 5 of 7
Which commands may administrators use to schedule services or scripts to run automatically at specified times?
 Select two responses.

 	at
 	bat
 	chgmode
 	cron

*Answer: The commands administrators may use are at and cron.*

###Question 6 of 7
You are experiencing a slower than expected response time on your Linux server and want to see all the processes that are running. 

What command would you use?

 	nice
 	pidof process
 	ps -ef
 	sigint

*Answer: The command you would use is ps -ef.*

###Question 7 of 7
You have located process 1233 that seems to be causing your slow response time and you want to stop the process. You have been unable to gracefully quit the vm and need to immediately kill the process instead. 
What command would you use?

 	1233 kill
 	kill -9 1233
 	ps -ef
 	renice -19 1233

*Answer: The command you would use is kill -9 1233.*

##Linux L9 - v1

###Question: 1 of 7
What is the purpose of the ssh command?

 	Used to disable audio output
 	Used to lower audio output
 	Used to openly broadcast remote system connections
 	Used to securely connect to remote server or system

*Answer: The purpose of the ssh command is to securely connect to remote server or system*

###Question: 2 of 7
Which are systemctl sub commands?  Select three responses.
 
 	disable
 	nano
 	start
 	status

*Answer: Disable, start, and status are all systemctl sub commands*

###Question: 3 of 7
Which top task category is for a child process whose parent process has been terminated?

 	Running
 	Sleep
 	Stopped
 	Zombie

*Answer: Zombie is a top task category that is for a child process whose parent process has been terminated*

###Question: 4 of 7
All are information displayed using the df command EXCEPT:

 	date
 	hard disk size
 	used and free space
 	system file partition location

*Answer: The information displayed is the date*

###Question: 5 of 7
You think that restarting the sshd program may solve your problem. What command would you enter to complete this task?

 	ctlsystem restart sshd
 	cat sshd restart
 	restart sshd
 	systemctl restart sshd

*Answer: The command you would use is systemctl restart sshd*

###Question: 6 of 7
Where is memory utilization information viewed after running the top command?

 	Bottom of the page
 	Left of the page
 	Right of the page
 	Top of the page

*Answer: The memory utilization information viewed after running the top command can be found at the top of the page*

###Question: 7 of 7
You have been asked to troubleshoot a remote server. What command would allow you to securely connect to the remote server, assuming you are user03 on computer 15?

 	user03@computer15 ssh
 	secure user03 computer 15
 	login user01 computer 15
 	ssh user03@computer15

*Answer: The command to use would be ssh user03@computer15.*
 
##Linux L10

###Question 1 of 7
Which are use cases of the ping command?  Select two responses.

 	Determining the speed of connection
 	Killing connections
 	Locating new connections
 	Testing connections

*Answer: These two are cases of the ping command.*

###Question 2 of 7
What are the results of the netstat command?  Select three responses.

 	Displays connection information
 	Displays hardware configuration
 	Displays routing tables
 	Displays status of ports

*Answer: All of those are results of the netstat command.*

###Question 3 of 7
Which is the correct syntax for the telnet command?

 	telnet host port
 	telnet [host [port]]
 	telnet "host" port
 	telnet | host | port

*Answer: The correct syntax is telnet [host [port]].*

###Question 4 of 7
Which are key services for networking troubleshooting?  Select three responses.

 	Firewall
 	Hard drive
 	Network
 	Secure Shell (SSH)

*Answer: Firewall, network, Secure Shell (SSH) are key services for networking troubleshooting.*

###Question 5 of 7
All are recommended troubleshooting steps EXCEPT:

 	Verify physical status (plugged in, on)
 	Call your supervisor first
 	Check service status with the systemctl command
 	Restart the service with the systemctl command

*Answer: All of these are recommended troubleshooting steps except Call your supervisor first.*

###Question 6 of 7
You are trying to determine if a web server that hosts Linuxabc.com is connected. What command would you use?

 	chown Linuxabc.com
 	find Linuxabc.com
 	ping Linuxabc.com
 	:wq

*Answer: The command is ping Linuxabc.com.*

###Question 7 of 7
You have determined the web server for Linuxabc.com is connected and now want to learn how many hops the packets are taking to reach this destination. What command would you use?

 	ping Linuxabc.com
 	scp Linuxabc.com
 	traceroute Linuxabc.com
 	query ssh

*Answer: The command to use is traceroute Linuxabc.com.*

##Linux L11 - v1

###Question 1 of 7
All are primary methods of managing software in Linux operating systems EXCEPT:

 	Blue Hat method
 	Compile from source code
 	Debian method
 	Red Hat method

*Answer: The Blue Hat method is not a primary method of managing software in Linux operating systems*

###Question: 2 of 7
What is the file extension for Red Hat software packages?

 	.com
 	.deb
 	.net
 	.rpm

*Answer: The file extension for Red Hat software packages is .rpm*

###Question: 3 of 7
Which are attributes for managing software by compiling from source code?   Select three responses.
 
 	Common in Linux but not in Windows or macOS
 	Has a .deb file extension
 	Turns human-readable code into machine-readable code
 	Uses GCC compiler

*Answer: Has a .deb file extension is not an attribute for managing software by compiling from source code*

###Question: 4 of 7
What do packages contain for software installation?  Select three responses.
 
 	Documentation
 	Discounts on future software purchases
 	Installation instructions
 	Pre-compiled code

*Answer: All of these are contained in packages for software installation*

###Question: 5 of 7
Which command can be combined with yum to display specific installed software packages?

 	grep
 	kill
 	regedit
 	whoami

*Answer: The command grep can be combined with yum to display specific installed software packages*

###Question: 6 of 7
You want to see a list of all the ssh packages that have been installed on your Red Hat distribution. 
What command would you use?

 	grep yum ssh
 	yum list installed | grep ssh
 	yum remove ssh
 	yum zsh

*Answer: The command yum list installed | grep ssh should be used*

###Question: 7 of 7
You are using a RedHat distribution and need to use yum to install a package update for zsh. What command would you use?

 	yum update zsh
 	zsh install
 	yum remove zsh
 	zsh yum

*Answer: The command to use would be yum update zsh.*

##Linux L12

###Question 1 of 7
What is logging in Linux?

 	Keeping a personal diary
 	Keeping records of events on the system, allowing for auditing
 	Recalling common help commands
 	Recording video files

*Answer: Keeping records of events on the system, allowing for auditing is logging in Linux.*

###Question 2 of 7
What types of events are logged?  Select three responses.
 
 	System startup information
 	Your birthday
 	System shutdown times
 	User login and logout events

*Answer: Your birthday is not a logged event.*

###Question 3 of 7
Where does Linux normally store log files?

 	/boot
 	command prompt
 	/dns
 	/var/log

*Answer:  Linux normally stores log files in /var/log.*

###Question 4 of 7
Which are true statements about log rotation?  Select three responses.
 
 	Log rotation is a way to limit the total size of the logs retained
 	Log rotation is an automated process in which dated log files are archived.
 	Log rotation is not used frequently because log files are few and small in size.
 	Log rotation still allows analysis of recent events.

*Answer: Those are all true statements.*

###Question 5 of 7
All are a logging levels EXCEPT:

 	BASE
 	DEBUG
 	FATAL
 	WARN

*Answer: BASE is not a logging level.*

###Question 6 of 7
You need to review the most recent system logs. Where would you find the logs that are created for system information?

 	var/log/maillog
 	system/var/log
 	var/log/boot.log
 	var/log/syslog

*Answer: The logs can be found in var/log/syslog.*

###Question 7 of 7
You are performing a routine security check and need to see a list of recent logins. What command would you use to see all recent logins?

 	backlog
 	fastlog
 	firstlog
 	lastlog

*Answer: The command you would use is lastlog.*
 
##Linux L13

###Question 1 of 6
Which command maintains a table of recently executed programs?

 	diff
 	find
 	hash
 	tar

*Answer: The command to maintain a table of recently executed programs is hash.*

###Question 2 of 6
What is the purpose of the diff command?

 	Applies a different configuration
 	Compares files line by line and displays the differences
 	Moves a file to a different location
 	Renames a file to a different name

*Answer: The purpose of the diff command is to compare files line by line and displays the differences.*

###Question 3 of 6
What is the result of the bundling several files into a single file called?

 	tardigrade
 	tarball
 	tarnation
 	tarweed

*Answer: The result is tarball.*

###Question 4 of 6
What is the purpose of the gzip command?

 	Compress files
 	Delete files
 	Move files
 	Restore files

*Answer: The purpose of the gzip command is to compress files.*

###Question 5 of 6
You need to bundle files 2 - 6 together to make copying them to another server easier.  What command would you use?

 	combine file2 file3 file4 file5 file6
 	copy file 2-6
 	tar file 2-6
 	tar -cvf tarball.tar file[2-6]

*Answer: The command to use is tar -cvf tarball.tar file[2-6].*

###Question 6 of 6
You need to see a list of your jpg files. Assuming your user name is student 02, what command would you use to see a list of your jpg files?

 	*.jpg find
 	find /home/student02 -name *.jpg
 	concat *.jpg
 	find -user student 01

*Answer: The command to use would be find /home/student02 -name *.jpg.*


##Linux L14 - v1

###Question:  1 of 7
Which are Bash Shell features?
 Select three responses.
 
 	Cannot be added to Windows
 	History
 	Tab Completion
 	Variables

*Answer: Bash Shell features cannot be added to Windows*

###Question: 2 of 7
Variables are usually declared in what case?

 	UPPERCASE
 	Title Case
 	lowercase
 	mIXeDcAsE

*Answer: Variables are usually declared in UPPERCASE*

###Question: 3 of 7
Which command allows a user to view, set or remove environmental variables?

 	env
 	environvar
 	varenv
 	varenvironment

*Answer: The env command allows a user to view, set or remove environmental variables*

###Question: 4 of 7
What is the command to remove a configured alias?

 	minusalias
 	negalias
 	notalias
 	unalias

*Answer: The command to use to remove a configured alias is unalias*

###Question: 5 of 7
Which statement describes the purpose of the # character, when not found on the first line of a bash script?

 	Lines starting with # are generally ignored by bash so comments or notes to user can be communicated
 	Precedes a file name selected to combine into a tarball file
 	Precedes a number to direct bash to follow a specific order of steps (#1, #2, etc.)
 	Used to tag command lines
 
*Answer: This statement describes the purpose of the # character, when not found on the first line of a bash script*

###Question: 6 of 7
You want users to see a Please Be Patient, Long Script message on the screen when they run a script. 
What command would you use to do so?

 	Copy "Please Be Patient, Long Script"
 	Echo 'Please Be Patient, Long Script'
 	Insert "Please Be Patient, Long Script"
 	"Please Be Patient, Long Script" in progress

*Answer: The command Echo 'Please Be Patient, Long Script' should be used*

###Question: 7 of 7
You want to set the number of lines stored in your history list in your bash session to 1500. 
What command would you use?

 	env XDG_VTNR=1500
 	1500 set history
 	env 1500
 	env HISTSIZE=1500

*Answer: The env HISTSIZE=1500 command should be used to set the number of lines stored in your history list in your bash session to 1500.*
 
##Linux L15

###Question 1 of 7
Which are true statements about scripts?
 Select three responses.
 
 	Scripts are text files of commands and related data.
 	When the script file is executed, the commands are run.
 	Scripts may NOT be set as scheduled tasks by using the cron command.
 	Scripts are executed more consistently by being automated than by manually typing commands.

*Answer: Those are all true statements about scripts.*

###Question 2 of 7
What are arguments in Linux?

 	A shell type you can use instead of bash
 	Log of script results
 	Two or more commands that conflict with each other
 	Values you want a script to act upon

*Answer: Arguments are values you want a script to act upon.*

###Question 3 of 7
All are included in the process of creating a script EXCEPT:

 	Create script using a text editor
 	Set script permissions to execute
 	Use [ ] to run a script
 	Use ./ to run a script

*Answer: Use [ ] to run a script is not included in the process of creating a script.*

###Question 4 of 7
Which are true statements about functions?  Select three responses.

 	A function is a script within a script.
 	A function is a small chunk of code to be reused within a script.
 	Scripts are tidier, which makes them easier to understand and troubleshoot.
 	Scripts create too much complexity, which makes them hard to understand and troubleshoot.

*Answer: Those are all true statements about functions.*

###Question 5 of 7
What is a section of script that can be configured to repeat itself?

 	Backup statement
 	Loop statement
 	Recycle statement
 	Restart statement

*Answer: The loop statement is a section of script that can be configured to repeat itself.*

###Question 6 of 7
You want to create a script to back up your user home directory. What would script would you enter given your user name is student04?

 	tar -czf backup-job.tar /home/student04
 	backup-job.tar student 04
 	i -csv /home/student04 tar
 	backup student 04

*Answer: The script to use would be tar -czf backup-job.tar /home/student04.*

###Question 7 of 7
You have created a script that says hello to the current user and you would also like to include the current date in the message. The first two lines of your script are: 
    1 #!/bin/bash
    2 echo "Hello, $USER!"
What should the third line say to specify the date?

 	3 echo "Today's date is <current date>"
 	3 echo: Today's date is x
 	3 echo "Today's date is 'date'"
 	3 echo show date

*Answer: The third line should say: 3 echo "Today's date is 'date'".*


