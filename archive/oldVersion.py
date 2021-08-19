'''Joshua Alexander Auw-Yang
'''
import math
import pygame
import random

pygame.init()
count = 0
masses_list = []
G_con = 6.67e-11
planets_num = 200
win_width = 1000
win_height = 1000
hours_per_realsecond = 168
t = (3.6 * hours_per_realsecond)

# Initializes the 'black hole' of the system
alpha = {'Mass': 2e30, 'Colour': [0, 0, 0], 'X_coord': (win_width * 100000000) / 2,
         'Y_coord': (win_height * 100000000) / 2, 'X_velocity': 0, 'Y_velocity': 0, 'X_acceleration': 0,
         'Y_acceleration': 0, 'Radius': 7}
masses_list.append(alpha)


def mass_input():
    # Stores [INPUTED] or [RANDOM] MASS, COLOUR, X+Y COORDINATES, X+Y VELOCITIES of bodies of masses
    ask = True
    while ask:
        random_input = input("Custom [C] or random [R] masses? ")
        if random_input.upper() != 'C' and random_input.upper() != 'R':
            print("Invalid Input")
            continue
        elif random_input.upper() == 'C':
            add_masses = True
            while add_masses:
                planet_name = input("Name of celestial body: ")
                planet_mass = float(input("Mass of celestial body in KG: "))
                planet_xcoord = float(input("X coordinate of celestial body in KM (1000km MAX): "))
                planet_ycoord = float(
                    input("Y coordinate of celestial body in KM (1000km MAX): "))  # prevent negative values
                planet_xvelocity = float(input("X velocity of celestial body in M/S: "))
                planet_yvelocity = float(input("Y velocity of celestial body in M/S: "))
                rgb_values_list = []
                for colours in range(3):
                    rgb_value = random.randint(0, 255)
                    rgb_values_list.append(rgb_value)
                planet_name = {}
                planet_name['Mass'] = planet_mass
                planet_name['Colour'] = rgb_values_list
                planet_name['X_coord'] = planet_xcoord * 100000000
                planet_name['Y_coord'] = planet_ycoord * 100000000
                # planet_name['X_velocity'] = planet_xvelocity
                # planet_name['Y_velocity'] = planet_yvelocity
                planet_name['X_velocity'] = 0
                planet_name['Y_velocity'] = 0
                planet_name['X_acceleration'] = 0
                planet_name['Y_acceleration'] = 0
                planet_name['Radius'] = 7
                masses_list.append(planet_name)
                check_input = True
                while check_input == True:
                    another_mass = input("Add another celestial body (Y/N)? ")
                    another_mass = another_mass.upper()
                    if another_mass == 'N':
                        add_masses = False
                        check_input = False
                    elif another_mass == 'Y':
                        check_input = False
                    else:
                        print("Invalid input.")
            ask = False

        elif random_input.upper() == 'R':
            for i in range(planets_num):
                planet_name = str(random.randint(0, 10000))
                planet_name = {}
                a = random.randint(5, 9)
                power = random.randint(1, 18)
                planet_name['Mass'] = float(str(a) + 'e' + str(power))
                rgb_values_list = []
                for colours in range(3):
                    rgb_value = random.randint(0, 255)
                    rgb_values_list.append(rgb_value)
                planet_name['Colour'] = rgb_values_list
                planet_name['X_coord'] = random.randint(1, win_width) * 100000000
                planet_name['Y_coord'] = random.randint(1, win_height) * 100000000

                planet_xvelocity = random.randint(0, 50000)
                direction_xvelocity = random.randint(0, 1)
                if direction_xvelocity == 0:
                    planet_xvelocity = -planet_xvelocity

                planet_name['X_velocity'] = planet_xvelocity
                planet_yvelocity = random.randint(0, 50000)
                direction_yvelocity = random.randint(0, 1)
                if direction_yvelocity == 0:
                    planet_yvelocity = -planet_yvelocity
                planet_name['Y_velocity'] = planet_yvelocity
                planet_name['X_acceleration'] = 0
                planet_name['Y_acceleration'] = 0
                planet_name['Radius'] = 7
                masses_list.append(planet_name)

            ask = False

    graphics()


def graphics():
    # UPDATES IMAGES + IMAGE SETUP
    count = 0
    pygame.init()
    win = pygame.display.set_mode((win_width, win_height))
    run = True
    while run:
        pygame.time.delay(1)  # refresh rate of game time, 1000 = 1s
        win.fill((242, 230, 242))
        for event in pygame.event.get():  # QUIT sim
            if event.type == pygame.QUIT:
                run = False
        for body in range(len(masses_list)):
            x = round((masses_list[body]['X_coord']) / 100000000)
            y = round((masses_list[body]['Y_coord']) / 100000000)  # rounds off x and y
            colour = masses_list[body]['Colour']
            pygame.draw.circle(win, colour, (x, y), masses_list[body]['Radius'])
        pygame.display.update()
        acceleration_calc()
    pygame.quit()


def acceleration_calc():
    # Calculates R-VALUES, 'ANGLES' (similar triangles), and X+Y ACCELERATION of celestial bodies
    for first in range(len(masses_list)):
        masses_list[first]['X_acceleration'] = 0
        masses_list[first]['Y_acceleration'] = 0
        for second in range(len(masses_list)):
            if second != first:
                x_first = masses_list[first]['X_coord']
                y_first = masses_list[first]['Y_coord']
                x_second = masses_list[second]['X_coord']
                y_second = masses_list[second]['Y_coord']

                r = math.sqrt(((x_first - x_second) ** 2) + ((y_first - y_second) ** 2))
                accel = (G_con * (masses_list[second]['Mass'])) / (r ** 2)
                accel_x = (accel * (x_first - x_second)) / r
                accel_y = (accel * (y_first - y_second)) / r

                if x_first > x_second:
                    accel_x = -abs(accel_x)
                elif x_first < x_second:
                    accel_x = abs(accel_x)
                else:
                    accel_x = 0
                masses_list[first]['X_acceleration'] = masses_list[first]['X_acceleration'] + accel_x

                if y_first > y_second:
                    accel_y = -abs(accel_y)
                elif y_first < y_second:
                    accel_y = abs(accel_y)
                else:
                    accel_y = 0
                masses_list[first]['Y_acceleration'] = masses_list[first]['Y_acceleration'] + accel_y
                
                if (r / 100000) < 3500:  # combines masses

                    new_mass = masses_list[second]['Mass'] + masses_list[first]['Mass']
                    new_xvelocity = (masses_list[first]['Mass'] * masses_list[first]['X_velocity'] +
                                     masses_list[second]['Mass'] * masses_list[second]['X_velocity']) / new_mass
                    new_yvelocity = (masses_list[first]['Mass'] * masses_list[first]['Y_velocity'] +
                                     masses_list[second]['Mass'] * masses_list[second]['Y_velocity']) / new_mass
                    new_colour_list = []
                    for c in range(3):
                        a = masses_list[first]['Colour'][c]
                        b = masses_list[second]['Colour'][c]
                        colour_calc = (a + b) / 2
                        new_colour_list.append(colour_calc)
                    new_xcoord = round((masses_list[first]['X_coord'] + masses_list[second]['X_coord']) / 2)
                    new_ycoord = round((masses_list[first]['Y_coord'] + masses_list[second]['Y_coord']) / 2)
                    new_name = {}
                    new_name['Mass'] = new_mass
                    new_name['Colour'] = new_colour_list
                    new_name['X_coord'] = new_xcoord
                    new_name['Y_coord'] = new_ycoord
                    new_name['X_velocity'] = new_xvelocity
                    new_name['Y_velocity'] = new_yvelocity
                    new_name['X_acceleration'] = 0
                    new_name['Y_acceleration'] = 0
                    if masses_list[first]['Radius'] > masses_list[second]['Radius']:
                        new_name['Radius'] = masses_list[first]['Radius'] + 1
                    elif masses_list[second]['Radius'] > masses_list[first]['Radius']:
                        new_name['Radius'] = masses_list[second]['Radius'] + 1
                    else:
                        new_name['Radius'] = masses_list[first]['Radius'] + 1
                    masses_list.append(new_name)
                    if first > second:
                        del masses_list[first]
                        del masses_list[second]
                    elif second > first:
                        del masses_list[second]
                        del masses_list[first]
                    mass_created = 1
                    return

            else:
                continue
    coordinate_calc()


def coordinate_calc():
    # Calculates new VELOCITIES and X+Y POSITIONS
    for first_a in range(len(masses_list)):
        vi_x_first = masses_list[first_a]['X_velocity']
        vi_y_first = masses_list[first_a]['Y_velocity']
        accel_xa = masses_list[first_a]['X_acceleration']
        accel_ya = masses_list[first_a]['Y_acceleration']
        x_firsta = masses_list[first_a]['X_coord']
        y_firsta = masses_list[first_a]['Y_coord']

        x_firsta = vi_x_first * (t) + (1 / 2) * (accel_xa) * (t ** 2) + x_firsta
        y_firsta = vi_y_first * (t) + (1 / 2) * (accel_ya) * (t ** 2) + y_firsta

        vi_x_first = vi_x_first + (accel_xa) * (t)
        vi_y_first = vi_y_first + (accel_ya) * (t)

        # Barrier/limit
        if (x_firsta / 100000000) > win_width or (x_firsta / 100000000) < 0:
            vi_x_first = -vi_x_first
        if (y_firsta / 100000000) > win_height or (y_firsta / 100000000) < 0:
            vi_y_first = -vi_y_first

        masses_list[first_a]['X_coord'] = x_firsta
        masses_list[first_a]['Y_coord'] = y_firsta
        masses_list[first_a]['X_velocity'] = vi_x_first
        masses_list[first_a]['Y_velocity'] = vi_y_first


mass_input()