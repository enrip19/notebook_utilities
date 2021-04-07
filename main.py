#%%
from nbUtilities import csv_reader
csv = csv_reader
#%%
f = csv.csv_file('C:\\Users\\enric\\Documents\\SharedVMFolder\\data\\','20210330')
filenames,headers,data = f.read_csvFiles()
#%%
a = f.extract_data()

# %%

# %%
