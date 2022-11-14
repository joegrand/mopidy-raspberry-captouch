# Microchip/SMSC CAP1166 Capacitive Touch Sensor
# Joe Grand [@joegrand]
# Based on https://github.com/pimoroni/mopidy-raspberry-gpio

VOLUME_STEP = 5

import logging

import pykka
from mopidy import core

logger = logging.getLogger(__name__)

import touchphat  # https://github.com/pimoroni/touch-phat

class RaspberryCaptouchFrontend(pykka.ThreadingActor, core.CoreListener):
    def __init__(self, config, core):
        super().__init__()

        self.core = core
        self.config = config["raspberry_captouch"]
        self.pin_settings = {}

        for key in self.config:
            if key.startswith("cs"):
                pin = int(key.replace("cs", ""))
                settings = self.config[key]
                if settings is None:
                  continue

                # set event as specified in mopidy.conf to desired button
                self.pin_settings[pin] = settings
                #logger.info(self.pin_settings[pin])

        # set up capacitive touch to call event handler if any button is "pressed"
        touchphat.on_touch([1, 2, 3, 4, 5, 6], handler=self.handle_touch)

    def handle_touch(self, pad):
        pin = pad.pad
        #logger.info("Touch detected: CS%d", pin)

        settings = self.pin_settings[pin]
        event = settings.event
 
        if event:
            self.dispatch_input(event, settings)

    def dispatch_input(self, event, settings):
        handler_name = f"handle_{event}"
        try:
            #logger.info(handler_name)
            getattr(self, handler_name)(settings)
        except AttributeError:
            raise RuntimeError(
                f"Could not find input handler for event: {event}"
            )

    def handle_play_pause(self, config):
        if self.core.playback.get_state().get() == core.PlaybackState.PLAYING:
            self.core.playback.pause()
        else:
            self.core.playback.play()

    def handle_stop(self, config):
        self.core.playback.stop()

    def handle_next(self, config):
        self.core.playback.next()

    def handle_prev(self, config):
        self.core.playback.previous()

    def handle_volume_up(self, config):
        volume = self.core.mixer.get_volume().get()
        volume += VOLUME_STEP
        volume = min(volume, 100)
        self.core.mixer.set_volume(volume)
        #logger.info(volume)

    def handle_volume_down(self, config):
        volume = self.core.mixer.get_volume().get()
        volume -= VOLUME_STEP
        volume = max(volume, 0)
        self.core.mixer.set_volume(volume)
        #logger.info(volume)
