import csv
import pandas as pd
import matplotlib.pyplot as mp
import numpy as np

def estimatedState():

    data = pd.read_csv('/home/timi/Documents/DataAnalysisDune/csv/EstimatedState.csv')

    df = pd.DataFrame(data, columns=[" lat (rad)"," lon (rad)", " height (m)"," x (m)"," y (m)"," z (m)"])

    df.plot.scatter(x=" lat (rad)", y=" lon (rad)", c=" height (m)")
    mp.show()

    df.plot.scatter(x=" x (m)", y=" y (m)", c=" z (m)")
    mp.show()

    df1 = pd.DataFrame(data, columns=[" phi (rad)"," theta (rad)"," psi (rad)"])
    df1.plot.line()
    mp.show()

    df2 = pd.DataFrame(data, columns=[" u (m/s)"," v (m/s)"," w (m/s)"])
    df2.plot.line()
    mp.show()

    df3 = pd.DataFrame(data, columns=[" vx (m/s)"," vy (m/s)"," vz (m/s)"])
    df3.plot.line()
    mp.show()

    df4 = pd.DataFrame(data, columns=[" p (rad/s)"," q (rad/s)"," r (rad/s)"])
    df4.plot.line()
    mp.show()

    df5 = pd.DataFrame(data, columns=[" depth (m)"," alt (m)"])
    df5.plot.line()
    mp.show()

if __name__ == '__main__':
    estimatedState()