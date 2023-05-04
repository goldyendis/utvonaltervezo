from typing import List


class Schemes:
    def __init__(self, attributes: List[str] = None):
        base_schema = ["id", "geom_type", "name", "geometry"]
        if attributes is None:
            attributes = []
        self.schema = base_schema + attributes


