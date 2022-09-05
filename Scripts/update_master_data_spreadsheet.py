import glob
import os
import shutil
import time
from datetime import datetime

import Data
import download_boards as download_funcs
import formatboards


def update_master_data():
    driver = Initialize_Master_Data()

    print("downloaded boards: ", datetime.now().strftime("%H:%M:%S"))

    waittimeMin = Update_Process()
    System_Sleep(waittimeMin)

    while True:
        Empty_Folder_System()
        success = True
        try:
            Download_Boards(driver)
            print("initiated download: ", datetime.now().strftime("%H:%M:%S"))
        except Exception:
            success = False
            print("Master Data not updated")
        if success:
            waittimeMin = Update_Process()
            System_Sleep(waittimeMin)
        else:
            System_Sleep()

def Initialize_Master_Data():
    Empty_Folder_System()
    driver = download_funcs.Start_System()
    download_funcs.OpenMondayPage(driver)
    download_funcs.Monday_Process(driver)
    download_funcs.OpenApploiWindow(driver)
    time.sleep(5)
    download_funcs.download_Apploi_Sheet(driver)
    
    return driver

def Update_Process()-> float:
    waitTimeMin, downloaded = Wait_Until_Files_Downloaded(Data.Title_Ext_Dict, Data.DOWNLOADPATH)
    if downloaded:
        MoveFilesToFolder(Data.MONDAYINPUTPATH, Data.DOWNLOADPATH, *Data.Monday_Download_Settings)
        MoveFilesToFolder(Data.APPLOIINPUTPATH, Data.DOWNLOADPATH, *Data.Apploi_Download_Settings)
        print("moved files: ", datetime.now().strftime("%H:%M:%S"))

        folderpath = formatboards.Format_Boards()
        formatboards.Update_Master_Date(folderpath)
        print("Master Data updated at: ", datetime.now().strftime("%H:%M:%S"))
    
    return waitTimeMin

def Download_Boards(driver):
    driver.switch_to.window(driver.window_handles[0])
    download_funcs.Monday_Process(driver)
    driver.switch_to.window(driver.window_handles[1])
    download_funcs.download_Apploi_Sheet(driver)

def System_Sleep(waitTimeMin: float = 0):
    remaining_wait_time = 15 - waitTimeMin
    print(f"waiting for {remaining_wait_time} minutes")
    time.sleep(remaining_wait_time * 60)

def Wait_Until_Files_Downloaded(titleExtList: dict[str, str], downloadPath: str)-> tuple[float, bool]:
    downloaded = False
    waitTime = 0
    while not downloaded:
        #if fifteen minutes have passed and the files havent downloaded,
        #end the checking process
        if waitTime == 15:
            return waitTime, False
        print(f"waiting: {waitTime * 60}")
        time.sleep(30)
        waitTime += .5
        downloaded = Check_Files_Downloaded(titleExtList, downloadPath)
    print(f"files downloaded: {waitTime * 60}")
    return waitTime, True

def Check_Files_Downloaded(titleExtList: dict[str, str], downloadPath: str)-> bool:
    for title, ext in titleExtList.items():
        files = FilesInFolder(downloadPath, ext)
        desired_file = [file for file in files if title in file]
        
        if len(desired_file) == 0:
            return False
    return True

def MoveFilesToFolder(folderpath: str, downloadPath: str, fileExtension: str, fileTitles: list[str]):
    files = FilesInFolder(downloadPath, fileExtension)
    last_files = []
    for file_title in fileTitles:
        last_files += [[file for file in files if file_title in file][0]]

    for file in last_files:
        print(file)
        shutil.move(file, folderpath)

def FilesInFolder(downloadPath: str, fileExtension: str):
    pattern = r"{}".format(downloadPath + "\*" + fileExtension)
    files = list(filter(os.path.isfile, glob.glob(pattern)))
    # sort files by creation 
    files.sort(key=lambda x: os.path.getmtime(x))
    return files

def Clear_Download_Folder(downloadPath: str, titleExtList: dict[str, str]):
    for title, ext in titleExtList.items():
        files = FilesInFolder(downloadPath, ext)
        desired_files = [file for file in files if title in file]
        [os.remove(file) for file in desired_files]

def Empty_Folder_System():
    EmptyFolder(Data.MONDAYOUTPUTPATH)
    EmptyFolder(Data.APPLOIINPUTPATH)
    EmptyFolder(Data.MONDAYINPUTPATH)
    Clear_Download_Folder(Data.DOWNLOADPATH, Data.Title_Ext_Dict)

def EmptyFolder(folder):
    for root, dirs, files in os.walk(folder):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))



update_master_data()
