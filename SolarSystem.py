import Physics
import matplotlib.pyplot as plt
from matplotlib import animation

mass = {
    "sun" : 1.989e30,
    "earth" : 5.972e24
}

initial_position = {
    "sun" : Physics.Vector(0,0),
    "earth" : Physics.Vector(1.496e11,0)
}

initial_velocity = {
    "sun" : Physics.Vector(0,0),
    "earth" : Physics.Vector(0,29290)
}

class SolarSystemBody:
    
    def __init__(self, mass, initial_velocity, initial_position):
        self.mass = mass
        self.initial_velocity = initial_velocity
        self.initial_position = initial_position
        

sun = SolarSystemBody(mass["sun"],initial_velocity["sun"],initial_position["sun"])
earth = SolarSystemBody(mass["earth"],initial_velocity["earth"],initial_position["earth"])


# set up the initial conditions
velocity_earth = earth.initial_velocity
position_earth = earth.initial_position

velocity_sun = sun.initial_velocity
position_sun = sun.initial_position

# The change in time is one day
day = 1
day_in_seconds = 1*24*3600

# Storage for data
time_in_days = []
time_in_seconds = []
x_coordinate_earth = []
y_coordinate_earth = []
x_coordinate_sun = []
y_coordinate_sun = []

while day <= 365:
     
    # Calculate the displacement between the two bodies
    displacement = Physics.vector_subtraction(position_earth,position_sun)
    
    # Calculate the force between the two bodies
    force = Physics.calc_grav_force(sun.mass,earth.mass,displacement)
    
    # Update the Earths velocity
    delta_velocity_e = Physics.calc_velocity(force,earth.mass,day_in_seconds)
    velocity_earth = Physics.vector_addition(velocity_earth,delta_velocity_e)
    
    # Update the Earths position
    delta_position_e = Physics.calc_position(velocity_earth,day_in_seconds)
    position_earth = Physics.vector_addition(position_earth,delta_position_e)
    
    # Update the Suns velocity
    delta_velocity_s = Physics.calc_velocity(force,sun.mass,day_in_seconds)
    velocity_sun = Physics.vector_addition(velocity_sun, delta_velocity_s)
    
    # Update the Suns position
    delta_position_s = Physics.calc_position(velocity_sun,day_in_seconds)
    position_sun = Physics.vector_addition(position_sun,delta_position_s)
    
    # Collect data in a list to be used later
    time_in_days.append(day)
    time_in_seconds.append(day*24*3600)
    x_coordinate_earth.append(position_earth.x)
    y_coordinate_earth.append(position_earth.y)
    x_coordinate_sun.append(position_sun.x)
    y_coordinate_sun.append(position_sun.y)
    
    day+=1

# initialising a figure in which the graph will be plotted
fig = plt.figure()