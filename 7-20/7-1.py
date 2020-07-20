import os
import subprocess
def new_user():
  confirm = "N"
  while confirm != "Y":
    username = str(input("Please enter the name of the user to add: "))
    print("Use the username '" + username + "'? (Y/N)")
    confirm = str(input("")).upper()
    os.system("sudo useradd " + username)
def remove_user():
    confirm = "N"
    while confirm != "Y":
        username = str(input("Please enter the name of the user to remove: "))
        print("Remove the user : '" + username + "'? (Y/N)")
        confirm = str(input("")).upper()
        os.system("sudo userdel -r " + username)
def add_user_to_group():
    username = str(input("Please enter the name of the user that you wish to add to a group: "))
    output = str(subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0])
    print("Please input a list of groups to add the user to")
    print("The list should be separated by spaces, e.g:\r\n group1 group2 group3")
    print("The available groups are:\r\n " + output)
    chosenGroups = str(input("Groups: "))
    output = output.split(" ")
    chosenGroups = chosenGroups.split(" ")
    print("Add To:")
    found = True
    groupString = ""
    for grp in chosenGroups:
        for existingGrp in output:
            if grp == existingGrp:
                found = True
                print("-Existing Group : " + grp)
                groupString = groupString + grp + ","
        if found == False:
            print("-New Group : " + grp)
            groupString = groupString + grp + ","
        else:
            found = False
        groupString = groupString[:-1] + " "
        while True:
            print("Add user '" + username + "' to the groups above? (Y/N)")
            confirm = str(input("")).upper()
            if confirm == "N":
                break
            if confirm == "Y":
                os.system("sudo usermod -aG " + groupString + username)
                break
# new_user()
# remove_user()
add_user_to_group()

