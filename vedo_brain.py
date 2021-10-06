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
filepath1 = '/Users/claraweber/Desktop/brainrender/mniedges.nii.gz'
#grey matter, white matter and significant changes
filepath2 = '/Users/claraweber/Desktop/brainrender/corg_sk_div1000_thr.nii.gz'
#JHU atlas
filepath3 = '/Users/claraweber/Desktop/brainrender/combi2_enh.nii.gz'
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

outputgifname = "rotate_significant_4"

#once data is loaded as above, addition is possible to display more volumes simultaenously
#all files have to be in same space (MNI152)
#use multiplication to enhance contrast. Intensity range should not exceed factor 3

im4=im1*3+im2

#---vedo settings---
#https://vedo.embl.es/autodocs/content/vedo/settings.html
#xtitle = 'x'
#ytitle = 'y'
#ztitle = 'z'
#defaultFont = 'Normografo' 
#screeshotScale = 1
#screenshotTransparentBackground = False
#screeshotLargeImage = False 
#computeNormals = None
#autoResetScalarRange = True
#allowInteraction = True
#enableDefaultMouseCallbacks = True
#enableDefaultKeyboardCallbacks = True
#immediateRendering = True
#rendererFrameColor = None
#rendererFrameAlpha = 0.5
#rendererFrameWidth = 0.5
#rendererFramePadding = 0.001
#windowSplittingPosition = None
#enablePrintColor = True
#usingQt = False
#renderLinesAsTubes = False
#pointSmoothing = False
#lineSmoothing = False
#polygonSmoothing = False
#hiddenLineRemoval = False
#visibleGridEdges = False
#lightFollowsCamera = False
#twoSidedLighting = True
#useDepthPeeling = False
#alphaBitPlanes  = True  
#multiSamples    = 0  
#maxNumberOfPeels= 8     
#occlusionRatio  = 0.0
#useFXAA = False
#preserveDepthBuffer = False
#useSSAO         = False
#SSAORadius      = 0.5   # the SSAO hemisphere radius
#SSAOBias        = 0.01  # the bias when comparing samples
#SSAOKernelSize  = 32    
#SSAOBlur        = False # blurring of the ambient occlusion (helps for low samples nr)
#usePolygonOffset    = False
#polygonOffsetFactor = 0.1
#polygonOffsetUnits  = 0.1
#interpolateScalarsBeforeMapping = True
#useParallelProjection = False
#tiffOrientationType = 4
#annotatedCubeColor      = (0.75, 0.75, 0.75)
#annotatedCubeTextColor  = None 
#annotatedCubeTextScale  = 0.2
#annotatedCubeTexts      = ["right","left ", "front","back ", " top ", "bttom"]
#k3dMenuVisibility = True
#k3dPlotHeight = 512
#k3dAntialias  = True
#k3dLighting   = 1.2
#k3dCameraAutoFit = True
#k3dGridAutoFit= True
#k3dAxesHelper = True    # size of the small triad of axes on the bottom right
#k3dPointShader= "3d"    # options are '3d', 'mesh', '3dSpecular', 'dot', 'flat'
#k3dLineShader = "thick" # options are 'flat', 'mesh', 'thick'
#-------------------

#options for Volume
#https://vedo.embl.es/autodocs/content/vedo/volume.html#interpolatetovolume
#https://vedo.embl.es/autodocs/_modules/vedo/volume.html
#c (list,str) – sets colors along the scalar range, or a matplotlib color map name
#alphas (float,list) – sets transparencies along the scalar range
#alphaUnit (float) – default 1, low values make composite rendering look brighter and denser
### 10 will appear ghostish and 0.001 very dense and surface like
#origin (list) – set volume origin coordinates
#spacing (list) – voxel dimensions in x, y and z.
#dims (list) – specify the dimensions of the volume.
#mapper (str) – either ‘gpu’, ‘opengl_gpu’, ‘fixed’ or ‘smart’
#mode (int) –define the volumetric rendering style:
###0, composite rendering
###1, maximum projection rendering (appears smoother)
###2, minimum projection (not applicable)
###3, average projection (not applicable)
###4, additive mode (will give black cube with white brain)

#color options
#'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu',
#'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r',
#'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired',
#'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu',
#'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r',
#'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn',
#'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r',
#'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r',
#'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r',
#'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis',
#'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix',
#'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r',
#'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r',
#'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2',
#'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno',
#'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r',
#'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow',
#'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10',
#'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain',
#'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted',
#'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r'

###===define cameras===
cam1=dict(pos=(180, -400, -400),
          viewup=(1,0,0),
          distance=200,
          clippingRange=(300,400),
          focalPoint=(150,50,50)
          )

#========================================


###===show significant changes, grey and white matter===
vol1 = Volume(im1, alpha=(0.0, 1), alphaUnit=1, mode=0)
vol2 = Volume(im2, c='bwr', alpha=(0.0, 0.5), alphaUnit=1, mode=0)
vol3 = Volume(im3, c='bwr', alpha=(0.0, 1), alphaUnit=5, mode=0)
vol4 = Volume(im4, alpha=(0.0, 1), alphaUnit=8, mode=4)

sig1 = Volume(im1, alpha=(0.0, 1), alphaUnit=1, mode=1)
sig2 = Volume(im2, c='bwr',alpha=(0.0, 1), alphaUnit=1, mode=1)
sig3 = Volume(im3, c='binary', alpha=(0.0, 1), alphaUnit=1, mode=1)
sig4 = Volume(im4, alpha=(0.0, 1), alphaUnit=1, mode=4)

sig3.show(axes=0,camera=cam1, bg='white')
#show(sig2, axes=1, camera=cam1)


#===IsosurfaceBrowser: surface rendering===
#from vedo.applications import IsosurfaceBrowser
#import matplotlib.cm as cm
#plt=IsosurfaceBrowser(vol3, c='grey')
#plt.show(axes=0, bg2='white')
#========================================

#===RaycastPlotter: colors and sliders===
#from vedo.applications import RayCastPlotter
#plt=RayCastPlotter(vol4)
#plt = plt.show(axes=0, bg2='white')

#========================================

#===Slicer 2D===
#from vedo.applications import Slicer2d
#plt=Slicer2d(sig2, levels=(None, None), size=(900, 900), zoom=1.2)
#plt.show()
#========================================

#===Slicer 3D===
#from vedo.applications import SlicerPlotter
#plt=SlicerPlotter(sig2)
#plt.show()
#========================================


#from vedo.io import Video
#vdo = Video(name='movie.mp4', duration=12, fps=24)
#vdo = action(elevation_range=(0,80), azimuth_range=(0,359), zoom=None, cam1=None, cam2=None, resetcam=False)
#vdo.close()

video= Video(outputgifname+'.mp4', duration =13, backend='opencv')
video.action(elevation_range=(-10,30), azimuth_range=(0,720), zoom=None, cam1=cam1, resetcam=True)
video.close()

from moviepy.editor import *
clip = (VideoFileClip(outputgifname+'.mp4').resize(0.5))
clip.write_gif(outputgifname+'.gif')
