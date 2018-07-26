#! /usr/bin/env python
import pybullet as p
import time

sp = {'t_rad' : 0.5, 't_m' : 1, 't_pos' : [0, 0, 0],'p_rad': 0.15, 'p_m' : 0.01, 'p_pos': [0, 0, 0.9],'lv' : [0, 0, -1],'av' : [0, 0, 0], }

#p.connect(p.GUI)
p.connect(p.DIRECT)

# Global body params
visual_shape_id = -1
use_maximal_coordinates = 0
sim_time = 5

# Create target (i.e. pollen) shape and body
target = p.createCollisionShape(p.GEOM_SPHERE, radius=sp['t_rad'])
tuid = p.createMultiBody(sp['t_m'],target,visual_shape_id, sp['t_pos'], useMaximalCoordinates=use_maximal_coordinates)

# Create projectile (i.e. air) shape and body
proj_rad = 0.15
proj_mass = 0.01
proj_pos = [0, 0, 0.9]
proj = p.createCollisionShape(p.GEOM_SPHERE, radius=sp['p_rad'])
puid = p.createMultiBody(sp['p_m'], proj, visual_shape_id, sp['p_pos'], useMaximalCoordinates=use_maximal_coordinates)

# Give projectile initial velocity
p.resetBaseVelocity(puid, sp['lv'], sp['av'])

# Start simulation
p.setGravity(0, 0, 0)	# ignore gravity since this is orientation-agnostic
p.setRealTimeSimulation(1)

start = time.time()
while (time.time() - start < sim_time):
    keys = p.getKeyboardEvents()
    time.sleep(0.001)

print 'end base vel: ' + str(p.getBaseVelocity(tuid))
