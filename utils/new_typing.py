from typing import NewType
import osmium
from osm_features.abstract.super_osm_feature import AbstractOSM
from enum import Enum

OSMArea = NewType("OSMArea", osmium.osm.Area)
OSMWay = NewType("OSMWay", osmium.osm.Way)
OSMNode = NewType("OSMNode", osmium.osm.Node)
OSMAbstract = NewType("OSMAbstract", AbstractOSM)

OSMType = [OSMArea, OSMWay, OSMNode]


class OSMKeyTagsEnum(Enum):
    Landuse = "landuse"
    Natural = "natural"
    Highway = "highway"
    Building = "building"
    Railway = "railway"
    Aeroway = "aeroway"
    Man_Made = "man_made"
    Power = "power"
    Leisure = "leisure"
    Amenity = "amenity"
    Tourism = "tourism"
    Historic = "historic"
    Military = "military"
    Place = "place"
    Barrier = "barrier"
    Waterway = "waterway"
    Aerialway = "aerialway"
    Office = "office"
    Shop = "shop"
    Water = "water"


