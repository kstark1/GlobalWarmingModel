# GlobalWarmingModel

## Model Formation
__ Goal:__ simulate the temperatures of a naked planet changes as it approaches equilibrium state

Incoming Solar Heat: L * (1 - albedo)/4
Outgoing Infared: epsilon * sigma * T^4

Heat Capacity (c): 
dc/dt = L * (1 - alpha)/4 - epsilon * sigma * T^4

timeStep = 100           # years
waterDepth = 4000        # meters
L = 1350                 # Watts/m2
albedo = 0.3
epsilon = 1
sigma = 5.67E-8          # W/m2 K4

