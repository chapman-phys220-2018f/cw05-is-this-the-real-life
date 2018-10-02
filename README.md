[![Build Status](https://travis-ci.com/chapman-phys220-2018f/cw05-is-this-the-real-life.svg?branch=master)](https://travis-ci.com/chapman-phys220-2018f/cw05-is-this-the-real-life)

# PHYS220/MATH220/CPSC220 CW 5

**Author(s):** **Gage Kaazar, Morgan Holve, Jessica Trawick**

## Specification

1. The first thing we will do this week is go through the first few slides of the [Python object slides](http://slides.com/profdressel/python-objects-overview) together. Be sure to ask questions and make sure you understand the main points before continuing.
1. With your **new** group, skim through the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) that specifies proper coding style in Python for Google. No code is allowed in the Google code repositories that does not conform to this style guide. You will use this style guide to assess both your own code and that of your class mates.
1. Critique CW 3 for your group member:
    * Open a Jupyter notebook: ```critique.ipynb```
    * Have one member of your group (the "reviewee") open the python code for their previous CW03 (i.e., the module, the test module, and the Juyter notebook). Have the other member (the "reviewer") constructively critique the code in a clearly labeled section of the critique Jupyter notebook. Use the following questions as a guideline: Is it clear how the code is organized? Is the code properly documented with both docstrings and supplementary comments according to industry standards? Can you follow the algorithm of the code, i.e., what it is doing, and how? Does the code work? (Try cloning the respository and running it yourself to make sure it runs correctly.) Do you see any suggestions for how to improve the code? Are the test cases in the test module run by the code automatically by Travis? Do the tests verify correct functionality? On a scale of 0-100, the reviewer should rate the work produced by the reviewee. As the reviewer writes this critique and evaluation into the Jupyter notebook, the reviewer should discuss these questions and any issues that arise with the reviewee.
    * Repeat this exercise, but swapping roles of "reviewee" and "reviewer", and record the second critique in a new section of the notebook.
    * Note that in industry, code is typically reviewed in this fashion by fellow employees or bosses at regular intervals, for quality assurance. You are always liable for anything you commit to a repository. Moreover, constructive criticism is essential: do not demean your colleagues, dismiss their feedback, or engage in any behavior that could be construed as promoting a toxic environment. The end goal of such a process is to increase the quality of code being generated throughout the organization, so it is not to your advantage to allow bad coding practices to continue---that is, be vocal about things that could use improvement.
1. With your new partner, carefully go through all of the [Python object slides](http://slides.com/profdressel/python-objects-overview) together. Record your work in a Jupyter notebook ```python-classes.ipynb```. Discuss amongst yourselves anything that is new or unclear, and make comments in the notebook.
1. In a module, ```elementary.py```, write a new class called ```Particle``` that has three attributes: ```.mass``` that is a float, as well as ```.position``` and ```.momentum``` that are tuples of three floats. Make the constructor ```.__init__(self, x, y, z)``` set the initial floats of the ```.position``` tuple to the three values ```(x, y, z)``` passed into the constructor, set the mass to ```1.0```, and set the initial momentum to ```(0.0, 0.0, 0.0)```. Give the class a method ```.impulse(self, px, py, pz)``` that takes three floats as increments for an impulse that changes the ```.momentum``` attribute by adding the increments ```(px, py, pz)``` to the existing momentum values. Give the class a method ```.move(self, dt)``` that moves the particle by one time increment ```dt``` by using its current momentum and mass values to update its position to a new value. Make sure the docstrings for the class and all methods accurately describe what units you expect for each of the attributes and values.
1. In ```elementary.py```, write another class ```ChargedParticle``` that subclasses ```Particle``` and adds an attribute ```.charge```. Write one more class ```Electron``` that subclasses ```ChargedParticle```. When an instance of electron is created, make sure its constructor sets the charge and mass to the appropriate constants contained in the module [```scipy.constants```](https://docs.scipy.org/doc/scipy/reference/constants.html) (make sure the sign of the charge is correct for an electron).  Similarly, write a class ```Proton``` that also subclasses ```ChargedParticle``` and sets the attributes ```.charge``` and ```.mass``` to the proper values for a proton.
