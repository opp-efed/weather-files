import arcpy
import os
import numpy as np
import csv


def weather_points_to_shapefile(points_file, out_file, template):
    """ Convert a file of weather points into a nearest station raster """

    # Read in the weather station points
    arcpy.MakeXYEventLayer_management(points_file, 'lon', 'lat', "temp_lyr", arcpy.SpatialReference(4326))
    arcpy.Project_management("temp_lyr", out_file, template)
    arcpy.Delete_management("temp_lyr")

def weather_points_to_raster(points_file, out_raster):  # Create a nearest-point raster
    arcpy.CreateThiessenPolygons_analysis(points_file, "in_memory/tp", "ALL")
    arcpy.FeatureToRaster_conversion("in_memory/tp", "weather_gr", out_raster, cell_size=30)
    arcpy.Delete_management("in_memory/tp")


def main():
    from paths import grid_table_path, grid_shapefile_path, grid_raster_path, template_raster

    arcpy.env.cellSize = 30
    arcpy.env.snapRaster = template_raster
    arcpy.env.overwriteOutput = True

    weather_points_to_shapefile(grid_table_path, grid_shapefile_path, template_raster)
    weather_points_to_raster(grid_shapefile_path, grid_raster_path)


main()
