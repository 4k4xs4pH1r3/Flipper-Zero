"""
This code monitors the temperature of a PC with Windows using the Flipper Zero.

Documentation:

1. [Read the flipperzero documentation](https://github.com/flipperdevices/flipperzero-firmware/tree/dev)

2. [Clone the source code](git clone --recursive https://github.com/flipperdevices/flipperzero-firmware.git)

3. [Build the code as a FAP using the fbt tool](https://github.com/flipperdevices/flipperzero-firmware/blob/dev/documentation/fbt.md)

4. [Copy the FAP file to the ext/apps directory on your Flipper Zero SD card](https://docs.flipperzero.one/basics/sd-card)

5. [Run the FAP by pressing Down on the Flipper Zero home screen and then selecting the Archive app](https://docs.flipperzero.one/basics/first-start)

The FAP will start running and it will continue to monitor the temperature of your PC until you stop it.
"""

import flipperzero
import time

def main():
    # Initialize the Flipper Zero
    fzero = flipperzero.FlipperZero()

    # Get the current time
    now = time.time()

    # Check the temperature of the PC
    temp = fzero.temp()

    # Print the temperature
    print("The temperature of the PC is {} degrees Celsius".format(temp))

    # Sleep for 1 second
    time.sleep(1)

if name == "main":
    main()
