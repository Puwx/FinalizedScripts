
import math

pi = math.pi

class ThreeD:

    class Cube:

        "This Class has the following parameters/attributes: Area and Units (optional and defaults to meters.) "    

        def __init__(self,area,units="meter"):
            self.area = area
            self.units = units

        def __str__(self):
            return ("The cube has edges that are {} long/wide and the units are in {} .".format(self.area,self.units))

        def volume(self):
            vol = self.area**3
            print("The area is {} {}s cubed in volume".format(round(vol,3),self.units))
            return round(vol,3)

        def surface_area(self):
            sa = 6 * (self.area**2)
            print("The surface area of the cube is {} {}s squared. ".format(round(sa,3),self.units))
            return round(sa,3)

    class Cylinder:

        "This Class has the following parameters/attributes: Radius, Height, and Units (optional and defaults to meters). "

        def __init__(self,radius,height,units="meter"):
            self.radius = radius
            self.height = height
            self.units = units
        
        def __str__(self):
            return "The cylinder has a radius of: {} a height of: {} and the units are in {} .".format(self.radius,self.height,self.units)

        def volume(self):
            vol = pi * (self.radius**2)*self.height
            print("The volume of the cylinder is {} {} cubed.".format(round(vol,3),self.units))
            return round(vol,3)

        def surface_area(self):
            sa = (2 * pi * self.radius *self.height)*(2 * pi * (self.radius**2))
            print ("The surface area of the cylinder is {} {} sqaured.".format(round(sa,3),self.units))
            return round(sa,3)

    class Sphere:

        "This Class has the following parameters/attributes: Radius and Units (optional and defaults to meters). "

        def __init__(self,radius,units="meter"):
            self.radius = radius
            self.units = units

        def __str__(self):
            return "The sphere has a radius of {} and the units are in {}.".format(self.radius,self.units)
        
        def volume(self):
            vol = ((4/3)*pi*(self.radius**2))
            print ("The volume of the sphere is {} {} cubed.".format(round(vol,3),self.units))
            return round(vol,3)
        
        def surface_area(self):
            sa = (4*pi*(self.radius**2))
            print("The sphere has a surface area of {} {}.".format(round(sa,3),self.units))
            return round(sa,3)

    class Pyramid:

        "This Class has the following parameters/attributes: Length, Width, Height, Units are optional and defaults to meters. "

        def __init__(self,length,width,height,units="meter"):
            self.length = length
            self.width = width
            self.height = height
            self.units = units

        def __str__(self):
            return ("The pyramid has a lenght of {}, a width of {}, and a height of {}. The units are {}.".format(self.length,self.width,self.height,self.units))

        def volume(self):
            vol = ((self.length * self.width * self.height)/3)
            print("The pyramid has a volume of {} {}s.".format(round(vol,3),self.units))
            return round(vol,3)
        
        def surface_area(self):
            #This is currently not working. The results are always higher than those calculated on google, error increases exponentially.
            pt1 = self.length*(math.sqrt( ((self.width / 2) ** 2) + (self.height ** 2)))
            pt2 = self.width*(math.sqrt( ((self.length / 2) ** 2) + (self.height ** 2)))
            sa  = ((self.length * self.width) + pt1 + pt2)
            print("The surface area of the pyramid is {} {}.".format(round(sa,3),self.units))
            return round(sa,3)
        
    class Box:

        "This Class has the following parameters/attributes: Length, Width, Height, Units (optional and defaults to meters). A box differs from a cube by having asymmetrical sides. "

        def __init__(self,length,width,height,units="meter"):
            self.length = length
            self.width = width
            self.height = height
            self.units = units
        
        def __str__(self):
            return ("The Box has a length of: {} a width of {} and a height of {}. The units are in {}".format(self.length,self.width,self.height,self.units))

        def volume(self):
            vol = self.length * self.width * self.height
            print("The volume of the Box is {} {}.".format(vol,self.units))
            return round(vol,3)
        
        def surface_area(self):
            sa = (2 * self.length) + (2 * self.width) * (2 *self.height)
            print ("The surface area of the box is {} {}.".format(sa,self.units))
            return round(sa,3)
