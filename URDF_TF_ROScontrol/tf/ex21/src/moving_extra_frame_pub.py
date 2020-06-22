#!/usr/bin/env python
import rospy
import tf
from math import cos,pi

if __name__=='__main__':
    rospy.init_node('my_moving_frame')
    r=tf.TransformBroadcaster()
    rate=rospy.Rate(3)
    while not rospy.is_shutdown():
        t = (rospy.Time.now().to_sec() * pi)*2
        t=t%(2*pi)
        angular=[0,0,cos(t)]
        q = tf.transformations.quaternion_from_euler(angular[0],angular[1],angular[2])
     #   print(rospy.Time.now().to_sec())
        rospy.loginfo(angular[2])
        r.sendTransform((1,0,0),q,rospy.Time.now(),'my_moving_frame','coke_can')
        rate.sleep()