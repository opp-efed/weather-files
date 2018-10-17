import os

project_path = os.path.join("..", "bin")
input_path = os.path.join(project_path, "MetData")
output_path = os.path.join(project_path, "Output")

weather_cube_path = os.path.join(output_path, "weather_cube.dat")
key_path = os.path.join(output_path, "key.csv")
grid_table_path = os.path.join(output_path, "weather_grid.csv")
grid_shapefile_path = os.path.join(output_path, "weather_grid.shp")
grid_raster_path = os.path.join(output_path, "weather_grid.tif")
template_raster = r"C:\Users\Admin\Documents\NationalData\CustomSSURGO\al\al"

