import geopandas
from osmium.osm import OSMObject

from manipulation.manipulate_geodataframe import MyGeoDataFrame
from osm_features.abstract.super_osm_feature import AbstractOSM


class OSMWayHighway(AbstractOSM):
    def __init__(self, osm_feature: OSMObject, key_tag: str, count: int = None) -> None:
        self.dataframe = MyGeoDataFrame(osm_feature, key_tag)
        super(OSMWayHighway, self).__init__(dataframe=self.dataframe)
        super().create_geometry()
        self.dataframe.gpdf = self.manipulate_dataframe()
        file_number: int = (count//50000)+1
        super().export_data(filename=f"highway_{file_number}")
        self.dataframe.gpdf = self.dataframe.reduce_columns(attributes=[self.dataframe.key_tag, "ref"])
        super().export_data(filename=f"highway_egyben_{file_number}")
        print(f"Highway {file_number} as {count} exported")

    def manipulate_dataframe(self) -> geopandas.GeoDataFrame:
        self.dataframe.gpdf = super().set_dataframe()
        self.dataframe.gpdf = self.dataframe.extra_columns(attributes=["bridge", "tunnel", "ref"])
        self.dataframe.gpdf = self.dataframe.reduce_columns(
            attributes=[self.dataframe.key_tag, "bridge", "tunnel", "ref"])
        return self.dataframe.gpdf


