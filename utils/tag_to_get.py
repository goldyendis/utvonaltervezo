class Queries:
    """OSM Objects to process for the Base Map"""
    aerialway_line_to_get = {"cable_car", "gondola", "mixed_lift", "chair_lift", "drag_lift",
                             "j-bar", "t-bar", "platter", "rope_tow", "magic_carpet", "zip_line", "goods"}
    aeroway_node_to_get = {"aerodrome"}
    aeroway_line_to_get = {"runway", "taxiway", }
    aeroway_area_to_get = {"aerodrome", "runway", "airstrip"}
    amenity_node_to_get = {"bar", "bbq", "biergarten", "bus_station", "cafe", "clinic", "doctors", "drinking_water",
                           "fast_food", "ferry_terminal", "food_court", "fuel", "hospital", "monastery",
                           "parking", "pharmacy", "place_of_worship", "post_office", "post_depot", "pub", "public_bath",
                           "restaurant", "shelter",
                           }
    amenity_area_to_get = {"bar", "biergarten", "cafe", "fast_food", "food_court", "pub", "restaurant", "college",
                           "driving_school", "kindergarten", "research_institute", "school", "traffic_park",
                           "university", "bus_station", "car_rental", "car_wash", "vehicle_inspection",
                           "driver_training", "fuel", "parking", "clinic", "hospital", "nursing_home", "veterinary",
                           "fountain", "post_depot", "prison", "shelter", "animal_boarding", "animal_breeding",
                           "animal_shelter", "animal_training", "childcare", "grave_yard", "marketplace", "monastery",
                           "place_of_worship", "public_bath", "refugee_site"}
    barrier_node_to_get = {"border_control"}
    barrier_line_to_get = {"city_wall", "fence", "wall", }
    barrier_area_to_get = {"city_wall", "fence", "wall", }
    highway_node_to_get = {"bus_stop", "motorway_junction"}
    highway_line_to_get = {"bridleway", "cycleway", "footway", "living_street", "motorway", "motorway_link", "path",
                           "pedestrian", "primary", "primary_link", "raceway", "residential", "road",
                           "secondary", "secondary_link", "service", "steps", "tertiary", "tertiary_link",
                           "track", "trunk", "trunk_link", "unclassified"}
    highway_area_to_get = {"pedestrian", "platform", "services", "rest_area", }
    historic_node_to_get = {"archaeological_site", "castle", "fort", "church", "mine",
                            "memorial", "mine_shaft", "monastery", "monument", "ruins",
                            "tomb", "wayside_cross", "wayside_shrine"}
    historic_area_to_get = {"archaeological_site", "castle", "castle_wall", "citywalls", "fort", "church",
                            "memorial", "monastery", "monument", "ruins", "wayside_cross", "wayside_shrine"}
    landuse_area_to_get = {"allotments", "orchard", "vineyard", "forest", "farmyard", "brownfield",
                           "commercial", "residential", "retail", "industrial", "garages", "landfill", "railway",
                           "cemetery", "recreation_ground", "religious", "quarry", "military", "basin", "reservoir",
                           "scrub", "construction", "education", "winter_sports"}
    leisure_node_to_get = {"bathing_place", "beach_resort", "fishing", "marina",
                           "picnic_table", "slipway", "swimming_area", "water_park"}
    leisure_line_to_get = {"track"}
    leisure_area_to_get = {"bathing_place", "beach_resort", "dog_park", "fishing", "fitness_station",
                           "garden", "golf_course", "horse_riding", "ice_rink", "marina", "miniature_golf", "park",
                           "pitch", "playground", "summer_camp", "swimming_area", "swimming_pool", "track",
                           "water_park"}
    man_made_node_to_get = {"chimney", "communications_tower", "cross", "mast",
                            "obelisk", "stupa", "tower", "water_tap", "water_well",
                            "water_tower", "watermill", "windmill"}
    man_made_tower_type_not_to_get = {"ad", "advertisement", "advertising", "lighting", "Gólyafészek",
                                      "gólyafészek", "Söréttorony", "aircraft_control", "beacon", "campanile", "church",
                                      "clock", "concrete", "control", "crossing", "defensive", "drill_rig", "floodlight",
                                      "geodetic_survey", "industrial", "indusxtrial", "lightning_rod", "mast", "meteo",
                                      "monitoring", "navigációs", "oil_tower", "sport", "technológia", "templomtorony",
                                      "watchtower", "weather"}
    man_made_line_to_get = {"cutline", "embankment", "groyne", "goods_conveyor", "pier"}
    man_made_area_to_get = {"antenna", "bridge", "gasometer", "monitoring_station", "pier",
                            "pipeline", "pumping_station", "silo", "storage_tank", "tailings_ponds", "tower",
                            "wastewater_plant", "water_works"}
    military_node_to_get = {"airfield"}
    military_area_to_get = {"airfield", "ammunition", "barracks", "danger_area", "naval_base", "range", "training_area"}
    natural_node_to_get = {"bay", "cape", "isthmus", "peninsula", "spring", "cliff",
                           "peak", "rock", "saddle", "sinkhole", "cave_entrance", "stone"}
    natural_line_to_get = {"cliff", "ridge", "tree_row", "valley"}
    natural_area_to_get = {"scrub", "wood", "water", "wetland", "cave_entrance", "beach", "shingle",
                           "shoal", "rock", "scree", "stone", "sinkhole", "sand", "bare_rock"}
    place_node_to_get = {"city", "county", "district", "islet", "square", "island", "allotments",
                         "isolated_dwelling", "hamlet", "isolated_dwelling", "locality", "neighbourhood", "quarter",
                         "suburb", "town", "village", "city_block", "borough", "state", "region", "province"}
    place_area_to_get = {"locality", "square", "islet", "island", "allotments", "farm", "isolated_dwelling", "hamlet",
                         "village", "town", "city_block", "neighbourhood", "quarter", "suburb", "borough", "city",
                         "state", "region", "province", "district", "county", }
    power_line_to_get = {"line"}
    power_area_to_get = {"compensator", "plant"}
    railway_node_to_get = {"halt", "station", "tram_stop", }
    railway_line_to_get = {"funicular", "light_rail", "miniature", "narrow_gauge", "construction", "rail", "subway",
                           "tram", "platform"}
    railway_area_to_get = {"platform"}
    shop_node_to_get = {"convenience", "dairy", "general", "supermarket", "beverages", "greengrocer", "wholesale", }
    tourism_node_to_get = {"alpine_hut", "artwork", "apartment", "camp_site",
                           "caravan_site", "chalet", "guest_house", "hostel", "hotel", "motel", "museum",
                           "picnic_site", "viewpoint", "wilderness_hut"}
    tourism_area_to_get = {"alpine_hut", "apartment", "aquarium", "attraction", "camp_pitch", "camp_site",
                           "caravan_site", "chalet", "guest_house", "hostel", "hotel", "motel", "museum",
                           "picnic_site", "theme_park", "wilderness_hut", "zoo"}
    waterway_node_to_get = {"dock", "waterfall", "lock_gate", "weir", "sluice_gate", }
    waterway_line_to_get = {"river", "stream", "canal", "drain", "ditch", "dam", "weir", "lock_gate", }
    # waterway_area_to_get = {"dock", "boatyard", "dam", "sluice_gate"}
    water_node_to_get = {"lake", "pond"}
    water_area_to_get = {"river", "oxbow", "canal", "ditch", "lock", "fish_pass", "lake", "reservoir", "pond", "basin",
                         "stream_pool", "reflecting_pool", "moat", "wastewater"}
