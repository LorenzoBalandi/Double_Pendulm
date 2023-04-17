# Double_Pendulm
Simulation of a double pendulum written in **Python** with visualization implemented using the Animation function of **Matplotlib**.
Every parameter is configurable in the parameters file. The pendulum will move depending on initial conditions, gravity and friction.

<img src="https://user-images.githubusercontent.com/100198704/231795094-6fdc78e5-9349-4eb9-a9a2-8cb2d591a416.png" width="300" >

Examples with no friction and different initial conditions and visualization styles:
<p float="left">
  <img src="https://user-images.githubusercontent.com/100198704/232058234-02a25b07-1997-4a23-a39f-10a3fef1cde7.gif" width="500" /> 
  <img src="https://user-images.githubusercontent.com/100198704/232058248-571f1cca-ea97-4195-9d72-1e858939f532.gif" width="500" />
</p>

Examples with friction and different colors:
<p float="left">
  <img src="https://user-images.githubusercontent.com/100198704/232058260-394c0afe-c9a0-46b1-8414-c4399c6dd410.gif" width="500" /> 
  <img src="https://user-images.githubusercontent.com/100198704/232058271-1d8ff7b5-7075-4041-af4d-8a6d9f967dc0.gif" width="500" />
</p>

More videos on [Youtube](https://youtu.be/ndNXlVD7ytE)


The script can be run in **two modes**, depending on the value of SAVE_VIDEO set in the parameters file:
- `SAVE_VIDEO=False`: the simulation goes on forever, the discretization step specified in the parameters file affects the visualization speed and the accuracy of the discretization because the dynamics update is performed in the animation function. The position of End Effector and joint 2 are printed on the terminal;
- `SAVE_VIDEO=True`: the system is simulated for the time specified in the parameter file and then the animation is saved on disk in the current directory in `mp4` format. When saving the video, the percentage of progress is shown on terminal.

### Files:
- `double_pendulum.py`: main code to execute for the simulation. You can execute it directly from the code editor or opening a terminal in the folder of the file and typing `python3 double_pendulum.py`;
- `utils.py`: utility functions. It implements the dynamics of the system and its discretization;
- `params.py`: parameter file, used to specify any parameter concerning the dynamics, the initial conditions and the graphics. 

Enjoy changing the parameters and trying different initial conditions!


### Dynamic model

![equation](https://user-images.githubusercontent.com/100198704/231793024-0843b32f-b863-4cdc-b679-236908df053c.svg)

### System scheme

![scheme](https://user-images.githubusercontent.com/100198704/231837108-0fe1edcd-14b6-4414-90df-bd087057a5f2.svg)

**Comments and suggestions to improve the code are welcome** (write in the discussion section), especially for:
- avoid the use of global variables in the main file and pass parameters to functions in the most efficient way;
- implement a better integration method
- decouple the simulation and the visualization in case `SAVE_VIDEO=False`
