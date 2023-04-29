from typing import NewType
import osmium
from osm_features.abstract.super_osm_feature import AbstractOSM

OSMArea = NewType("OSMArea", osmium.osm.Area)
OSMWay = NewType("OSMWay", osmium.osm.Way)
OSMNode = NewType("OSMNode", osmium.osm.Node)
OSMAbstract = NewType("OSMAbstract", AbstractOSM)

OSMType = [OSMArea, OSMWay, OSMNode]
