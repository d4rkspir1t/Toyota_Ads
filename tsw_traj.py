#!/usr/bin/python
# -*- coding: utf-8 -*-
standby = [
    {'arm_flex_joint': -0.0,
     'arm_lift_joint': 0.05,
     'arm_roll_joint': -1.6,
     'wrist_flex_joint': -1.55,
     'wrist_roll_joint': -0.0,
     'head_pan_joint': -0.0,
     'head_tilt_joint': -0.2,
     'time': 1.0}
]

wake_up = [
    {'arm_flex_joint': -0.0,
     'arm_lift_joint': 0.05,
     'arm_roll_joint': 0.0,
     'wrist_flex_joint': -1.55,
     'wrist_roll_joint': 0.0,
     'head_pan_joint': 0.0,
     'head_tilt_joint': 0.2,
     'time': 2.5}
]

wake_up2 = [
    {'arm_flex_joint': -0.0,
     'arm_lift_joint': 0.2,
     'arm_roll_joint': 0.0,
     'wrist_flex_joint': -1.55,
     'wrist_roll_joint': 0.0,
     'head_pan_joint': 0.0,
     'head_tilt_joint': 0.2,
     'time': 2.5}
]

invite_start = [
    {'arm_flex_joint': -0.0,
     'arm_lift_joint': 0.05,
     'arm_roll_joint': 0.0,
     'wrist_flex_joint': -1.55,
     'wrist_roll_joint': 0.0,
     'head_pan_joint': 0.0,
     'head_tilt_joint': 0.0,
     'time': 1.0}
]

invite_motion = [
    {'arm_flex_joint': -0.05,
     'arm_lift_joint': 0.10,
     'arm_roll_joint': 1.6,
     'wrist_flex_joint': -1.55,
     'wrist_roll_joint': 0.0,
     'head_pan_joint': 0.8,
     'head_tilt_joint': 0.0,
     'time': 2.0}
]

conduct_start = [
    {'arm_flex_joint': -0.05,
     'arm_lift_joint': 0.10,
     'arm_roll_joint': 0.0,
     'wrist_flex_joint': -1.55,
     'wrist_roll_joint': 0.0,
     'head_pan_joint': 0.0,
     'head_tilt_joint': 0.0,
     'time': 1.0}
     ]

conduct1 = [
     {'arm_flex_joint': -0.25,
     'arm_lift_joint': 0.10,
     'arm_roll_joint': 0.0,
     'wrist_flex_joint': -1.85,
     'wrist_roll_joint': 0.0,
     'head_pan_joint': 0.0,
     'head_tilt_joint': 0.0,
     'time': 0.5},
     {'arm_flex_joint': -0.05,
     'arm_lift_joint': 0.15,
     'arm_roll_joint': 1.0,
     'wrist_flex_joint': -1.0,
     'wrist_roll_joint': 0.0,
     'head_pan_joint': 0.2,
     'head_tilt_joint': 0.2,
     'time': 1.0},
     {'arm_flex_joint': -0.25,
     'arm_lift_joint': 0.10,
     'arm_roll_joint': 0.0,
     'wrist_flex_joint': -1.85,
     'wrist_roll_joint': 0.0,
     'head_pan_joint': 0.0,
     'head_tilt_joint': 0.0,
     'time': 0.5},
     {'arm_flex_joint': -0.05,
     'arm_lift_joint': 0.15,
     'arm_roll_joint': -1.0,
     'wrist_flex_joint': -1.0,
     'wrist_roll_joint': 0.0,
     'head_pan_joint': -0.2,
     'head_tilt_joint': 0.2,
     'time': 1.0},
     {'arm_flex_joint': -0.05,
     'arm_lift_joint': 0.10,
     'arm_roll_joint': 0.0,
     'wrist_flex_joint': -1.55,
     'wrist_roll_joint': 0.0,
     'head_pan_joint': 0.0,
     'head_tilt_joint': 0.0,
     'time': 0.5}
]

flower_getgive = [
    {'arm_flex_joint': -0.4,
     'arm_lift_joint': 0.4,
     'arm_roll_joint': 0.0,
     'wrist_flex_joint': -1.2,
     'wrist_roll_joint': -0.0,
     'head_pan_joint': -0.0,
     'head_tilt_joint': 0.3,
     'time': 1.0}
                    ]


wave_goodbye = [
    {'arm_flex_joint': -0.0,
     'arm_lift_joint': 0.2,
     'arm_roll_joint': -1.6,
     'wrist_flex_joint': 0.6,
     'wrist_roll_joint': 1.6,
     'head_pan_joint': -0.0,
     'head_tilt_joint': -0.0,
     'time': 1.0},
    {'arm_flex_joint': -0.0,
     'arm_lift_joint': 0.2,
     'arm_roll_joint': -1.6,
     'wrist_flex_joint': -0.6,
     'wrist_roll_joint': 1.6,
     'head_pan_joint': -0.0,
     'head_tilt_joint': -0.0,
     'time': 1.0},
    {'arm_flex_joint': -0.0,
     'arm_lift_joint': 0.2,
     'arm_roll_joint': -1.6,
     'wrist_flex_joint': 0.6,
     'wrist_roll_joint': 1.6,
     'head_pan_joint': -0.0,
     'head_tilt_joint': -0.0,
     'time': 1.0},
    {'arm_flex_joint': -0.0,
     'arm_lift_joint': 0.2,
     'arm_roll_joint': -1.6,
     'wrist_flex_joint': -0.6,
     'wrist_roll_joint': 1.6,
     'head_pan_joint': -0.0,
     'head_tilt_joint': -0.0,
     'time': 1.0}
]

wave_hi_expo = [
    {'arm_flex_joint': -0.0,
     'arm_lift_joint': 0.2,
     'arm_roll_joint': -1.6,
     'wrist_flex_joint': 0.6,
     'wrist_roll_joint': 1.6,
     'head_pan_joint': -0.0,
     'head_tilt_joint': 0.3,
     'time': 1.0},
    {'arm_flex_joint': -0.0,
     'arm_lift_joint': 0.2,
     'arm_roll_joint': -1.6,
     'wrist_flex_joint': -0.6,
     'wrist_roll_joint': 1.6,
     'head_pan_joint': -0.0,
     'head_tilt_joint': 0.3,
     'time': 1.0},
    {'arm_flex_joint': -0.0,
     'arm_lift_joint': 0.2,
     'arm_roll_joint': -1.6,
     'wrist_flex_joint': 0.6,
     'wrist_roll_joint': 1.6,
     'head_pan_joint': -0.0,
     'head_tilt_joint': 0.3,
     'time': 1.0},
    {'arm_flex_joint': -0.0,
     'arm_lift_joint': 0.2,
     'arm_roll_joint': -1.6,
     'wrist_flex_joint': -0.6,
     'wrist_roll_joint': 1.6,
     'head_pan_joint': -0.0,
     'head_tilt_joint': 0.3,
     'time': 1.0}
]

rest_position = [
    {'arm_flex_joint': -0.0,
     'arm_lift_joint': 0.1,
     'arm_roll_joint': 0.0,
     'wrist_flex_joint': -1.6,
     'wrist_roll_joint': 0.0,
     'head_pan_joint': -0.0,
     'head_tilt_joint': 0.2,
     'time': 1.0}
]

pick_up_move = [
    {'arm_flex_joint': -0.3,
     'arm_lift_joint': 0.22,
     'arm_roll_joint': 0.0,
     'wrist_flex_joint': -1.2,
     'wrist_roll_joint': 0.0,
     'head_pan_joint': -0.0,
     'head_tilt_joint': 0.1,
     'time': 1.0},
     {'arm_flex_joint': -0.3,
     'arm_lift_joint': 0.2,
     'arm_roll_joint': 0.0,
     'wrist_flex_joint': -1.2,
     'wrist_roll_joint': 0.0,
     'head_pan_joint': -0.0,
     'head_tilt_joint': 0.1,
     'time': 1.0}
]

put_down_move = [
    {'arm_flex_joint': -0.3,
     'arm_lift_joint': 0.22,
     'arm_roll_joint': 0.0,
     'wrist_flex_joint': -1.2,
     'wrist_roll_joint': 0.0,
     'head_pan_joint': -0.0,
     'head_tilt_joint': 0.1,
     'time': 1.0},
    {'arm_flex_joint': -0.05,
     'arm_lift_joint': 0.2,
     'arm_roll_joint': 0.0,
     'wrist_flex_joint': -1.6,
     'wrist_roll_joint': 0.0,
     'head_pan_joint': -0.0,
     'head_tilt_joint': 0.1,
     'time': 1.0}
]

frame_puck_1 = [
    {'arm_flex_joint': -1.6,
                     'arm_lift_joint': 0.0,
                     'arm_roll_joint': 0.0,
                     'wrist_flex_joint': -1.6,
                     'wrist_roll_joint': 0.0,
                     'head_pan_joint': -0.0,
                     'head_tilt_joint': -0.2,
                     'time': 1.0}
    ]
frame_puck_2 = [
    {'arm_flex_joint': -0.3,
                     'arm_lift_joint': 0.1,
                     'arm_roll_joint': 1.6,
                     'wrist_flex_joint': -1.6,
                     'wrist_roll_joint': 1.2,
                     'head_pan_joint': -0.0,
                     'head_tilt_joint': -0.2,
                     'time': 1.0}
]

# SIGNING THE PAD
frame1signing_pre = [{'arm_flex_joint': -1.0,
             'arm_lift_joint': 0.1,
             'arm_roll_joint': 0.0,
             'wrist_flex_joint': -0.4,
             'wrist_roll_joint': 0.0,
             'head_pan_joint': 0.0,
             'head_tilt_joint': 0.0,
             'time': 2.0}]

frame1signing = [{'arm_flex_joint': -0.8,
             'arm_lift_joint': 0.1,
             'arm_roll_joint': 0.0,
             'wrist_flex_joint': -0.4,
             'wrist_roll_joint': 0.0,
             'head_pan_joint': 0.0,
             'head_tilt_joint': -0.5,
             'time': 2.0},
             {'arm_flex_joint': -0.8,
             'arm_lift_joint': 0.1,
             'arm_roll_joint': 0.0,
             'wrist_flex_joint': -0.6,
             'wrist_roll_joint': 0.0,
             'head_pan_joint': 0.0,
             'head_tilt_joint': -0.5,
             'time': 0.1},
             {'arm_flex_joint': -0.8,
             'arm_lift_joint': 0.1,
             'arm_roll_joint': 0.0,
             'wrist_flex_joint': -0.4,
             'wrist_roll_joint': 0.0,
             'head_pan_joint': 0.0,
             'head_tilt_joint': -0.5,
             'time': 0.2},
             {'arm_flex_joint': -0.8,
             'arm_lift_joint': 0.1,
             'arm_roll_joint': 0.0,
             'wrist_flex_joint': -0.6,
             'wrist_roll_joint': 0.0,
             'head_pan_joint': 0.0,
             'head_tilt_joint': -0.5,
             'time': 0.1},
             {'arm_flex_joint': -0.8,
             'arm_lift_joint': 0.1,
             'arm_roll_joint': 0.0,
             'wrist_flex_joint': -0.4,
             'wrist_roll_joint': 0.0,
             'head_pan_joint': 0.0,
             'head_tilt_joint': -0.5,
             'time': 0.2},
             # arm away
             {'arm_flex_joint': -0.1,
             'arm_lift_joint': 0.1,
             'arm_roll_joint': 0.0,
             'wrist_flex_joint': -0.4,
             'wrist_roll_joint': 0.0,
             'head_pan_joint': 0.0,
             'head_tilt_joint': 0.0,
             'time': 0.2}]
