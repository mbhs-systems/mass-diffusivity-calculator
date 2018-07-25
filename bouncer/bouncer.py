import pybullet as p
import time

p.connect(p.GUI)

sphereRadius = 0.05
mass = 1
visualShapeId = -1
orn = p.getQuaternionFromEuler([1.5707963,0,0])
useMaximalCoordinates = 0
shift = [0,-0.02,0]

target = p.createCollisionShape(p.GEOM_SPHERE, radius=0.5)

tuid = p.createMultiBody(mass,target,visualShapeId,[0,0,0],useMaximalCoordinates=useMaximalCoordinates)

air_rad = 0.15
air_mass = 0.01
proj = p.createCollisionShape(p.GEOM_SPHERE, radius=air_rad)
air_lin_vel = [0, 0, -1]
air_ang_vel = [0, 0, 0]
puid = p.createMultiBody(air_mass,proj,visualShapeId,[0,0,.9],useMaximalCoordinates=useMaximalCoordinates)
p.resetBaseVelocity(puid, air_lin_vel, air_ang_vel)

p.setGravity(0, 0, 0)	# ignore gravity since this is orientation-agnostic
p.setRealTimeSimulation(1)

while (1):
    keys = p.getKeyboardEvents()
    time.sleep(0.01)
