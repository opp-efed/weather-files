from utilities import WeatherCube
from paths import output_path


wc = WeatherCube(output_path)

print(wc.precip_points)
a = wc.fetch(10000)

