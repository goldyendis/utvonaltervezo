import osmium
from utils.constans import FILE_PATH, TEST
import pyrosm
import osmium.osm.mutable as mut

class OSMHandlerHighway(osmium.SimpleHandler):
    """OSM Way Highway Line Handler"""

    def __init__(self,writer) -> None:
        super(OSMHandlerHighway, self).__init__()
        self.file_path: str = FILE_PATH
        self.writer = writer
        
        if TEST:
            pyrosm.get_data("budapest", directory=self.file_path)
            self.osm_file = f"{self.file_path}\\Budapest.osm.pbf"
        else:
            pyrosm.get_data("hungary", directory=self.file_path)
            self.osm_file = f"{self.file_path}\\hungary-latest.osm.pbf"
            
        self.apply_file(self.osm_file, locations=True)
        self.count: int = 1

    def way(self, w) -> None:
        if "highway" in w.tags:
            mutableWay = mut.Way(w)
            mutableWay.version = 1
            self.writer.add_way(mutableWay)

if __name__ == '__main__':
    writer = osmium.SimpleWriter(fr"{FILE_PATH}\\test_budapest.osm")
    handler = OSMHandlerHighway(writer)
    writer.close()
