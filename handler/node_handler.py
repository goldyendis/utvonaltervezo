import osmium as o
from osmium.osm import Node
from osm_features.abstract.abstract import OSMFactory
from utils.tag_to_get import Queries


class OSMHandlerNode(o.SimpleHandler):
    """OSM Node Handler"""

    def __init__(self) -> None:
        super(OSMHandlerNode, self).__init__()
        self.count = 0

    def node(self, n: Node) -> None:
        """Osmium Node callback
        :param n: osmium.osm.Node immutable class object to process
        """
        if n.tags.get("natural") in Queries.natural_node_to_get:
            OSMFactory.create_factory(osm_feature=n, key_tag="natural")
        elif n.tags.get("historic") in Queries.historic_node_to_get:
            OSMFactory.create_factory(osm_feature=n, key_tag="historic")
        elif n.tags.get("barrier") in Queries.barrier_node_to_get:
            OSMFactory.create_factory(osm_feature=n, key_tag="barrier")
        elif n.tags.get("highway") in Queries.highway_node_to_get:
            name: str = str(n.tags.get("name"))
            if not (n.tags.get("highway") == "motorway_junction" and name.lower().find("pihenő") > -1):
                OSMFactory.create_factory(osm_feature=n, key_tag="highway")
        # # TODO public_transport???
        elif n.tags.get("railway") in Queries.railway_node_to_get:
            OSMFactory.create_factory(osm_feature=n, key_tag="railway")
        elif n.tags.get("man_made") in Queries.man_made_node_to_get \
                and n.tags.get("tower:type") not in Queries.man_made_tower_type_not_to_get:
            OSMFactory.create_factory(osm_feature=n, key_tag="man_made")
        elif n.tags.get("place") in Queries.place_node_to_get:
            OSMFactory.create_factory(osm_feature=n, key_tag="place")
        elif n.tags.get("amenity") in Queries.amenity_node_to_get and "historic" not in n.tags \
                and n.tags.get("shelter_type") != "public_transport":
            OSMFactory.create_factory(osm_feature=n, key_tag="amenity")
        elif n.tags.get('waterway') in Queries.waterway_node_to_get and "natural" not in n.tags:
            OSMFactory.create_factory(osm_feature=n, key_tag="waterway")
        elif n.tags.get("leisure") in Queries.leisure_node_to_get:
            OSMFactory.create_factory(osm_feature=n, key_tag="leisure")
        elif n.tags.get("aeroway") in Queries.aeroway_node_to_get:
            OSMFactory.create_factory(osm_feature=n, key_tag="aeroway")
        elif n.tags.get("shop") in Queries.shop_node_to_get:
            OSMFactory.create_factory(osm_feature=n, key_tag="shop")
        elif "office" in n.tags:
            OSMFactory.create_factory(osm_feature=n, key_tag="office")
        elif n.tags.get("tourism") in Queries.tourism_node_to_get \
                and "amenity" not in n.tags and "man_made" not in n.tags:
            OSMFactory.create_factory(osm_feature=n, key_tag="tourism")
        elif n.tags.get("military") in Queries.military_node_to_get:
            OSMFactory.create_factory(osm_feature=n, key_tag="military")
        self.count += 1
        print(f"Point:  {self.count}")
