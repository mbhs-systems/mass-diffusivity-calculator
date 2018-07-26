import pybullet as p
import time

#p.connect(p.GUI)
p.connect(p.DIRECT)

# Global body params
visual_shape_id = -1
use_maximal_coordinates = 0
sim_time = 5

# Create target (i.e. pollen) shape and body
target_rad = 0.5
target_mass = 1
target_pos = [0, 0, 0]
target = p.createCollisionShape(p.GEOM_SPHERE, radius=target_rad)
tuid = p.createMultiBody(target_mass,target,visual_shape_id, target_pos, useMaximalCoordinates=use_maximal_coordinates)

# Create projectile (i.e. air) shape and body
proj_rad = 0.15
proj_mass = 0.01
proj_pos = [0, 0, 0.9]
proj = p.createCollisionShape(p.GEOM_SPHERE, radius=proj_rad)
puid = p.createMultiBody(proj_mass,proj,visual_shape_id,proj_pos,useMaximalCoordinates=use_maximal_coordinates)

# Give projectile initial velocity
proj_lin_vel = [0, 0, -1]
proj_ang_vel = [0, 0, 0]
p.resetBaseVelocity(puid, proj_lin_vel, proj_ang_vel)

# Start simulation
p.setGravity(0, 0, 0)	# ignore gravity since this is orientation-agnostic
p.setRealTimeSimulation(1)

start = time.time()
while (time.time() - start < sim_time):
    keys = p.getKeyboardEvents()
    time.sleep(0.001)

print 'end base vel: ' + str(p.getBaseVelocity(tuid))

