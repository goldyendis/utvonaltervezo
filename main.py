from osmiumstart import OsmiumStart


def main() -> None:
    osmium_start = OsmiumStart()
    osmium_start.get_areas()
    # osmium_start.get_nodes()
    # osmium_start.get_lines()
    # osmium_start.highway_thread()
    # osmium_start.building_thread()


if __name__ == '__main__':
    main()
