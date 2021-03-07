#!/usr/bin/env python2

import sys
import numpy as np
import rospy
from nav_msgs.msg import Odometry

class RecordSpeeds:
    # topic for odometry information (pose and twist)
    ODOM_TOPIC = "/tesse/odom" #eventually: ("wall_follower_tesse/odometry_topic")

    def __init__(self, speed_log_filename):
        # subscribe to odometry messages
        rospy.Subscriber(
                self.ODOM_TOPIC,
                Odometry,
                self.odom_callback)

        # log will contain all speed data collected from odometry messages
        self.log_file = speed_log_filename
        self.speed_log = None

    def odom_callback(self, odom_data):
        twist = odom_data.twist.twist
        linear_velocity = np.array([[twist.linear.x, twist.linear.y, twist.linear.z]])
        #angular_velocity = np.array([[twist.angular.x, twist.angular.y, twist.angular.z]])

        if self.speed_log is None:
            self.speed_log = linear_velocity
        else:
            self.speed_log = np.vstack((self.speed_log,
                                       linear_velocity))

        np.savetxt(fname=self.log_file,
                   X=self.speed_log)

if __name__ == "__main__":
    rospy.init_node("record_speeds")

    speed_log_filename = sys.argv[1] if len(sys.argv) > 1 else "speed_log.txt"
    speed_recorder = RecordSpeeds(speed_log_filename=speed_log_filename)

    rospy.spin()
