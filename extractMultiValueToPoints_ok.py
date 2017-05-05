
import arcpy,os,arcgisscripting
from arcpy import mapping
os.system('cls')
gp = arcgisscripting.create(9.3)
gp.CheckOutExtension("Spatial")

entrada = r"W:\_chirps" 
gp.workspace = entrada

rasters = gp.ListRasters("", "TIF")
print "listando"
points = r"D:\Personal\_colaboraciones\_harold\_shp\points.shp"

for layer in rasters:
	print layer
	arcpy.sa.ExtractMultiValuesToPoints(points, layer, 'NONE')

print "Finish"
  
