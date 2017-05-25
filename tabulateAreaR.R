

require(raster)
require(rgdal)
require(tidyverse)
require(foreign)
require(spdplyr)
require(data.table)

##### Function ##### 

tabArea <- function(path_raster, name_raster, name_field, shp_zone, out_table, nameCode){
  
  sink(paste0(path, '/_codes/', nameCode, '.py'))
  cat('import arcpy', fill = T)
  cat('from arcpy import env', fill = T)
  cat('from arcpy.sa import *', fill = T)
  cat(paste0('arcpy.env.workspace = ', '"', path_raster, '"'), fill = T)
  cat(paste0('env.extent = ', '"', name_raster, '"'), fill = T)
  cat(paste0('env.snapRaster = ', '"', name_raster, '"'), fill = T)
  cat(paste0('inZoneData = ', '"', name_raster, '"'), fill = T)
  cat('desc = arcpy.Describe(inZoneData)', fill = T)
  cat('zoneField = "VALUE"', fill = T)
  cat(paste0('inClassData = ', '"', shp_zone, '"'), fill = T)
  cat(paste0('classField = ', '"', name_field, '"'), fill = T)
  cat(paste0('outTable = ', '"', out_table, '"'), fill = T)
  cat('arcpy.processingCellSize = desc.meanCellHeight', fill = T)
  cat('print "Process"', fill = T)
  cat('arcpy.CheckOutExtension("Spatial")', fill = T)
  cat('TabulateArea(inZoneData, zoneField, inClassData, classField, outTable, arcpy.processingCellSize)', fill = T)
  cat('print "Finish"', fill = T)
  sink()
  
  system(paste0('python D:/directory/', nameCode, '.py'))
  
}


#### Execute function ####

path  <- 'D:/directory/_data'
files <- list.files(paste0(path, '/_raster'), full.names = T, pattern = '.tif$')
basin <- shapefile(paste0(path, '/_shp/shapefile.shp'))
namesBasin <- as_data_frame(apply(basin@data,2,function(x)gsub('//s+', '',x)))$name_field
basin <- mutate(basin, NameOk = substr(namesBasin, 1, 10))

detach("package:spdplyr", unload=TRUE)
writeOGR(basin, dsn = paste0(path, '/_shp'), layer = 'cuencas_prj', driver = 'ESRI Shapefile') 

for(i in 1:length(files)){ 
  
  print(basename(files[[i]]))
  
  tabArea(path_raster = paste0(path, '/_raster'),
          name_raster = basename(files[[i]]),
          name_field = 'NamePolygons',
          shp_zone = paste0(path, '/_shp/shapefile.shp'),
          out_table = paste0(path, '/_tables/tabArea', unlist(strsplit(basename(files[[i]]), '.tif')), '.dbf'),
          nameCode = 'tabAreaHansen') 
  
} 
