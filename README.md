# PythonFinalProject
This is a repository for my final project for Python 3200K

For my project, I wanted to write some code that would perform an unsupervised classification on an image using the Iso Cluster and Maximum Likelihood Classification tools and then extract the polygons that were classified as "urban."

Requirements
ESRI’s Spatial Analyst extension for ArcMap offers tools to help accomplish this classification, both within ArcMap environment and externally in the Python scripting environment by means of ESRI’s arcpy and arcpy.sa modules. Arcpy and arcpy.sa, together, offer access to all of ArcMap’s geoprocessing tools and Spatial Analyst’s more specialized toolbox. For classification purposes, Spatial Analyst offers the ISO Unsupervised Classification tool, which “performs unsupervised classification on a series of input raster bands using the Iso Cluster and Maximum Likelihood Classification tools.”

Modules
•	Arcpy – for the use of geoprocessing tools and environment settings
•	Arcpy.sa – the Spatial Analyst extension for the Iso Unsupervised Classification

Environments
	Since the code is designed to be used as a repetitive workflow, it was important to allow overwriting of existing data. For this reason, the env.overwriteOutput was set to ‘True.’

Process
•	Import necessary modules
•	Set up workspace
•	Extract by Mask NAIP_10m.tif by ClarkeCounty.shp
•	Checkout the ArcGIS Spatial Analyst extension license
•	Execute Extract by Mask
  IsoCluster tool
  •	Check out the ArcGIS Spatial Analyst extension license
  •	Execute IsoCluster
  Raster to Polygon tool
  •	Set local variables
  •	Execute RasterToPolygon
  Extract by attribute tool
  •	Set local variables
  •	Check out Spatial Analyst extension license
  •	Execute Extract by Attributes
  •	Save the output
  Raster to Polygon tool for urban extract file
  •	Set local variables
  •	Execute RasterToPolygon
  Create a new field
  •	Set local variables
  •	Execute AddField for new field
  •	Calculate Geometry of Area field with Calculate Field Tool	
