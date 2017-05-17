# MakeXYLayer.py
# Description: Creates an XY layer and exports it to a layer file

# import system modules 
import arcpy, sys, os
from arcpy import env

# Set environment settings
#env.workspace = "W:/SBA/tmp/"
arcpy.env.overwriteOutput = True

# Set environment settings
repository = "W:/Raj Dany/geocoding/"
x_coords = "lon"
y_coords = "lat"

# Read all the shapefiles in folder 'targetFeatures'
for file in os.listdir(repository):
    if file.endswith('txt'):
    	in_Table = repository + file
    	print in_Table
    	base = file.split(".")
    	code = base[0][-3:]
    	out_Layer = "Awards" + code + "_Layer"
    	saved_Layer = repository + "XY" + code + ".lyr"
    	saved_Shp = repository + "XY" + code + ".shp"
    	# Set the spatial reference
        spRef = "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],\
               PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];\
               -400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;\
               0.001;0.001;IsHighPrecision"
    	#spRef = "GEOGCS['NAD83',DATUM['North_American_Datum_1983',SPHEROID['GRS 1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision"
    	# Make the XY event layer...
    	arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef)
    	# Print the total rows
    	print arcpy.GetCount_management(out_Layer)
    	# Save to a layer and shapefile file
    	arcpy.SaveToLayerFile_management(out_Layer, saved_Layer)
    	arcpy.CopyFeatures_management(saved_Layer, saved_Shp)  
    	os.remove(saved_Layer)
        
