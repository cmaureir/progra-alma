Lecture 30
----------

   * CCL-related topics (to be defined)


http://wikis.alma.cl/bin/view/AIV/CCLUserDocumentation
http://wikis.alma.cl/bin/view/AIV/CCLFAQ
http://wikis.alma.cl/bin/view/AIV/CCLDeviceSoftware
http://wikis.alma.cl/bin/view/AIV/CCLDeviceCommissioning
http://wikis.alma.cl/bin/view/AIV/CCLCommissioningProcedure

http://aivwiki.alma.cl/index.php/CCL_Device_Software

CONTROL Subsystem
-----------------

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

The Control Command Language (CCL)
----------------------------------

Apart from the Observing Modes there is another way of making use of the underlying hardware devices: using the Control Command Language (CCL). The CCL is Python plus the corresponding device or mode wrappings (usually located in src/CCL/). By using the CCL it is possible to manually invoke and control the different devices and/or observing modes. It is also possible to write custom scripts whenever necessary.

For example, review the CCL wrapper for the DGCK device at CONTROL/Device/HardwareDevice/DGCK/src/CCL. Note the that the base-class is code-generated and that the child-class contains the custom functionality.
There are also some documents available at EDM:

What is CCL?
------------

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
---------------

What do I need to run CCL on Windows?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You only need a SSH-client in order to connect to the computer ("osf-gns" at the AIV-Lab). There are many SSH-clients for Windows, one well known is "putty" which you can get from here.
'What do I need to run CCL on Mac?
As in the case of Windows, you just need a SSH-client in order to connect to the computer ("osf-gns" at the AIV-Lab). A free client can be downloaded from here (TBD).

What do I need to run CCL on LINUX?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From Linux open a terminal and use the "ssh" command to log into the computer ("osf-gns" at the AIV-Lab). Example: "ssh -Y osf-gns" (here -Y allows you to also start GUIs from that terminal)

Using CCL
----------

How do I run CCL on my computer?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In reality, you do not run CCL on "your" computer, but on a remote one which is
connected to the corresponding control units (ABMs).
This means that from your computer you first have to log into this computer,
e.g. using a SSH-client (see explanation above). The CCL Python wrapper is then
started by issuing "startCCL" at the command prompt.

How do I monitor and control a device?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First of all you need to create an "instance" belonging to the physical device you want to monitor or control. For this review the list of device types you obtain when issuing cclhelp(). Once you know the device type you create your instance by indicating its location (e.g. antenna name), its absolut component name, and eventually some additional parameters (e.g. polarization), for example:

>>>lpr = LPR("DA41")
>>>ifp0 = IFProc("DA41", 0)
>>>lo20 = LO2(componentName="CONTROL/DA41/LO2BBpr0")

Use help(<device type>), e.g. help(LO2) for a detailed description and an example of usage if you encounter problems. Note that "lorr", "ifp0" and "lo20" are variables that you can define as you want, for example, you could have used "x", "y" and "z" instead. However, a good convention is to use the device's name in lowercase. You can now use your variable to access both monitor- and control points, for example:

>>>lpr.GET_TEMP0_TEMP()
(2.9744236469268799, 134315513756484480L)
>>>lpr.SET_OPT_SWITCH_PORT(8)

As you can see, the methods that retrieve the monitor points all start with 'GET_', and the ones for control points with 'SET_'. Use tab-completion and help(<function>) for further details:

>>>help(lo20.SET_PHASE_VALS)
Last but not least, you can also display the devices monitor points or the status information using the helper functions "monitor" and "status", for example:
>>>monitor(ifp0)
>>>status(lpr)

When should I use the sitckyFlag option?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the sotfware is not in operational mode, eg when just the containers are up and running you should add the stickyFlag=True option to your device instanciation:
psa=PSA("DV01",stickyFlag=True)

Troubleshooting
---------------

I can't instantiate a device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The software might not be in operational state. Add the stickyFlag=True to your call

I cant get any information from a device after an instantiation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You should turn on the device from the software point of view for that you should use the turn_on() function:

psa=PSA("DV01",stickyFlag=True)
turn_on(psa)
psa.STATUS()

Also read the CCL documentation of your device, some of them have a more complicated way of turning on devices.
