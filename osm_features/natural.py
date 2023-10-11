from osmium.osm import OSMObject

from manipulation.manipulate_geodataframe import MyGeoDataFrame
from osm_features.abstract.super_osm_feature import AbstractOSM


class OSMAreaNatural(AbstractOSM):
    def __init__(self, osm_feature: OSMObject, key_tag: str) -> None:
        self.dataframe = MyGeoDataFrame(osm_feature, key_tag)
        super(OSMAreaNatural, self).__init__(dataframe=self.dataframe)
        super().create_geometry()
        self.dataframe.gpdf = self.manipulate_dataframe()
        super().export_data()

    def manipulate_dataframe(self):
        self.dataframe.gpdf = super().set_dataframe()
        if self.dataframe.osm_feature.tags.get(self.dataframe.key_tag) == "water":
            self.dataframe.key_tag = "water"
            self.dataframe.gpdf.loc[0, "water"] = str(self.dataframe.osm_feature.tags.get(self.dataframe.key_tag))
            self.dataframe.gpdf = self.dataframe.reduce_columns(attributes=[self.dataframe.key_tag])

        elif super().key_tag_value == "wood" or super().key_tag_value == "scrub":
            self.dataframe.rename_column("natural", "landuse")
            self.dataframe.key_tag = "landuse"
            if super().key_tag_value == "wood":
                self.dataframe.gpdf.loc[0,"landuse"] = "forest"
            self.dataframe.gpdf = self.dataframe.reduce_columns(attributes=[self.dataframe.key_tag])

        else:
            self.dataframe.gpdf = self.dataframe.reduce_columns(attributes=[self.dataframe.key_tag])

        return self.dataframe.gpdf


class OSMNodeNatural(AbstractOSM):
    def __init__(self, osm_feature: OSMObject, key_tag: str) -> None:
        self.dataframe = MyGeoDataFrame(osm_feature, key_tag)
        super(OSMNodeNatural, self).__init__(dataframe=self.dataframe)
        super().create_geometry()
        self.dataframe.gpdf = self.manipulate_dataframe()
        super().export_data()

    def manipulate_dataframe(self):
        self.dataframe.gpdf = super().set_dataframe()
        self.dataframe.gpdf = self.dataframe.extra_columns(attributes=["ele"])
        self.dataframe.gpdf = self.dataframe.reduce_columns(
            attributes=[self.dataframe.key_tag, "ele"])
        return self.dataframe.gpdf
