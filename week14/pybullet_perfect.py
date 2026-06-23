#!/usr/bin/env python3
"""Week 14 - Laikago Stability Control in PyBullet"""
import pybullet as p
import time

p.connect(p.GUI)
p.setGravity(0, 0, -9.8)
p.loadURDF("plane.urdf")
robot = p.loadURDF("laikago/laikago.urdf", [0, 0, 0.5])

print("Laikago loaded. Running stability simulation...")
for i in range(1000):
    p.stepSimulation()
    time.sleep(1./240.)
print("Simulation complete.")
p.disconnect()
