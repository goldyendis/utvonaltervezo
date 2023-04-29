class Schemes:
    def __init__(self, attributes=[], base_schema = ["id", "geom_type", "name", "geometry"]):
        self.schema = base_schema + attributes


