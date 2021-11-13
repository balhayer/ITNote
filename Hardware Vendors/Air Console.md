# Installation

- Get driver from this link: http://support.get-console.com/support/solutions/articles/5000501221-airconsole-osx-drivers
- Install it, need to allow in System Preference and reinstall
- Check for the presence of the file /dev/cu.Airconsole-1 to verify that the driver has loaded correctly. If not:
- Load driver: sudo kextload /Library/Extensions/Airconsole.kext
- Open AirconsoleOSX in Application Folder and connect to use

# Using Screen to access console

- screen /dev/tty.Airconsole-1
- screen -r to list sessions
- Ctrl_a, Ctrl_\ to quit

# Using WIFI to connect to Airconsole has the same defaults regardless of operating system:

– SSID = Airconsole-XX where XX is the last 2 digits of units Mac Address
– Password = 12345678
– Authentication = WPA2 Pre shared Key
– 2.4Ghz band
– IP: 192.168.10.1
– Credential: admin/admin

# Using Ethernet – connect Airconsole to LAN or directly to PC/Mac via Ethernet cable. Airconsole operates by default as DHCP server so will allocate client an IP address 192.168.10.x

- Browse to Airconsole’s Web terminal at http://192.168.10.1/terminal.asp
- Other settings are the same as Wifi

# Uninstallation

- The installer has created two packages that need to be deleted
– a kernel level driver at /Library/Extensions/Airconsole.kext
– a user mode application at /Applications/AirconsoleOSX.app

1. Ensure that the driver has been unloaded – this can be done by opening a terminal prompt and entering the following
sudo kextunload /Library/Extensions/Airconsole.kext
2. Delete the driver file using the command
sudo rm -rf /Library/Extensions/Airconsole.kext
3. Delete the AirconsoleOSX file by dragging it to the Trash icon from Finder

# Reference

- https://semfionetworks.com/blog/easily-use-airconsole-on-macosx/
- http://support.get-console.com/support/solutions/articles/5000768313-installing-uninstalling-macos-drivers-on-high-sierra-10-13-
- https://pbxbook.com/other/mac-tty.html
- http://support.get-console.com/support/solutions/articles/5000503419-troubleshooting-process-and-flowchart-for-serial-connectivity