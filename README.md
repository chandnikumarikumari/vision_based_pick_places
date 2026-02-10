# Vision-Based Pick and Place (ROS 2 + MoveIt 2)

## Objective
Design a vision-based pick-and-place robotic system using ROS 2, MoveIt 2,
and an eye-in-hand camera configuration.

## System Overview
This project follows a Task and Motion Planning (TAMP) architecture:
- Perception
- TF-based pose transformation
- Symbolic task planning
- Motion planning using MoveIt 2

## Architecture
Gazebo → Perception → TF → Task Planner → MoveIt 2 → Execution

## Perception
Object pose is detected in the camera frame and published as PoseStamped.

## TF Tree
world → base_link → end_effector → camera_link

## Task Planning
High-level symbolic actions:
- move
- pick
- place

## Motion Planning
Motion execution is handled via MoveIt 2 using OMPL planners
(RRTConnect / RRTStar) with collision checking enabled.

Reference:
https://github.com/ros-planning/moveit2_tutorials

## Pick and Place Pipeline
Pick:
- Move to pre-grasp
- Open gripper
- Approach
- Close gripper
- Lift

Place:
- Move to pre-place
- Lower
- Open gripper
- Retreat

## Visualization
RViz is used to visualize:
- Robot model
- TF frames
- Camera feed
- Planned trajectories

## Notes
Due to hardware constraints, this repository focuses on
architecture, code structure, and planning logic.
