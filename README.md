| Deliverable | Due Date              |
|---------------|----------------------------------------------------------------------------|
| Presentation Due Date  | Wednesday, March 17th at 3:00PM EST                |
| Report Due Date     | Friday, March 19th at 1:00PM EST on github pages site |


# Lab 3: Wall Following in TESSE

## Introduction

- introduce tesse
- team-based lab
- link to tesse_install

## Submission

- include team assessment form

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
- list of topics available

## Recording and Playing Back Rosbags with TESSE

Rosbags are a useful tool for recording various published messages when running your code and playing it back later. To record a rosbag while using TESSE and tesse-ros-bridge:
- Start the TESSE executable on your host machine.
- Run `roscore` in a terminal inside your VM.
- In a new terminal, navigate to `~/racecar_ws/src/tesse-ros-bridge/ROS/scripts` and run `./rosbag_record.bash` to start recording.
- In a new terminal, run the code that you want to record - this could be launching tesse-ros-bridge or your wall following code.
- When you're done running what you want to record, you can terminate it, and then terminate the rosbag recording script. It will tell you what filename the rosbag was saved to in the `scripts` directory.
- Next, make sure to restamp the rosbag by running `./restamp_rosbag.py -i <input_rosbag_name.bag> -o <output_rosbag_name.bag>` where `<input_rosbag_name.bag>` is the filename that was specified in the recording script output and `<output_rosbag_name.bag>` must be a different name than the input name. (This step is important for setting the expected frame rate and imu rate for the bag file.)
- You can view info regarding the recording, including what topics and how many messages of different types were published, by running `rosbag info <output_rosbag_name.bag>`.
- You can play back your recording by running `rosbag play <output_rosbag_name.bag>` - you will need to be running `roscore` in a separate terminal for this to work. If you run `rostopic list` or `rostopic echo <topic>` while playing back the recording, it will behave as it would have while the recorded code was running. 

## MODULES (maybe break up into two tracks and speed)

- details about what we expect them to show
- details about how to get average speed (how it will included in scoring, refer to scoring)

## Steps to Success (some tips)
