#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Bool
from geometry_msgs.msg import PoseStamped
from Tkinter import *

def callback(data):
    if(data.data == True):

	pub = rospy.Publisher('chatter', PoseStamped, queue_size=10)
	#rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(15) # 15hz

	message = PoseStamped()
	print(message)

	message.header.frame_id="map"

	message.pose.position.x = 0
	message.pose.position.y = 0
	a = 0
	b = 0
	 

	if(message.pose.position.x == 0 & message.pose.position.y == 0):

		while(message.pose.position.y != 4):
			message.pose.position.y = a
			a = a + 1
			pub.publish(message)
			rate.sleep()

		while(message.pose.position.x != 4):
			message.pose.position.x = b
			b = b + 1
			pub.publish(message)
			rate.sleep()
		
	if(message.pose.position.x == 4 & message.pose.position.y == 4):
		while(message.pose.position.y != 0):
			a = a - 1
			message.pose.position.y = a
			pub.publish(message)
			rate.sleep()

		while(message.pose.position.x != 0):
			b = b - 1
			message.pose.position.x = b
			pub.publish(message)
			rate.sleep()


	    	
	#pub.publish(message)
	#rate.sleep()


def listener():

    rospy.init_node('listen', anonymous=True)
 
    rospy.Subscriber('button_state', Bool, callback)

    rospy.spin()
 
if __name__ == '__main__':
    listener()
