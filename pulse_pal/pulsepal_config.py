#%%

"""

Author: tclarity

This script creates a definition to configure PulsePal stimulation settings for photometry, optogenetics, cameras etc.

Adapted from scripts.py by mmyros

args: output channels 1-4, acquisition_freq: 20 or 40, stim_duration: seconds, optional stim_delay: seconds

"""

# first, pip install pulse_pal @ https://github.com/mmyros/pulse_pal

from pulse_pal import PulsePal
import time


def pulsepal_config(channel, acquisition_freq, stim_duration, stim_delay=0):
    myPulsePal = PulsePal()  # Create a new instance of a PulsePal object
    myPulsePal.connect(serialPortName='COM10')  # Connect to PulsePal on port COM# CHANGE FOR YOUR COMPUTER # will this throw an error if it tries to connect simultaneously?

    assert channel in [1, 2, 3, 4], NotImplemented(f'Output Channel {channel} is not implemented')
    assert acquisition_freq in [20, 40], NotImplemented(f'Frequency {acquisition_freq} is not implemented')

    if acquisition_freq == 40:
        photo_up_time = 0.017
        photo_down_time = 0.008
    elif acquisition_freq == 20:
        photo_up_time = 0.035
        photo_down_time = 0.015

    myPulsePal.setDisplay("Stimming", "")
    myPulsePal.programOutputChannelParam('isBiphasic', channel, 0)
    myPulsePal.programOutputChannelParam('phase1Voltage', channel, 5)
    myPulsePal.programOutputChannelParam('interPulseInterval', channel, photo_down_time)
    myPulsePal.programOutputChannelParam('restingVoltage', channel, 0)
    myPulsePal.programOutputChannelParam('phase1Duration', channel, photo_up_time)
    myPulsePal.programOutputChannelParam('pulseTrainDuration', channel, stim_duration)
    myPulsePal.programOutputChannelParam('pulseTrainDelay', channel, stim_delay)


myPulsePal.triggerOutputChannels(1, 1, 1, 0)    # user triggers stimulation manually
time.sleep(stim_duration)

myPulsePal.setDisplay("Done", " Click for menu")

myPulsePal.disconnect()
