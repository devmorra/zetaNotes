Challenge Lab 1: Bash Scripting Exercise
Duration
This lab takes approximately 55 minutes to complete.

Launch Your Lab Environment
At the top of these instructions, click Start Lab to launch this lab.

A Start Lab panel opens displaying the lab status.

Wait until you see the message "Lab status: ready", then click the X to close the Start Lab panel.

This lab launches an EC2 instance named Linux Host. You will use this server to execute Bash commands and develop Bash scripts.

Click the Details drop down menu above these instructions, and then click Show. Copy the value of the ips -- public field to a text file and save the file as Lab Details.txt, using a text editor such as Atom, Sublime Text or Visual Studio Code. This value is the public IP address of the Linux Host. The information you have saved will be referred to as Lab Details in the lab.

Using SSH to Connect to the Linux Host
 Windows Users: Using SSH to Connect
 These instructions are specifically for Windows users. If you are using macOS or Linux, skip to the next section.

Click the Details drop down menu above the instructions you are currently reading, and then click Show. A Credentials window will be presented.
Click the Download PPK button and save the labsuser.ppk file. Typically your browser will save it to the Downloads directory.
Exit the Details panel by clicking the X.
Download PuTTY to SSH into the Amazon EC2 instance. If you do not have PuTTY installed on your computer, download it here.
Open putty.exe
Configure PuTTY timeout to keep the PuTTY session open for a longer period of time:
Click Connection.
Set Seconds between keepalives to 30.
Configure your PuTTY session:
Click Session.
Host Name (or IP address): Paste the IP address of the Linux Host instance you saved in the Lab Details file earlier.
Back in PuTTY, in the Connection list, expand  SSH
Click Auth (don't expand it).
Click Browse.
Browse to and select the labsuser.ppk file that you downloaded.
Click Open to select it.
Click Open again.
Click Yes, to trust and connect to the host.
When prompted login as, enter: ec2-user. This will connect you to the EC2 instance.
Windows Users: Click here to skip ahead to the next task.

macOS  and Linux  Users
These instructions are specifically for Mac/Linux users. If you are a Windows user, skip ahead to the next task.

Click the Details drop down menu above the instructions you are currently reading, and then click Show. A Credentials window will be presented.

Click the Download PEM button and save the labsuser.pem file.

Exit the Details panel by clicking the X.

Open a terminal window, and change directory cd to the directory where the labsuser.pem file was downloaded. For example, if the labsuser.pem file was saved to your Downloads directory, run this command:

cd ~/Downloads
Change the permissions on the key to be read-only, by running this command:

chmod 400 labsuser.pem
Run the command below (replace <public-ip> with the Linux Host IP address you saved in the Lab Details file earlier).

ssh -i labsuser.pem ec2-user@<public-ip>
Type yes when prompted to allow the first connection to this remote SSH server. Because you are using a key pair for authentication, you will not be prompted for a password.


Your Challenge
Create a directory with a name of <yourName>-<currentDate>.

Write a bash script to:

Create twenty-five empty (0 KB) files (Hint: Use the touch command).
The file names should be <yourName><number>, <yourName><number+1>, <yourName><number+2> and so on.
Design the script so that each time you execute it, it creates the next batch of 25 files with increasing numbers starting with the last or max number that already exists.
Do not hard code these numbers. You need to generate them using automation.
Test the script. Display a long list of the directory and its contents to validate that the script created the expected files.

Save the script and make a note of its location (absolute path) for future reference.

Lab Complete
When you are finished with the lab:

Click End Lab at the top of this page and then click Yes to confirm that you want to end the lab. A panel will appear indicating that "Lab resources are stopping."

Click the X in the top right corner to close the panel. Your lab resources are persisted and accessible to you when you start the lab again.

Errors or corrections? Email us at aws-course-feedback@amazon.com

Other questions? Contact us at https://aws.amazon.com/contact-us/aws-training

©2020 Amazon Web Services, Inc. and its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited.