import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class Vehicle():
    def __init__(self):
 
        # ==================================
        #  Parameters
        # ==================================
    
        #Throttle to engine torque
        self.a_0 = 400
        self.a_1 = 0.1
        self.a_2 = -0.0002
        
        # Gear ratio, effective radius, mass + inertia
        self.GR = 0.35
        self.r_e = 0.3
        self.J_e = 10
        self.m = 2000
        self.g = 9.81
        
        # Aerodynamic and friction coefficients
        self.c_a = 1.36
        self.c_r1 = 0.01
        
        # Tire force 
        self.c = 10000
        self.F_max = 10000
        
        # State variables
        self.x = 0
        self.v = 5
        self.a = 0
        self.w_e = 100
        self.w_e_dot = 0
        
        self.sample_time = 0.01
        
    def reset(self):
        # reset state variables
        self.x = 0
        self.v = 5
        self.a = 0
        self.w_e = 100
        self.w_e_dot = 0
class Vehicle(Vehicle):
    def step(self, throttle, alpha):
        # ==================================
        #  Implement vehicle model here
        # ==================================
        w_wheel = self.GR * self.w_e
        s = ((w_wheel * self.r_e) - self.v )/self.v
        #if s < 1 and s > -1:
        if abs(s):
            Fx = self.c * s
        else :
            Fx = self.F_max
        Te = throttle * (self.a_0 + self.a_1 * self.w_e + self.a_2 * self.w_e * self.w_e)
        F_aero = self.c_a * self.v * self.v
        Rx = self.c_r1 * self.v
        Fg = self.m * self.g * np.sin(alpha)
        F_load = F_aero + Rx + Fg
        self.w_e_dot = ( Te - ( self.GR * self.r_e * F_load ) ) / self.J_e
        self.a = ( Fx - F_load ) / self.m
        self.x = self.x + self.v * self.sample_time
        self.v = self.v + self.a * self.sample_time 
        self.w_e = self.w_e + self.w_e_dot * self.sample_time


'''sample_time = 0.01
time_end = 100
model = Vehicle()

t_data = np.arange(0,time_end,sample_time)
v_data = np.zeros_like(t_data)

# throttle percentage between 0 and 1
throttle = 0.2

# incline angle (in radians)
alpha = - 0.02

for i in range(t_data.shape[0]):
    v_data[i] = model.v
    model.step(throttle, alpha)
    
plt.plot(t_data, v_data)
plt.show()'''
sample_time = 0.01
time_end = 20
t_data = np.arange(0,time_end,sample_time)
x_data = np.zeros_like(t_data)
wed_data = np.zeros_like(t_data)
v_data = np.zeros_like(t_data)
throttle_data = np.zeros_like(t_data)
alpha_data = np.zeros_like(t_data)
model = Vehicle()

# reset the states
model.reset()

# ==================================
#  Learner solution begins here
# ==================================

for i in range(t_data.shape[0]):
    if i >= 0 and i < 500:
       throttle = 0.2 + 0.0006 * i
    elif i>=500 and i < 1500:
       throttle = 0.5
    elif i >= 1500 and i < 2000:
       throttle = 2 - 0.001 * i

    if model.x >= 0 and model.x < 60 :
       alpha = 0.05
    elif model.x >= 60 and model.x < 150 :
       alpha = 0.1
    elif model.x > 150 :
       alpha = 0

    throttle_data[i] = throttle
    alpha_data[i] = alpha
    model.step(throttle,alpha)
    x_data[i]= model.x
    wed_data[i] = model.w_e_dot
    v_data[i] = model.v

# ==================================
#  Learner solution ends here
# ==================================

# Plot x vs t for visualization
plt.plot(t_data, x_data)
plt.plot(t_data, throttle_data)
#plt.plot(t_data, alpha_data)
#plt.plot(t_data, wed_data)
#plt.plot(t_data, v_data)
plt.show()
