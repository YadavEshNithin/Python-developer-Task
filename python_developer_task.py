import platform
import psutil
import speedtest
import socket
import os
import re
import uuid
import pyautogui
import sys
from PyQt5 import QtWidgets
import subprocess
import getmac




def get_installed_software():
    try:
        installed_software = [line.split('==')[0] for line in os.popen('pip freeze').read().splitlines()]
        return installed_software
    except Exception as e:
        return str(e)

def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  
    upload_speed = st.upload() / 1_000_000  
    return download_speed, upload_speed

def get_screen_resolution():
    try:
        screen_width, screen_height = pyautogui.size()
        return screen_width, screen_height
    except Exception as e:
        return str(e)

def get_cpu_info():
    cpu_info = platform.processor()
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    return cpu_info, cpu_cores, cpu_threads



def get_gpu_info():
    try:
        result = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total,memory.free", "--format=csv,noheader"], capture_output=True, text=True)

        if result.returncode == 0:
            gpu_info = result.stdout.strip().split(',')
            if gpu_info[0]:
                gpu_name, memory_total, memory_free = gpu_info
                return f"Name: {gpu_name}\nTotal Memory: {memory_total}\nFree Memory: {memory_free}"
            else:
                return "No GPU found."
        else:
            return f"Error: {result.stderr.strip()}"
    except Exception as e:
        return str(e)




def get_ram_size():
    ram_size = psutil.virtual_memory().total / (1024 ** 3)  
    return ram_size



def get_screen_size_inches():
    app = QtWidgets.QApplication.instance()

    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    screen = app.primaryScreen()

    if screen is None:
        return "N/A", "N/A", "N/A"

    size = screen.size()
    rect = screen.availableGeometry()

    if QtWidgets.QApplication.startingUp():
        app.exit()

    width_pixels, height_pixels = size.width(), size.height()
    width_inches = width_pixels / 96  
    height_inches = height_pixels / 96  

    return  f"{width_inches:.2f} inch", f"{height_inches:.2f} inch"


    

def get_network_info():
    try:
        mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        public_ip = socket.gethostbyname(socket.gethostname())
        return mac_address, public_ip
    except Exception as e:
        return str(e)
    


def get_windows_version():
    try:
        windows_version = platform.system() + ' ' + platform.version()
        return windows_version
    except Exception as e:
        return str(e)
    





    
    

if __name__ == "__main__":
    print("Installed Software:")
    print(get_installed_software())

    print("\nInternet Speed:")
    download_speed, upload_speed = get_internet_speed()
    print(f"Download Speed: {download_speed} Mbps")
    print(f"Upload Speed: {upload_speed} Mbps")

    print("\nScreen Resolution:")
    screen_width, screen_height = get_screen_resolution()
    print(f"Width: {screen_width}px, Height: {screen_height}px")

    print("\n")
    cpu_info, cpu_cores, cpu_threads = get_cpu_info()
    print(f"CPU Model: {cpu_info}")
    print(f"Number of Cores: {cpu_cores}")
    print(f"Number of Threads: {cpu_threads}")

   
    print("\nGPU Model:")
    print(get_gpu_info())

    print("\nRAM Size:")
    print(f"{get_ram_size()} GB")

    
    print("\nScreen Size in Inches:")
    width_inches, height_inches = get_screen_size_inches()

    print(f"Width: {width_inches} , Height: {height_inches} ")

    

    print("\n")
    mac_address, public_ip = get_network_info()
    print(f"MAC Address: {mac_address}")
    print(f"Public IP Address: {public_ip}")


    print("\nWindows Version:")
    print(get_windows_version())




   

