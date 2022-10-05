import arcpy
from os import *

#本程序用于将一个文件夹下的所有栅格转为矢量

raster_path = r'E:\project_xinjiang\forest\3-predict_result_0915'#输入的栅格文件夹路径
polygon_path = r'E:\project_xinjiang\forest\4-polygon'#输出的矢量文件夹路径
for raster in listdir(raster_path):
    file_type = raster.split('.')[-1]
    # print(file_type)
    if(file_type=='tif'):
        file_name = raster.split('.')[0]
        # print(file_name)
        arcpy.RasterToPolygon_conversion(path.join(raster_path,raster), path.join(polygon_path,file_name+'.shp'), "NO_SIMPLIFY", 'Value')