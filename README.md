# android_utility

This program requires the libraries Numpy, Pandas, and Beautiful Soup

This program is intended to install, unistall, and gather apk and device information

It can also process this information into a csv file

The commands are:
<br> i - install this will install all apks in the apk folder to the devices connected
<br> u - uninstall this will remove all non-system apps from all devices connected
<br> p - process compiles apk information and writes them to a csv file
<br> g - get device info, will gather connected device information and print them to the console
<br> d - will do the same thing as the command above but will be modified to just return device serial numbers
<br> e - will close the adb server and exit the program

For this program to work you must change the directory in Main.py to the directory where the apk's you intend to install are located
Bundle tool (and android development tool) must be put into the apk directory and renamed bundletool-all
The tool can be downloaded here: 
<br>https://developer.android.com/studio/command-line/bundletool

This program also requires that you have the environment varibles for android development tool set in windows. The version of these tool may vary.
For example:
<br>..\AppData\Local\Android\Sdk\build-tools\32.0.0
<br>..\AppData\Local\Android\Sdk\platform-tools
  
Android developement tools can be installed by going to https://developer.android.com/studio and with Android Studio the tools should also be installed

If you have trouble with the use of this program please reach out and I will get back with you
