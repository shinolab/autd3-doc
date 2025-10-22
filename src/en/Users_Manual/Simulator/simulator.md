# AUTD3 Simulator

AUTD Simulator (hereinafter referred to as the simulator) is a simulator for AUTD and works on Windows/Linux/macOS.

## AUTD Server

The simulator is included with the `AUTD Server`.
The installer is distributed on [GitHub](https://github.com/shinolab/autd3-server), so download it and follow the instructions to install it.

When you run `AUTD Server`, you will see a screen like the one below. Open the `Simulator` tab and press the `Run` button to start the simulator.

<figure>
  <img src="../../fig/Users_Manual/autdserver_simulator.jpg"/>
</figure>

When the simulator starts, it will be in a waiting state.

<figure>
  <img src="../../fig/sim_waiting.jpg"/>
</figure>

In this state, when you open the `Controller` using the `Remote` link, circles representing the positions of the transducers and a black panel in the center of the screen will be displayed on the simulator.

<figure>
  <img src="../../fig/sim_init.jpg"/>
</figure>

This black panel is called a "Slice", and you can use this "Slice" to visualize the sound field at any position.
At that time, the phase of the transducers is represented by hue, and the amplitude is represented by color intensity.

<figure>
  <img src="../../fig/sim_focus.jpg"/>
</figure>

Note that the sound field displayed by the simulator is a simple superposition of spherical waves, and does not consider directivity or nonlinear effects.

You can operate the Slice and camera using the GUI displayed on the left side of the screen.

### Slice Tab

In the Slice tab, you can change the size, position, and rotation of the Slice.
Rotation is specified by XYZ Euler angles.
Pressing the "xy", "yz", or "zx" buttons rotates the Slice to be parallel to each plane.

In addition, in the "Color settings" section, you can change the coloring palette and the Max pressure.
If the colors become saturated when using a large number of devices, you can increase the value of "Max pressure".

### Camera Tab

In the Camera tab, you can change the position, rotation, Field of View, Near clip, and Far clip settings of the camera.
Rotation is specified by XYZ Euler angles.

### Config Tab

In the Config tab, you can set the speed of sound, font size, and background color.

You can also toggle the show/enable/overheat settings for each device.
If show is turned off, the device will not be displayed but will still contribute to the sound field.
If enable is turned off, the device will not contribute to the sound field.
If overheat is turned on, you can simulate a state where the temperature sensor is asserted.

### Info Tab

In the Info tab, you can check the information of Silencer, Modulation, and STM for each device.

You can check the settings of Silencer, but they are not reflected in the sound field.

If "Mod enable" is turned on, Modulation will be reflected in the sound field.

Modulation and STM determine which index data to output based on real time.
This time is represented by "System time", which is the elapsed time in nanoseconds since January 1, 2000, 0:00:00.

If "Auto play" is turned on, "System time" is automatically set.
Otherwise, you can manually advance the time.
