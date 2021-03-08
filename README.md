| Deliverable | Due Date              |
|---------------|----------------------------------------------------------------------------|
| Presentation Due Date  | Wednesday, March 17th at 1:00PM EST                |
| [Team Member Assessment](https://docs.google.com/forms/d/e/1FAIpQLScM6T3JsnlFQldhL_fVmAr9FkUILOjbXHM_nYxK280UZwJPww/viewform)  | Wednesday, March 17th at 1:00PM EST                |
| Report Due Date     | Friday, March 19th at 11:59PM EST on github pages site |


# Lab 3: Wall Following in TESSE

## Introduction
Welcome to the world of 3D! We're transitioning to using the realistic car simulator in TESSE for this lab. Make sure you've followed all the instructions in [tesse_install](https://github.com/mit-rss/tesse_install) before proceeding.

In this week's lab you're going to work with your team to implement a wall follower in tesse. This environment uses a realistic physics simulator, so you will need to account for delays in acceleration and deceleration. The car can tilt, and drift, which will add significant noise to recieved lidar data. In addition, the environment is dense with other buildings, lamposts, trees, and city fixtures. 

The goal is to complete the two tracks described below autonomously without collisions, with an added challenge of maintaining an average speed above 4m/s (see grading rubric). 

A good place to start would be to sit down with your new team and consolidate your wall folower code from last week's lab. You should be able to put your working code in `/src/wall_follower_tesse.py`, change the parameters to the appropriate tesse parameters in `params_tesse.yaml`, and run the example launch file in `/launch` to get a minimal working wall follower in tesse. 

## Submission

- include team assessment form (should this also be in due date chart above?)
- spell out deliverables

## Grading

- include a rubric: 7 points report, 2 points briefing, 1 point speed
- explain how speed-based grading will work

## Starter Code

- what we tell them to not modify, how to begin, file structure

Clone this repository into your catkin workspace:

    cd ~/racecar_ws/src
    git clone https://github.com/mit-rss/wall_follower_tesse.git

Then rebuild your workspace with `catkin_make`:

    cd ~/racecar_ws
    catkin_make
    source devel/setup.bash



## Adapting 2D Wall Follower
- differences between 2d and tesse

## Recording and Playing Back Rosbags with TESSE

Rosbags are a useful tool for recording various published messages when running your code and playing it back later.

To record a rosbag while using TESSE and `tesse-ros-bridge`:
- Start the TESSE executable on your host machine with `--client_ip_addr` set to your VM IP address (see the [TESSE setup handout](https://github.com/mit-rss/tesse_install) if you need a refresher on how to find this).
- Run `roscore` in a terminal inside your VM.
- In a new terminal, navigate to `~/racecar_ws/src/tesse-ros-bridge/ROS/scripts` and run `./rosbag_record.bash` to start recording.
- In a new terminal, run the code that you want to record - this could be launching `tesse-ros-bridge` or your wall following code.
- When you're done running what you want to record, you can terminate it, and then terminate the rosbag recording script. You can also stop running the TESSE simulator. The output of the rosbag recording script will tell you what filename the rosbag was saved to in the `scripts` directory.
- Next, make sure to restamp the rosbag by running `./restamp_rosbag.py -i <input_rosbag_name.bag> -o <output_rosbag_name.bag>` where `<input_rosbag_name.bag>` is the filename that was specified in the recording script output and `<output_rosbag_name.bag>` must be a *different* name than the input name. (This step is important for setting the expected frame rate and imu rate for the bag file.)

To analyze and play back your rosbag file:
- You do not need to be running `tesse-ros-bridge` or the TESSE simulator while playing back the rosbag.
- You can view info regarding the recording, including what topics and how many messages of different types were published, by running `rosbag info <output_rosbag_name.bag>`.
- You can play back your recording by running `rosbag play <output_rosbag_name.bag>` - you will need to be running `roscore` in a separate terminal for this to work. If you run `rostopic list` or `rostopic echo <topic>` while playing back the recording, it will behave as it would have while the recorded code was running.

## Modules
You will be implementing a wall follower in tesse to complete a loop around two different buildings without collisions, and quickly. The tracks are shown in the map below with the direction you should be following, and you will be able to spawn your cars at the start of either track (indicated with green stars) with a parameter in `params_tesse.yaml`. We suggest you start with the simple course, but we expect you to complete both without collisions and analyze your performance and average speeds achieved in the reports and briefings. 
### Tracks and Spawn Points
There are two tracks you must complete. You can toggle which track your car spawns at by changing the `track` parameter in `/wall_follower_tesse/params_tesse.yaml`. The two options are `wall_follower_simple` and `wall_follower_complex` for the simple and complex tracks respectively. **For the simple track, you will be required to follow the wall on the right side of the car. For the complex track, you will be required to follow the wall on the left side of the car.**
![map](./media/map.png)
#### Note:

* Simple track spawn POV, follow the right wall.
    - <img src="./media/wall_follower_simple.png" width="500">
* Complex track spawn POV, follow the left wall.
    - <img src="./media/wall_follower_complex.png" width="500">

### todo

- details about what we expect them to show
- details about how to get average speed (how it will included in scoring, refer to scoring)

## Import Topic Details 
* `/tesse/drive`
    - [http://docs.ros.org/en/melodic/api/ackermann_msgs/html/msg/AckermannDriveStamped.html](http://docs.ros.org/en/melodic/api/ackermann_msgs/html/msg/AckermannDriveStamped.html)
* `/tesse/odom`
    - [http://docs.ros.org/melodic/api/nav_msgs/html/msg/Odometry.html](http://docs.ros.org/melodic/api/nav_msgs/html/msg/Odometry.html)
* `/tesse/front_lidar/scan`
    - [http://docs.ros.org/melodic/api/sensor_msgs/html/msg/LaserScan.html](http://docs.ros.org/melodic/api/sensor_msgs/html/msg/LaserScan.html)
* `/tesse/collision`
    - [https://github.mit.edu/rss/tesse-ros-bridge/blob/master/ROS/msg/CollisionStats.msg](https://github.mit.edu/rss/tesse-ros-bridge/blob/master/ROS/msg/CollisionStats.msg)
* `/tesse/imu/clean/imu`
    - [ http://docs.ros.org/melodic/api/sensor_msgs/html/msg/Imu.html]( http://docs.ros.org/melodic/api/sensor_msgs/html/msg/Imu.html)
* `/initialpose`
    - [http://docs.ros.org/en/melodic/api/geometry_msgs/html/msg/PoseStamped.html](http://docs.ros.org/en/melodic/api/geometry_msgs/html/msg/PoseStamped.html)
    - You should not need to publish messages directly to `/initialpose` in your code! This is helper topic that allows you to spawn your car around the scene with the "2D Pose Estimate" tool in rviz if you wish to use it. The correct way to spawn your car is by changing the parameter in `params_tesse.yaml`. However, this topic is here if you wish to test your wall follower in other places in the environment. 

## Steps to Success (some tips)
- start with simple track at slow speeds
- look at hz drive commands speed
- increase VM compute
- rqt_multiplot tool
- link to ransac
- 
