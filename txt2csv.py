import pandas as pd
import numpy as np

def to_csv(fname):
    data1 = np.loadtxt(fname+".txt", unpack=False)
    data2 = np.loadtxt(fname+"-b.txt", unpack=False)
    data3 = np.loadtxt(fname+"-c.txt", unpack=False)
    df_closed = pd.DataFrame()
    df_open = pd.DataFrame()
    df_ref = pd.DataFrame()
    df_closed["alpha"] = data1[:,0]
    df_closed["cl"] = data1[:,1]
    df_closed["cd"] = data1[:,2]
    df_closed.to_csv("closed-jet_{}.csv".format(fname), index=False)
    df_open["alpha"] = data1[:,3]
    df_open["cl"] = data1[:,4]
    df_open["cd"] = data1[:,5]
    df_open2 = pd.DataFrame()
    df_open2["alpha"] = data2[:,0]
    df_open2["cl"] = data2[:,1]
    df_open2["cd"] = data2[:,2]
    df_open = df_open.append(df_open2, ignore_index=True)
    df_open.to_csv("open-jet_{}.csv".format(fname), index=False)
    df_ref["alpha"] = data1[:,6]
    df_ref["cl"] = data1[:,7]
    df_ref["cd"] = data1[:,8]
    df_ref2 = pd.DataFrame()
    df_ref2["alpha"] = data2[:,3]
    df_ref2["cl"] = data2[:,4]
    df_ref2["cd"] = data2[:,5]
    df_ref3 = pd.DataFrame()
    df_ref3["alpha"] = data3[:,0]
    df_ref3["cl"] = data3[:,1]
    df_ref3["cd"] = data3[:,2]
    df_ref = df_ref.append(df_ref2, ignore_index=True)
    df_ref = df_ref.append(df_ref3, ignore_index=True)
    df_ref.to_csv("reference_{}.csv".format(fname), index=False)
    
def main():
    fnames = ["1.4e5", "1e5", "6e4"]
    for f in fnames:
        to_csv(f)
        
if __name__ == "__main__":
    main()