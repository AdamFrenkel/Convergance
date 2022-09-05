import datetime
import os
import random

import clean_board as clean
import Data
import dataframeFuncs as dataframe_funcs

import tools


def BoardProcess(filename: str, folderPath: str, fileID: str, type: str):
    clean_board, title = clean.Monday_Sheet_Clean(filename) if type == "Monday" else clean.Apploi_Sheet_Clean(filename)
    print(title)
    dataframe_funcs.SaveFrame(clean_board, title, folderPath, fileID)

def FormatMondayBoards(folderpath: str, fileID: str):
    for dirpath, dirnames, files in os.walk(Data.MONDAYINPUTPATH):
        for file_name in files:
            BoardProcess(file_name, folderpath, fileID, "Monday")

def FormatApploiBoard(folderpath: str, fileID):
    for dirpath, dirnames, files in os.walk(Data.APPLOIINPUTPATH):
        for file_name in files:
            BoardProcess(file_name, folderpath, fileID, "Apploi")

def Format_Boards()-> str:
    rand = str(random.randint(100,1000))
    folderID = str(datetime.date.today()) + '_' + rand
    fileID = folderID + ".xlsx"
    FOLDERPATH = Data.MONDAYOUTPUTPATH + folderID + "\\"
    os.mkdir(FOLDERPATH)
    FormatMondayBoards(FOLDERPATH, fileID)
    FormatApploiBoard(FOLDERPATH, fileID)
    full_board = dataframe_funcs.CombineFrames(FOLDERPATH)
    full_board = tools.RemoveDuplicates(full_board)
    dataframe_funcs.SaveFrame(full_board, "MASTER DATA", FOLDERPATH)
    
    return FOLDERPATH
    
    
def Update_Master_Date(folderpath: str):   
    os.replace(folderpath + "MASTER DATA.xlsx", Data.MAINPATH + "MASTER DATA.xlsx")
