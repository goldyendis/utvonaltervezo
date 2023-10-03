import osmium as o
from osmium.osm import Way, Node, Area
from osm_features.abstract.factory import OSMFactory
from utils.tag_to_get import Queries


class OSMHandlerArea(o.SimpleHandler):
    """OSM Area Handler"""

    def __init__(self) -> None:
        super(OSMHandlerArea, self).__init__()
        self.count = 0

    def area(self, a: Area) -> None:
        """Osmium Area callback
        :param a: osmium.osm.Area immutable class object to process
        """
        if a.tags.get("landuse") in Queries.landuse_area_to_get:
            OSMFactory.create_factory(osm_feature=a, key_tag="landuse")
        elif "natural" in a.tags and "landuse" not in a.tags and a.tags.get("natural") in Queries.natural_area_to_get:
            OSMFactory.create_factory(osm_feature=a, key_tag="natural")
        elif a.tags.get("highway") in Queries.highway_area_to_get:
            OSMFactory.create_factory(osm_feature=a, key_tag="highway")
        # elif a.tags.get("waterway") in Queries.waterway_area_to_get:
        #     OSMFactory.create_factory(osm_feature=a, key_tag="waterway")
        elif a.tags.get("railway") in Queries.railway_area_to_get and "building" not in a.tags:
            OSMFactory.create_factory(osm_feature=a, key_tag="railway")
        elif a.tags.get("aeroway") in Queries.aeroway_area_to_get and "building" not in a.tags:
            OSMFactory.create_factory(osm_feature=a, key_tag="aeroway")
        elif a.tags.get("man_made") in Queries.man_made_area_to_get and "building" not in a.tags:
            OSMFactory.create_factory(osm_feature=a, key_tag="man_made")
        elif a.tags.get("power") in Queries.power_area_to_get and "building" not in a.tags and "landuse" not in a.tags:
            OSMFactory.create_factory(osm_feature=a, key_tag="power")
        elif a.tags.get(
                "leisure") in Queries.leisure_area_to_get and "building" not in a.tags and "landuse" not in a.tags:
            OSMFactory.create_factory(osm_feature=a, key_tag="leisure")
        elif a.tags.get(
                "amenity") in Queries.amenity_area_to_get and "building" not in a.tags and "landuse" not in a.tags:
            OSMFactory.create_factory(osm_feature=a, key_tag="amenity")
        elif a.tags.get(
                "tourism") in Queries.tourism_area_to_get and "building" not in a.tags and "landuse" not in a.tags:
            OSMFactory.create_factory(osm_feature=a, key_tag="tourism")
        elif a.tags.get(
                "historic") in Queries.historic_area_to_get and "building" not in a.tags and "landuse" not in a.tags:
            OSMFactory.create_factory(osm_feature=a, key_tag="historic")
        elif a.tags.get(
                "military") in Queries.military_area_to_get and "building" not in a.tags and "landuse" not in a.tags:
            OSMFactory.create_factory(osm_feature=a, key_tag="military")
        elif "place" in a.tags:
            OSMFactory.create_factory(osm_feature=a, key_tag="place")
        if "building" in a.tags:
            OSMFactory.create_factory(osm_feature=a, key_tag="building")
        # self.count += 1
        # print(f"Building:  {self.count}")
        self.count += 1
        print(f"Area:  {self.count}")

    def way(self, w: Way) -> None:
        """Osmium Way callback
        :param w: osmium.osm.Way immutable class object to process
        """
        if w.tags.get("natural") in Queries.natural_line_to_get:
            OSMFactory.create_factory(osm_feature=w, key_tag="natural")
        # TODO public_transport???
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
        # elif w.tags.get("historic") in Queries.historic_line_to_get:
        #     OSMFactory.create_factory(osm_feature=w, key_tag="historic")
        elif w.tags.get("man_made") in Queries.man_made_line_to_get:
            OSMFactory.create_factory(osm_feature=w, key_tag="man_made")
        elif w.tags.get("power") in Queries.power_line_to_get:
            OSMFactory.create_factory(osm_feature=w, key_tag="power")
        if w.tags.get("highway") in Queries.highway_line_to_get:
            OSMFactory.create_factory(osm_feature=w, key_tag="highway")
            # self.count += 1
            # print(f"Highway Line:  {self.count}")
        self.count += 1
        print(f"Way:  {self.count}")

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
        # TODO public_transport???
        elif n.tags.get("railway") in Queries.railway_node_to_get and n.tags.get("station") not in ["abandoned",
                                                                                                    "disused"]:
            OSMFactory.create_factory(osm_feature=n, key_tag="railway")
        elif n.tags.get("man_made") in Queries.man_made_node_to_get:
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