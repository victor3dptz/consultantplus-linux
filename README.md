# consultantplus-linux
Bash scripts to run ConsultantPlus on CentOS (Linux)

Edit file 1rootinstall.sh for your ConsultantPlus Server's IP and shared folder.
Then, edit file "files/cons" and supply your username, password and domain for connecting the server.

Installation is done in 2 steps:
1) Log in as root and run ./1rootinstall.sh, then reboot.
2) Log in as user and run ./2userinstall.sh.

Shortcuts should appear on the desktop and if everything is ok user will be able to run ConsultantPlus in Linux.


Tested on CentOS 6.8 (x86)


