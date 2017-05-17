import sys, os, arcpy

# Set environment settings
#env.workspace = "W:/SBA/tmp/"
arcpy.env.overwriteOutput = True
from arcpy import env


# Create the geoprocessor object
try:
    # 9.2 and beyond    
    import arcgisscripting
    gp = arcgisscripting.create()
    print "\nImporting geoprocessor for 9.2 and beyond..."    
except:    
    # 9.1 and before    
    import win32com.client
    gp = win32com.client.Dispatch("esriGeoprocessing.GpDispatch.1")
    print "\nImporting geoprocessor for 9.1 and before..."
    
targetFeatures = "W:/SBA/shapefiles/sba_data/"
joinFeatures = "W:/My Data/Shapefiles/CongressionalDistricts/"
outfc = "W:/SBA/shapefiles/sba_districts_join/"
outascii = "W:/SBA/data/"

# Read all the shapefiles in folder 'targetFeatures'
for shp in os.listdir(targetFeatures):
    if shp.endswith('shp'):        
        # Split on the extension
        base = shp.split(".")
        # Get the numbers
        code = base[0][-3:]
        
        # Do it
        print "Joining "+targetFeatures+shp+" with "+joinFeatures+"districts"+code+".shp to get "+outfc+shp
        gp.SpatialJoin(targetFeatures+shp, joinFeatures+"districts"+code+".shp", outfc+shp, "JOIN_ONE_TO_ONE", "KEEP_ALL")		
print "\nDone."
