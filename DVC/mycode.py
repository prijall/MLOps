import pandas as pd
import os
print("Current working directory:", os.getcwd())
#@ Data Creation:
data={'Name':['Alice', 'Bob', 'Charlie'],
      'Age':[21, 45, 66],
      'City': ['Ktm', 'pkr', 'chtwn']}

df=pd.DataFrame(data)

#new entry:
new_row_loc = {'Name': 'GF1', 'Age': 20, 'City': 'City1'}
df.loc[len(df.index)] = new_row_loc


#@ Checking for data dir:
data_dir='C:/Users/khadk/Desktop/MLOps/MLOPs_Basics/data'
os.makedirs(data_dir, exist_ok=True)

#@ Defining paths:
file_path=os.path.join(data_dir, 'sample_data.csv')

#@ Saving to csv:
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")