import os
from utils.constans import FILE_PATH, TEST
from manipulation.abstract.export import Export


class ExportSHP(Export):
    """Export the data to ESRI SHP file format"""

    def __init__(self, dataframe) -> None:
        self.dataframe = dataframe
        if TEST:
            self.file_path = f"{FILE_PATH}\\budapest"
        else:
            self.file_path = FILE_PATH

    def export(self, filename=None) -> None:
        geometry_type = self.dataframe.gpdf['geom_type'].unique()
        if "Polygon" in geometry_type or "MultiPolygon" in geometry_type:
            # print("export AREA " + self.dataframe.key_tag)
            self.export_feature(geom_type="area", filename=filename)
        elif "LineString" in geometry_type or "MultiLineString" in geometry_type:
            # print("export LINE " + self.dataframe.key_tag)
            self.export_feature(geom_type="line", filename=filename)
        elif "Point" in geometry_type:
            # print("export POINT " + self.dataframe.key_tag)
            self.export_feature(geom_type="point", filename=filename)

    def export_feature(self, geom_type: str, filename=None):
        append: bool = os.path.exists(f"{self.file_path}\\{self.dataframe.key_tag}_{geom_type}.shp"
                                      if filename is None
                                      else f"{self.file_path}\\{filename}_{geom_type}.shp")

        path: str = f"{self.file_path}\\{self.dataframe.key_tag}_{geom_type}.shp" \
                    if filename is None \
                    else f"{self.file_path}\\{filename}_{geom_type}.shp"

        try:
            self.dataframe.gpdf.to_file(path, index=False, mode="a" if append else "w",
                                        crs="EPSG:3857", encoding="utf-8")
        except:
            pass
