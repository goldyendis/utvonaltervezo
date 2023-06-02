import geopandas
from osmium.osm import OSMObject

from manipulation.manipulate_geodataframe import MyGeoDataFrame
from osm_features.abstract.super_osm_feature import AbstractOSM


class OSMNodeManMade(AbstractOSM):
    def __init__(self, osm_feature: OSMObject, key_tag: str) -> None:
        self.dataframe = MyGeoDataFrame(osm_feature, key_tag)
        super(OSMNodeManMade, self).__init__(dataframe=self.dataframe)
        super().create_geometry()
        self.dataframe.gpdf = self.manipulate_dataframe()
        super().export_data()

    def manipulate_dataframe(self) -> geopandas.GeoDataFrame:
        self.dataframe.gpdf = super().set_dataframe()
        self.dataframe.gpdf = self.dataframe.get_man_made_value()
        self.dataframe.gpdf = self.dataframe.reduce_columns(
            attributes=[self.dataframe.key_tag, "tower_type"])
        return self.dataframe.gpdf


class OSMWayManMade(AbstractOSM):
    def __init__(self, osm_feature: OSMObject, key_tag: str) -> None:
        self.dataframe = MyGeoDataFrame(osm_feature, key_tag)
        super(OSMWayManMade, self).__init__(dataframe=self.dataframe)
        super().create_geometry()
        self.dataframe.gpdf = self.manipulate_dataframe()
        super().export_data()

    def manipulate_dataframe(self) -> geopandas.GeoDataFrame:
        self.dataframe.gpdf = super().set_dataframe()
        if super().key_tag_value == "goods_conveyor":
            self.dataframe.rename_column("man_made", "aerialway")
            self.dataframe.key_tag = "aerialway"
        self.dataframe.gpdf = self.dataframe.reduce_columns(attributes=[self.dataframe.key_tag])
        return self.dataframe.gpdf
