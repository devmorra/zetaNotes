import subprocess
def runCommand1():
    command=input("What bash command do you want to run? (command + arguments)")
    commandList = command.split()
    subprocess.run(commandList)
def runCommand2():
    command=input("What bash command do you want to run? (command only)")
    arg = "a"
    args =  []
    args.append(command)
    #print(args)
    while arg != "":
        arg = input("With what argument? Or finish by just hitting enter")
        if arg != "":
            args.append(arg)
    #print(args)
    subprocess.run(args)
runCommand1()
runCommand2()
