======================
Pulse Pal for Python 3
======================


.. image:: https://img.shields.io/pypi/v/pulse_pal.svg
        :target: https://pypi.python.org/pypi/pulse_pal

.. image:: https://img.shields.io/travis/mmyros/pulse_pal.svg
        :target: https://travis-ci.com/mmyros/pulse_pal

.. image:: https://readthedocs.org/projects/pulse-pal/badge/?version=latest
        :target: https://pulse-pal.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/mmyros/pulse_pal/shield.svg
     :target: https://pyup.io/repos/github/mmyros/pulse_pal/
     :alt: Updates



Unofficial port of Pulse Pal for Python 3


* Free software: MIT license
* Documentation: https://pulse-pal.readthedocs.io.


Features
--------
- Python 3 compatibility
- Easy install
- Command line interface (In progress)
- Limited support

Test your Pulse Pal connection
------------------------------

.. code-block:: python

    def test_pulse_pal(serialPortName='COM10'):
        import serial,struct

        OpMenuByte = 213
        serialObject = serial.Serial(serialPortName, 115200, timeout=1)
        handshakeByteString = struct.pack('BB', OpMenuByte, 72)
        serialObject.write(handshakeByteString)
        Response=serialObject.read(5)
        print(len(Response))

    test_pulse_pal('COM10')


