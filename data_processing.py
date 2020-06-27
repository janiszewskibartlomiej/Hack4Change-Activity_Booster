from connect_to_db import ConnectToDb


class DataProcessing:
    def __init__(self):
        super().__init__()
        self.connection = ConnectToDb()

        self.interval = {
            "#29a329": [1, 1000],
            "#196619": [1000, 5000],
            "#f2c718": [5000, 10000],
            "#ffcc00": [10000, 25000],
            "#ff9900": [25000, 50000],
            "#ff5c33": [50000, 100000],
            "#ff3300": [100000, 150000],
            "#ff3333": [150000, 250000],
            "#ff0000": [250000, 100 ** 10],
        }

    def get_all_towns(self):
        select = self.connection.select_all_records(
            query=r"SELECT * from towns",
            parameter="",
        )
        return select

    def get_icon_color(self, number_of_cases):
        for key, volume in self.interval.items():
            if volume[1] > number_of_cases >= volume[0]:
                return key

    def slice_location(self, coordinates_str):
        coordinates_str = coordinates_str.replace("[", "")
        coordinates_str = coordinates_str.replace("]", "")
        coordinates_split = coordinates_str.split(", ")
        latitude = float(coordinates_split[0])
        longitude = float(coordinates_split[1])
        coordinates = [latitude, longitude]
        return coordinates

