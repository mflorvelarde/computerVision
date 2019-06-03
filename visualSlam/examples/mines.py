'''
mines.py - classes for the SLAM apparatus used at Paris Mines Tech
'''

from breezyslam.vehicles import WheeledVehicle
from breezyslam.sensors import URG04LX



# Method to load all from file ------------------------------------------------
# Each line in the file has the format:
#
#  TIMESTAMP  ... Q1  Q1 ... Distances
#  (usec)                    (mm)
#  0          ... 2   3  ... 24 ... 
#  
#where Q1, Q2 are odometry values

def load_data(datadir, dataset):
    
    filename = '%s/%s.dat' % (datadir, dataset)
    print('Loading data from %s...' % filename)
    
    fd = open(filename, 'rt')
    
    timestamps = []
    scans = []
    odometries = []
    
    while True:  
        
        s = fd.readline()
        
        if len(s) == 0:
            break       
            
        toks = s.split()[0:-1] # ignore ''

        timestamp = int(toks[0])

        odometry = timestamp, int(toks[2]), int(toks[3])
                        
        lidar = [int(tok) for tok in toks[24:]]

        timestamps.append(timestamp)
        scans.append(lidar)
        odometries.append(odometry)
        
    fd.close()
        
    return timestamps, scans, odometries

class MinesLaser(URG04LX):
    
    def __init__(self):
        
        URG04LX.__init__(self, 70, 145)
        
# Class for MinesRover custom robot ------------------------------------------

class Rover(WheeledVehicle):
    
    def __init__(self):
        
        WheeledVehicle.__init__(self, 77, 165)
        
        self.ticks_per_cycle = 2000
                        
    def __str__(self):
        
        return '<%s ticks_per_cycle=%d>' % (WheeledVehicle.__str__(self), self.ticks_per_cycle)
        
    def computePoseChange(self, odometry):
        
        return WheeledVehicle.computePoseChange(self, odometry[0], odometry[1], odometry[2])

    def extractOdometry(self, timestamp, leftWheel, rightWheel):
                
        # Convert microseconds to seconds, ticks to angles        
        return timestamp / 1e6, \
               self._ticks_to_degrees(leftWheel), \
               self._ticks_to_degrees(rightWheel)
               
    def odometryStr(self, odometry):
        
        return '<timestamp=%d usec leftWheelTicks=%d rightWheelTicks=%d>' % \
               (odometry[0], odometry[1], odometry[2])
               
    def _ticks_to_degrees(self, ticks):
        
        return ticks * (180. / self.ticks_per_cycle)
        
        
        
        
        
