# URDF-TF-ROS_Control
Packages related to URDF, TF and ROS_Control. Written in python

### mira robot in rviz
![mira_geometric_spawn3_urdf](https://user-images.githubusercontent.com/56476887/85279776-a3904a00-b4a4-11ea-99b1-fdb8699f1c40.png)

### mira robot launched in gazebo
![mira_geometric_spawn1](https://user-images.githubusercontent.com/56476887/85279781-a4c17700-b4a4-11ea-8d8b-6b9b8d39c3f7.png)

### mira robot launched in gazebo using it's 3D CAD model but with no controllers (thus it's head always moves)
![mira_nocontrollers](https://user-images.githubusercontent.com/56476887/85279769-9ffcc300-b4a4-11ea-8dd2-b9f375b9ca85.gif)



### pi robot launched in gazebo with few joints activated by running publishing to it's topics
![pi_robot_moving](https://user-images.githubusercontent.com/56476887/85285334-5fa24280-b4ae-11ea-8b92-8998a8e7cb54.gif img width="400")


### tf will not be published if robot_state_publisher is not launched, thus we fail to obtain the pi robot in rviz 
<img width="720" alt="tf_no_rst1" src="https://user-images.githubusercontent.com/56476887/85285651-df301180-b4ae-11ea-80cd-cb478334c337.png">


### after launching robot_state_publisher
![rviz_pirobot1](https://user-images.githubusercontent.com/56476887/85285333-5f09ac00-b4ae-11ea-8332-dda4631b2e6b.png)



### The joint_state_publisher with the use_gui parameter enabled
![pi_robot_jointstatepublisher](https://user-images.githubusercontent.com/56476887/85285329-5d3fe880-b4ae-11ea-890e-8a92cc1072f3.png)
