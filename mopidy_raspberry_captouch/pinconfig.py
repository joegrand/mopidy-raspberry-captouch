# Based on https://github.com/pimoroni/mopidy-raspberry-gpio

from collections import namedtuple

from mopidy import config
from mopidy.config import types


class ValidList(list):
    def __format__(self, format_string=None):
        if format_string is None:
            format_string = ", "
        return format_string.join(self)


class PinConfig(config.ConfigValue):
    tuple_pinconfig = namedtuple(
        "PinConfig", ("event")
    )

    valid_events = ValidList(
        ["play_pause", "stop", "prev", "next", "volume_up", "volume_down"]
    )

    def __init__(self):
        pass

    def deserialize(self, value):
        if value is None:
            return None

        value = types.decode(value).strip()

        value = value.split(",")

        # Event setting is required
        if len(value) < 1:
            return None

        event = value[0]

        if event not in self.valid_events:
            raise ValueError(
                f"invalid event for pin config {event} (Must be {self.valid_events})"
            )

        return self.tuple_pinconfig(event)

    def serialize(self, value, display=False):
        if value is None:
            return ""
        value = f"{value.event}"
        return types.encode(value)
