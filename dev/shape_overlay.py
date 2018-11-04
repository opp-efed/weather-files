import arcpy
import os

from paths import shapefile_path, weather_path
from parameters import nhd_regions


def initialize_grid(grid_file, sample_shape):
    arcpy.MakeXYEventLayer_management(grid_file, 'lon', 'lat', "points", sample_shape)
    return "points"


def main():
    for region in nhd_regions:
        shapefiles = ([os.path.join(shapefile_path, 'counties_fips.shp'), ('GEOID', 'county', 'state')],
                      [os.path.join(shapefile_path, 'anetd_poly.shp'), ('anetd',)],
                      [os.path.join(shapefile_path, 'rainfall_poly.shp'), ('rainfall',)])

        grid_file = os.path.join(weather_path.format(region), 'weather_grid.csv')



main()
