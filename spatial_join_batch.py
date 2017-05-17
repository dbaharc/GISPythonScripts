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

masterpath = "X:/Raj Dany/geocoding/"
targetFeatures = masterpath + "intermediate/"
joinFeature = masterpath + "airportsData/XYAirportsWCountryCodes.shp"
output = masterpath + "output/"

# Read all the shapefiles in folder 'targetFeatures'
for shp in os.listdir(targetFeatures):
    if shp.startswith('XY'):        
        # Split on the extension
        base = shp.split(".")
        # Get the numbers
        code = base[2][-3:]
        outfc = intermediate + code + "Airports.sph
        # Do it
        print "Joining "+targetFeatures+shp+" with "+joinFeature + "to get "+ outfc
        gp.SpatialJoin(targetFeatures+shp, joinFeature, outfc, "JOIN_ONE_TO_MANY", "KEEP_ALL","WITHIN_A_DISTANCE","50 Miles","#")
        gp.ExportXYv_stats(outfc,"gc_pairid;lat;lon;airportid;airportNam;airportCod;airportC_1;airportISO;airportI_1","COMMA",output + base + "Airports.csv","ADD_FIELD_NAMES")
print "\nDone."
