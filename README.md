# android_utility

This program requires the libraries Numpy, Pandas, and Beautiful Soup

This program is intended to install, unistall, and gather apk and device information

This program also assumes that connected devices are in debug mode with USB debugging enabled

It can also process this information into a csv file

The commands are:
<br> i - install, will sideload all apks in the apk folder to the devices connected
<br> u - uninstall, will remove all non-system apps from all devices connected
<br> p - process compiles apk information and writes them to a csv file
<br> g - get device info, will gather connected device information and print them to the console
<br> d - will do the same thing as the command above but will be modified to return device serial numbers
<br> e - will close the adb server and exit the program

For this program to work you must change the directory in Main.py to the directory where the apk's you intend to install\process are located
<br>Bundle tool (an android development tool) must be put into the apk directory and renamed bundletool-all
The tool can be downloaded here: 
<br>https://developer.android.com/studio/command-line/bundletool

  
Android developement tools can be installed by going to https://developer.android.com/studio and with Android Studio the tools should also be installed

This program also requires that you have the environment varibles for android development tool set in windows. The version of these tools may vary.
For example:
<br>..\AppData\Local\Android\Sdk\build-tools\32.0.0
<br>..\AppData\Local\Android\Sdk\platform-tools

If you have trouble with the use of this program please reach out and I will get back with you
