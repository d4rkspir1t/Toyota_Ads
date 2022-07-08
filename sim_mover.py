#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Simple hacky node that calls selection of TME movement functions and other stuff based on controller buttons
"""
import rospy
import tnu_traj as traj
import hsrb_interface
from tme_hsr_lib import movements
import time

from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

gripper_state = 0
move = movements.Movements()
robot = hsrb_interface.Robot()
# gripper = robot.get('gripper')
joystick_camera = False
p = rospy.Publisher("/hsrb/command_velocity", Twist, queue_size=1)


def callback(data):
    global gripper_state
    if data.buttons[1]:  # if button 2 is pressed, perform trajectory 1
        move_joint_target(traj.frame14A)
    elif data.buttons[2]:  # if button 2 is pressed, perform trajectory 2
        move_joint_target(traj.frame33B)
    if data.buttons[11]:  # if button 11 is pressed, close the gripper
        gripper_state = close_gripper_full_force()
    if joystick_camera:
        if data.buttons[7] and (data.axes[2] is not 0.0 or data.axes[3] is not 0.0):
            pan = data.axes[2]
            tilt = -data.axes[3]
            move_head(pan/5, tilt/5)
    elif data.buttons[4] and (data.axes[4] is not 0.0 or data.axes[5] is not 0.0):
        pan = data.axes[4]
        tilt = -data.axes[5]
        move_head(pan/3.5, tilt/5)
    if data.buttons[8]:
        move_base_skewed()


def move_base_skewed():
    tw = Twist()
    tw.linear.x = 0.1
    tw.linear.y = -0.1
    p.publish(tw)


def move_head(pan, tilt):
    move.move_head_to_pan_tilt_target_relative_angles_async(pan, tilt, movement_duration_in_s=0.3)


def close_gripper_full_force():
    rospy.sleep(0.05)
    if (gripper_state % 2) == 0:
        gripper.command(2)
    else:
        gripper.apply_force(2)
    global gripper_state
    gripper_state = gripper_state + 1


def move_joint_target(trajectory):
    for pose in trajectory:
        move.move_to_joint_target_positions_async(arm_flex_joint=pose['arm_flex_joint'],
                                                  arm_lift_joint=pose['arm_lift_joint'],
                                                  arm_roll_joint=pose['arm_roll_joint'],
                                                  wrist_flex_joint=pose['wrist_flex_joint'],
                                                  wrist_roll_joint=pose['wrist_roll_joint'],
                                                  head_pan_joint=pose['head_pan_joint'],
                                                  head_tilt_joint=pose['head_tilt_joint'],
                                                  movement_duration_in_s=pose['time'])
        rospy.sleep(pose['time'])

# def joy_mover():
#     # rospy.init_node('joy_mover', anonymous=True)

#     # rospy.Subscriber("/hsrb/joy", Joy, callback, queue_size=1)
#     # spin() simply keeps python from exiting until this node is stopped
#     rospy.spin()


if __name__ == '__main__':
    move_joint_target(traj.standby)
    rospy.sleep(3)
    print('DONE')
    move_joint_target(traj.toast)
    rospy.sleep(3)
    print('DONE')
    move_joint_target(traj.clink_start)
    rospy.sleep(1)
    move_joint_target(traj.clink)
    rospy.sleep(3)
    print('DONE')
    move_joint_target(traj.selfie)
    rospy.sleep(3)
    print('DONE')