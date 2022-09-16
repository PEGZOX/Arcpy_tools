import arcpy
from os import *

raster_path = r'E:\project_xinjiang\forest\3-predict_result_0915'
polygon_path = r'E:\project_xinjiang\forest\4-polygon'
for raster in listdir(raster_path):
    file_type = raster.split('.')[-1]
    # print(file_type)
    if(file_type=='tif'):
        file_name = raster.split('.')[0]
        # print(file_name)
        arcpy.RasterToPolygon_conversion(path.join(raster_path,raster), path.join(polygon_path,file_name+'.shp'), "NO_SIMPLIFY", 'Value')