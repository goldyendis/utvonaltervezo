import geopandas
from manipulation.manipulate_geodataframe import MyGeoDataFrame
from utils.new_typing import OSMWay, OSMNode
from osm_features.abstract.super_osm_feature import AbstractOSM


class OSMWayRailway(AbstractOSM):
    def __init__(self, osm_feature: OSMWay, key_tag: str) -> None:
        self.dataframe = MyGeoDataFrame(osm_feature, key_tag)
        super(OSMWayRailway, self).__init__(dataframe=self.dataframe)
        super().create_geometry()
        self.dataframe.gpdf = self.manipulate_dataframe()
        super().export_data()
        self.dataframe.gpdf = self.dataframe.reduce_columns(attributes=[self.dataframe.key_tag, "service", "usage"])
        super().export_data(filename="railway_egyben")

    def manipulate_dataframe(self) -> geopandas.GeoDataFrame:
        self.dataframe.gpdf = super().set_dataframe()
        self.dataframe.gpdf = self.dataframe.extra_columns(
            attributes=["bridge", "tunnel", "service", "usage", "station"])
        self.dataframe.gpdf = self.dataframe.reduce_columns(
            attributes=[self.dataframe.key_tag, "tunnel", "bridge", "service", "usage", "station"])
        return self.dataframe.gpdf


class OSMNodeRailway(AbstractOSM):
    def __init__(self, osm_feature: OSMNode, key_tag: str) -> None:
        self.dataframe = MyGeoDataFrame(osm_feature, key_tag)
        super(OSMNodeRailway, self).__init__(dataframe=self.dataframe)
        super().create_geometry()
        self.dataframe.gpdf = self.manipulate_dataframe()
        super().export_data()

    def manipulate_dataframe(self) -> geopandas.GeoDataFrame:
        self.dataframe.gpdf = super().set_dataframe()
        self.dataframe.gpdf = self.dataframe.extra_columns(attributes=["station", "subway"])
        self.dataframe.gpdf = self.dataframe.reduce_columns(
            attributes=[self.dataframe.key_tag, "station", "subway"])
        return self.dataframe.gpdf
