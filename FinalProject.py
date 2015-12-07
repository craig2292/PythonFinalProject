##Import Necessary Modules
import arcpy
from arcpy import env
from arcpy.sa import *


##Set up workspace
env.workspace = "E:\Fall2015\Python\PythonProject\Data"
env.overwriteOutput = True


## Extract by mask NAIP_10m.tif by AOI
inRaster = "Data\Image\NAIP_10m.tif"
inMaskData = "Data\Image\ClarkeCounty.shp"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute ExtractByMask
outExtractByMask = ExtractByMask(inRaster, inMaskData)

# Save the output 
outExtractByMask.save("E:\Fall2015\Python\PythonProject\Data\Outputs\ClarkeCo.tif")





#IsoCluster Tool
inRaster = "E:\Fall2015\Python\PythonProject\Data\Outputs\ClarkeCo.tif"
classes = 6
minMembers = 20
sampInterval = 10

#Checkout the ArcGIS Spatial Analyst Extension License
arcpy.CheckOutExtension("Spatial")

#Execute IsoCluster
outUnsupervised = IsoClusterUnsupervisedClassification(inRaster, classes, minMembers, sampInterval)

#Save the Output
outUnsupervised.save("E:\Fall2015\Python\PythonProject\Data\Outputs\AOI_IsoClust.tif")





#Raster to Polygon Tool
inRaster = "E:\Fall2015\Python\PythonProject\Data\Outputs\AOI_IsoClust.tif"
outPolygons = "E:\Fall2015\Python\PythonProject\Data\Outputs\Polygons.shp"
field = "VALUE"

#Execute Raster To Polygon
arcpy.RasterToPolygon_conversion(inRaster, outPolygons, "NO_SIMPLIFY", field)

#Extract by Attributes Tool
inRaster = "E:\Fall2015\Python\PythonProject\Data\Outputs\AOI_IsoClust.tif"
inSQLClause = "VALUE = 6"

#Check out the ArcGIS Spatial Analyst Extension License
arcpy.CheckOutExtension("Spatial")

#Execute Extract by Attributes
attExtract = ExtractByAttributes(inRaster, inSQLClause)

#Save the Output
attExtract.save("E:\Fall2015\Python\PythonProject\Data\Outputs\UrbanExtract.tif")



#Raster to Polygon tool for urban extract
inRaster = "E:\Fall2015\Python\PythonProject\Data\Outputs\UrbanExtract.tif"
outPolygons = "E:\Fall2015\Python\PythonProject\Data\Outputs\UrbanPolygons.shp"
field = "VALUE"

#Execute Raster to Polygon
arcpy.RasterToPolygon_conversion(inRaster, outPolygons, "NO_SIMPLIFY", field)



#Create new field
inFeatures = "E:\Fall2015\Python\PythonProject\Data\Outputs\UrbanPolygons.shp"
fieldName1 = "Area"
fieldPrecision = 15
fieldAlias = "refcode"
fieldName2 = "status"
fieldLength = 15

#Execute AddField for new field
arcpy.AddField_management(inFeatures, fieldName1, "FLOAT", fieldPrecision, "", "", fieldAlias, "NULLABLE")

#Calculate Geometry of Area field with Calculate Field tool
arcpy.CalculateField_management(inFeatures, fieldName1, "!SHAPE.area!", "PYTHON_9.3")

#Select by Attribute Area greater than 0 square meters
arcpy.MakeFeatureLayer_management("E:\Fall2015\Python\PythonProject\Data\Outputs\UrbanPolygons.shp", "Outlyr")

arcpy.SelectLayerByLocation_management ("Outlyr", "intersect", "E:\Fall2015\Python\PythonProject\Data\Outputs\Polygons.shp", 0, "new_selection")
arcpy.SelectLayerByAttribute_management("Outlyr", "SUBSET_SELECTION", ' "AREA" > 0 ')
arcpy.CopyFeatures_management("Outlyr", "Urban")
