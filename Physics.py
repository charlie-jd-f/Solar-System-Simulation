from math import sqrt

class Vector:
    
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        
    def get_magnitude(self):
        
        magnitude = sqrt(self.x**2 + self.y**2)
        
        return magnitude

def vector_addition(vector_1,vector_2):
    x = vector_1.x + vector_2.x
    y = vector_1.y + vector_2.y
    new_vector = Vector(x,y)

    return new_vector
   
def vector_subtraction(vector_1,vector_2):
    
    x = vector_1.x - vector_2.x
    y = vector_1.y - vector_2.y
    new_vector = Vector(x,y)
    
    return new_vector
    
def calc_grav_force(mass_1,mass_2,position_vector):
    
    Grav_constant = 6.674e-11
    distance = position_vector.get_magnitude()
    
    force = -(Grav_constant*mass_1*mass_2)/distance**3
    force_x = force*position_vector.x
    force_y = force*position_vector.y
    force_vector = Vector(force_x,force_y)
    
    return force_vector

def calc_velocity(force_vector,mass,change_in_time):
    velocity_x = force_vector.x*change_in_time/mass
    velocity_y = force_vector.y*change_in_time/mass
    velocity_vector = Vector(velocity_x,velocity_y)
    
    return velocity_vector

def calc_position(velocity,change_in_time):
    
    x = velocity.x*change_in_time
    y = velocity.y*change_in_time
    position_vector = Vector(x,y)
    
    return position_vector
    