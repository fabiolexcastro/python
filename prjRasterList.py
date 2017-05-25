import arcpy,os,arcgisscripting
from arcpy import mapping
os.system("cls")
gp = arcgisscripting.create(9.3)
gp.CheckOutExtension("Spatial")
entrada = "W:/_africaCoffee/_RF/_arabica/_results/_process/_diff/_tif"
salida = "W:/_africaCoffee/_RF/_arabica/_results/_process/_diff/_tif"
sistema_code = 'PROJCS["WGS_1984_UTM_Zone_36S",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",10000000.0],PARAMETER["Central_Meridian",33.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0],AUTHORITY["EPSG",32736]]'
gp.workspace = entrada
rasters = gp.ListRasters("","TIF")
for raster in rasters:
    gp.workspace = salida
    entreRas = entrada + "/" + raster
    sale = salida + "/prj_" + raster
    entra = entrada + "/" + raster
    print entreRas
    arcpy.ProjectRaster_management(entra, sale, sistema_code) 
print("Finish...")
