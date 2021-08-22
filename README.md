# GRAVITY SIMULATION

This is a 2D simulation that recreates the motion of bodies of masses in space through gravitational attraction.
This provides insight on how moons, planets, and galaxies like the Milky Way are formed.

The simulation is based off of Newtonian Physics for calculating the force of gravity between masses using the [gravitation constant - G](https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation). 
Collision detection of the masses was done through use of the [Quad Tree](https://en.wikipedia.org/wiki/Quadtree) data structure for a more efficient time complexity of O(nlogn).



# Getting Started


## Installing pip

First, make sure you have ```pip``` installed on your system. Running the following command will display the current version of pip installed on your system:
* Windows
```sh
py -m pip --version
```
* Unix/MacOS
```sh
python3 -m pip --version
```


## Installing and creating a virtual environment
Next, make sure you have virtual environments installed using the following command:
* Windows
```sh
py -m pip install --user virtualenv
```
* Unix/MacOS
```sh
python3 -m pip install --user virtualenv
```


Create a virtual environment by running the following command:
* Windows
```sh
py -m venv env
```
* Unix/MacOS
```sh
python3 -m venv env
```

