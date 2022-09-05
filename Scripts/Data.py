MAINPATH = "C:\\Users\\a3210\\Convergence\\Samba\\"
DOWNLOADPATH = "C:\\Users\\a3210\\downloads"
MONDAYINPUTPATH = MAINPATH + "Board_Input\\"
MONDAYOUTPUTPATH = MAINPATH + "Board_Output\\"
APPLOIINPUTPATH = MAINPATH + "Apploi_Input\\"

columns = {
    "Name": 1,
    "Recruiter": 2,
    "Status": 3,
    "Position": 4,
    "State": 5,
    "State Abbreviation": 6,
    "Application Date": 7,
    "Creation Date": 8,
    "Hired Date": 9,
    "Hire Week Number": 10,
    "Week Start": 11,
    "Week of": 12
}

StatusOrder = {
    "Hired": 1,
    "Onboarding": 2,
    "Progressing": 3,
    "New": 4
}

RowTitles = [
    "Onboarding Issue", 
    "Onboarding", 
    "Hired", 
    "Progressing"
    ]

Apploi_Download_Settings = (
    '.csv',
    ['widget']
)

Title_Ext_Dict = {
    'Onboarding': '.xlsx',
    'Progressing': '.xlsx',
    'widget': '.csv'
}

Monday_Download_Settings = (
    '.xlsx',
    ['Onboarding', 'Progressing']
)

us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}
    
# invert the dictionary
abbrev_to_us_state = dict(map(reversed, us_state_to_abbrev.items()))

Monday_blank_values = {
    "Name": "",
    "Recruiter": "",
    "Status": "",
    "Position": "",
    "State": "",
    "State Abbreviation": "",
    "Application Date": "",
    "Creation Date": "",
    "Hired Date": "",
    "Hire Week Number": "",
    "Week Start": "",
    "Week of": ""
    }

Apploi_blank_values = {
    "Team Name": "",
    "Email": "",
    "First Name": "",
    "Last Name": "",
    "Phone Number": "",
    "Job Name": "",
    "Application Date": "",
    "Applicant Status": "",
    "Zip Code": "",
    "City": "",
    "State": "",
    "Notes": "",
    "First Outreach Date": "",
    "Interview Date": ""
}

date_columns = [
    "Application Date",
    "Creation Date",
    "Hired Date"
]

state_by_recruiter = {
    "Ohio": "Charlie Cohen",
    "Maryland": "Charlie Cohen",
    "Virginia": "Charlie Cohen",
    "Indiana": "Charlie Cohen",
    "Michigan": "Charlie Cohen",
    "West Virginia": "Charlie Cohen",
    "Delaware": "Charlie Cohen",
    "Pennsylvania": "Tali Cohen",
    "Florida": "Tali Cohen",
    "Rhode Island": "Tali Cohen",
    "Connecticut": "Tali Cohen",
    "Massachusetts": "Tali Cohen",
    "Texas": "Tali Cohen",
    "New Hampshire": "Tali Cohen",
    "New Jersey": "Elisheva Walfish",
    "New York": "Elisheva Walfish"
}
