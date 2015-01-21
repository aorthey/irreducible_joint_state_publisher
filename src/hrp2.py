from math import pi
class hrp2:
        halfSitting = \
        {"base_joint_x": 0.0,
         "base_joint_y": 0.0,
         "base_joint_z": 0.648702,
         #"base_joint_SO3": (1.0, 0.0, 0.0, 0.0),
         "CHEST_JOINT0": 0.0,
         "CHEST_JOINT1": 0.0,
         "HEAD_JOINT0": 0.0,
         "HEAD_JOINT1": 0.0,
         "LARM_JOINT0": 0.261799,
         "LARM_JOINT1": 0.17453,
         "LARM_JOINT2": 0.0,
         "LARM_JOINT3": -0.523599,
         "LARM_JOINT4": 0.0,
         "LARM_JOINT5": 0.0,
         "LARM_JOINT6": 0.1,
         "LHAND_JOINT0": 0.0,
         "LHAND_JOINT1": 0.0,
         "LHAND_JOINT2": 0.0,
         "LHAND_JOINT3": 0.0,
         "LHAND_JOINT4": 0.0,
         "RARM_JOINT0": 0.261799,
         "RARM_JOINT1": -0.17453,
         "RARM_JOINT2": 0.0,
         "RARM_JOINT3": -0.523599,
         "RARM_JOINT4": 0.0,
         "RARM_JOINT5": 0.0,
         "RARM_JOINT6": 0.1,
         "RHAND_JOINT0": 0.0,
         "RHAND_JOINT1": 0.0,
         "RHAND_JOINT2": 0.0,
         "RHAND_JOINT3": 0.0,
         "RHAND_JOINT4": 0.0,
         "LLEG_JOINT0": 0.0,
         "LLEG_JOINT1": 0.0,
         "LLEG_JOINT2": -0.453786,
         "LLEG_JOINT3": 0.872665,
         "LLEG_JOINT4": -0.418879,
         "LLEG_JOINT5": 0.0,
         "RLEG_JOINT0": 0.0,
         "RLEG_JOINT1": 0.0,
         "RLEG_JOINT2": -0.453786,
         "RLEG_JOINT3": 0.872665,
         "RLEG_JOINT4": -0.418879,
         "RLEG_JOINT5": 0.0
         }

        def __init__(self,tf):
                self.tf =tf
        def setIrreducibleJoints(self,jmap):
                jmap[self.tf+'RARM_JOINT0'] = 0.0
                jmap[self.tf+'RARM_JOINT1'] = -1.5708
                jmap[self.tf+'RARM_JOINT2'] = 0.0
                jmap[self.tf+'RARM_JOINT3'] = 0.0
                jmap[self.tf+'RARM_JOINT4'] = 0.0
                jmap[self.tf+'RARM_JOINT5'] = 0.0
                jmap[self.tf+'RARM_JOINT6'] = 0.0
                jmap[self.tf+'LARM_JOINT0'] = 0.0
                jmap[self.tf+'LARM_JOINT1'] = 1.5708
                jmap[self.tf+'LARM_JOINT2'] = 0.0
                jmap[self.tf+'LARM_JOINT3'] = 0.0
                jmap[self.tf+'LARM_JOINT4'] = 0.0
                jmap[self.tf+'LARM_JOINT5'] = 0.0
                jmap[self.tf+'LARM_JOINT6'] = 0.0
                jmap[self.tf+'RHAND_JOINT0'] = 0.0
                jmap[self.tf+'RHAND_JOINT1'] = 0.0
                jmap[self.tf+'RHAND_JOINT2'] = 0.0
                jmap[self.tf+'RHAND_JOINT3'] = 0.0
                jmap[self.tf+'RHAND_JOINT4'] = 0.0
                jmap[self.tf+'LHAND_JOINT0'] = 0.0
                jmap[self.tf+'LHAND_JOINT1'] = 0.0
                jmap[self.tf+'LHAND_JOINT2'] = 0.0
                jmap[self.tf+'LHAND_JOINT3'] = 0.0
                jmap[self.tf+'LHAND_JOINT4'] = 0.0
                jmap[self.tf+'HEAD_JOINT0']=0.0
                jmap[self.tf+'CHEST_JOINT0']=0.0
                jmap[self.tf+'LLEG_JOINT0']=0.0
                jmap[self.tf+'LLEG_JOINT1']=0.0
                jmap[self.tf+'LLEG_JOINT5']=0.0
                jmap[self.tf+'RLEG_JOINT0']=0.0
                jmap[self.tf+'RLEG_JOINT1']=0.0
                jmap[self.tf+'RLEG_JOINT5']=0.0

        def getJointMapFromQ(self,q0,q1,q2,q3,q4):
                q0 = float(q0)
                q1 = float(q1)
                q2 = float(q2)
                q3 = float(q3)
                q4 = float(q4)

                #jmap = self.halfSitting
                jmap={}
                self.setIrreducibleJoints(jmap)
                jmap[self.tf+'LLEG_JOINT4']=q0
                jmap[self.tf+'LLEG_JOINT3']=q1
                jmap[self.tf+'LLEG_JOINT2']=q2
                jmap[self.tf+'RLEG_JOINT4']=q0
                jmap[self.tf+'RLEG_JOINT3']=q1
                jmap[self.tf+'RLEG_JOINT2']=q2
                jmap[self.tf+'CHEST_JOINT1'] = q3
                jmap[self.tf+'HEAD_JOINT1'] = q4
                #jmap[self.tf+'base_joint_x']=0.0
                #jmap[self.tf+'base_joint_y']=0.0
                #jmap[self.tf+'base_joint_z']=0.6487
                return jmap

        def jointNames(self):
                return self.halfSitting.keys()
        def getHalfSittingMap(self):
                return self.halfSitting
