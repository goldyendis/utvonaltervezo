from typing import Any

import shapely
from osmium.osm import Area, Way, Node, OSMObject
from shapely.geometry import MultiLineString, Point, MultiPolygon, LineString
from osmium import geom


class MyGeometry:
    """Geometry manipulator class"""

    def __init__(self, osm_feature: OSMObject) -> None:
        self.wktfab = geom.WKTFactory()
        self.osm_feature = osm_feature

    def create_geometry(self) -> shapely.geometry:
        """ Create shapely geometry for the GeoDataframe geometry column from the osmium OSMObject.
        :rtype: shapely.geometry
        """
        geometry: Any[MultiPolygon, MultiLineString, Point, LineString]
        wkt = None
        try:
            if issubclass(type(self.osm_feature), Area):
                wkt = self.wktfab.create_multipolygon(self.osm_feature)
            if issubclass(type(self.osm_feature), Way):
                wkt = self.wktfab.create_linestring(self.osm_feature)
            if issubclass(type(self.osm_feature), Node):
                wkt = self.wktfab.create_point(self.osm_feature)
            geometry = shapely.wkt.loads(wkt)
            return geometry
        except:
            pass
