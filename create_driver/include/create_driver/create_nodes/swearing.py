#!/usr/bin/env python
import rospy
from create_msgs.msg import Bumper
from playsound import playsound
import random

class Swear:
    def __init__(self):
        rospy.init_node('create_swear')

        self.bumper_sub = rospy.Subscriber('/bumper',
                                           Bumper,
                                           self.bumper_callback)
        self.bumper_right = None
        self.bumper_left = None

    def bumper_callback(self, msg):
        self.bumper_left = msg.is_left_pressed
        self.bumper_right = msg.is_right_pressed

    def run(self):

        rate = rospy.Rate(10.0)

        while not rospy.is_shutdown():
            if self.bumper_left == True or self.bumper_right == True:
                sound1 = "/home/neiman/catkin_ws/src/create_robot/create_soundfiles/ebat.ogg"
                sound2 = "/home/neiman/catkin_ws/src/create_robot/create_soundfiles/blyad.ogg"
                sound3 = "/home/neiman/catkin_ws/src/create_robot/create_soundfiles/suka.ogg"
                playsound(random.choice([sound1, sound2, sound3]))
                rospy.loginfo(self.bumper_left)
                rospy.loginfo(self.bumper_right)
            else:
                pass


            rate.sleep()

if __name__ == '__main__':
    try:
        Swear().run()
    except rospy.ROSInterruptException:
        print("Something went wrong in the create_swear node.")