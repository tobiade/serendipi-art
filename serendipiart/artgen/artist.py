from abc import ABC, abstractmethod
import io


class Artist(ABC):
    @abstractmethod
    def draw() -> io.BytesIO:
        raise NotImplementedError


class ArtistFactory(ABC):
    @abstractmethod
    def make(self, seed: int, img_width: int, img_height: int) -> Artist:
        raise NotImplementedError
