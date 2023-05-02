import geopandas as gpd

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

    def rename_column(self, original: str, changed: str):
        """
        Change [original] column name to [changed]
        :param original: str | Column name to change
        :param changed: str | Column name to be changed
        :return: GeoPandas.GeoDataFrame
        """
        self.gpdf.rename(columns={original: changed}, inplace=True)
        return self.gpdf

    def extra_columns(self, attributes: list):
        """
        Function to add extra columns to GeoDataFrame except the key columns
        :param attributes: list[str] | Additional column names to add to GeoDataFrame
        :return: GeoPandas.GeoDataFrame
        """
        for attribute in attributes:
            self.gpdf.loc[0, attribute] = str(self.osm_feature.tags.get(attribute))
        return self.gpdf

    def swap_column_values(self, from_column: str, to_column: str, tag_for: list = None):
        """
        Override the to_column value with the from_column value. Useful for example with churches, where the display
        depend on the religion, not on the fact that it is a church,chapel etc...
        :param from_column: str | Column to get the data from
        :param to_column: str | Column to put the data
        :param tag_for : list[str] | if the original(to) column has this value, only then overwrite with the from_column
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
        Process the place_of_worship tag, to get back either it is a chapel,church and to what religion belongs to.
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
