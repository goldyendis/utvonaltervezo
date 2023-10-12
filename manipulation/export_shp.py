import geopandas
import os

from manipulation.manipulate_geodataframe import MyGeoDataFrame
from utils.constans import FILE_PATH, TEST
from manipulation.abstract.export import Export
from enum import Enum


class GeomType(Enum):
    Area = "area"
    Line = "line"
    Point = "point"


class ExportSHP(Export):
    """Export the data to ESRI SHP file format"""

    def __init__(self, dataframe: MyGeoDataFrame) -> None:
        self.dataframe = dataframe
        if TEST:
            self.file_path = f"{FILE_PATH}\\budapest"
        else:
            self.file_path = FILE_PATH

    def export(self, filename=None) -> None:
        geometry_type = self.dataframe.gpdf['geom_type'].unique()
        if "Polygon" in geometry_type or "MultiPolygon" in geometry_type:
            self.export_feature(geom_type=GeomType.Area, filename=filename)
        elif "LineString" in geometry_type or "MultiLineString" in geometry_type:
            self.export_feature(geom_type=GeomType.Line, filename=filename)
        elif "Point" in geometry_type:
            self.export_feature(geom_type=GeomType.Point, filename=filename)

    def export_feature(self, geom_type: GeomType, filename=None) -> None:
        append: bool = os.path.exists(f"{self.file_path}\\{self.dataframe.key_tag}_{geom_type.value}.shp"
                                      if filename is None
                                      else f"{self.file_path}\\{filename}_{geom_type.value}.shp")

        path: str = f"{self.file_path}\\{self.dataframe.key_tag}_{geom_type.value}.shp" \
            if filename is None \
            else f"{self.file_path}\\{filename}_{geom_type.value}.shp"

        try:
            self.dataframe.gpdf.to_file(path, index=False, mode="a" if append else "w",
                                        crs="EPSG:3857", encoding="utf-8")
        except Exception as e:
            print(e, filename)
