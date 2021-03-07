#!/usr/bin/env python2

import numpy as np

if __name__ == "__main__":
    speed_log_filename = "/home/racecar/.ros/speed_log.txt"

    xyz_speeds = np.loadtxt(speed_log_filename)
    average_speeds = np.mean(a=xyz_speeds,
                             axis=0)
    average_forward_speed = average_speeds[0]

    print("average speed was {} m/s".format(average_forward_speed))
