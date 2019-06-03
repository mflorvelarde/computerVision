#!/usr/bin/env python3

from roboviz import Visualizer
from time import time
import numpy as np
import argparse

MAP_SIZE_PIXELS = 800
MAP_SIZE_METERS = 32
SPEED_MPS       = 1

class _MyArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(1)

if __name__ == '__main__':

    # Parse optional command-line arguments
    parser = _MyArgumentParser(description='Visualize a random walk.')
    parser.add_argument('-s', '--seed', help='set seed for pseudo-random number generator')
    cmdargs = parser.parse_args()

    # Set seed for pseudo-random number generator if indicated
    if not cmdargs.seed is None:
        np.random.seed(int(cmdargs.seed))

    # Create a Visualizer object with a trajectory, centered at 0,0

    viz = Visualizer(MAP_SIZE_PIXELS, MAP_SIZE_METERS, 'Random Walk', True)

    # Start in the center of the map with a random heading
    pose = np.array([0,0,360*np.random.random()])

    # Start timing
    prevtime = time()

    # Loop till user closes the display
    while True:

        # Set current pose in visualizer the display, exiting gracefully if user closes it
        if not viz.display(*pose):
            exit(0)

        # Rotate randomly and move forward
        currtime = time()
        s = SPEED_MPS * (currtime - prevtime)
        prevtime = currtime
        theta = np.radians(pose[2])
        pose[0] += s * np.cos(theta)
        pose[1] += s * np.sin(theta)
        pose[2] += 10 * np.random.randn()
