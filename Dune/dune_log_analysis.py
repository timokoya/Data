import csv
import pandas as pd
import matplotlib.pyplot as mp

#################
# SOUND SPEED   
#################
def soundSpeed():
    data = pd.read_csv('/home/timi/Documents/DataAnalysisDune/csv/SoundSpeed.csv', nrows=1000)
    df = pd.DataFrame(data, columns=[" value (m/s)"])
    df.plot.line(title="SOUND SPEED")
    mp.show()

##############################
# ALLOCATED CONTROL TORQUE   
##############################
def AllocatedControlTorques():
    data = pd.read_csv('/home/timi/Documents/DataAnalysisDune/csv/AllocatedControlTorques.csv')
    df = pd.DataFrame(data, columns=[" k (nm)"," m (nm)"," n (nm)"])
    df.plot.line(title="ALLOCATED CONTROL TORQUE")
    mp.show()

####################
# CONTROL PARCEL   
####################
def ControlParcel():
    data = pd.read_csv('/home/timi/Documents/DataAnalysisDune/csv/ControlParcel.csv', nrows=1000)
    df = pd.DataFrame(data, columns=[" p"," i"," d", " a"])
    df.plot.line(title="CONTROL PARCEL")
    mp.show()

##############
# DISTANCE   
##############
def Distance():
    data = pd.read_csv('/home/timi/Documents/DataAnalysisDune/csv/Distance.csv', nrows=1000)
    df = pd.DataFrame(data, columns=[" value (m)"])
    df.plot.line(title="DISTANCE")
    mp.show()

##############
# ANNOUNCE   
##############
def Announce():
    data = pd.read_csv('/home/timi/Documents/DataAnalysisDune/csv/Announce.csv', nrows=1000)
    df = pd.DataFrame(data, columns=[" lat (rad)"," lon (rad)", " height (m)"])
    df.plot.scatter(x=" lat (rad)", y=" lon (rad)", c=" height (m)")
    mp.show()

###########
# GoTo    
###########
def GoTo():
    data = pd.read_csv('/home/timi/Documents/DataAnalysisDune/csv/Goto.csv', nrows=1000)
    df = pd.DataFrame(data, columns=[" lat (rad)"," lon (rad)", " z (m)"])
    df.plot.scatter(x=" lat (rad)", y=" lon (rad)", c=" z (m)")
    mp.show()

##############
# GPS FIX    
##############
def GpsFix():
    data = pd.read_csv('/home/timi/Documents/DataAnalysisDune/csv/GpsFix.csv')
    df = pd.DataFrame(data, columns=[" lat (rad)"," lon (rad)", " height (m)"])
    df.plot.scatter(x=" lat (rad)", y=" lon (rad)", c=" height (m)")
    mp.show()

####################
# DESIRED SPEED    
####################
def DesiredSpeed():
    data = pd.read_csv('/home/timi/Documents/DataAnalysisDune/csv/DesiredSpeed.csv')
    df = pd.DataFrame(data, columns=[" value"])
    df.plot.line(title="DESIRED SPEED")
    mp.show()

####################
# SERVO POSITION   
####################
def ServoPosition():
    data = pd.read_csv('/home/timi/Documents/DataAnalysisDune/csv/ServoPosition.csv')
    df = pd.DataFrame(data, columns=[" value (rad)"])
    df.plot.line(title="Servo Position")
    mp.show()

##########################
# SetThrusterActuation   
##########################
def SetThrusterActuation():
    data = pd.read_csv('/home/timi/Documents/DataAnalysisDune/csv/SetThrusterActuation.csv')
    df = pd.DataFrame(data, columns=[" value"])
    df.plot.line(title="Set Thruster Actuation")
    mp.show()

####################
# Water Velocity   
####################
def WaterVelocity():
    data = pd.read_csv('/home/timi/Documents/DataAnalysisDune/csv/WaterVelocity.csv')
    df = pd.DataFrame(data, columns=["  x (m/s)"," y (m/s)"," z (m/s)"])
    df.plot.line(title="Water Velocity")
    mp.show()

if __name__ == '__main__':
    soundSpeed()
    AllocatedControlTorques()
    GoTo()
    Announce()
    Distance()
    ControlParcel()
    GpsFix()
    DesiredSpeed()
    ServoPosition()
    SetThrusterActuation()
    WaterVelocity()