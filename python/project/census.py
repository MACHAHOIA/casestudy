# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 10:09:26 2021

@author: ahoia
"""

import csv
import pandas as pd
import io
import requests
import matplotlib.pyplot as plt
import urllib3

url = " https://www.censtatd.gov.hk/en/EIndexbySubject.html?pcode=D5211601&scode=459&file=D5211601E2016XXXXE.xlsx"


df = pd.read_excel(url,sheet_name=0,header=1)

df.head()