## Check if a library isn't installed 
import sys
import subprocess
import pkg_resources
import json
import os
required = {'pandas','requests','ipython'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    for i in missing:
        print('Please wait while is installed: '+ i)
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

## Import necesary libraries and classes

import pandas as pd
import requests
import time
from IPython.display import display
from Point1 import Point1
from Point2and3 import Point2and3
from sqlite import sqlite
## API Requests:
pd.set_option('display.max_rows', 10)
pd.set_option('precision', 5)
urlpoint1 = "https://restcountries-v1.p.rapidapi.com/all"
urlpoint2 = "https://restcountries.eu/rest/v2/all"
headers = {
    'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
    'x-rapidapi-key': "4e34e06932msh5cf6f7a8474133bp13ee23jsn52a85002c1fd"
    }
## GET API information:

try:
    API_1 = requests.request("GET", urlpoint1, headers=headers).json()
    API_2 = requests.request("GET",urlpoint2).json()
    Point1Class= Point1(API_1)
    Point2and3Class=Point2and3(API_2)
except:
    print("We have a issue to get the information from some URL")


## Processing information:  

Keys=['name','languages']
Columns=['Region','City Name','Languaje','Time']
Table=[]
if 'Point1Class' in globals() and 'Point2and3Class' in globals():
    RegionsOfPoint1=Point1Class._FindDiferentKeys('region',Point1Class.GetAPIRequest())
    for City in RegionsOfPoint1:
        tic = time.time()
        Output=Point2and3Class.OutputToChoose(Input=City,KeyInput='region',KeysOutput=Keys,Subindex='name')
        toc=(time.time()-tic)*1000
        Table.append([City]+Output+ [toc])
    DataBase=sqlite();

    dfTable=pd.DataFrame(data=Table,columns=Columns)
    display(dfTable)
    TotalTime=dfTable['Time'].sum()
    MeanTime=dfTable['Time'].mean()
    MinTime=dfTable['Time'].min()
    MaxTime=dfTable['Time'].max()
    DataBase.IFCreateTable()
    DataBase.InsertFromTable(SumTime=str(TotalTime),MeanTime=str(MeanTime),MinTime=str(MinTime),MaxTime=str(MaxTime))
    JsonPath=os.getcwd()+'\data.json'
    dfTable.to_json(JsonPath)
    print('The total time to build this table is:'+str(TotalTime))
    print('The average time to add a row  in table is:'+str(TotalTime))
    print('The minimal time to add a row  in this table is:'+str(MinTime))
    print('The maximum time to add a row  in this table is:'+str(MaxTime))