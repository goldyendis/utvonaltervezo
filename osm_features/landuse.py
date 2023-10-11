import geopandas
from osmium.osm import OSMObject
from manipulation.manipulate_geodataframe import MyGeoDataFrame
from osm_features.abstract.super_osm_feature import AbstractOSM


class OSMAreaLanduse(AbstractOSM):
    """Processor of the Landuse Area OSM Entities"""
    def __init__(self, osm_feature: OSMObject, key_tag: str) -> None:
        self.dataframe = MyGeoDataFrame(osm_feature, key_tag)
        super(OSMAreaLanduse, self).__init__(dataframe=self.dataframe)
        super().create_geometry()
        self.dataframe.gpdf = self.manipulate_dataframe
        super().export_data()

    def manipulate_dataframe(self) -> geopandas.GeoDataFrame:
        self.dataframe.gpdf = super().set_dataframe()
        if super().key_tag_value == "basin":
            self.dataframe.gpdf = self.dataframe.rename_column("landuse", "water")
            self.dataframe.key_tag = "water"
        self.dataframe.gpdf = self.dataframe.reduce_columns(attributes=[self.dataframe.key_tag])
        return self.dataframe.gpdf
