#===install packages in python===
## using pip install in comand line
## required: vedo, nibabel, numpy, mesh, MoviePy, matplotlib, opencv-python
#--------------------------------
#===additional resources===
##https://github.com/marcomusy/vedo/issues/180
##jupyter incompatibility: https://githubmemory.com/repo/brainglobe/brainrender/issues/132
#--------------------------------


from vedo import *
from vedo import Volume
from vedo import embedWindow, show, colorMap
import nibabel as nib
import numpy as np

#---specify nifti file here---
#MNI outer surface
filepath1 = '/mniedges.nii.gz'
#grey matter, white matter and significant changes
filepath2 = '/thr.nii.gz'
#JHU atlas
filepath3 = '/nii.gz'
#Harvard Oxford subcortical atlas
#filepath4 = '/Users/claraweber/Desktop/hosub.nii.gz'
#Harvard Oxford cortical atlas
#filepath5 = '/Users/claraweber/Desktop/hocor.nii.gz'

im1 = nib.load(filepath1).get_fdata()
type(im1)
im1.shape
np.unique(im1)

im2 = nib.load(filepath2).get_fdata()
type(im2)
im2.shape
np.unique(im2)

im3 = nib.load(filepath3).get_fdata()
type(im3)
im3.shape
np.unique(im3)

outputgifname = "output"

#once data is loaded as above, addition is possible to display more volumes simultaenously
#all files have to be in same space (MNI152)
#use multiplication to enhance contrast. Intensity range should not exceed factor 3

im4=im1*3+im2

###===define cameras===
cam1=dict(pos=(180, -400, -400),
          viewup=(0,1,0),
          distance=200,
          clippingRange=(300,400),
          focalPoint=(150,50,50)
          )


###===show significant changes, grey and white matter===
vol1 = Volume(im1, alpha=(0.0, 1), alphaUnit=1, mode=0)
vol2 = Volume(im2, c='bwr', alpha=(0.0, 0.5), alphaUnit=1, mode=0)
vol3 = Volume(im3, c='bwr', alpha=(0.0, 1), alphaUnit=5, mode=0)
vol4 = Volume(im4, alpha=(0.0, 1), alphaUnit=8, mode=4)

sig1 = Volume(im1, alpha=(0.0, 1), alphaUnit=1, mode=1)
sig2 = Volume(im2, c='bwr',alpha=(0.0, 1), alphaUnit=1, mode=1)
sig3 = Volume(im3, c='binary', alpha=(0.0, 1), alphaUnit=1, mode=1)
sig4 = Volume(im4, alpha=(0.0, 1), alphaUnit=1, mode=4)


#===IsosurfaceBrowser: surface rendering===
from vedo.applications import IsosurfaceBrowser
import matplotlib.cm as cm
plt=IsosurfaceBrowser(vol3, c='tomato')
plt.show(axes=0, bg2='white')


video= Video(outputgifname+'.mp4', duration =13, backend='opencv')
video.action(elevation_range=(-10,30), azimuth_range=(0,720), zoom=None, cam1=cam1, resetcam=True)
video.close()

from moviepy.editor import *
clip = (VideoFileClip(outputgifname+'.mp4').resize(0.5))
clip.write_gif(outputgifname+'.gif')
