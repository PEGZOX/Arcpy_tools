import pandas as pd
import osgeo.ogr as ogr
import osgeo.osr as osr

aral_csv_path = r'D:\硕士毕业论文\aral.csv'
aral_poi_path = r'D:\硕士毕业论文\aral_point.shp'

#根据csv生成矢量结果
def csv_toPoint(csv_path,point_path):

    point_data = pd.read_csv(csv_path)
    
    #创建空的点shp文件
    driver = ogr.GetDriverByName('ESRI Shapefile')
    data_source = driver.CreateDataSource(point_path)
    proj = osr.SpatialReference()
    proj.ImportFromEPSG(4326)
    layer = data_source.CreateLayer('test',proj,ogr.wkbPoint)

    #创建字段
    columns_names_raw = ['Latitude','Longitude','Along-Track (m)','point_num','std','time','beam','Height (m MSL)']#原表中的列名
    columns_names = ['Latitude','Longitude','AT','point_num','std','time','beam','Height']#shp文件的对应的列名，因为有长度限制，所以需要对原表中部分列名进行修改
    for col in columns_names:
        if(col=='Height'):
        #height字段为了后面的计算，设置为float字段
            field_name = ogr.FieldDefn(col,ogr.OFTReal)
            field_name.SetWidth(20)#设置自然数的位数
            field_name.SetPrecision(6)#设置小数的位数，必须要设置这个，否则好像默认位数为0，输出为int，网上找了好多资料才找到
            layer.CreateField(field_name)
        else:
        #其他字段都自动设为string字段
            field_name = ogr.FieldDefn(col,ogr.OFTString)
            field_name.SetWidth(20)
            layer.CreateField(field_name)
    
    #填入字段
    for poi in range(point_data.shape[0]):
        feature = ogr.Feature(layer.GetLayerDefn())
        for col_num in range(len(columns_names)):
            if(columns_names[col_num]=='Height'):
                feature.SetField(columns_names[col_num],float(point_data[columns_names_raw[col_num]][poi]))
            else:
                feature.SetField(columns_names[col_num],str(point_data[columns_names_raw[col_num]][poi]))
        point = ogr.Geometry(ogr.wkbPoint)
        #设置点的经纬度
        point.AddPoint(float(point_data['Longitude'][poi]),float(point_data['Latitude'][poi]))
        feature.SetGeometry(point)
        layer.CreateFeature(feature)
        feature.Destroy()
    data_source.Destroy()    

csv_toPoint(aral_csv_path,aral_poi_path)        
