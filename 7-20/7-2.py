import os
def install_or_remove_packages():
    while True:
        print("Would you like to install or remove packages? (I/R)")
        iOrR = str(input("")).upper()
        if iOrR == "I":
            iOrR = "install"
            break
        elif iOrR == "R":
            iOrR = "remove"
            break
    print("Please input a list of packages to install")
    print("The list should be seperated by spaces, e.g: ")
    print(" firefox gimp libreoffice")
    print("Otherwise, input 'default' to " + iOrR + " the default packages listed in this program")
    packages = str(input("")).lower()
    if packages == "default":
        #defaultPackages will vary depending on needs of the user/system
        packages = ''
        #packages = defaultPackages
    if iOrR == "install":
        os.system("sudo yum install " + packages)
    elif iOrR == "remove":
        #yum does not have a --purge switch
        os.system("sudo yum " + iOrR + " " + packages)
        #while True:
            # print("Purge files after removing? (Y/N)")
            # choice = str(input("")).upper()
            # if choice == "Y":

            #     os.system("sudo yum --purge " + iOrR + " " + packages)
            #     break
            # elif choice == "N":
            #     os.system("sudo yum " + iOrR + " " + packages)
            #     break
            # os.system("sudo apt autoremove")
def clean_environment():
    os.system("sudo yum autoremove")
    #yum does not have autoclean
    #os.system("sudo yum autoclean")
def update_environment():
    os.system("sudo yum update")
    os.system("sudo yum upgrade")
    #yum does not have dist-upgrade or equivalent as far as I could tell
    #os.system("sudo yum dist-upgrade")
install_or_remove_packages()