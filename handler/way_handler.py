import osmium as o
from osmium.osm import Way
from osm_features.abstract.factory import OSMFactory
from utils.tag_to_get import Queries


class OSMHandlerWay(o.SimpleHandler):
    """OSM Way Handler"""

    def __init__(self) -> None:
        super(OSMHandlerWay, self).__init__()
        self.count = 0

    def way(self, w: Way) -> None:
        """Osmium Way callback
        :param w: osmium.osm.Way immutable class object to process
        """
        if w.tags.get("natural") in Queries.natural_line_to_get:
            OSMFactory.create_factory(osm_feature=w, key_tag="natural")
        elif w.tags.get("railway") in Queries.railway_line_to_get:
            OSMFactory.create_factory(osm_feature=w, key_tag="railway")
        elif w.tags.get('waterway') in Queries.waterway_line_to_get and "natural" not in w.tags:
            OSMFactory.create_factory(osm_feature=w, key_tag="waterway")
        elif w.tags.get("leisure") in Queries.leisure_line_to_get:
            OSMFactory.create_factory(osm_feature=w, key_tag="leisure")
        elif w.tags.get("aeroway") in Queries.aeroway_line_to_get:
            OSMFactory.create_factory(osm_feature=w, key_tag="aeroway")
        elif w.tags.get("aerialway") in Queries.aerialway_line_to_get:
            OSMFactory.create_factory(osm_feature=w, key_tag="aerialway")
        elif w.tags.get("barrier") in Queries.barrier_line_to_get:
            OSMFactory.create_factory(osm_feature=w, key_tag="barrier")
        elif w.tags.get("man_made") in Queries.man_made_line_to_get:
            OSMFactory.create_factory(osm_feature=w, key_tag="man_made")
        elif w.tags.get("power") in Queries.power_line_to_get:
            OSMFactory.create_factory(osm_feature=w, key_tag="power")
        self.count += 1
        print(f"Way:  {self.count}")
