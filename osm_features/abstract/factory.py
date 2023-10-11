from osmium.osm import OSMObject, Area, Way, Node
from osm_features.aeroway import OSMWayAeroway
from osm_features.amenity import OSMNodeAmenity
from osm_features.building import OSMAreaBuilding
from osm_features.common import OSMCommon
from osm_features.highway import OSMAreaHighway, OSMWayHighway, OSMNodeHighway
from osm_features.landuse import OSMAreaLanduse
from osm_features.man_made import OSMNodeManMade, OSMWayManMade
from osm_features.natural import OSMAreaNatural, OSMNodeNatural
from osm_features.place import OSMNodePlace
from osm_features.railway import OSMWayRailway, OSMNodeRailway
from osm_features.waterway import OSMWayWaterway


class OSMFactory:
    """Decider to choose what kind of OSM Feature is under processing"""
    @staticmethod
    def create_factory(osm_feature: OSMObject, key_tag: str, count: int = None) -> None:
        """
        From the type of the OSMObject and from the layer name(key_tag) decide which class to instantiate
        :param count: For testing purpose
        :param osm_feature: The osmium.osm.OSMObject object which is under process right now
        :param key_tag: Name of the layer
        """
        if issubclass(type(osm_feature), Area):
            if key_tag == "landuse":
                OSMAreaLanduse(osm_feature, key_tag)
            elif key_tag == "natural":
                OSMAreaNatural(osm_feature, key_tag)
            elif key_tag == "highway":
                OSMAreaHighway(osm_feature, key_tag)
            elif key_tag == "building":
                OSMAreaBuilding(osm_feature, key_tag, count)
            else:
                OSMCommon(osm_feature, key_tag)
        if issubclass(type(osm_feature), Way):
            if key_tag == "highway":
                OSMWayHighway(osm_feature, key_tag)
            elif key_tag == "railway":
                OSMWayRailway(osm_feature, key_tag)
            elif key_tag == "aeroway":
                OSMWayAeroway(osm_feature, key_tag)
            elif key_tag == "waterway":
                OSMWayWaterway(osm_feature, key_tag)
            elif key_tag == "man_made":
                OSMWayManMade(osm_feature, key_tag)
            else:
                OSMCommon(osm_feature, key_tag)
        if issubclass(type(osm_feature), Node):
            if key_tag == "natural":
                OSMNodeNatural(osm_feature, key_tag)
            elif key_tag == "highway":
                OSMNodeHighway(osm_feature, key_tag)
            elif key_tag == "railway":
                OSMNodeRailway(osm_feature, key_tag)
            elif key_tag == "man_made":
                OSMNodeManMade(osm_feature, key_tag)
            elif key_tag == "place":
                OSMNodePlace(osm_feature, key_tag)
            elif key_tag == "amenity":
                OSMNodeAmenity(osm_feature, key_tag)
            else:
                OSMCommon(osm_feature, key_tag)
