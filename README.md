# Double_Pendulm
Simulation of a double pendulum written in **Python** with visualization implemented using the Animation function of **Matplotlib**.
Every parameter is configurable in the parameters file. 

videos examples with different initial conditions


The script can be run in **two modes**, depending on the value of SAVE_VIDEO set in the parameters file:
- `SAVE_VIDEO=False`: the simulation goes on forever, the discretization step specified in the parameters file affects the visualization speed and the accuracy of the discretization because the dynamics update is performed in the animation function. The position of End Effector and joint 2 are printed on the terminal;
- `SAVE_VIDEO=True`: the system is simulated for the time specified in the parameter file and then the animation is saved on disk in the current directory in `mp4` format. When saving the video, the percentage of progress is shown on terminal.

**Expanation of the files**:
`double_pendulum.py`: main code to execute for the simulation;
`utils.py`: utility functions. It implements the dynamics of the system and its discretization;
`params.py`: parameter file, used to specify any parameter concerning the dynamics, the initial conditions and the graphics. 

Enjoy changing the parameters and trying different initial conditions!


**Dynamic model**
image

**System scheme**
image


