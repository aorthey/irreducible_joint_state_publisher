#!/usr/bin/env python
import pickle
import roslib; roslib.load_manifest('joint_state_publisher_standalone')
import roslib; roslib.load_manifest('tf')
import rospy
import os
import time
from sensor_msgs.msg import JointState
from geometry_msgs.msg import TransformStamped
from tf import TransformBroadcaster 
from hrp2 import hrp2

pub = rospy.Publisher ('/robot/joint_states', JointState)
rospy.init_node('jsp_standalone')

urdfName = "hrp2_14_capsule"
tf_root = "/robot/base_link"
packageName = "hrp2_14_description"
referenceFrame = "/robot/l_sole"
wall_tf_root = "/wall/base_link"
tf = ""

robot=hrp2(tf)

jointNames = robot.jointNames() 

walltf = TransformStamped ()
walltf.header.frame_id = referenceFrame;
walltf.child_frame_id = wall_tf_root

transform = TransformStamped ()
transform.header.frame_id = referenceFrame;
transform.child_frame_id = tf_root

broadcaster = TransformBroadcaster ()
js = JointState ()

folder = os.environ["MPP_PATH"]+"mpp-environment/output/hole-in-the-wall/"
svQValuesFname = folder +"/xpathQ.dat"
theta = pickle.load(open( svQValuesFname, "rb" ) )

jointMapArray=[]
jointValues =[]
jointKeys = []

tstart = -1
tend = 1
toffset = 0.01
t = tstart
forward = True
while not rospy.is_shutdown ():
        if t < tend and forward:
                t+=toffset
        else:
                if forward:
                        forward=False
                        t=tend
                else:
                        if t>tstart:
                                t-=toffset
                        else:
                                t=tstart
                                forward=True


        now = rospy.Time.now ()
        js.header.stamp.secs = now.secs
        js.header.stamp.nsecs = now.nsecs
        js.header.seq += 1
        js.header.frame_id = 'irrspace'
        transform.header.stamp.secs = now.secs
        transform.header.stamp.nsecs = now.nsecs
        transform.header.seq = js.header.seq

        q = theta[0]
        zz = theta[1]
        jmap = robot.getJointMapFromQ(q[0],q[1],q[2],q[3],q[4])
        #jmap = robot.halfSitting
        js.name = jmap.keys()
        js.position = jmap.values()
        js.velocity = len (js.position)*[0.,]
        js.effort = len (js.position)*[0.,]

        transform.transform.rotation = (0.0, 0.0, 0.0, 1.0)
        transform.transform.translation = (0.0, 0.0, zz)

        broadcaster.sendTransform \
        (transform.transform.translation,
         transform.transform.rotation,
         now, tf_root, referenceFrame)

        walltf.header.stamp.secs = now.secs
        walltf.header.stamp.nsecs = now.nsecs
        walltf.header.seq = js.header.seq
        walltf.transform.rotation = (0.0, 0.0, 0.0, 1.0)
        walltf.transform.translation = (0.0, t, 0.0)

        time.sleep(0.01)
        broadcaster.sendTransform \
        (walltf.transform.translation,
         walltf.transform.rotation,
         now, wall_tf_root, referenceFrame)

        print js
        pub.publish (js)
        #jointMapArray.append(jmap)
        #jointValues.append(jmap.values())
        #jointKeys.append(jmap.keys())

#pickle.dump( jointMapArray, open( qmname, "wb" ) )
#pickle.dump( jointValues, open( qvname, "wb" ) )
#pickle.dump( jointKeys, open( qkname, "wb" ) )
#pickle.dump( flpath, open( qflname, "wb" ) )
#pickle.dump( frpath, open( qfrname, "wb" ) )

