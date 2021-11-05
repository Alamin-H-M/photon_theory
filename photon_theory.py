# what is the angular momentum of an electron in 3rd shell? if the radius of the shell 3.6 * (10**-8)cm , determine the velocity of the shell. [mass of an electron = 9.11 * (10**-28 g)]


'''
here, shell no., n = 3
    plunk constant, h = 6.626 * (10**-34) Js
    constant, pi = 22/7
    mass of electron, m = 9.11 * (10**-31) kg
    radius of shell, r = 3.6 *(10**-10)

'''
n = 3
h = 6.626 * (10**-34) 
pi = 22/7
m = 9.11 * (10**-31) 
r = 3.6 *(10**-10)

angular_momentum = (n * h) / (2 * pi) 
velocity = angular_momentum / (m * r)

print(f"angular momentum = {angular_momentum} Js\n  and the velocity = {velocity} m/s")
