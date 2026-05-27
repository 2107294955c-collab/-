# Week 02 - Ubuntu 24.04 And ROS2 Setup

## Task Goal

This week focuses on preparing Ubuntu 24.04 and ROS2. The goal is to build a working robot software environment and verify it with a simple ROS2 demo.

## Folder Check

<pre>
week2/
|-- README.md          # required report
|-- screenshots/       # recommended
</pre>

## Environment

- Ubuntu 24.04 LTS
- ROS2 Jazzy
- Terminal
- VS Code

## Steps

1. Configure Ubuntu package sources.
2. Install ROS2 desktop tools.
3. Source the ROS2 environment script.
4. Run turtlesim to verify that ROS2 can launch graphical nodes.

## Commands

<pre><code>source /opt/ros/jazzy/setup.bash
ros2 run turtlesim turtlesim_node</code></pre>

## Result

ROS2 is ready for later topic, node, visualization, and container experiments.

## Summary

A correct ROS2 installation is the foundation of the whole course. This week confirms that the software stack can start ROS2 nodes and run a standard demo.

---

[Back to main archive](../README.md)
