*Created by Joshua Auw-Yang*


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


Now, create a virtual environment called ```env``` by running the following command in the root directory of the project:
* Windows
```sh
py -m venv env
```
* Unix/MacOS
```sh
python3 -m venv env
```

To activate the environment run ```env\Scripts\activate``` on Windows and ```source env/bin/activate``` for Unix/MacOS.
To deactivate run ```deactivate```

To install the required packages to run the project, use ```py -m pip install -r requirements.txt``` on Windows and ```python3 -m pip install -r requirements.txt``` on Unix/MacOS.

# How to Use

To start the program, run the `app.py` script.

You will be prompted with a text asking if you would like the simulated system to contain bodies of masses with **random** coordinates, masses, and velocities or to generate particles with **preset data**.

The **preset data** can be configured under the ```particlePresets\custom``` directory. The program will use the data stored in `preset.py` for the particle presets. The `preset_template.py` script can be used to help create simulations specified by the user. Two presets have been provided: `preset_single_orbit.py` and `preset_double_orbit.py`. These can be used by changing their names to `preset.py`.

## Configuration

The settings of the simulation can be adjusted in the ```config.py``` file. The following parameters can be adjusted:

* *SCALE* - Adjusts the relative scale of the entire simulation. The units of the scale is in meters (i.e. 100 units = 100 meters). Note: The randomly generated value for the masses must be adjusted for smaller scales.
* *RADIUS* - Adjusts the radius of the displayed particles
* *TIME_INTERVAL* - The time interval that passes between every frame (1 unit = 1 second)
* *BARRIER* - Toggles a barrier along the borders of the simulation that prevents particles from leaving the screen (they will bounce off)
* *QUAD_TREE_GRAPH* - Toggles a graph of the quad tree used for collision detection
* *COLLISION_INDICATOR* - Toggle that makes particles that have collided flash red 
* *BLACK_HOLE* - Toggles a static black mass at the centre of the screen with a properties determined by ```custom\black_hole.py```
* *CENTRE_OF_MASS* - Toggles a point on the map that indicates the location of the centre of mass of the simulation
* *ACCELERATION_VECTOR* - Toggles a red vector representing the acceleration of each particle
* *VELOCITY_VECTOR* - Toggles a green vector on all particles representing their velocitites

## Understanding the Simulation

### Preview

[Here](https://youtu.be/ms6C7Pz67qg) is a video showcasing the custom and random settings of the simulation along with the velocity vectors and quad tree graph.


### Coloured Masses

The simulation uses a colour map from [Matplotlib](https://matplotlib.org/stable/tutorials/colors/colormaps.html) to visually represent the weight of each particle.

Currently the simulation uses the **Plasma** colour map as shown below. Their colour is determined by a logorithmic scale with lighter masses on the left of the colour gradient and heavier masses on the right.

![image of colourmap](https://matplotlib.org/stable/_images/sphx_glr_colormaps_001.png)