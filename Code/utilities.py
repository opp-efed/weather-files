import os
import datetime as dt
import numpy as np
import pandas as pd


class WeatherCube(object):
    def __init__(self, weather_path, years=None, precip_points=None):
        from paths import weather_cube_path, grid_table_path, key_path
        self.storage_path = weather_cube_path
        self.key_path = grid_table_path
        self.dates_path = key_path
        self.columns = ["precip", "pet", "temp", "wind"]
        self.years = years
        self.precip_points = precip_points

        if years is None and precip_points is None:
            self.years, self.precip_points = self.load_key()
            print(self.years)

    def fetch(self, point_num):
        array = np.memmap(self.storage_path, mode='r', dtype=np.float32, shape=self.shape)
        out_array = array[:, point_num]
        del array
        dates = pd.date_range(self.start_date, self.end_date)
        return pd.DataFrame(data=out_array, columns=self.columns, index=dates)

    def load_key(self):
        years = np.genfromtxt(self.dates_path, delimiter=",").astype(np.int16)
        points = pd.read_csv(self.key_path, index_col=[0])
        return years, points

    @property
    def start_date(self):
        return dt.date(self.years[0], 1, 1)

    @property
    def end_date(self):
        return dt.date(self.years[-1], 12, 31)

    @property
    def shape(self):
        return (self.end_date - self.start_date).days + 1, self.precip_points.shape[0], len(self.columns)
