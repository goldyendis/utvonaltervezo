import osmium as o
from osmium.osm import Area
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
        self.count += 1
        print(f"Area:  {self.count}")
