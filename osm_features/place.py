import geopandas
from manipulation.manipulate_geodataframe import MyGeoDataFrame
from utils.new_typing import OSMNode
from osm_features.abstract.super_osm_feature import AbstractOSM


class OSMNodePlace(AbstractOSM):
    def __init__(self, osm_feature: OSMNode, key_tag: str) -> None:
        self.dataframe = MyGeoDataFrame(osm_feature, key_tag)
        super(OSMNodePlace, self).__init__(dataframe=self.dataframe)
        super().create_geometry()
        self.dataframe.gpdf = self.manipulate_dataframe()
        super().export_data()

    def manipulate_dataframe(self) -> geopandas.GeoDataFrame:
        self.dataframe.gpdf = super().manipulate_dataframe()
        self.dataframe.gpdf = self.dataframe.extra_columns(attributes=["population"])
        self.dataframe.gpdf = self.dataframe.reduce_columns(
            attributes=[self.dataframe.key_tag, "population"])
        return self.dataframe.gpdf
