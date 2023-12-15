# stream_publisher_package
ROS2 package to stream and publish images to a specified topic. 

This package uses the Arena SDK and ROS2 libraries to stream and publish images to a topic. Essential camera nodes can be specified in the config file, `stream_config.yaml`. 

ROS2 bags can be recorded using this package, further instructions are listed below.

**For more information on this package, check the Joplin documentation under the _Stream Publisher Package_ page.**

## Requirements:
* Ubuntu Focal Fossa
* ROS2 Foxy Fitzroy
* Arena SDK for Linux
* C++17 or higher

## To Use:
**_Before Use:_**
* **Make sure your ethernet configurations are set to maximize fps! For more information, check the Jopling documentation under the _Getting Started_ page**
* **Make sure ALL PATHS ARE SET CORRECTLY in the launch and config files before use!**
* **These steps assume you have already created a workspace folder and a `/src` directory within it!**

**_Stream/Publish Steps_:**
1. Navigate into the `\src` directory of your workspace and clone the repo using `git clone`
2. Navigate back into the workspace directory and source `$ source /opt/ros/foxy/setup.bash`
3. Build package `$ colcon build` or `$ colcon build --packages-select <package_name>`
4. Open a new terminal and source it `$ . install/setup.bash`
5. Run launch file `$ ros2 launch <package_name> <launch_file_name>` in this case it is `$ ros2 launch stream_publisher_package stream_launch.py`
6. To view the stream open a new terminal and source it (same as step 4), and run `image_tools` via `$ ros2 run image_tools showimage --ros-args --remap image:=<topic_name>`

**Note:** `<topic_name>` also includes the namespace and can be found using `$ ros2 topic list` in a sourced terminal

**_Recording a ROS bag Steps_:**
1. Make sure you are publishing images using the previous steps
2. Create the desired directory to record bags, navigate to it, and source it using `$source /opt/ros/foxy/setup.bash`
3. Record bag using `$ros2 bag record <topic_name> -o <bag_name>`. Where `<bag_name>` can be specified by user choice

**Note:** For more information on extracting data from recorded bags for post processing, check out the `utilities_package`.
