# DISORT
DISORT compiles the DISORT radiative transfer code into a .so file so it can be imported into Python.

Dependencies
============
- numpy

Install
=======
Note that I've only tested this on Ubuntu.
- Install gfortran. On Ubunutu it's simple: sudo apt-get install gfortran
- Clone this repo from Github
- cd into the cloned repo and run: "pip install ."

Miscellaneous
=============
- I got DISORT at: http://www.rtatmocn.com/disort/
- I included a tarball of the most recent release, along with modified DISORT code. These modifications are 
expanded upon in changelog.txt
