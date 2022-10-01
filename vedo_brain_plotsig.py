from vedo import *
from vedo import Volume
from vedo import embedWindow, show, colorMap
import nibabel as nib
import numpy as np

#---specify nifti file here---
#MNI outer surface
filepath1 = 'subtracted_novent.nii.gz'
#grey matter, white matter and significant changes
filepath2 = 'skeletonthr2bin.nii.gz'
#JHU atlas
filepath3 = 'FA32.nii.gz'
#combi
filepath4 = 'combi2_enh.nii.gz'
#Harvard Oxford subcortical atlas
#filepath4 = 'hosub.nii.gz'
#Harvard Oxford cortical atlas
#filepath5 = 'hocor.nii.gz'

im1 = nib.load(filepath1).get_fdata()
im2 = nib.load(filepath2).get_fdata()
im3 = nib.load(filepath3).get_fdata()
outputgifname = "output"

## this works well for black background
im4=im1*1.5+im2*8+im3*15

###===define cameras===
cam1=dict(pos=(180, -400, -400),
          viewup=(1,0,0),
          distance=200,
          clippingRange=(300,400),
          focalPoint=(150,50,50)
          )

###===show significant changes, grey and white matter===
sig4 = Volume(im4, c='seismic', alpha=(0.0, 1), alphaUnit=1, mode=1)
sig4.show(axes=0, bg="white",camera=cam1)


video= Video(outputgifname+'.mp4', duration =13, backend='opencv')
video.action(elevation_range=(-10,10), azimuth_range=(0,720), zoom=None, cam1=cam1, resetcam=True)
video.close()

from moviepy.editor import *
clip = (VideoFileClip(outputgifname+'.mp4').resize(0.5))
clip.write_gif(outputgifname+'.gif')
