# -*- coding: utf-8 -*- 
import os
import arcpy

#本程序用于将一个文件夹中的影像融合到另一个文件夹中的影像波段中去
#融合的依据是文件名相类似
raster_img_path =r'D:\BaiduNetdiskDownload\tmp\1-clip_img'
add_img_path =r'D:\BaiduNetdiskDownload\tmp\project'

output_path=r'D:\BaiduNetdiskDownload\tmp\band_merge'


for raster in os.listdir(raster_img_path):
    if(raster.split('.')[-1]=='tif'):
        #xj_fg_T44_8.tif
        for add_img in os.listdir(add_img_path):
            if(add_img.split('.')[-1]=='tif'):
                #dem_xj_fg_T44_8.tif
                if(add_img[4:]==raster):
                    print('yes')
                    arcpy.CompositeBands_management(
                        os.path.join(raster_img_path,raster)+';'+
                        os.path.join(add_img_path,add_img),
                        os.path.join(output_path,'merge'+raster))

