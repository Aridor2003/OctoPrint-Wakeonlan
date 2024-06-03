# OctoPrint Wake-on-LAN Plugin

An OctoPrint PlugIn letting you turn on your computer from anywhere using a raspberry pi.
To use the PlugIn just download the zip and install using the plugin Manager and input your Mac address in the settings

Overview:
The OctoPrint Wake-on-LAN (WoL) Plugin adds the capability to send Wake-on-LAN packets to designated devices directly from the OctoPrint interface. This is useful for waking up networked devices such as printers or computers before starting a print job.

Features:
Send Wake-on-LAN packets with a click of a button.
Configure MAC addresses for target devices.
Easy-to-use interface integrated into OctoPrint.
Installation
Prerequisites
OctoPrint instance up and running.
Networked device(s) with Wake-on-LAN capability enabled.
Installation Steps
Download the Plugin: Download the plugin package (OctoPrint-Wakeonlan.zip).

Upload Plugin via OctoPrint Web Interface:

Open your web browser and go to your OctoPrint web interface.
Navigate to Settings > Plugin Manager.
Click on Get More... and then ...from an uploaded file.
Select and upload the wake_on_lan.zip file.
Restart OctoPrint:

After the plugin is uploaded, OctoPrint will prompt you to restart.
Click Restart Now to apply the changes.
Configuration
Access Plugin Settings:

Go to Settings > Wake-on-LAN.
Add Devices:

Enter the MAC address of the device you want to wake up.

Save Settings:

Click Save to store the device configuration.
Usage
Wake Device:

In the OctoPrint interface, navigate to the Wake-on-LAN tab.
Click the Wake button next to the device you want to wake up.
Monitor Status:

Ensure the target device powers on and is ready for use.
Troubleshooting
Device Not Waking Up:
Verify the MAC address is correct.
Ensure Wake-on-LAN is enabled on the target device.
Check network configuration and ensure the device is reachable.
Contributing
Contributions are welcome! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request on GitHub.

License:
This project is licensed under the AGPL3 commercial use License. See the LICENSE file for details.

Acknowledgments:
This project was done with tremendous help from [itay zelikovich](https://github.com/zelikit) and [jneilliii](https://github.com/jneilliii) ,Thank you!
