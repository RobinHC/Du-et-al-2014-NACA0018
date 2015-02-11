import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")

def plot(name):
    df = pd.read_csv("closed-jet_{}.csv".format(name))
    plt.plot(df.alpha, df.cl/df.cd, "-o", label="$Re = {}$".format(name))
    
def main():
    names = ["6e4", "1e5", "1.4e5"]
    for name in names:
        plot(name)
    plt.xlabel(r"$\alpha$")
    plt.ylabel("$C_l/C_d$")
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    main()