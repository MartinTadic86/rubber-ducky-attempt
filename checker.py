import subprocess
import sys
from time import sleep
import psutil
import win32api

def get_drives():
    get_drive = subprocess.getoutput("fsutil fsinfo drives").split(" ")[1:]
    last_drive = get_drive [-1]
    len_drives = get_drive.index(last_drive)
    return len_drives + 1


while true :
    for drive in range(0, get_drives())
        try:
            removable = psutil.disk_partitions()[drive][3].split(",")[1]

            if "removable" in removable:
                disk_name = psutil.disk_partitions()[drive][1]
                disk_label = win32api.GetVolumeInformation(f"{disk_name}\\")[0]

                if disk_label =="péro":
                    print("find Drive :) -> name: "+ str(disk_label))
                    os.system("start {disk_name}rubber ducky.py")
                    sys.exit()

        expect IndexError:
            pass
    sleep(2)