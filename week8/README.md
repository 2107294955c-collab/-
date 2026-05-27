# Week 08 - Docker ROS2 Desktop Container

## Task Goal

This week uses Docker to create a reusable ROS2 desktop environment and access it through a browser GUI.

## Folder Check

<pre>
week8/
|-- README.md          # required report
|-- img/               # screenshot evidence
</pre>

## Environment

- Docker
- ROS2 desktop VNC image
- Browser
- NoVNC

## Steps

1. Pull or run a ROS2 desktop container.
2. Map the web access port.
3. Open the browser interface.
4. Run turtlesim inside the container.

## Commands

<pre><code>docker run -it --rm -p 6080:80 tiryoh/ros2-desktop-vnc:humble
ros2 run turtlesim turtlesim_node</code></pre>

## Result

<img src="img/粘贴的图像.png" width="800" alt="Docker ROS2 desktop screenshot">

## Summary

Docker makes the robot development environment portable. Browser-based GUI access is helpful when using ROS2 tools inside a container.

---

[Back to main archive](../README.md)
