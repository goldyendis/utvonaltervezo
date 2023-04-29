from manipulation.manipulate_geodataframe import MyGeoDataFrame
from utils.new_typing import OSMArea
from osm_features.abstract.super_osm_feature import AbstractOSM
import geopandas as gpd


class OSMAreaLanduse(AbstractOSM):
    def __init__(self, osm_feature: OSMArea, key_tag: str) -> None:
        self.dataframe = MyGeoDataFrame(osm_feature, key_tag)
        super(OSMAreaLanduse, self).__init__(dataframe=self.dataframe)
        super().create_geometry()
        self.dataframe.gpdf = self.manipulate_dataframe()
        super().export_data()

    def manipulate_dataframe(self) -> gpd.GeoDataFrame:
        self.dataframe.gpdf = super().manipulate_dataframe()
        if super().key_tag_value == "basin":
            self.dataframe.gpdf = self.dataframe.rename_column("landuse", "water")
            self.dataframe.key_tag = "water"
        self.dataframe.gpdf = self.dataframe.reduce_columns(attributes=[self.dataframe.key_tag])
        return self.dataframe.gpdf
