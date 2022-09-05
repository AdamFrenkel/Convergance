
import typing

import pandas as pd

import Data
import dataframeFuncs as df_funcs
import dateStuff
import tools


def Monday_Sheet_Clean(BoardFileName: str)-> typing.Tuple[pd.DataFrame, str]:
    board_title = BoardFileName.split("_")[0]

    print("processing " + board_title + " board")

    board = df_funcs.ExcelToDataframe(Data.MONDAYINPUTPATH + BoardFileName)

    board = tools.deleteBeginningRows(board)
    board = tools.RenameColumns(board)

    board = df_funcs.deleteBlankRows(board)
    board = df_funcs.deleteTitleRows(board)

    board = tools.deleteGroupTitleRows(board)
    board = tools.replaceMissingValues(board, Data.Monday_blank_values)
    board = tools.AddNewColumns(board, Data.columns)
    board = tools.StateAbbreColumn(board)
    hiredate = "Hired Date"
    board = dateStuff.HireWeekNumberColumn(board, hiredate)
    board = dateStuff.WeekStartColumn(board, hiredate)
    board = dateStuff.WeekOfColumn(board, hiredate)
    board = tools.StatusToProgressing(board)
    board = tools.FormatColumns(board)

    return board, board_title
    

def Apploi_Sheet_Clean(BoardFileName: str)-> typing.Tuple[pd.DataFrame, str]:
    board_title = BoardFileName.split(" ")[0]

    print("processing " + board_title + " board")

    board = df_funcs.CSVtoDataframe(Data.APPLOIINPUTPATH + BoardFileName)

    board = tools.replaceMissingValues(board, Data.Apploi_blank_values)
    board = tools.AddNewColumns(board, Data.columns)
    board = tools.NameColumn(board)
    board = tools.PositionColumn(board)
    board = tools.StatusToNew(board)
    board = tools.CreationDateColumn(board)
    board = tools.StateColumn(board)
    board = tools.FilterByState(board)
    board = tools.RecruiterColumn(board)
    board = tools.StateAbbreColumn(board)
    board = board.drop_duplicates()
    board = tools.FormatColumns(board)
    
    return board, board_title
