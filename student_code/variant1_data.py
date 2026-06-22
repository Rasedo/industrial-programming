import pandas as pd
f = open('C:\\Users\\admin\\Desktop\\data.csv', 'r')
df = pd.read_csv(f)
def proc(d):
    global res
    res = []
    for i in range(len(d)):
        if d['age'][i] > 18:
            res.append(d['name'][i])
proc(df)
print(res)
