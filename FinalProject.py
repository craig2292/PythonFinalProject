import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "F:\Fall2015\Python\PythonProject\Data"



#IsoCluster Tool
inRaster = "F:\Fall2015\Python\PythonProject\Data\Image\ClarkeCo.tif"
classes = 6
minMembers = 20
sampInterval = 10

#Checkout the ArcGIS Spatial Analyst Extension License
arcpy.CheckOutExtension("Spatial")

#Execute IsoCluster
outUnsupervised = IsoClusterUnsupervisedClassification(inRaster, classes, minMembers, sampInterval)

#Save the Output
outUnsupervised.save("F:\Fall2015\Python\PythonProject\Data\Outputs\AOI_IsoClust.tif")





#Raster to Polygon Tool
inRaster = "F:\Fall2015\Python\PythonProject\Data\Outputs\AOI_IsoClust.tif"
outPolygons = "F:\Fall2015\Python\PythonProject\Data\Outputs\Polygons.shp"
field = "VALUE"

#Execute Raster To Polygon
arcpy.RasterToPolygon_conversion(inRaster, outPolygons, "NO_SIMPLIFY", field)

#Extract by Attributes Tool
inRaster = "F:\Fall2015\Python\PythonProject\Data\Outputs\AOI_IsoClust.tif"
inSQLClause = "VALUE = 1"

#Check out the ArcGIS Spatial Analyst Extension License
arcpy.CheckOutExtension("Spatial")

#Execute Extract by Attributes
attExtract = ExtractByAttributes(inRaster, inSQLClause)

#Save the Output
attExtract.save("F:\Fall2015\Python\PythonProject\Data\Outputs\WaterExtract.tif")



#Raster to Polygon tool for water extract
inRaster = "F:\Fall2015\Python\PythonProject\Data\Outputs\WaterExtract.tif"
outPolygons = "F:\Fall2015\Python\PythonProject\Data\Outputs\WaterPolygons.shp"
field = "VALUE"

#Execute Raster to Polygon
arcpy.RasterToPolygon_conversion(inRaster, outPolygons, "NO_SIMPLIFY", field)



#Create new field
inFeatures = "F:\Fall2015\Python\PythonProject\Data\Outputs\WaterPolygons.shp"
fieldName1 = "Area"
fieldPrecision = 15
fieldAlias = "refcode"
fieldName2 = "status"
fieldLength = 15

#Execute AddField for new field
arcpy.AddField_management(inFeatures, fieldName1, "FLOAT", fieldPrecision, "", "", fieldAlias, "NULLABLE")

#Calculate Geometry of Area field with Calculate Field tool
arcpy.CalculateField_management(inFeatures, fieldName1, "!SHAPE.area!", "PYTHON_9.3")

#Select by Attribute Area greater than 700,000 square meters
arcpy.MakeFeatureLayer_management("F:\Fall2015\Python\PythonProject\Data\Outputs\WaterPolygons.shp", "Outlyr")

arcpy.SelectLayerByLocation_management ("Outlyr", "intersect", "F:\Fall2015\Python\PythonProject\Data\Outputs\Polygons.shp", 0, "new_selection")
arcpy.SelectLayerByAttribute_management("Outlyr", "SUBSET_SELECTION", ' "AREA" > 700000 ')
arcpy.CopyFeatures_management("Outlyr", "LakeChapman")

#Dissolve Tool to create final Output file
arcpy.Dissolve_management("LakeChapman.shp", "F:\Fall2015\Python\PythonProject\Data\LakeChapmanDissolved.shp", ["GRIDCODE"], "", "MULTI_PART", "DISSOLVE_LINES")
