from Code.utilities import WeatherCube
from Code.paths import output_path


conus_cube = WeatherCube('conus')

from Code.utilities import nhd_regions

conus_indices = set(conus_cube.points.index)
for region in nhd_regions:
    print(region)
    region_cube = WeatherCube(region)
    region_indices = set(region_cube.points.index)
    for point in region_indices:
        a = conus_cube.fetch(point)
        b = region_cube.fetch(point)
        try:
            c = a - b
            if c.sum().sum() > 0:
                print(c.sum())
        except TypeError:
            print(point)
            print(a)
            print(b)
            input()