#!/usr/bin/env python3
import datetime
#from datetime import date
import numpy as np
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

aktuellesDatum = datetime.datetime.today()
print(aktuellesDatum)

start = datetime.datetime(2021,2,5) 
end = datetime.datetime.today()
print(end)
apple = web.DataReader("BNTX", "yahoo",end)
print(apple)
apple = web.DataReader("5CV.DE", "yahoo",end)
print(apple)
