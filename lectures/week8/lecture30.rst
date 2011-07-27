Lecture 30 - CCL Introduction
-----------------------------

ALMA Control Subsystem
=======================

The CONTROL subsystem refers to all the required software
that is needed to move, operate the front- and backend devices,
the antennas and complete arrays of antennas.
To get the big picture review the document `Control Subsystem Design`_
To retrieve the CONTROL software source code you can
CVS check-out the package *CONTROL*.
If you want to compile and install it on your PC retrieve also the
packages "ICD" and "OFFLINE", then build (make build) them in the order
ICD, OFFLINE, CONTROL.

.. _`Control Subsystem Design`: http://edm.alma.cl/forums/alma/dispatch.cgi/SubsystemDesign/showFile/100015/d20030221230518/Yes/Control+Design.pdf

Based on ALMA Common Software (ACS): CORBA-based Control framework
Each HW device control module: One ACS Component, running inside an ABM
Components expose an external communication interface

Diagrama:

Componentes dentro de Container, dentro de ABM <--- Puerto CAN ---> Antenna


HW device control components are (mostly) code-generated, based on an XML spreadsheet, based on device ICD
XML spreadsheets are written in a way understandable for SW and HW engineers
Represents ICD – SW “mapping”
Allows to easily detect ICD v/s SW inconsistencies


Arquitectura.

PC -> CCL Wrapper -> SW device (Component) -> Control subsystem
                            |
                        HW device


Containers, Components & Properties

* Containers contain a set of components
    * The most important containers for CCL are the antenna containers (e.g. “DV01”, “DA41”, …)
* Components usually wrap physical hardware devices
    * DGCK
    * OpticalTelescope
* Properties are specific control or monitor points of a component
    * PS_VOLTAGE_CLOCK 
    * CCD_TEMPERATURE
* For standard HW devices the control and monitor points are defined at the ICDs

-----

CCL - Getting Started

* Starting CCL
    * startCCL (from command line)
* Getting help
    * In [1]: cclhelp()
        * Displays all loaded classes, functions and variables
    * In [2]: help(<object>)
        * Display the detailed help for <object>


Instantiating Objects/Devices

* Applies only to classes/device types
* Many instances are possible (e.g. the same device on two antennas)
* The classes have different constructors (see help)
* Once an object is instantiated it can be used to access the HW device
* Examples:
    * In [1]: dgck = DGCK(“DV01”)
    * In [2]: st = SampTool()

MonitorTool & monitor

* Allows to display property values on the screen in real-time
* MonitorTool is based on the ACS Monitor implementation
* Values refresh rate is defined in the CDB (default_trigger_time) and can/should be turned if incorrect
* Wrapper function “monitor(…)” provides a simplified syntax

SampTool & sample

* Allows to sample properties at high frequency (up to 20Hz) and to store the data into text files
* SampTool is based on the ACS Sampling System
* Does not allow precise TE sampling
* Wrapper function “sample” provides a simplified syntax

STATUS() Command

* This method will display a summary of the device status.
* Basically, this method contains the information of the device like type, name and the “status” monitor point displayed properly (decoded).
* It should be available for every device and can be called from the python interface as <device>.STATUS()

Device Grouping

* CCL allows the instantiation of several devices (same type) at the same time passing the list of devices as parameter.
* For example: instantiation of the DGCK for antennas DV01 and DA41
    * In [1]: dgGroup = DGCK([“DV01”, “DA41”])
* All the functionalities available for a single device is also available for the group.
* Monitor point values are returned using a dictionary.
    * In [8]: dg.GET_PS_VOLTAGE_CLOCK()
    * Out[8]:
    * {'DA41': (6.4907135963439941, 134258794536106775L),
    * 'DV01': (6.0117301940917969, 134258794540835083L)}


.. ODT mmora

Control Command Language (CCL)

* Each device control component (c++) has an associated Python
  wrapper, which is part of the system's CCL libraries.
* Therefore, CCL commands directly call an action of the control
  component's communication interface.

  CCL class ---> Componente [ Container ]

* Python scripts can import CCL library class
    * from CCL.MountVertex import MountVertex
    * mount = MountVertex('DV01')
    * mount.GET_ANTENNA_TEMPS()
* There is also a ready-to-use startCCL environment.
* startCCL = ipython + imports + special functions
* Some Mount monitor points are requested every TE by an internal process and stored in a data structure
    * statusData = mount.getMountStatusData()
    * statusData.azPosition
* These values are used internally by the SW and aren't always available through an exposed monitor point
    * AZ/EL current and commanded positions
    * (Aux) Pointing model corrections
    * AZ/EL encoder readouts
    * Subreflector current and commanded positions

.. Documentation

2.2 CCL Language Description

The CCL is intended to address a range of requirements, from allowing technicians and
engineers very low level access to hardware devices, to providing a simple environment
for inexperienced users to script their scientific observations. The design of the CCL is
hierarchical in nature allowing users to “burrow down” to the level required to
accomplish their goal.

2.2.1 Observing Modes
The observing modes are the highest level of synchronization in the CCL, these modules
provide functionality for managing all the equipment in an array. For instance tuning the
LO system to a specified frequency or having all antennas in the array point in the same
direction. The observing modes can be coupled to data capture and the production of
astronomical data in the ALMA Science Data Model (ASDM) format. For most
scientific users, there should not be a reason to work below the level of an observing
mode.
The observing modes are tied to specific ALMA use cases, for instance Single-Field
Interferometry, Optical Pointing, and Tower Holography all have observing modes
tailored to their specific requirements.

The name of these objects as observing modes can cause some confusion. An observing
mode in the CCL is a class which is designed to simplify and coordinate a type of
observing. The standard observing modes which you encounter in the ALMA Observing
Tool, and later in this document are scripts written in the CCL to implement a particular
observing strategy. Thus the standard observing mode scripts make use of the observing
mode CCL objects to implement a particular observing strategy. As an example the
standard observing mode script to perform a calibrator survey is very different from the
script to do an observation of a single source, but both scripts would make use of the
functionality provided by the single-field interferometry observing mode class in the
CCL.

2.2.2 Mode Controllers
Mode controllers play the same role for an antenna that the observing modes do for an
Array. These objects still have a concept of scientific intent for instance knowing that
setting frequency when using the holography receiver and setting frequency when using
the front-end are very different actions.
Users should be aware that there is no effort to synchronize changes made at the mode
controller level, with status at the observing mode level. As an example consider the
following case, the user sets the frequency of an entire array using the setFrequency
command of the observing mode. Then the user sets the frequency of antenna DA41
using the mode controller setFrequency command. Only the hardware in the antenna
DA41 will be affected, so the array will be in an inconsistent state and, depending on the
settings of the central photonic reference, the LO chain in DA41 may not even lock. This
level of flexibility is required to allow system testing but should only be utilized by users
who are aware of the full system implications.

2.2.3 Devices
Devices form the lowest layer in our hierarchy. These classes map one-to-one with the
physical hardware and provide both integrated methods (i.e. a single method to tune and
lock the second local oscillator module) and simple peek/poke level access, allowing
direct manipulation of most monitor and control points.

2.2.4 Utility Classes
There are a set of utility classes also contained within the CCL, these classes provide a
wide range of services. For example the SkyDelayServer module allows communication
and control of the delay server, while the classes in the CCL.Source package provide
flexible ways to specify an astronomical source. The user is referred to the reference
manual for the description of these classes.


The Control Command Language (CCL)
==================================

Apart from the Observing Modes there is another way of making use of the underlying hardware devices: using the Control Command Language (CCL). The CCL is Python plus the corresponding device or mode wrappings (usually located in src/CCL/). By using the CCL it is possible to manually invoke and control the different devices and/or observing modes. It is also possible to write custom scripts whenever necessary.

For example, review the CCL wrapper for the DGCK device at CONTROL/Device/HardwareDevice/DGCK/src/CCL. Note the that the base-class is code-generated and that the child-class contains the custom functionality.
There are also some documents available at EDM:

What is CCL?
============

CCL stands for Control Commmand Language,
which allows you to access the control software using a Python wrapper.
The CCL is a high-level scripting language that is used within the
Control subsystem to control the ALMA telescope. It has two functions:
to serve as the language in which standard “observing scripts” are written
and to serve as a suite of interactive commands to be used by hardware engineers,
testing or debugging equipment, or staff astronomers, developing new observing
procedures.
The language itself can be used in two modes,
reflecting the two purposes just stated.
For more information please refer to the document
Control Subsystem Control Command Language.
Where do I find CCL technical information?
Most of the information regarding CCL is self-contained in the CCL wrapper,
based on the Python documentation utility pydoc.
To access the documentation use the command help(<function>)
where <function> can be any of the device types or functions listed at cclhelp().
For general information regarding the usage of CCL you can also review the presentation
of the training session.

Installing CCL
==============

What do I need to run CCL on Windows?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You only need a SSH-client in order to connect to the computer ("osf-gns" at the AIV-Lab). There are many SSH-clients for Windows, one well known is "putty" which you can get from here.
'What do I need to run CCL on Mac?
As in the case of Windows, you just need a SSH-client in order to connect to the computer ("osf-gns" at the AIV-Lab). A free client can be downloaded from here (TBD).

What do I need to run CCL on LINUX?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From Linux open a terminal and use the "ssh" command to log into the computer ("osf-gns" at the AIV-Lab). Example: "ssh -Y osf-gns" (here -Y allows you to also start GUIs from that terminal)

FAQ CCL
==========

How do I run CCL on my computer?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In reality, you do not run CCL on "your" computer, but on a remote one which is
connected to the corresponding control units (ABMs).
This means that from your computer you first have to log into this computer,
e.g. using a SSH-client (see explanation above). The CCL Python wrapper is then
started by issuing "startCCL" at the command prompt.

How do I monitor and control a device?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First of all you need to create an "instance" belonging to the physical device you want to monitor or control. For this review the list of device types you obtain when issuing cclhelp(). Once you know the device type you create your instance by indicating its location (e.g. antenna name), its absolut component name, and eventually some additional parameters (e.g. polarization), for example:

>>>lpr = LPR("DA41")
>>>ifp0 = IFProc("DA41", 0)
>>>lo20 = LO2(componentName="CONTROL/DA41/LO2BBpr0")

Use help(<device type>), e.g. help(LO2) for a detailed description and an example of usage if you encounter problems. Note that "lorr", "ifp0" and "lo20" are variables that you can define as you want, for example, you could have used "x", "y" and "z" instead. However, a good convention is to use the device's name in lowercase. You can now use your variable to access both monitor- and control points, for example:

>>>lpr.GET_TEMP0_TEMP()
(2.9744236469268799, 134315513756484480L)
>>>lpr.SET_OPT_SWITCH_PORT(8)

As you can see, the methods that retrieve the monitor points all start with *GET_*, and the ones for control points with *SET_*. Use tab-completion and help(<function>) for further details:

>>>help(lo20.SET_PHASE_VALS)
Last but not least, you can also display the devices monitor points or the status information using the helper functions "monitor" and "status", for example:
>>>monitor(ifp0)
>>>status(lpr)

When should I use the sitckyFlag option?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the sotfware is not in operational mode, eg when just the containers are up and running you should add the stickyFlag=True option to your device instanciation:
psa=PSA("DV01",stickyFlag=True)

Troubleshooting
===============

I can't instantiate a device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The software might not be in operational state. Add the stickyFlag=True to your call

I cant get any information from a device after an instantiation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You should turn on the device from the software point of view for that you should use the turn_on() function:

psa=PSA("DV01",stickyFlag=True)
turn_on(psa)
psa.STATUS()

Also read the CCL documentation of your device, some of them have a more complicated way of turning on devices.





Exercises
~~~~~~~~~~

1. Exercise 1
    * Start CCL
    * Display the available device types, functions and variables
    * Display the help-text for the classes OpticalTelescope and for the DGCK
    * Display the help-text for the functions pingabm(), get_devices() and turn_on()

2. Exercise 2
    * Instantiate the following objects (check the help-text for __init__ to obtain the constructors parameters):
        * DGCK on container DV01 (if available)
        * OpticalTelescope on container DV01 (if available)
        * SampTool
        * MonitorTool

3. Exercise 3
    * Access the device functionality (use tab-completion to see the available methods):
        * Read the value of PS_VOLTAGE_CLOCK of the DGCK
        * Check if the OpticalTelescope aperture is open or closed

4. Exercise 4
    * Review the help description by issuing “help(MonitorTool)” and “help(monitor)”
    * Use the monitor() function to display the DGCK’s PS_VOLTAGE_CLOCK property on the screen

5. Exercise 5
    * Review the help description by issuing “help(SampTool)” and “help(sample)”
    * Use the sample() function to register the values of the DGCK’s PS_VOLTAGE_CLOCK and DGCK_STATUS properties every 100ms

6. Exercise 6
    * Execute the STATUS method for DGCK on container DV01.
    * Execute the STATUS method for FLOOG on container DA41.

7. Exercise 7
    * Instantiate a group of DGCKs devices for DV01 and DA41 containers.
    * Execute STATUS() method for the group.
    * Use DelayTrackingEnabled() method for the DGCK group.
    * Set DelayTracking to False over the DGCK group.
