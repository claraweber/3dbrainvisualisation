# 3dbrainvisualisation
---
vedo-based application to create 3D animations, gifs and mp4s from Nifti files. 
different Python files contain several options for plotting, including Volume plotting (plotvol, isobrow), coloring significant voxels (plotsig) and an interactive plotting (raycast). 
Get started by
- downloading the files in the same folder your niftis are in
- specify file paths in the beginning of .py-files
- specify output name
- preinstall libraries needed (given at the beginning of each script)
---
This code was written to show three files simultaneously (surface, white matter skeleton, significant voxels). You can specify less or more than three. In an intermediate step, they will be added up together and weighted to adjust contrast. If errors occur in this step, coregister them using FSL flirt.
Unfortunately, there is limited compatibility with Jupyter notebook.

---
Any questions? Reach out to me! 
