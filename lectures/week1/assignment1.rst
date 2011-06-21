Assignment 1
============

    *Exercise from* [Lang09]_.


How to cook the perfect egg.
----------------------------

As an egg cooks, the proteins ﬁrst denature and then coagulate.
When the temperature exceeds a critical point, reactions begin and
proceed faster as the temperature increases.

In the egg white the proteins start to coagulate for temperatures above 63°C, while in the yolk
the proteins start to coagulate for temperatures above 70°C. For a soft
boiled egg, the white needs to have been heated long enough to coagulate at a temperature above 63°C,
but the yolk should not be heated above 70°C.
For a hard boiled egg, the center of the yolk should be allowed to reach 70°C.

The following formula expresses the time t it takes (in seconds) for
the center of the yolk to reach the temperature `T_y` (in Celsius degrees):

.. math::

    t = \frac{M^{2/3} c \rho^{1/3}}
             {K\pi^2(4\pi/3)^{2/3}}
        \ln\left[
            0.76\frac{T_o - T_w}
                     {T_y - T_w}
        \right],



Here, `M` , `\rho`, `c`, and `K` are properties of the egg:

* `M` is the mass,
* `\rho` is the density,
* `c` is the speciﬁc heat capacity,
* and `K` is thermal conductivity.

 Relevant values are:

* `M = 47\,[\text{g}]` for a small egg and 
  `M = 67\,[\text{g}]` for a large egg,
* `\rho = 1.038\,[\text{g}\,\text{cm}^{-3}]`,
* `c = 3.7\,[\text{J}\,\text{g}^{-1} \text{K}^{-1}]`, and
* `K = 5.4\cdot 10^{-3}\,[\text{W}\,\text{cm}^{-1} \text{K}^{-1}]`.

Furthermore, `T_w` is the temperature (in C
degrees) of the boiling water (`100^{o}`), and `T_o` is the original temperature (in C
degrees) of the egg before being put in the water.

Write a program which receive as input
the original temperature `T_o` of the egg
and return as output the time in seconds
that it takes to reach the maximum temperature to
cook properly.

You can use the `T_y` with `70^{o}` or `63^{o}` celcius degrees.

**Hint:**

* to use the ``ln()`` function do this::

   from math import log
   n = 10 # example number
   log(n) # calculate the ln(n)

* to use the ``pi`` constant, do this::

   from math import pi
   pi # return 3.141592653589793



.. [Lang09] Hans Petter Langtangen.
           *A Primer on Scientific Programming with Python*.
           Springer-Verlag, 2009.
