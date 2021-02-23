#!/usr/bin/env python
# license removed for brevity
import math
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

def talker():
    pub = rospy.Publisher('chatter', PoseStamped, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(15) # 15hz

    message = PoseStamped()
    print(message)

    message.header.frame_id="map"

    a = 0
    b = 0

    message.pose.position.x = 0
    message.pose.position.y = 0
 
    while not rospy.is_shutdown():

	if(message.pose.position.x == -4 && message.pose.position.y == -4)
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
	
	elif 



	
	
    	
	pub.publish(message)
	rate.sleep()

if __name__ == '__main__':
     try:
         talker()
     except rospy.ROSInterruptException:
         pass
