import geopandas
from osmium.osm import OSMObject

from manipulation.manipulate_geodataframe import MyGeoDataFrame
from osm_features.abstract.super_osm_feature import AbstractOSM


class OSMAreaHighway(AbstractOSM):
    def __init__(self, osm_feature: OSMObject, key_tag: str) -> None:
        self.dataframe = MyGeoDataFrame(osm_feature, key_tag)
        super(OSMAreaHighway, self).__init__(dataframe=self.dataframe)
        super().create_geometry()
        self.dataframe.gpdf = self.manipulate_dataframe()
        super().export_data()

    def manipulate_dataframe(self) -> geopandas.GeoDataFrame:
        self.dataframe.gpdf = super().set_dataframe()
        self.dataframe.gpdf = self.dataframe.extra_columns(attributes=["bridge", "tunnel"])
        self.dataframe.gpdf = self.dataframe.reduce_columns(attributes=[self.dataframe.key_tag, "bridge", "tunnel"])
        return self.dataframe.gpdf


class OSMWayHighway(AbstractOSM):
    def __init__(self, osm_feature: OSMObject, key_tag: str) -> None:
        self.dataframe = MyGeoDataFrame(osm_feature, key_tag)
        super(OSMWayHighway, self).__init__(dataframe=self.dataframe)
        super().create_geometry()
        self.dataframe.gpdf = self.manipulate_dataframe()
        super().export_data()
        self.dataframe.gpdf = self.dataframe.reduce_columns(attributes=[self.dataframe.key_tag, "ref"])
        super().export_data(filename="highway_egyben")

    def manipulate_dataframe(self) -> geopandas.GeoDataFrame:
        self.dataframe.gpdf = super().set_dataframe()
        self.dataframe.gpdf = self.dataframe.extra_columns(attributes=["bridge", "tunnel", "ref"])
        self.dataframe.gpdf = self.dataframe.reduce_columns(
            attributes=[self.dataframe.key_tag, "bridge", "tunnel", "ref"])
        return self.dataframe.gpdf


class OSMNodeHighway(AbstractOSM):
    def __init__(self, osm_feature: OSMObject, key_tag: str) -> None:
        self.dataframe = MyGeoDataFrame(osm_feature, key_tag)
        super(OSMNodeHighway, self).__init__(dataframe=self.dataframe)
        if osm_feature.tags.get("highway") == "motorway_junction":
            if "ref" in osm_feature.tags and str(osm_feature.tags.get("ref")) != "None":
                super().create_geometry()
                self.dataframe.gpdf = self.manipulate_dataframe()
                super().export_data()
        else:
            super().create_geometry()
            self.dataframe.gpdf = self.manipulate_dataframe()
            super().export_data()

    def manipulate_dataframe(self) -> geopandas.GeoDataFrame:
        self.dataframe.gpdf = super().set_dataframe()
        self.dataframe.gpdf = self.dataframe.extra_columns(attributes=["ref"])
        self.dataframe.gpdf = self.dataframe.reduce_columns(
            attributes=[self.dataframe.key_tag, "ref"])
        return self.dataframe.gpdf
