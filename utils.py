# LB 8/04/2023
# Utility functions for double pendulum project

import numpy as np
import params


############################### READ PARAMS ###############################

# Parameters (constant) read from params.py
m1 = params.mass_1 # kg, mass of link 1
m2 = params.mass_2 # kg, mass of link 2
I1 = params.inertia_1 # kgm^2, inertia of link 1 about axis through the center 0f mass and parallel to z
I2 = params.inertia_2 # kgm^2, inertia of link 2
gg = params.gg # m/s^2, gravity acceleration
a1 = params.link_1_length # m, length of link 1
a2 = params.link_2_length # m, length of link 2
a_c1 = params.link_1_center # m, distance between joint 1 and CoM of link 1
a_c2 = params.link_2_center # m, distance between joint 2 and CoM of link 2
friction1 = params.friction_joint_1 # friction coefficient on joint1
friction2 = params.friction_joint_2 # friction coefficient on joint2


############################### FUNCTIONS ###############################


def compute_system_matrices(teta,teta_dot):
    # Dynamic model: M(q)ddq + C(q,dq)qd + Dqd + g(q) = tau + J^T(q)F_a
    # System matrices
    M11 = m1*a_c1**2+m2*(a1**2+a_c2**2+2*a1*a_c2*np.cos(teta[1]))+I1+I2
    M12 = m2*(a_c2**2)+a1*a_c2*np.cos(teta[1])+I2 # = M21 due to simmetry
    M22 = m2*a_c2**2+I2
    MM = np.array([[M11,M12],[M12,M22]])
    #
    hh = -m2*a1*a_c2*np.sin(teta[1])
    CC = np.array([[hh*teta_dot[1], hh*(teta_dot[0]+teta_dot[1])],[-hh*teta_dot[0], 0]])
    #
    GG = np.array([(m1*a_c1+m2*a1)*gg*np.cos(teta[0])+m2*gg*a_c2*np.cos(teta[0]+teta[1]), m2*gg*a_c2*np.cos(teta[0]+teta[1])])
    #
    DD = np.diag([friction1,friction2])
    #
    return MM,CC,GG,DD


def integrate_dynamics(tau,teta,teta_dot,dt):
    # Dynamic model: M(q)ddq + C(q,dq)qd + Dqd + g(q) = tau + J^T(q)F_a
    MM,CC,GG,DD = compute_system_matrices(teta,teta_dot)
    #print(MM)
    #print(CC)
    #print(GG)
    #print(DD)
    teta_doubledot = np.linalg.pinv(MM,hermitian=True)@(tau-CC@teta_dot-DD@teta_dot-GG)
    # Numerical integration (EULER), default value is dt from parameter file, for the video another dt is passed
    teta_dot += dt*teta_doubledot
    teta += dt*teta_dot
    #print(teta)
    #print(teta_dot)
    return teta,teta_dot


def forward_kinematics(teta,verbose=True):
    # fw kinematics for the position of joint2 (end of link1)
    px1 = a1*np.cos(teta[0])
    py1 = a1*np.sin(teta[0])
    p1 = np.array([px1,py1])
    # fw kinematics for the position of the EE
    px2 = px1 + a2*np.cos(teta[0]+teta[1])
    py2 = py1 + a2*np.sin(teta[0]+teta[1])
    p2 = np.array([px2,py2])
    if verbose:
        print("Position of joint2:",p1,"\tPosition of EE:",p2)
    return p1,p2
