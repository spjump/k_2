#credits and debits  
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Read Debit and credits to plot
columns = ['Debit', 'Credit', 'Date', 'Category']
df = pd.read_csv(r'C:\Users\spjum_000\OneDrive\Desktop\My Repo\assets\assets.CSV', usecols=columns)
print("Contents in csv file:", df)
plt.plot(df.Debit, df.Credit)
plt.plot(df.Credit)
plt.show()
                    


