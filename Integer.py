# Importar Modulos
import arcgisscripting, os, sys, string
gp = arcgisscripting.create(9.3)
gp.CheckOutExtension("Spatial")
os.system('cls')

entrada = raw_input("\ncarpeta entrada (carpeta con los raster a convertir a entero )")

salida = raw_input("\ncarpeta salida ")

# Si la carpeta de salida no existe con las siguientes dos lineas se pueden crear
if not os.path.exists(salida):
	os.system('mkdir ' + salida)

gp.workspace = entrada #se sentencia el espacio de trabajo
rasters = gp.ListRasters("*","TIF") #listamos los archivos raster que estan en la carpeta de entrada, el TIF se usa para que solamente liste los archivos tif, esto es util en caso dado que en la carpeta tengamos datos ascii, grids, entre otros.

# Las lineas de print se usan cuando queremos ver que esta haciendo el cpdigo, para usarlas simplemente eliminamos el simbolo #

#print entrada 

#Ahora se realiza un ciclo, con el cual se hace el mismo proceso para todos los raster existentes en la carpeta
for raster in rasters:
	#print rasters
	conversion = salida + "\\" + 'int' + raster#sentenciamos la ruta de los archivos de salida
	print raster
	print conversion
	gp.Int_sa(raster, conversion) #es la linea que hace la conversion de float a entero, es la misma funcion "Int" existente dentro de ArcGIS
print "ya existe --> " + conversion
print "Proceso terminado !!!" 