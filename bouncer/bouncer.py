#! /usr/bin/env python
import pybullet as p
import time
import threading
import multiprocessing

gst = time.time()

SP = {'t_rad' : 0.5, 't_m' : 1, 't_pos' : [0, 0, 0],'p_rad': 0.15, 'p_m' : 0.01, 'p_pos': [0, 0, 0.9],'lv' : [0, 0, -1],'av' : [0, 0, 0], 'sim_time' : 5000, 'pci': 0}
SP1 = {'t_rad' : 0.5, 't_m' : 1, 't_pos' : [0, 0, 0],'p_rad': 0.15, 'p_m' : 0.01, 'p_pos': [0, 0, 0.9],'lv' : [0, 0, -1],'av' : [0, 0, 0], 'sim_time' : 5000, 'pci': 1}

class BouncerThread(threading.Thread):
    def __init__(self, sp):
        threading.Thread.__init__(self)
        self.sp = sp

    def run(self):
        p.connect(p.DIRECT, options="physicsClientId=" + str(self.sp['pci']))
        simulate(self.sp)
        print 'time: ' + str(time.time() - gst)

def simulate(sp):
    # Global body params
    visual_shape_id = -1
    use_maximal_coordinates = 0
    sim_time = 5

    # Create target (i.e. pollen) shape and body
    target = p.createCollisionShape(p.GEOM_SPHERE, radius=sp['t_rad'], physicsClientId=sp['pci'])
    tuid = p.createMultiBody(sp['t_m'],target,visual_shape_id, sp['t_pos'], useMaximalCoordinates=use_maximal_coordinates, physicsClientId=sp['pci'])

    # Create projectile (i.e. air) shape and body
    proj_rad = 0.15
    proj_mass = 0.01
    proj_pos = [0, 0, 0.9]
    proj = p.createCollisionShape(p.GEOM_SPHERE, radius=sp['p_rad'], physicsClientId=sp['pci'])
    puid = p.createMultiBody(sp['p_m'], proj, visual_shape_id, sp['p_pos'], useMaximalCoordinates=use_maximal_coordinates, physicsClientId=sp['pci'])

    # Give projectile initial velocity
    p.resetBaseVelocity(puid, sp['lv'], sp['av'], physicsClientId=sp['pci'])

    # Start simulation
    p.setGravity(0, 0, 0, physicsClientId=sp['pci'])    # ignore gravity since this is orientation-agnostic

    start = time.time()
    for i in range(sp['sim_time']):
        p.stepSimulation(physicsClientId=sp['pci'])
        keys = p.getKeyboardEvents()
        time.sleep(0.001)

    print 'bv' + str(sp['pci']) + ': ' + str(p.getBaseVelocity(tuid, physicsClientId=sp['pci']))
    return p.getBaseVelocity(tuid, physicsClientId=sp['pci'])

if __name__ == '__main__':
    lock = threading.Lock()
    threads = []

    for i in range(multiprocessing.cpu_count()):
        th = BouncerThread(SP)
        th.start()
        threads.append(th)

    for t in threads:
        t.join()

    print 'All done'
