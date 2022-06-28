#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk, threading
from tkinter import *
from PIL import Image, ImageTk
# new
import imageio

video_name = "tsw/vid2.mp4" #This is my video file path
video = imageio.get_reader(video_name)

def stream(label):
    while True:
        for image in video.iter_data():
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            label.config(image=frame_image)
            label.image = frame_image

if __name__ == "__main__":
    root = tk.Tk()
    my_label = tk.Label(root)
    my_label.pack()
    thread = threading.Thread(target=stream, args=(my_label,))
    thread.daemon = 1
    thread.start()
    root.mainloop()

# import rospy
# from std_msgs.msg import String

# import numpy as np


# class DisplayFullscreen:
#     def __init__(self):
#         self.w = FullscreenWindow('default.jpg')


# class FullscreenWindow:
#     def __init__(self, path):
#         self.display_sub = rospy.Subscriber('/disp_image', String, self.rgb_disp)
#         self.tk = Tk()
#         self.tk.attributes('-zoomed', True)  # This just maximizes it so we can see the window. It's nothing to do with fullscreen.
#         img = ImageTk.PhotoImage(Image.open(path).resize((1024, 600), Image.ANTIALIAS))
#         self.frame = Label(self.tk, image=img)
#         self.frame.pack(side="bottom", fill="both", expand="yes")
#         print('build img')
#         # self.frame.pack()
#         self.tk.attributes("-fullscreen", True)
#         self.tk.mainloop()

#     def rgb_disp(self, msg):
#         print(msg)
#         self.set_img(msg.data)

#     def set_img(self, image1):
#         print('gets called')
#         img2 = ImageTk.PhotoImage(Image.open(image1).resize((1024, 600), Image.ANTIALIAS))
#         self.frame.configure(image=img2)
#         self.frame.image = img2
#         print('gets finished')
#         self.tk.update()

#         # test = ImageTk.PhotoImage(image1)
#         # label1 = tkinter.Label(image=test)
#         # label1.image = test
#         # label1.place(x=0, y=0)

# if __name__ == '__main__':
#     rospy.init_node('img_display_node')
#     dispfull = DisplayFullscreen()
#     # dispfull.rgb_disp('happy.png')
#     rospy.spin()