# tp_ros_zahrah

## Launch file that launch 2 nodes and rviz

-This package contains a launch file that will launch a publisher node, a button node and rviz.
-When the toggle button is pressed a square pattern is formed.
-And when the toggle button is pressed again the pattern will stop.

> STEPS:

## Install package

- Copy and clone the package in your catkin workspace in the src folder
```
cd ~/catkin_workspace/src
git clone https://github.com/zahrah925/tp_ros_zahrah.git
catkin build
source ~/catkin_workspace/devel/setup.bash
```

## Run the launch file

- To run the launch file with the nodes
  - `roslaunch tp_ros_zahrah btn.launch`

- A toggle button will appear as well as rviz will run.
- Press the toggle button twice to get the `chatter` node in rviz.
- Open rviz and select the add topic as `chatter > pose`.
- Press the toggle button once and a square pattern will be formed.
- Repress the toggle button and the square pattern will stop.


