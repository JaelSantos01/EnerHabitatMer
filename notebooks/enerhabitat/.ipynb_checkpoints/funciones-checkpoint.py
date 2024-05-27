from iertools.read import read_epw
import pandas as pd
import matplotlib.pyplot as plt
from dateutil.parser import parse  


def carga_epw(f_epw):
    epw = read_epw(f_epw,alias=True,year=2024)
    return epw

def grafica_mes(epw,mes,dia="15"):
    fig, ax = plt.subplots(figsize=(10,3))
    f1 = parse(f"2024-{mes}-{dia}")
    f2 = f1 + pd.Timedelta("7D")

    ax.plot(epw.To,label="Ta")
    ax.set_xlim(f1,f2)