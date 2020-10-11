=====
Usage
=====

To use Pulse Pal for Python 3 in a project::

    from pulse_pal.pulse_pal import PulsePal

Through python
--------------

.. code-block:: python

    from pulse_pal import PulsePal
    myPulsePal = PulsePal()  # Create a new instance of a PulsePal object
    myPulsePal.connect(serialPortName='COM10')  # Connect to PulsePal on port COM# (


Through console
---------------

See help:

.. code-block:: bash

   pulse_pal --help

Set phase 1 voltage to 5:

.. code-block:: bash

   pulse_pal --do set --port COM2 --param_name phase1Voltage --param_value 5

Trigger channel 1:

.. code-block:: bash

   pulse_pal --do trigger --channel 1


- Test your Pulse Pal connection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Easy (from console):

.. code-block:: bash

   pulse_pal --do test


- Low-level (from python):

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


See more examples in scripts.py
