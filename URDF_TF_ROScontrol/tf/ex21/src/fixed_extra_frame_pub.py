#!/usr/bin/env python
import rospy
import tf

if __name__=='__main__':
    rospy.init_node('my_fixed_frame')
    r=tf.TransformBroadcaster()
    rate=rospy.Rate(3)
    while not rospy.is_shutdown():
        r.sendTransform((1,0.3,0),(0,0,0,1.0),rospy.Time.now(),'my_fixed_frame','turtle2')
        rate.sleep()