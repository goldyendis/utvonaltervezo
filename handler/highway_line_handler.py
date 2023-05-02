import osmium as o
from osmium.osm import Way
from osm_features.abstract.factory import OSMFactory
from utils.tag_to_get import Queries


class OSMHandlerHighway(o.SimpleHandler):
    """OSM Way Highway Line Handler"""

    def __init__(self) -> None:
        super(OSMHandlerHighway, self).__init__()
        self.count = 0

    def way(self, w: Way) -> None:
        """Osmium Way callback, only to process the Highway Ways
        :param w: osmium.osm.Way immutable class object to process
        """
        if w.tags.get("highway") in Queries.highway_line_to_get:
            OSMFactory.create_factory(osm_feature=w, key_tag="highway")
            self.count += 1
            print(f"Highway Line:  {self.count}")