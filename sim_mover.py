#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Simple hacky node that calls selection of TME movement functions and other stuff based on controller buttons
"""
import rospy
import tdk_traj as traj
import hsrb_interface
from tme_hsr_lib import movements
import time

from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

gripper_state = 0
move = movements.Movements()
robot = hsrb_interface.Robot()
gripper = robot.get('gripper')
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
    # joy_mover()
    # print('FIRST')
    #-----------------------------------------------
    # close_gripper_full_force()
    # rospy.sleep(1)
    # close_gripper_full_force()
    # # print(gripper_state)
    # move_joint_target(traj.frame_stick_2x10)
    # rospy.sleep(1)
    # move_joint_target(traj.frame_stick_down)
    # rospy.sleep(1)
    # close_gripper_full_force()
    # rospy.sleep(1)
    # move_joint_target(traj.frame_stick_lift)
    # gripper.command(0.5)
    # rospy.sleep(1)
    # -----------------------------------------------

    move_joint_target(traj.flower_getgive)
    rospy.sleep(5)
    move_joint_target(traj.flower_transport)
    rospy.sleep(5)
    move_joint_target(traj.wave_goodbye)
    rospy.sleep(3)
    # rate = rospy.Rate(10)
    # while not rospy.is_shutdown():
    #     move_joint_target(traj.frame_stick_1)
    #     rate.sleep()

    #------------------------------------------------

    # gripper_state = close_gripper_full_force()
    # gripper_state = close_gripper_full_force()
    # rospy.init_node('play', anonymous=True)

    # print(time.time())
    # rospy.sleep(4)
    # print(time.time())
    # print('SECOND')
    # move_joint_target(traj.frame33B)
    # print(time.time())
    # rospy.sleep(4)
    # print(time.time())
    # print('THIRD')
    # gripper_state = close_gripper_full_force()
    # rospy.sleep(4)
    # gripper_state = close_gripper_full_force()
    
    # move_joint_target(traj.frame10A)
    # gripper.command(0.5)

    # move_joint_target(traj.frame23s)
    # rospy.sleep(5)
    # move_joint_target(traj.frame23)

    # move_joint_target(traj.frameBOX1)
    # rospy.sleep(1)
    # move_joint_target(traj.frameBOX2)    
    # move_joint_target(traj.frameBOX2)