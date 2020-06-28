import pandas as pd
f=pd.read_csv("file1.csv")
keep_col = ['gene_id','tracking_id']
new_f = f[keep_col]
new_f.to_csv("output.csv", index=False)


