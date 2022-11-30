给字段赋值
import os
import arcpy

pathfile = r"E:\conf_split\4.dissolve"
for file in os.listdir(pathfile):
    if file[-3:] == "shp":
        arcpy.AddField_management(os.path.join(pathfile, file), "id", "TEXT", field_length=12)
        cursor = arcpy.UpdateCursor(os.path.join(pathfile, file))
        for row in cursor:
            row.setValue("id", file[:-4])
            cursor.updateRow(row)  #这句话不写赋值不会生效