import numpy as np
import math


def reward_function(params):
   
    speed = params["speed"]
    
    if params["is_offtrack"] == False and params["steps"] > 0:
        reward = speed
    else:
        reward = 0.0001
        return float(reward)

    return float(reward)
