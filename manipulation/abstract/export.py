from abc import ABC, abstractmethod


class Export(ABC):
    """Interface to export GeoDataframes"""
    @abstractmethod
    def export(self, filename=None) -> None:
        """
        Factory to decide from the geometry type what to export
        :param filename: str | Can export the same data to multiple file with different filename
        """
        pass

    @abstractmethod
    def export_feature(self, geom_type: str, filename=None):
        """
        Concrete export of the Data
        :param geom_type: str | Point, line, area as String representation
        :param filename: str | Can export the same data to multiple file with different filename
        """
        pass
