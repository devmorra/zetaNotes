# What is SysAdmin:
Manage hardware and software systems
All systems are working well
Maintain and update
Install, maintain, create, and plan system issues and accounts

Discussion: 
 How might you use Python to make system administration tasks easier? (ReStart, 03/2020)
Automate many things
Deploy many automated tools at once
Update systems all at once
Build safety protocols 
Saves you time and faster than manually
Uniformity

Benefit to SysAdmin:
 
Python Lab 7: Using the os system package to run system commands in your bash system.

Python to manage users by creating a function

See [7-1.py](7-1.py)

Asks the user to continue adding users as long as they keep answering “n” to the prompt.
The program is then run in a Linux program which you can tell by after os.system with code having ‘sudo’.
The prompt needs to be improved, it is not asking “Do you want to stop removing users” or remove you out of the while loop once you have created the new user.


Activity 7-1:
Created an add_user_to_group

After clearing up the many syntax errors, it seems like the code worked. You used your ‘usermod’ and it gave out the manual of how to use the ‘usermod.’

Overview of Github markdown ‘how to’:
https://guides.github.com/features/mastering-markdown/

Three three functions:
add_user(): User adds to group. [page 11]
remove_user(): Removes user either Y or N. [page 9]
add_user_group():Add user and uses the os.system package

Errors: 
Not well defined prompts
Many syntax errors

How would we use the functions:
Use the created functions as how they are meant to be created, usage could vary depending on need of the network
When we have to maintain Linux users within the network. The admin could use CodeDeploy to maintain the users. Example: A lead from HR would like to create and deploy a new user/group from any location within a network. The SysAdmin would give privileges to the individual(s) to help maintain the users/groups. 

Python 7-2: Handling Packages
Discussion: IORr means install or remove packages and check the user input then depending on the input will remove from the loop or keep them in the loop, if valid. 
While True: It will continue it breaks
Tell us what to install or install default packages
Purpose: Install or uninstall a package
elif iOrR == “remove” at this point can only use remove
Purge is manually uninstalling a package and autoremove will remove the “older” that is no longer used
clean: clean clears out the local repository of retrieved package files. It removes everything but the lock file from /var/cache/apt/archives/ and /var/cache/apt/archives/partial/. When APT is used as a dselect(1) method, clean is run automatically. Those who do not use dselect will likely want to run apt-get clean from time to time to free up disk space.
autoclean: Like clean, autoclean clears out the local repository of retrieved package files. The difference is that it only removes package files that can no longer be downloaded, and are largely useless. This allows a cache to be maintained over a long period without it growing out of control. The configuration option APT::Clean-Installed will prevent installed packages from being erased if it is set to off.
autoremove: is used to remove packages that were automatically installed to satisfy dependencies for some package and that are no more needed.

Packages:
Gimp:GIMP is a cross-platform image editor available for GNU/Linux, OS X, Windows and more operating systems.
Thunderbird Mozilla Thunderbird is an open source, cross-platform email client, developed by the Mozilla Foundation. ... Email can work with Thunderbird mail storage structures. The MboxrdStorageReader class lets developers read messages from Mozilla Thunderbird's mail storage file.:
Pidgin :Pidgin is a chat program which lets you log into accounts on multiple chat networks simultaneously.

We are now trying to install the above packages using the package handling code.
The code: https://pastebin.com/RhQvGk70


Take two:
yum needs to be added.


Take Three WORKED for installing packages:

 Yum does not have a purge switch like apt does:


He said not to purge:



Difference between forks and branches:
https://yangsu.github.io/pull-request-tutorial/#:~:text=Pull%20requests%20let%20you%20tell,follow%2Dup%20commits%20if%20necessary.
A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project. Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.
The main key word is: contributor. There are more privileges to being a contributor. 
Limited privileges to push, so pull gives it to someone else to push it.

Potential: 
Code >> Fork >> Pull >> Source Code

Os.system subprocess:
os.system() vs. subprocess.run():
System: directly ask the system to run system
Subprocess runs small program instead of going to the shell
Shell injection variables, subprocess is more secure than os.system: https://docs.python.org/3/library/subprocess.html#security-considerations
Slide 33: Safety and separate process (gives you more control with the process to see if it is running with termination rights)
Popen: 
Random note: The Great Suspender to put tabs to sleeps

Lab 7:
args: argument to take in
https://docs.python.org/2/library/subprocess.html
Using the f’string to run the code


Change name of document within vi:

You can run a bash script with a Python script:



Lab 7 Debrief:
os.system: List files in one line
System.run: List files in one file
No difference

Group (Christian) Challenge: Using subprocess.run, let the user run a bash command with as many arguments as they want (for example, (touch file1 file2 file3 file4)).
Get the user input
What is required for the solution?

Group:
Issue was that a variable was in a local variable and not a global variable

Question Marks:
Need to pass all the ones that you failed
Every Monday need to have the week completed

