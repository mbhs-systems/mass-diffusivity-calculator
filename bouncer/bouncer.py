import pybullet as p
import time

# Setup pybullet
p.connect(p.GUI)
p.setRealTimeSimulation(0)
p.setGravity(0, 0, 0)	# ignore gravity since this is orientation-agnostic

# Load PF particle shape
target = p.loadURDF('../meshes/in.urdf')	# TODO actually convert to URDF

# Setup air molecule to shoot at the particle (dummy values for now)
air_rad = 0.05
air_mass = 0.001
col_sphere_id = p.createCollisionShape(p.GEOM_SPHERE, radius=air_rad, mass=air_mass)
air_lin_vel = [1, 1, 1]
air_ang_vel = [0, 0, 0]
p.resetBaseVelocity(air, air_lin_vel, air_ang_vel)

# Run simulation as long as you want
# TODO figure out how to simulate more precisely than real-time
sim_time = 1
while (time.time() - sim_time < 0):
	p.stepSimulation()

lin_vel = p.getLinearVelocity(target)
ang_vel = p.getAngularVelocity(target)

print 'Linear Velocity: ' + str(lin_vel)
print 'Angular Velocity: ' + str(ang_vel)

# Teardown pybullet
p.resetSimulation()
p.disconnect()
