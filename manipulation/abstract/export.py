from abc import ABC, abstractmethod

from manipulation.export_shp import GeomType


class Export(ABC):
    """Interface to export GeoDataframes"""
    @abstractmethod
    def export(self, filename=None) -> None:
        """
        Factory to decide from the geometry type what to export
        :param filename: str | Can export the same data to multiple file with different filename
        """

    @abstractmethod
    def export_feature(self, geom_type: GeomType, filename=None) -> None:
        """
        Concrete export of the Data
        :param geom_type: GeomType | Type of the geometry to be exported
        :param filename: str | Can export the same data to multiple file with different filename
        """
