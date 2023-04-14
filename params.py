# Parameter file for the double pendulum simulation
# LB, 11/04/23

SAVE_VIDEO = False # save video or not

# SIMULATION PARAMETERS
time_max = 30 # s, time of simulation (only to save video!)
discretization_step_no_video = 1/30 # discretization step (case with SAVE_VIDEO=False)
discretization_step_video = 1e-3 # discretization step (case with SAVE_VIDEO=True)
mass_1 = 1 # kg, mass of link 1
mass_2 = 1 # kg, mass of link 2
inertia_1 = 1 # kgm^2, inertia of link 1 about axis through the center 0f mass and parallel to z
inertia_2 = 1 # kgm^2, inertia of link 2
gg = 9.81 # m/s^2, gravity acceleration
link_1_length = 1 # m, length of link 1
link_2_length = 1 # m, length of link 2
link_1_center = 0.5 # m, distance between joint 1 and CoM of link 1
link_2_center = 0.5 # m, distance between joint 2 and CoM of link 2
friction_joint_1 = 0 # friction coefficient on joint1
friction_joint_2 = 0 # friction coefficient on joint2


# INITIAL CONDITIONS
teta1_init = 0.0 # deg, initial joint1 angle
teta2_init = 0.0 # deg, initial joint2 angle
teta1_dot_init = 0.0 # rad/s, initial joint1 angular velocity
teta2_dot_init = 0.0 # rad/s, initial joint2 angular velocity


# GRAPHICAL PARAMETERS
link_color = 'red' # color of links
joint_color = 'red' # color of joints
background_color = 'white'
trajectory_color = 'blue'