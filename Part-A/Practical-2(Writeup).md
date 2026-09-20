Practical No. 2

Title

To implement a model-based intelligent agent capable of navigating a grid environment with obstacles using internal state representation.

Objectives

To understand the concept of a model-based intelligent agent.
To study the use of internal state representation in an intelligent agent.
To implement an agent for navigating through a grid environment.
To enable the agent to maintain information about previously observed obstacles and positions.
To analyze the behavior of the agent while navigating from a starting position to a goal position.

Problem Statement

Design and implement a Model-Based Intelligent Agent that navigates through a grid environment containing obstacles. The environment is represented as a grid consisting of free cells and blocked cells.

The agent starts from a specified position and has to reach a given goal position. The agent perceives the current cell and updates its internal state representation using the information obtained from the environment.

The agent should:
Identify its current position.
Detect obstacles in the environment.
Maintain an internal representation of the environment.
Select a valid movement based on its current state and internal model.
Avoid obstacles while navigating.
Continue moving until the goal position is reached.
The possible movements of the agent are Up, Down, Left, and Right.

Software Requirements

Python 3.x
Python-supported IDE such as IDLE, VS Code, PyCharm, or Jupyter Notebook
Operating System: Windows/Linux
Hardware Requirements
Processor: Dual Core or above
RAM: 4 GB or above
Storage: Minimum 1 GB free space

Theory / Concept in Brief

1. Intelligent Agent

An intelligent agent is a system that perceives its environment and performs actions to achieve a particular goal. An agent uses sensors to obtain information from the environment and actuators to perform actions.

The basic working of an intelligent agent can be represented as:

Environment → Perception → Decision → Action → Environment

2. Model-Based Intelligent Agent

A Model-Based Agent maintains an internal representation or model of the environment. Unlike a simple reflex agent, it does not depend only on the current percept.

The agent uses:

Current percept
Previous information
Internal state
Model of the environment
to decide its next action.

The internal state helps the agent remember relevant information about the environment that may not be directly observable at the current moment.

3. Grid Environment

In this experiment, the environment is represented as a rectangular grid.
For example:
<img width="426" height="348" alt="Screenshot 2026-09-20 110834" src="https://github.com/user-attachments/assets/9d79219f-b231-4958-8aa0-14529b59e60a" />

Where:
S = Starting position
G = Goal position
X = Obstacle
. = Free cell

The agent starts from S and navigates through free cells to reach G.

4. Internal State Representation

The internal state stores the information known by the agent about the environment.

For example, the agent may maintain:

Current Position = (0,0)
Known Obstacles = {(0,3), (1,1), (1,3), (3,0), (3,2)}
Goal = (3,4)

Whenever the agent perceives an obstacle, it updates its internal representation.

Thus, the agent can use previously obtained information when deciding its next movement.

5. Model of the Environment

The agent maintains a model of the grid using different symbols:

0 → Unknown or unvisited cell
1 → Free cell
X → Obstacle
S → Starting position
G → Goal position

The internal model is updated as the agent moves through the environment.

6. Rational Behavior

The agent behaves rationally when it selects a valid movement that helps it reach the goal while avoiding known obstacles.

For example, if the cell directly to the right contains an obstacle, the agent should not move right. It should select another valid direction such as Up, Down, or Left, depending on the current state.

Agent Components

The model-based grid navigation agent consists of the following components:

Sensors:
Used to perceive the current cell and nearby obstacles.

Internal State:
Stores the agent's current position and information about the environment discovered so far.

Environment Model:
Represents known free cells and obstacles.

Decision Mechanism:
Selects the next valid movement.

Actuators:
Execute movements such as Up, Down, Left, and Right.

Algorithm
1. Start the program.
2. Define the grid environment.
3. Specify the starting position and goal position.
4. Define the obstacle positions.
5. Initialize the internal state of the agent.
6. Set the current position to the starting position.
7. Perceive the current environment.
8. Update the internal state with the observed information.
9.Check the possible movements: Up, Down, Left, and Right.
10. Remove movements that lead outside the grid or into known obstacles.
11. Select a valid movement that brings the agent closer to the goal.
12. Move the agent to the selected cell.
13. Update the current position in the internal state.
14. Repeat the process until the goal is reached.
15. Display the path followed by the agent.
16. Stop the program.

Flowchart

Draw the following flowchart in the journal:

Start
↓
Initialize Grid, Obstacles, Start and Goal
↓
Initialize Internal State
↓
Sense Current Environment
↓
Update Internal State
↓
Goal Reached?
→ Yes → Display Path → Stop
↓ No
Identify Valid Movements
↓
Avoid Obstacles and Invalid Cells
↓
Select Next Movement
↓
Move Agent
↓
Update Current Position
↓
Repeat


Test Cases

<img width="766" height="360" alt="image" src="https://github.com/user-attachments/assets/fdddda1a-3a9e-4972-94e0-3836cb4f7093" />


Conclusion / Analysis
The Model-Based Intelligent Agent was successfully implemented for navigating a grid environment containing obstacles. The agent maintains an internal state representation of its current position and the information discovered about the environment.
The agent successfully avoids known obstacles and selects valid movements to reach the goal. The experiment demonstrates that maintaining an internal state enables an intelligent agent to make better decisions using information obtained from previous perceptions. Thus, a model-based agent is more suitable than a simple reflex agent for environments where the complete state of the environment cannot always be directly observed.


