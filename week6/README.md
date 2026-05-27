# Week 06 - KITTI Dataset And Multi-Sensor Visualization

## Task Goal

This week works with KITTI-style sensor data and ROS2 visualization. The goal is to publish point cloud and image data, then inspect the result with visualization tools.

## Folder Check

<pre>
week6/
|-- README.md          # required report
|-- img/               # visualization image
</pre>

## Environment

- ROS2 Jazzy
- KITTI Raw Dataset
- RViz2
- RQT
- cv_bridge

## Steps

1. Study the KITTI dataset structure.
2. Convert point cloud and image data into ROS2 messages.
3. Run the publisher node.
4. Inspect the output with RViz2 and RQT.

## Commands

<pre><code>ros2 run ros2_kitti_publishers publisher_node
rviz2
rqt</code></pre>

## Result

<img src="img/粘贴的图像.png" width="800" alt="KITTI visualization screenshot">

## Summary

Multi-sensor visualization is a key robot perception skill. This week strengthens the connection between datasets, ROS2 message types, and visual debugging tools.

---

[Back to main archive](../README.md)
