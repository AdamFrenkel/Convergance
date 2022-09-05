import re
import pandas as pd
import Data

def ExcelToDataframe(filename: str)-> pd.DataFrame:
    '''convert an excel file to a DataFrame'''
    return pd.read_excel(filename)

def deleteBeginningRows(df: pd.DataFrame)-> pd.DataFrame:
    """remove first row from DataFrame"""

    df.drop([df.index[0]], inplace=True)
    return df    

def RenameColumns(df: pd.DataFrame)-> pd.DataFrame:
    """
    rename columns of DataFrame by values in first row
    """

    cols = list(df.iloc[0])
    df.columns = cols
    return df

def replaceMissingValues(df: pd.DataFrame, values: list[str])-> pd.DataFrame:
    df.fillna(value=values, inplace=True)
    return df

def deleteGroupTitleRows(df: pd.DataFrame)-> pd.DataFrame:
    """remove rows that correspond to the group titles"""

    for title in Data.RowTitles:
        df = df[df["Name"].str.contains(title) == False]
        #TODO: refactor to take the column name as a parameter
    return df

def AddNewColumns(df: pd.DataFrame, titles)-> pd.DataFrame:
    for title in titles:
        if title not in df.columns:
            df[title] = ["" for _ in range(df.shape[0])]
    return df

def StateAbbreColumn(df: pd.DataFrame)-> pd.DataFrame:
    df["State"] = [value.split(', ')[1] if ', ' in value else value for value in df["State"]]
    df["State Abbreviation"] = [Data.us_state_to_abbrev[value] if value is not "" else "" for value in df["State"]]
    return df

def FormatColumns(df: pd.DataFrame)-> pd.DataFrame:
    """sort and filter the columns by the correct order"""
    formatlist = list(Data.columns.keys())

    #removing the columns that are not in the correct format
    cols = [value for value in df.columns if value in formatlist]

    #sorting the columns by the correct format order
    cols.sort(key=lambda x: Data.columns[x])

    #reordering the board by the correct column order
    df = df[cols]
    return df

def StatusToProgressing(df: pd.DataFrame)-> pd.DataFrame:
    df["Status"] = df["Status"].apply(lambda x: "Progressing" if x in ["Completed", "Issue"] else x)
    return df

def NameColumn(df: pd.DataFrame)-> pd.DataFrame:
    [print(value, type(value)) for value in df["First Name"] if type(value) is not str]
    first_names = [value.title().strip() for value in df["First Name"]]
    last_names = [value.title().strip() for value in df["Last Name"]]
    df["Name"] = [value[0] + ' ' + value[1] for value in zip(first_names, last_names)]
    return df

def PositionColumn(df: pd.DataFrame)-> pd.DataFrame:
    df["Position"] = [CleanPosition(value) for value in df["Job Name"]]
    return df

def CreationDateColumn(df: pd.DataFrame)-> pd.DataFrame:
    df["Creation Date"] = df["Application Date"]
    return df

def FilterByState(df: pd.DataFrame)-> pd.DataFrame:
    df = df[df["State"].isin(Data.state_by_recruiter.keys())]
    return df

def StateColumn(df: pd.DataFrame)-> pd.DataFrame:
    df["State"] = [CleanState(value[0], value[1]) for value in zip(df["State"], df["City"])]
    return df

def CleanState(text: str, city: str)-> str:
    """return the state in correct format according to the text of the state"""
    text = text.strip()
    #if the state is the abbreviation of a state
    if text.upper() in Data.abbrev_to_us_state.keys():
        return Data.abbrev_to_us_state[text.upper()]
    #if the state is the name of a state
    elif text.title() in Data.us_state_to_abbrev.keys():
        return text.title()
    #if the text is blank, and the city has the state in it
    if len(city.split()) > 1 and city.split()[-1].upper() in Data.abbrev_to_us_state.keys():
        return Data.abbrev_to_us_state[city.split()[-1].upper()]
    #if city is the abbreviation of a state
    if city.title() in Data.us_state_to_abbrev.keys():
        return city.title()
    #if the text is a single word
    if ' ' not in text.strip():
        #if the text is the abbreviation of a state with extra punctuation
        s = re.sub(r'[^a-zA-Z ]', '', text)
        if s.upper() in Data.abbrev_to_us_state.keys():
            return Data.abbrev_to_us_state[s.upper()]
        #if the text is the name of a state with extra punctuation
        if s.title() in Data.us_state_to_abbrev.keys():
            return Data.us_state_to_abbrev[s.title()]
        if s.title() == "Conneticut": return "Connecticut"
    if len(text.split()) > 1:
        words = text.split()
        state = words[-1]
        if state.upper() in Data.abbrev_to_us_state.keys():
            return Data.abbrev_to_us_state[state.upper()]
    if text == "":
        return ""
    # print(text + " /X/ " + city)
    return ""

def RecruiterColumn(df: pd.DataFrame)-> pd.DataFrame:
    df["Recruiter"] = [RecruiterByState(value) for value in df["State"]]
    return df

def RecruiterByState(state: str)-> str:
    return Data.state_by_recruiter[state] if state in Data.state_by_recruiter.keys() else ""

def StatusToNew(df: pd.DataFrame)-> pd.DataFrame:
    df["Status"] = df["Status"].apply(lambda _: "New")
    return df

def CleanPosition(pos: str)-> str:
    if pos.find('/') != -1 and (pos.find("na") != -1 or pos.find("NA") != -1):
        return "Nurses and Aides"
    elif pos.find('/') != -1 and pos.find("na") == -1 and pos.find("NA") == -1:
        return "RN/LPN"
    elif pos.find("RN") != -1 or pos.find("rn") != -1:
        return "RN"
    elif pos.find("Registered N") != -1:
        return "RN"
    elif pos.find("LPN") != -1:
        return "LPN"
    elif pos.find("Licensed P") != -1:
        return "LPN"
    elif pos.find("CNA") != -1:
        return "CNA"
    elif pos.find("Certified N") != -1:
        return "CNA"
    elif pos.find("GNA") != -1:
        return "GNA"
    elif pos.find("Geriatric N") != -1:
        return "GNA"
    elif pos.find("STNA") != -1:
        return "STNA"
    elif pos.find("State Tested") != -1:
        return "STNA"
    elif pos.find("QMA") != -1:
        return "QMA"
    elif pos.find("Qualified M") != -1:
        return "QMA"
    elif pos.find("CMA") != -1:
        return "CMA"
    elif pos.find("Certified M") != -1:
        return "CMA"
    else:
        return "Not Relevant"

def RemoveDuplicates(df: pd.DataFrame)-> pd.DataFrame:
    sortedFrame = SortByStatus(df)
    filteredFrame = sortedFrame.drop_duplicates(subset=["Name"])
    return filteredFrame

def SortByStatus(df: pd.DataFrame)-> pd.DataFrame:
    df.sort_values(by=["Status"], key=lambda x: x.map(Data.StatusOrder), inplace=True)
    return df