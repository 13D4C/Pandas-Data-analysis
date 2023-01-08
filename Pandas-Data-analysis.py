import pandas as pd
//อ่านไฟล์ข้อมูล//
df = pd.read_csv('ไฟล์')
df
//ตรวจดูข้อมูล//
df.head(10)

df = df[['คอลัมน์','คอลัมน์']]
df.head()

df['คอลัมน์'].value_counts()

df.describe()

//สร้างกราฟ//
df['คอลัมน์'].hist()

df['คอลัมน์'].hist(bins=[0, 20, 40, 60, 80, 100, 120])

mydf = df[(df['คอลัมน์'] == 'คอลัมน์') & (df['คอลัมน์'] == '21/8/2021')]
mydf.groupby('คอลัมน์').count()['No.'].plot.bar()

df.info()

df.insert(0, "คอลัมน์", pd.to_datetime(df['คอลัมน์'], format='%d/%m/%Y'), True)
df

df.groupby('date').count()['No.'].plot.line(figsize=(10, 5))
