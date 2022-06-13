#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image, ImageTk

import rospy
from std_msgs.msg import String

import numpy as np


class DisplayFullscreen:
    def __init__(self):
        self.w = FullscreenWindow('default.jpg')
        self.display_sub = rospy.Subscriber('/disp_image', String, self.rgb_disp)

    def rgb_disp(self, msg):
        print(msg)
        self.w.set_img(msg.data)


class FullscreenWindow:
    def __init__(self, path):
        self.tk = Tk()
        self.tk.attributes('-zoomed', True)  # This just maximizes it so we can see the window. It's nothing to do with fullscreen.
        img = ImageTk.PhotoImage(Image.open(path))
        self.frame = Label(self.tk, image=img)
        self.frame.pack(side="bottom", fill="both", expand="yes")
        print('build img')
        # self.frame.pack()
        self.tk.attributes("-fullscreen", True)
        self.tk.mainloop()

    def set_img(self, image1):
        print('gets called')
        img2 = ImageTk.PhotoImage(Image.open(image1))
        self.frame.configure(image=img2)
        self.frame.image = img2
        print('gets finished')
        self.tk.update()

        # test = ImageTk.PhotoImage(image1)
        # label1 = tkinter.Label(image=test)
        # label1.image = test
        # label1.place(x=0, y=0)

if __name__ == '__main__':
    rospy.init_node('tf_dist_capture')
    dispfull = DisplayFullscreen()
    # dispfull.rgb_disp('happy.png')
    rospy.spin()