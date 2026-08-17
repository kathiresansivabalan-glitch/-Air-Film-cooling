
import matplotlib.pyplot as plt
import pandas as pd
##Enable Latex Font
## When running the code it will ask to install some packages
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


data1 = pd.read_csv("F:\Temporay_DATA\Blow_Ratio_M1_05.csv",header=None,skiprows=1)
data_paper1 = pd.read_csv("F:\Temporay_DATA\Blow_Ratio105_PAPER.csv", header=None, skiprows=1)

T = data1.loc[:,12]  # accessing temperature all row
x = data1.loc[:,2]

scale = x/0.008
efftvns = (400-T)/100
paper_eff = data_paper1.loc[:,1]
scale_paper = data_paper1.loc[:,0]
plt.plot(scale,efftvns,label='Present Numerical M105', marker='o',markevery=22)
plt.plot(scale_paper, paper_eff, label='Li and Wang M105',marker='d', markevery =2)
plt.title("Effectiveness Comparison")
plt.xlabel(r"$x/2D$")
plt.ylabel(r"Effectiveness($\eta_o$)")
plt.legend()
plt.show()
