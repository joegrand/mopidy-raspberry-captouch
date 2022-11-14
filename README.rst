****************************
Mopidy-Raspberry-Captouch
****************************

Mopidy extension for I2C-based capacitive touch on a Raspberry Pi

Originally created for `The World's Thinnest Boombox <http://www.grandideastudio.com/portfolio/the-worlds-thinnest-boombox>`__

This extension is not maintained. Use at your own risk.

Installation
============

Install by running::

    python3 -m pip install Mopidy-Raspberry-Captouch


Configuration
=============

Before starting Mopidy, you must add configuration for
Mopidy-Raspberry-Captouch to your Mopidy configuration file::

    [raspberry_captouch]
    enabled = true
    cs1 = prev
    cs2 = play_pause
    cs3 = stop
    cs4 = volume_down
    cs5 = volume_up
    cs6 = next


Project resources
=================

- `Source code <https://github.com/joegrand/mopidy-raspberry-captouch>`_

Credits
=======

- Author: `Joe Grand <https://github.com/joegrand>`__
- `mopidy-raspberry-gpio <https://github.com/pimoroni/mopidy-raspberry-gpio>`_
- `Pimoroni Touch pHAT <https://github.com/pimoroni/touch-phat>`_
