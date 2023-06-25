To compile the `temperature_monitor.py` script as a FAP using fbt, you can follow these steps:

1. Clone the Flipper Zero firmware repository:

```
git clone https://github.com/flipperdevices/flipperzero-firmware.git && cd flipperzero-firmware
```

2. Prepare FBT Environment

https://github.com/flipperdevices/flipperzero-firmware/blob/dev/documentation/fbt.md#environment

3. Create the new directory "tmpc" in your FAP :

```
 mkdir tmpc && cd tmpc
```

4. Download the `temperature_monitor.py` script into the `tmpc` directory.
   
```
wget https://raw.githubusercontent.com/4k4xs4pH1r3/Flipper-Zero/main/temperature_monitor/temperature_monitor.py
```

5. Download the manifest.json file for your mtpc FAP into the `tmpc` directory.

```
wget https://raw.githubusercontent.com/4k4xs4pH1r3/Flipper-Zero/main/temperature_monitor/manifest.json
```

6. Run the following command to compile the FAP:

```
cd .. && ./fbt build mtpc
```

This will compile the `temperature_monitor.py` script into a FAP that can be flashed to the Flipper ZeZero.Here are some additional notes:

7. Notes:

* The `fbt build` command will automatically create a build directory for your FAP. The compiled FAP will be located in the `build/latest` directory.
* You can also use the `fbt flash` command to flash the compiled FAP to the Flipper Zero.
* For more information on compiling FAPs, please see the fbt documentation: https://github.com/flipperdevices/flipperzero-firmware/blob/dev/documentation/fbt.md.
