# Double_Pendulm
Simulation of a double pendulum written in **Python** with visualization implemented using the Animation function of **Matplotlib**.
Every parameter is configurable in the parameters file. The pendulum will move depending on initial conditions, gravity and friction.

<img src="https://user-images.githubusercontent.com/100198704/231795094-6fdc78e5-9349-4eb9-a9a2-8cb2d591a416.png" width=40%>

videos examples with different initial conditions, no friction.


https://user-images.githubusercontent.com/100198704/231829223-082b2548-a723-45c6-97f0-0059141d5487.mp4



The script can be run in **two modes**, depending on the value of SAVE_VIDEO set in the parameters file:
- `SAVE_VIDEO=False`: the simulation goes on forever, the discretization step specified in the parameters file affects the visualization speed and the accuracy of the discretization because the dynamics update is performed in the animation function. The position of End Effector and joint 2 are printed on the terminal;
- `SAVE_VIDEO=True`: the system is simulated for the time specified in the parameter file and then the animation is saved on disk in the current directory in `mp4` format. When saving the video, the percentage of progress is shown on terminal.

**Files**:
- `double_pendulum.py`: main code to execute for the simulation. You can execute it directly from the code editor or opening a terminal in the folder of the file and typing `python3 double_pendulum.py`;
- `utils.py`: utility functions. It implements the dynamics of the system and its discretization;
- `params.py`: parameter file, used to specify any parameter concerning the dynamics, the initial conditions and the graphics. 

Enjoy changing the parameters and trying different initial conditions!


**Dynamic model**

![equation](https://user-images.githubusercontent.com/100198704/231793024-0843b32f-b863-4cdc-b679-236908df053c.svg)

**System scheme**

![scheme](https://user-images.githubusercontent.com/100198704/231793573-39874c63-d99e-4404-816b-356cd95e450b.svg)

**Comments and suggestions to improve the code are welcome** (write in the discussion section), especially for:
- avoid the use of global variables in the main file and pass parameters to functions in the most efficient way;
- implement a better integration method
- decouple the simulation and the visualization in case `SAVE_VIDEO=False`
