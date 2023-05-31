from osmium.osm import OSMObject

from manipulation.manipulate_geodataframe import MyGeoDataFrame
from osm_features.abstract.super_osm_feature import AbstractOSM
import geopandas as gpd


class OSMCommon(AbstractOSM):
    """OSMObject with the common procedures"""
    def __init__(self, osm_feature: OSMObject, key_tag: str) -> None:
        self.dataframe = MyGeoDataFrame(osm_feature, key_tag)
        super(OSMCommon, self).__init__(dataframe=self.dataframe)
        super().create_geometry()
        self.dataframe.gpdf = self.manipulate_dataframe()
        super().export_data()

    def manipulate_dataframe(self) -> gpd.GeoDataFrame:
        """Unique dataframe attribute manipulation"""
        self.dataframe.gpdf = super().set_dataframe()
        self.dataframe.gpdf = self.dataframe.reduce_columns(attributes=[self.dataframe.key_tag])
        return self.dataframe.gpdf
