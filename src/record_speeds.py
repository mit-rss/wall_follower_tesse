#!/usr/bin/env python2

import numpy as np
import rospy
from nav_msgs.msg import Odometry

class RecordSpeeds:
    # topic for odometry information (pose and twist)
    ODOM_TOPIC = rospy.get_param("record_speeds/odometry_topic")

    def __init__(self):
        # subscribe to odometry messages
        rospy.Subscriber(
                self.ODOM_TOPIC,
                Odometry,
                self.odom_callback)

        # log will contain all speed data collected from odometry messages
        self.log_file = "speed_log.txt"
        self.speed_log = None

        self.got_first_message = False

    def odom_callback(self, odom_data):
        if not self.got_first_message:
            self.got_first_message = True
            print("logging speed at ~/.ros/{}".format(self.log_file))
        
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
    speed_recorder = RecordSpeeds()
    rospy.spin()
