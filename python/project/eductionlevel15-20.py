import csv
import pandas as pd
import io
import requests
import matplotlib.pyplot as plt

url = " http://www.edb.gov.hk/attachment/en/about-edb/publications-stat/figures/educational-attainment.csv"


urlData = requests.get(url)
df = pd.read_csv(io.StringIO(urlData.text))
dfc = df.drop(columns = ['Type','Row']).drop([5])

dfc.plot.line()

ax = df.plot(x='Description')
ax.set_yscale('linear')
plt.show()