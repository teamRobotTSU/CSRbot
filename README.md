CSRbot setup instructions
*************************
Complete the setup instructions here.  This will also go into chapter 5.  After following these instructions the user should have all necessary packages and dependencies on their robot and be able to run the robot.py script.

1.  run raspi-config to enable the raspicam, ssh, login options, and change localization settings (screenshots)
2.  reboot
3.  login in and enable wi-fi
4.  open a terminal and type: pwd (print working directory)
      you should see something like /home/pi or /home/yourUserName
5.  Next type: ls (lowercase L, list)
      you should see an output listing the contents of the current working directory
5.  type: git clone https://github.com/teamrobottsu/csrbot.git and then type ls again
      you should now see a folder "csrbot" in your directory. 
6.  type: cd csrbot (change directory).  See what pwd and ls commands show now.
7.  type: cd pi (then press tab before pressing enter) remember tab completion!!!
8.  We need to run the piSetup.sh,
      any file that ends with .sh means it is a "shell" file, and can be executed from
      the shell.  This is equivelant to double clicking on a program in Windows.
9.  First, make it executable by typing: sudo chmod +x piSetup.sh
      if prompted for your password, enter it.  "sudo" in linux is equivalent to running
      something as an administrator, or Super User in linux terms. to find out what 
      chmod does (or anything else for the matter) type: man chmod (man = manual)
10. Now to execute this file, or any other executable file from the shell, type:
      ./piSetup.sh and wait for the script to finish.  This script installs the following:
          - package 1 
          - package 2
          - package 3
          - package n
11. Reboot your pi.  
12. With a correctly assembled robot, open a terminal, navigate to the robot-api folder in the
      csrbot directory, and type: sudo python3 robot.py to verify complete functionality (see
      keymap.txt for the list of controls).

______________________________________________________________________________________________________________
The non-pi-setup-scripts are tested for linux ubuntu 14.X and 16.X

To verify opencv was properly built, open a terminal and run python3, after the >>> type import cv2, then type print(cv2.__version__) and you should get 3.1.0 returned

To verify tensorflow was properly built, in the same python3 terminal type import tensorflow as tf and then type print(tf.__version__) and you should get 0.12.1 or similar
