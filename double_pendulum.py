'''
LB, 07/04/2023
Double Pendulum Simulation and Visualization
'''

# Libraries
import numpy as np
from utils import *
import params # parameters file
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

'''
TODO: https://stackoverflow.com/questions/17511843/python-animation-without-globals
      check if __name__ == '__main__'
'''

np.set_printoptions(precision=4)


############################### READ PARAMS AND DEFINE STATE VARIABLES ###############################
dt = params.discretization_step_no_video
dt_save = params.discretization_step_video # small discretization step (increase accuracy)

# Initial values read from parameters.py
teta1_init = params.teta1_init # deg, initial joint1 angle
teta2_init = params.teta2_init # deg, initial joint2 angle
teta1_dot_init = params.teta1_dot_init # rad/s, initial joint1 angular velocity
teta2_dot_init = params.teta2_dot_init # rad/s, initial joint2 angular velocity
p1,p2 = np.zeros((2)),np.zeros((2)) # position xy of the joint2, # position xy of the end-effector (EE)

# Joint angles
teta1_init_rad = np.deg2rad(teta1_init) # convert in radians
teta2_init_rad = np.deg2rad(teta2_init) # convert in radians

 
teta = np.array([teta1_init_rad,teta2_init_rad])
teta_dot = np.array([teta1_dot_init,teta2_dot_init])
tau = np.zeros((2)) # N, joint torques to be computed by a control

link_color = params.link_color # color of links
joint_color = params.joint_color # color of joints
background_color = params.background_color
trajectory_color = params.trajectory_color


# Initial position of the End Effector
p1,p2 = forward_kinematics(teta)
EE_traj_x = [p2[0]] # trajectory x of the end effector
EE_traj_y = [p2[1]] # trajectory y of the end effector



############################### FIGURE INITIALIZATION ###############################

# Figure initialization
fig = plt.figure('Animation',figsize=(10,8))
ax = fig.add_subplot(111)
ax.set_aspect('equal')
ax.grid()

# Setting the axes properties
lengths_sum = params.link_1_length + params.link_2_length
axes_lim = 1.3*lengths_sum
ax.set_xlim([-axes_lim, axes_lim])
ax.set_xlabel('X')
ax.set_ylim([-axes_lim, axes_lim])
ax.set_ylabel('Y')
ax.set_title('Double Pendulum', fontsize=20)
ax.set_facecolor(background_color) # background of the plot

# Draw reference frame axes
#ax.quiver(0,0, 1,0, linewidth=0.2,color='blue') # draw arrow x
#ax.quiver(0,0, 0,1, linewidth=0.2,color='blue') # draw arrow y
ax.arrow(0,0, 0.5,0,head_width=0.05, head_length=0.1,zorder=1, color='black')
ax.arrow(0,0, 0,0.5,head_width=0.05, head_length=0.1,zorder=1, color='black')

# Draw origin
ax.plot(0,0, marker="o", markersize=10, color=joint_color)
# Draw joint 1
joint1_point, = ax.plot(p1[0],p1[1],marker="o", markersize=10,color=joint_color,zorder=1)
# Draw link1
link1_line, = ax.plot([0,p1[0]],[0,p1[1]],color=link_color,linewidth=4,zorder=1)
# Draw link2
link2_line, = ax.plot([p1[0],p2[0]],[p1[1],p2[1]],color=link_color,linewidth=4,zorder=1)
# Draw EE
EE_point, = ax.plot(p2[0],p2[1], marker="o", markersize=10,color=joint_color,zorder=0)
# Draw trajectory of EE (new values will be appended during the simulation)
EE_traj, = ax.plot(EE_traj_x,EE_traj_y,color=trajectory_color,zorder=0)

txt = ax.text(-2,2,'0.0 s',fontsize=15) # print the time
txt_ref = ax.text(2.35,-2.55,'By LB',fontsize=6,alpha=0.7)



# Animation frame update (SAVE_VIDEO=False)
def animation_update(frame):
    # Numerical integration of the CT dynamics
    global teta,teta_dot,tau # use global to modify a global variable inside a function
    teta,teta_dot = integrate_dynamics(tau,teta,teta_dot,dt)
    # Knowing angles compute x-y positions of joint 2 and end-effector
    p1,p2 = forward_kinematics(teta,verbose=True)
    joint1_point.set_data(p1[0],p1[1])
    link1_line.set_data([0,p1[0]],[0,p1[1]])
    link2_line.set_data([p1[0],p2[0]],[p1[1],p2[1]])
    EE_point.set_data(p2[0],p2[1])
    EE_traj_x.append(p2[0])
    EE_traj_y.append(p2[1])
    EE_traj.set_data(EE_traj_x,EE_traj_y)
    txt.set_text(str(round(dt*frame,1))+' s')
    # return joint1_point,link1_line,link2_line,EE_point,EE_traj,txt



# Animation frame update (SAVE_VIDEO=True)
def animation_update_save(frame):
    p1 = p1_array[:,frame]
    p2 = p2_array[:,frame]
    joint1_point.set_data(p1[0],p1[1])
    link1_line.set_data([0,p1[0]],[0,p1[1]])
    link2_line.set_data([p1[0],p2[0]],[p1[1],p2[1]])
    EE_point.set_data(p2[0],p2[1])
    EE_traj_x.append(p2[0])
    EE_traj_y.append(p2[1])
    EE_traj.set_data(EE_traj_x,EE_traj_y)
    txt.set_text(str(round(dt_save*frame,1))+' s')
    # Write on terminal the progress
    percentage = '\r' + str(round((frame/n_iters)*100)) + ' %'
    sys.stdout.write(percentage)
    #sys.stdout.write("\r{0}>".format("="*frame))
    sys.stdout.flush()
    #return joint1_point,link1_line,link2_line,EE_point,EE_traj



# Main body

if not params.SAVE_VIDEO:
    interval_ms = dt*1000
    animation = FuncAnimation(fig, animation_update, interval=interval_ms)
    plt.show()

else:
    import sys # used to print the progress of the saving of the video
    Tmax = params.time_max
    print("Simulating double pendulum for", Tmax, "seconds...")
    n_iters = round(Tmax/dt_save) # total number of iterations
    interval_ms = dt_save*1000
    # initialize arrays to host p1 and p2 from 0 to Tmax
    p1_array = np.zeros((2,n_iters))
    p2_array = np.zeros((2,n_iters))
    # simulate the system from 0 to Tmax
    for i in range(n_iters):
        teta,teta_dot = integrate_dynamics(tau,teta,teta_dot,dt=dt_save)
        p1_array[:,i], p2_array[:,i] = forward_kinematics(teta,verbose=False)
    print("Done.")
    print("Saving video...")
    animation_save = FuncAnimation(fig, animation_update_save, frames=n_iters, interval=interval_ms)
    fps = round(1/dt_save)
    # saving to mp4 using ffmpeg writer
    writervideo = FFMpegWriter(fps=fps)
    video_name = 'double_pendulum.mp4'
    animation_save.save(video_name, writer=writervideo)
    print("\nSaved video", video_name)






#if __name__ == '__main__':
 #   main()