import geopandas as gpd
from typing import Set

from utils.schemes import Schemes


class MyGeoDataFrame:
    """Class containing as attributes the Osmium OSMObjects, the processing tags and the GeoPanda GeoDataframe from it
       Also the functions, to manipulate the GeoDataframe"""

    def __init__(self, osm_feature, key_tag: str) -> None:
        self.osm_feature = osm_feature
        self.gpdf = gpd.GeoDataFrame(columns=["geometry"])
        self.key_tag = key_tag

    def set_projection(self, epsg: int) -> gpd.geodataframe:
        """Convert the MyGeoDataFrame from WGS84 to other projection
        :param epsg: int | the projection epsg code
        :return: GeoPandas.GeoDataFrame in the new projection
        """
        self.gpdf.crs = "EPSG:4326"
        gpdf_crs = self.gpdf.to_crs(epsg=epsg)
        return gpdf_crs

    def set_key_columns(self) -> gpd.GeoDataFrame:
        """Set the common attributes of every (tag) version of GeoDataframe
        :return: GeoPandas.GeoDataFrame
        """
        name = self.osm_feature.tags.get("name")
        lay = self.osm_feature.tags.get(self.key_tag)
        self.gpdf.loc[0, 'name'] = str(name)
        self.gpdf.loc[0, self.key_tag] = str(lay)
        return self.gpdf

    def reduce_columns(self, attributes: list) -> gpd.GeoDataFrame:
        """Truncate the columns to only the needed ones with help of Schemes class
        :param attributes:list[str] | Additional column names to keep
        :return: GeoPandas.GeoDataFrame
        """
        self.gpdf = self.gpdf[self.gpdf.columns.intersection(
            Schemes(attributes=attributes).schema)]
        return self.gpdf

    def rename_column(self, original: str, changed: str) -> gpd.GeoDataFrame:
        """
        Change [original] column name to [changed]
        :param original: str | Column name to change
        :param changed:  str | Column name to be changed
        :return: GeoPandas.GeoDataFrame
        """
        self.gpdf.rename(columns={original: changed}, inplace=True)
        return self.gpdf

    def extra_columns(self, attributes: list) -> gpd.GeoDataFrame:
        """
        Function to add extra columns to GeoDataFrame except the key columns
        :param attributes: List[str] | Additional column names to add to GeoDataFrame
        :return: GeoPandas.GeoDataFrame
        """
        for attribute in attributes:
            self.gpdf.loc[0, attribute] = str(self.osm_feature.tags.get(attribute))
        return self.gpdf

    def swap_column_values(self, from_column: str, to_column: str, tag_for: list = None) -> gpd.GeoDataFrame:
        """
        Override the to_column value with the from_column value. Useful for example with churches, where the display
        depend on the religion, not on the fact that it is a church,chapel etc...
        :param from_column: str | Column to get the data from
        :param to_column:   str | Column to put the data
        :param tag_for :    List[str] | if the original(to) column has this value, only then overwrite with the from_column
        :return: GeoPandas.GeoDataframe
        """
        if str(self.gpdf.loc[0, from_column]) is not None:
            if tag_for is None:
                self.gpdf.loc[0, to_column] = self.gpdf.loc[0, from_column]
            elif tag_for is not None:
                if self.gpdf.loc[0, to_column] in tag_for:
                    self.gpdf.loc[0, to_column] = self.gpdf.loc[0, from_column]
        return self.gpdf

    def get_place_of_worship_value(self) -> gpd.GeoDataFrame:
        """
        Process the place_of_worship tag, to get back as a useful representation.
        Suppose only catholic items can be other than "church"
        :return: GeoPandas.GeoDataframe
        """
        religion: str = str(self.osm_feature.tags.get("religion"))
        name: str = str(self.osm_feature.tags.get("name"))

        if name.lower().find("harangláb") != -1:
            self.gpdf.loc[0, self.key_tag] = "harangláb"
            return self.gpdf
        elif self.osm_feature.tags.get("building") in ["church", "chapel", "temple"]:
            if religion == "christian" or religion == "None":
                self.gpdf.loc[0, self.key_tag] = self.osm_feature.tags.get("building")
                return self.gpdf
            else:
                self.gpdf.loc[0, self.key_tag] = religion
                return self.gpdf
        elif name.lower().find("kápolna") != -1 and religion in ["christian", "None"]:
            self.gpdf.loc[0, self.key_tag] = "chapel"
            return self.gpdf
        else:
            if religion != "None":
                self.gpdf.loc[0, self.key_tag] = religion
                return self.gpdf
            else:
                return self.gpdf

    def get_man_made_value(self) -> gpd.GeoDataFrame:
        """
        Process the man_made tag with the tower_type tag, to normalize the return value
        :return: GeoPandas.GeoDataframe
        """
        man_made: str = str(self.osm_feature.tags.get(self.key_tag))
        name: str = str(self.osm_feature.tags.get("name"))
        tower_type: str = str(self.osm_feature.tags.get("tower:type"))
        simple_man_made_features: Set[str] = {"chimney", "communications_tower", "cross", "obelisk", "stupa",
                                              "water_tap", "water_tower", "water_well", "watermill", "windmill"}
        mast_comm_towers: Set[str] = {"antenna", "communication", "radar", "radio"}
        mast_from_name_comm_towers: Set[str] = {"adó", "antenna", "rádió", "gsm", "tv", "tévé", "mobiltelefon"}
        tower_observation: Set[str] = {"kilátó", "observ"}
        tower_comm: Set[str] = {"radio", "rádió", "comm", "radar"}

        if man_made in simple_man_made_features:
            """Easily identifiable man_made objects"""
            self.gpdf.loc[0, self.key_tag] = man_made
            return self.gpdf
        elif man_made == "mast":
            """Man_made tag does not descriptive enough. Have to check the tower:type tag too.
             For MTSZ BaseMap only the Communication towers important from the 'Mast' tag"""
            if tower_type in mast_comm_towers:
                """Clear tower tags which are listed in the mast_comm_tower"""
                self.gpdf.loc[0, self.key_tag] = "communications_tower"
                return self.gpdf
            elif tower_type == "None":
                """Search in the name attribute, and determine if the mast is a communications_tower"""
                if any(name.lower() in element for element in mast_from_name_comm_towers):
                    self.gpdf.loc[0, self.key_tag] = "communications_tower"
                    return self.gpdf
        elif man_made == "tower":
            """Man_made tag does not descriptive enough. Have to check the tower:type tag too.
            Tower tag contains communications_towers, observation_towers, bell_towers."""
            if tower_type.lower() == "bell_tower":
                self.gpdf.loc[0, self.key_tag] = "bell_tower"
                return self.gpdf
            elif any(tag in tower_type.lower() for tag in tower_observation):
                "Tag that hint that it is an observation tower"
                self.gpdf.loc[0, self.key_tag] = "observation"
                return self.gpdf
            elif any(tag in tower_type.lower() for tag in tower_comm):
                "Tag that hint that it is a communication tower"
                self.gpdf.loc[0, self.key_tag] = "communications_tower"
                return self.gpdf
            elif tower_type == "None":
                """Search in the name attribute, and determine if the mast is an observation tower,
                 a bell tower or a communications tower"""
                if any(tag in name.lower() for tag in tower_observation):
                    self.gpdf.loc[0, self.key_tag] = "observation"
                    return self.gpdf
                elif any(tag in name.lower() for tag in tower_comm):
                    self.gpdf.loc[0, self.key_tag] = "communications_tower"
                    return self.gpdf
                elif name.lower().find("harang") > -1:
                    self.gpdf.loc[0, self.key_tag] = "bell_tower"
                    return self.gpdf

        self.gpdf.loc[0, self.key_tag] = "None"
        return self.gpdf


