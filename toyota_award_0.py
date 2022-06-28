#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""
Simple hacky node that calls selection of TME movement functions and other stuff based on controller buttons
"""
import random

import rospy
import tdk_traj as traj
import hsrb_interface
from tme_hsr_lib import movements

from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from std_msgs.msg import ColorRGBA, String

# from sound_play.msg import SoundRequest
# from sound_play.libsoundplay import SoundClient
# import threading

show_text_state = 0
gripper_state = 0
move = movements.Movements()
print('MOVEMENT SETUP')
robot = hsrb_interface.Robot()
gripper = robot.get('gripper')
joystick_camera = False
p = rospy.Publisher("/hsrb/command_velocity", Twist, queue_size=1)
# display_pub = rospy.Publisher('/robot_mount_wui/display_image', String, queue_size=10)
tts = robot.try_get('default_tts')
tts.language = tts.ENGLISH
tts.volume = 1.0

# soundhandle = SoundClient()

blue = ColorRGBA(0,0,1,0)
green = ColorRGBA(0,1,0,0)
cyan = ColorRGBA(0,1,1,0)
red = ColorRGBA(1,0,0,0)
purple = ColorRGBA(1,0,1,0)
yellow = ColorRGBA(1,1,0,0)
status_led_topic = '/hsrb/command_status_led_rgb'
led_pub = rospy.Publisher(status_led_topic,
                          ColorRGBA, queue_size=100)
led_pub.publish(green)
color_arr = [cyan, cyan, cyan, cyan, cyan, cyan]
# color_arr = [blue, green, cyan, red, purple, yellow]
current_color_idx = 0
color = color_arr[current_color_idx]
# led_pub.publish(blue) 
# rospy.sleep(1) 

# rospy.sleep(1)
# led_pub.publish(cyan)
# rospy.sleep(1)
# led_pub.publish(red)
# rospy.sleep(1)
# led_pub.publish(purple)
# rospy.sleep(1)
# led_pub.publish(yellow)
# rospy.sleep(1)

def callback(data):
    global gripper_state
    # print('DATA in', data)
    if data.buttons[0]:
        print(0)
    elif data.buttons[1]:
        print(1)
    elif data.buttons[2]:
        print(2)
    elif data.buttons[3]:
        print(3)
    elif data.buttons[4]:
        print(4)
    elif data.buttons[5]:
        print(5)
    elif data.buttons[6]:
        print(6)
    elif data.buttons[7]:
        print(7)
    elif data.buttons[8]:
        print(8)
    elif data.buttons[9]:
        print(9)
    elif data.buttons[10]:
        print(10)
    elif data.buttons[11]:
        print(11)
    # if data.buttons[0] and not data.buttons[4]:
    if data.buttons[0]:
        # tts.say(u'Work it. Make it. Do it. Makes us.')
        # rospy.sleep(4)
        move_joint_target(traj.flower_getgive)
        # tts.say(u'Oh no')
        # rospy.sleep(1)
    # if data.buttons[1] and not data.buttons[4]:
    if data.buttons[1]:
        # move_joint_target(traj.frame_hood_off)
        move_joint_target(traj.flower_transport)
        # tts.say(u'Goodbye!')
        # volume = 1.0
        # rospy.sleep(1)
    # elif data.buttons[2] and not data.buttons[4]:
    elif data.buttons[2]:
        move_joint_target(traj.flower_getgive)
        rospy.sleep(1.5)
        tts.say(say_congrats())
        rospy.sleep(1)
    # elif data.buttons[3] and not data.buttons[4]:
    elif data.buttons[3]:
        tts.say(say_script())
        move_joint_target(traj.wave_goodbye)
        # move_joint_target(traj.frame_last_move_4)
        # tts.say(u'Hello')
        # rospy.sleep(2)
        pass

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
    # if data.buttons[8]:
    #     move_base_skewed()


def say_congrats():
    possible_sentences = [u'Congratulations!', u'Thank you!', u'I am pleased to give this to you!', u'Please accept this award!']
    sentence = random.choice(possible_sentences)
    return sentence


def say_script():
    speech_segment = ['Goodbye! And I hope to see you all later at the demo booth!']
    return speech_segment[show_text_state]

# def move_base_skewed():
#     tw = Twist()
#     tw.linear.x = 0.1
#     tw.linear.y = -0.1
#     p.publish(tw)


def move_head(pan, tilt):
    move.move_head_to_pan_tilt_target_relative_angles_async(pan, tilt, movement_duration_in_s=0.3)


def close_gripper_full_force():
    rospy.sleep(0.05)
    if (gripper_state % 2) == 0:
        # gripper.command(1)
        gripper.apply_force(0)
    else:
        # gripper.command(0)
        gripper.apply_force(5)
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


def color_set(color_cb):
    if color_cb != color:
        led_pub.publish(color)


def display_cb(msg):
    image_path = msg.data
    if image_path != '/home/administrator/images/test_img.png':
        display_pub.publish('/home/administrator/images/test_img.png')


def joy_mover():
    # rospy.init_node('joy_mover', anonymous=True)

    # rospy.Subscriber("/hsrb/joy", Joy, callback, queue_size=1)
    rospy.Subscriber("/hsrb/joy_ps4", Joy, callback, queue_size=1)
    print('subscribed!')
    rospy.Subscriber(status_led_topic, ColorRGBA, color_set, queue_size=1)
    # rospy.Subscriber('/robot_mount_wui/display_image', String, display_cb)
    # display_pub.publish('/home/administrator/images/test_img.jpg')
    # move_joint_target(traj.frame23s)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    joy_mover()
