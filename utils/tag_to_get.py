from typing import Set


class Queries:
    """Collection of Tags from the specific OSM Objects. This tags processed by the OSMHandlers for the MTSZ baseMap"""
    aerialway_line_to_get: Set[str] = {"cable_car", "gondola", "mixed_lift", "chair_lift", "drag_lift",
                                       "j-bar", "t-bar", "platter", "rope_tow", "magic_carpet", "zip_line", "goods"}
    aeroway_node_to_get: Set[str] = {"aerodrome"}
    aeroway_line_to_get: Set[str] = {"runway", "taxiway"}
    #TODO Apron
    aeroway_area_to_get: Set[str] = {"aerodrome", "runway", "airstrip", "apron"}
    amenity_node_to_get: Set[str] = {"bar", "bbq", "biergarten", "bus_station", "cafe", "clinic", "doctors",
                                     "drinking_water",
                                     "fast_food", "ferry_terminal", "food_court", "fuel", "hospital", "monastery",
                                     "parking", "pharmacy", "place_of_worship", "post_office", "post_depot", "pub",
                                     "public_bath",
                                     "restaurant", "shelter",
                                     }
    amenity_area_to_get: Set[str] = {"bar", "biergarten", "cafe", "fast_food", "food_court", "pub", "restaurant",
                                     "college",
                                     "driving_school", "kindergarten", "research_institute", "school", "traffic_park",
                                     "university", "bus_station", "car_rental", "car_wash", "vehicle_inspection",
                                     "driver_training", "fuel", "parking", "clinic", "hospital", "nursing_home",
                                     "veterinary",
                                     "fountain", "post_depot", "prison", "shelter", "animal_boarding",
                                     "animal_breeding",
                                     "animal_shelter", "animal_training", "childcare", "grave_yard", "marketplace",
                                     "monastery",
                                     "place_of_worship", "public_bath", "refugee_site"}
    barrier_node_to_get: Set[str] = {"border_control"}
    barrier_line_to_get: Set[str] = {"city_wall", "fence", "wall", }
    barrier_area_to_get: Set[str] = {"city_wall", "fence", "wall", }
    highway_node_to_get: Set[str] = {"bus_stop", "motorway_junction"}
    highway_line_to_get: Set[str] = {"bridleway", "cycleway", "footway", "living_street", "motorway", "motorway_link",
                                     "path",
                                     "pedestrian", "primary", "primary_link", "raceway", "residential", "road",
                                     "secondary", "secondary_link", "service", "steps", "tertiary", "tertiary_link",
                                     "track", "trunk", "trunk_link", "unclassified"}
    highway_area_to_get: Set[str] = {"pedestrian", "platform", "services", "rest_area", }
    historic_node_to_get: Set[str] = {"archaeological_site", "castle", "fort", "church", "mine",
                                      "memorial", "mine_shaft", "monastery", "monument", "ruins",
                                      "tomb", "wayside_cross", "wayside_shrine"}
    historic_area_to_get: Set[str] = {"archaeological_site", "castle", "castle_wall", "citywalls", "church",
                                      "memorial", "monument", "ruins"}
    landuse_area_to_get: Set[str] = {"allotments", "orchard", "vineyard", "forest", "farmyard", "brownfield",
                                     "commercial", "residential", "retail", "industrial", "garages", "landfill",
                                     "railway",
                                     "cemetery", "recreation_ground", "religious", "quarry", "military", "basin",
                                     "reservoir",
                                     "scrub", "construction", "education", "winter_sports"}
    leisure_node_to_get: Set[str] = {"bathing_place", "beach_resort", "fishing", "marina",
                                     "picnic_table", "slipway", "swimming_area", "water_park"}
    leisure_line_to_get: Set[str] = {"track"}
    leisure_area_to_get: Set[str] = {"bathing_place", "beach_resort", "dog_park", "fishing", "fitness_station",
                                     "garden", "golf_course", "horse_riding", "ice_rink", "marina", "miniature_golf",
                                     "park",
                                     "pitch", "playground", "summer_camp", "swimming_area", "swimming_pool", "track",
                                     "water_park"}
    man_made_node_to_get: Set[str] = {"chimney", "communications_tower", "cross", "mast",
                                      "obelisk", "stupa", "tower", "water_tap", "water_well",
                                      "water_tower", "watermill", "windmill"}
    man_made_tower_type_not_to_get: Set[str] = {"ad", "advertisement", "advertising", "lighting", "Gólyafészek",
                                                "gólyafészek", "Söréttorony", "aircraft_control", "beacon", "campanile",
                                                "church",
                                                "clock", "concrete", "control", "crossing", "defensive", "drill_rig",
                                                "floodlight",
                                                "geodetic_survey", "industrial", "indusxtrial", "lightning_rod", "mast",
                                                "meteo",
                                                "monitoring", "navigációs", "oil_tower", "sport", "technológia",
                                                "templomtorony",
                                                "watchtower", "weather"}
    man_made_line_to_get: Set[str] = {"cutline", "embankment", "groyne", "goods_conveyor", "pier"}
    man_made_area_to_get: Set[str] = {"bridge", "gasometer", "monitoring_station", "pier",
                                      "pipeline", "pumping_station", "silo", "storage_tank", "tailings_ponds", "tower",
                                      "wastewater_plant", "water_works"}
    military_node_to_get: Set[str] = {"airfield"}
    military_area_to_get: Set[str] = {"airfield", "ammunition", "barracks", "danger_area", "naval_base", "range",
                                      "training_area"}
    natural_node_to_get: Set[str] = {"bay", "cape", "isthmus", "peninsula", "spring", "cliff",
                                     "peak", "rock", "saddle", "sinkhole", "cave_entrance", "stone"}
    natural_line_to_get: Set[str] = {"cliff", "ridge", "tree_row", "valley"}
    natural_area_to_get: Set[str] = {"scrub", "wood", "water", "wetland", "cave_entrance", "beach", "shingle",
                                     "shoal", "rock", "scree", "stone", "sinkhole", "sand", "bare_rock"}
    place_node_to_get: Set[str] = {"city", "county", "district", "islet", "square", "island", "allotments",
                                   "isolated_dwelling", "hamlet", "isolated_dwelling", "locality", "neighbourhood",
                                   "quarter",
                                   "suburb", "town", "village", "city_block", "borough", "state", "region", "province"}
    place_area_to_get: Set[str] = {"city", "county", }
    power_line_to_get: Set[str] = {"line"}
    power_area_to_get: Set[str] = {"compensator", "plant"}
    railway_node_to_get: Set[str] = {"halt", "station", "tram_stop", "narrow_gauge"}
    railway_line_to_get: Set[str] = {"funicular", "light_rail", "miniature", "narrow_gauge", "construction", "rail",
                                     "subway",
                                     "tram", "platform"}
    railway_area_to_get: Set[str] = {"platform"}
    shop_node_to_get: Set[str] = {"convenience", "dairy", "general", "supermarket", "beverages", "greengrocer",
                                  "wholesale", }
    tourism_node_to_get: Set[str] = {"alpine_hut", "artwork", "apartment", "camp_site",
                                     "caravan_site", "chalet", "guest_house", "hostel", "hotel", "motel", "museum",
                                     "picnic_site", "viewpoint", "wilderness_hut"}
    tourism_area_to_get: Set[str] = {"alpine_hut", "apartment", "aquarium", "attraction", "camp_pitch", "camp_site",
                                     "caravan_site", "chalet", "guest_house", "hostel", "hotel", "motel", "museum",
                                     "picnic_site", "theme_park", "wilderness_hut", "zoo"}
    waterway_node_to_get: Set[str] = {"dock", "waterfall", "lock_gate", "weir", "sluice_gate", }
    waterway_line_to_get: Set[str] = {"river", "stream", "canal", "drain", "ditch", "dam", "weir", "lock_gate", }
    water_node_to_get: Set[str] = {"lake", "pond"}
    water_area_to_get: Set[str] = {"river", "oxbow", "canal", "ditch", "lock", "fish_pass", "lake", "reservoir", "pond",
                                   "basin",
                                   "stream_pool", "reflecting_pool", "moat", "wastewater"}
