from multiprocessing import Process
from osmiumstart import OsmiumStart


def main() -> None:
    """Starting multiple process"""
    osmium_start = OsmiumStart()
    osmium_start.building_thread()
    # t1 = Process(target=osmium_start.get_nodes)
    # t2 = Process(target=osmium_start.get_areas)
    # t3 = Process(target=osmium_start.building_thread)
    # t4 = Process(target=osmium_start.get_lines)
    # t5 = Process(target=osmium_start.highway_thread)
    # t3.start()
    # t5.start()
    # t1.start()
    # t2.start()
    # t4.start()
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # t5.join()


if __name__ == '__main__':
    main()
    # TODO boundary
