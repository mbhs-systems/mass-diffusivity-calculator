import pybullet as p
import time

p.connect(p.GUI)

# Global body params
visualShapeId = -1
useMaximalCoordinates = 0

# Create target (i.e. pollen) shape and body
target_mass = 1
target = p.createCollisionShape(p.GEOM_SPHERE, radius=0.5)
tuid = p.createMultiBody(target_mass,target,visualShapeId,[0,0,0],useMaximalCoordinates=useMaximalCoordinates)

# Create projectile (i.e. air) shape and body
proj_rad = 0.15
proj_mass = 0.01
proj = p.createCollisionShape(p.GEOM_SPHERE, radius=proj_rad)
puid = p.createMultiBody(proj_mass,proj,visualShapeId,[0,0,.9],useMaximalCoordinates=useMaximalCoordinates)

# Give projectile initial velocity
proj_lin_vel = [0, 0, -1]
proj_ang_vel = [0, 0, 0]
p.resetBaseVelocity(puid, proj_lin_vel, proj_ang_vel)

# Start simulation
p.setGravity(0, 0, 0)	# ignore gravity since this is orientation-agnostic
p.setRealTimeSimulation(1)

while (1):
    print 'My base vel: ' + str(p.getBaseVelocity(tuid))
    keys = p.getKeyboardEvents()
    time.sleep(0.01)
