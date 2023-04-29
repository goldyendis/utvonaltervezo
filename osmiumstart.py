from handler.area_handler import OSMHandlerArea
from handler.building_handler import OSMHandlerBuilding
from handler.highway_line_handler import OSMHandlerHighway
from handler.node_handler import OSMHandlerNode
from handler.way_handler import OSMHandlerWay
import pyrosm
from utils.constans import FILE_PATH, TEST


class OsmiumStart:
    """Class to start the *.osm.pbf processing"""
    def __init__(self) -> None:
        self.file_path = FILE_PATH
        if TEST:
            self.file_path = f"{self.file_path}\\budapest"
            pyrosm.get_data("budapest", directory=self.file_path)
            self.osm_file = f"{self.file_path}\\Budapest.osm.pbf"
        else:
            pyrosm.get_data("hungary", directory=self.file_path)
            self.osm_file = f"{self.file_path}\\hungary-latest.osm.pbf"

    def get_nodes(self) -> None:
        """Osmium processor of osm nodes"""
        handler_node = OSMHandlerNode()
        handler_node.apply_file(self.osm_file, locations=True)

    def get_areas(self) -> None:
        """Osmium processor of osm area features, except buildings"""
        handler_area = OSMHandlerArea()
        handler_area.apply_file(self.osm_file, locations=True)

    def building_thread(self) -> None:
        """Separate thread for building process by Osmium"""
        handler_building = OSMHandlerBuilding()
        handler_building.apply_file(self.osm_file, locations=True)

    def highway_thread(self) -> None:
        """Separate thread for highway line process by Osmium"""
        handler_highway = OSMHandlerHighway()
        handler_highway.apply_file(self.osm_file,locations=True)

    def get_lines(self) -> None:
        """Osmium processor of osm ways"""
        handler_way = OSMHandlerWay()
        handler_way.apply_file(self.osm_file, locations=True)
