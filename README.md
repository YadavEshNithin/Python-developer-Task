# System Information Fetcher

## Overview

The System Information Fetcher is a Python script that retrieves various details about the system it's run on. It provides information on installed software, internet speed, screen resolution, CPU details, GPU details, RAM size, screen size, network details (WiFi/Ethernet MAC address and public IP address), and Windows version.

## Features

- Fetches details about the system, including software, hardware, and network information.
- Provides accurate and relevant information about the system's configuration.
- Easy to use and integrate into your projects.

## Prerequisites

- Python 3.x
- Additional libraries (specified in requirements.txt)

## Installation

1. Clone the repository:

   git clone https://github.com/YadavEshNithin/Python_Task.git


2. Navigate to the project directory:
   
- cd Python_Task
  

3. Install the required libraries:
   
  pip install psutil
  pip install speedtest-cli
  pip install uuid
  pip install pyautogui
  pip install PyQt5
  pip install getmac


5. Run the system_info.py script:
   
- python python_task.py

- The script will display detailed information about the system.

## Details Fetched

- Installed Software's List: Lists all installed software on the system.
- Internet Speed: Measures the download and upload speed of the internet connection.
- Screen Resolution: Provides the screen width and height in pixels.
- CPU Model: Displays the model of the CPU.
- Number of Cores and Threads: Indicates the number of CPU cores and threads.
- GPU Model: Shows the model of the GPU (if available).
- RAM Size: Presents the size of RAM in gigabytes.
- Screen Size: Estimates the physical screen size in inches.
- WiFi/Ethernet MAC Address: Provides the MAC address of the WiFi or Ethernet interface.
- Public IP Address: Displays the public IP address of the system.
- Windows Version: Shows the version of the Windows operating system.
  
## Contributing

- Contributions are welcome! Feel free to open issues or pull requests for improvements, bug fixes, or new features.


--- Thank You ---
