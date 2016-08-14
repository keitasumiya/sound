# coding: utf-8

import numpy as np
import cv2
import random
import time
import image
import music
import sys



start_whole_time = time.time()
sr = 44100 # sampling rate

img_input= str(sys.argv[1])
img_name = "picasso"

img = cv2.imread(img_input)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


# melody -------------
## image parameters -------------
partition_num_width = 10
partition_num_height = 10
last_path_order = 20
first_shift = 1
repeatable_num = 3

## music parameters -------------
is_loop = 0
is_cut_loop = 0
cut_loop_num = 1
keyname = "F_mj"
first_octave = 3 # ex: 0=[C0, C#0, ..., C1] for "all"
plus_octave = 1
key_id_shift = 0 # ex: 0=C=ド for "all"
first_time_ratio = 8
time_length_ratio = 12
isnt_degeneratable = 1
bpm = 150
loop_count = 8
whole_wave_length = 0

img_prm = [partition_num_width, partition_num_height, last_path_order, first_shift, repeatable_num, is_loop]
msc_prm = [keyname, first_octave, plus_octave, key_id_shift, first_time_ratio, time_length_ratio, isnt_degeneratable, bpm, loop_count, sr, is_loop, is_cut_loop, cut_loop_num, whole_wave_length]

## img2wave -------------
path_hsv = image.img2path_hsv(img, img_prm)
melody_wave = music.path_hsv2wave(path_hsv, msc_prm)

# loop -------------
## image parameters -------------
partition_num_width = 3
partition_num_height = 3
last_path_order = 100
first_shift = 1
repeatable_num = 3

## music parameters -------------
is_loop = 1
is_cut_loop = 1
cut_loop_num = 1
keyname = "F_mj"
first_octave = 2 # ex: 0=[C0, C#0, ..., C1] for "all"
plus_octave = 1
key_id_shift = 0 # ex: 0=C=ド for "all"
first_time_ratio = 3
time_length_ratio = 12
isnt_degeneratable = 0
bpm = 150
loop_count = 4
whole_wave_length = len(melody_wave)

img_prm = [partition_num_width, partition_num_height, last_path_order, first_shift, repeatable_num, is_loop]
msc_prm = [keyname, first_octave, plus_octave, key_id_shift, first_time_ratio, time_length_ratio, isnt_degeneratable, bpm, loop_count, sr, is_loop, is_cut_loop, cut_loop_num, whole_wave_length]
## img2wave -------------
path_hsv = image.img2path_hsv(img, img_prm)
loop_wave = music.path_hsv2wave(path_hsv, msc_prm)

# unify melody and loop -------------

unified_sound_wave = music.unify1d(1*melody_wave, 1*loop_wave)

max_amp = max(abs(unified_sound_wave))
print(max_amp)
unified_sound_wave = unified_sound_wave/max_amp
music.wavwrite(unified_sound_wave,"music_"+img_name+".wav")

end_whole_time = time.time()
elapsed_whole_time = end_whole_time - start_whole_time
print(elapsed_whole_time, "sec   ", elapsed_whole_time/60, "min   ", elapsed_whole_time/3600, "hour")

