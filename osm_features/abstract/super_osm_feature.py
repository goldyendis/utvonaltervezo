from abc import ABC, abstractmethod

import geopandas
# from main2 import test
from manipulation.manipulate_geodataframe import MyGeoDataFrame
from manipulation.export_shp import ExportSHP
from manipulation.geometry import MyGeometry


class AbstractOSM(ABC):
    """Parent class of the unique OSMFeatureClasses"""
    def __init__(self, dataframe: MyGeoDataFrame) -> None:
        self._dataframe = dataframe
        self._key_tag_value = self.dataframe.osm_feature.tags.get(self.dataframe.key_tag)

    @property
    def key_tag_value(self) -> str:
        return self._key_tag_value

    @key_tag_value.setter
    def key_tag_value(self, value):
        self._key_tag_value = value

    @property
    def dataframe(self) -> MyGeoDataFrame:
        return self._dataframe

    @dataframe.setter
    def dataframe(self, value):
        self._dataframe = value

    @abstractmethod
    def manipulate_dataframe(self) -> geopandas.GeoDataFrame:
        """
        Abstract method to be implemented at the child classes.
        Editing the Geodataframe specifically as the child class need.
        :return: GeoPandas.GeoDataFrame
        """
        pass

    def create_geometry(self) -> geopandas.GeoDataFrame:
        """Put geometry into the GeoDataframe geometry column
        :return: GeoPandas.GeoDataframe
        """
        created_geometry = MyGeometry(osm_feature=self.dataframe.osm_feature).create_geometry()
        self.dataframe.gpdf.loc[0, "geometry"] = created_geometry
        self.dataframe.gpdf['geom_type'] = self.dataframe.gpdf.geometry.geom_type
        return self.dataframe.gpdf

    def set_dataframe(self) -> geopandas.GeoDataFrame:
        """Set the GeoDataframe columns with attributes
        :return: GeoPandas.GeoDataframe
        """
        self.dataframe.gpdf = self.dataframe.set_key_columns()
        self.dataframe.gpdf = self.dataframe.set_projection(epsg=3857)
        return self.dataframe.gpdf

    def export_data(self, filename=None) -> None:
        """Export GeoDataframe to file
        :param filename: str
        """
        ExportSHP(dataframe=self.dataframe).export(filename)
