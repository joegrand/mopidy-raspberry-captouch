import logging
import pathlib

import pkg_resources

from mopidy import config, ext

from .pinconfig import PinConfig

__version__ = pkg_resources.get_distribution("Mopidy-Raspberry-Captouch").version

logger = logging.getLogger(__name__)


class Extension(ext.Extension):

    dist_name = "Mopidy-Raspberry-Captouch"
    ext_name = "raspberry_captouch"
    version = __version__

    def get_default_config(self):
        return config.read(pathlib.Path(__file__).parent / "ext.conf")

    def get_config_schema(self):
        schema = super().get_config_schema()
        for pin in range(1,7):
            schema[f"cs{pin:d}"] = PinConfig()
        return schema

    def setup(self, registry):
        from .frontend import RaspberryCaptouchFrontend
        registry.add("frontend", RaspberryCaptouchFrontend)
