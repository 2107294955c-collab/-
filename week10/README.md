# Week 10 - Docker And OpenCV Experiment

## Task Goal

This week strengthens Docker image workflow and verifies OpenCV-related dependencies for robot vision experiments.

## Folder Check

<pre>
week10/
|-- README.md          # required report
|-- img/               # output image
</pre>

## Environment

- Docker
- Python
- OpenCV
- PyBullet

## Steps

1. Enter the ROS2 container environment.
2. Install OpenCV and PyBullet.
3. Verify that the environment works.
4. Save the configured container as an image.

## Commands

<pre><code>docker commit -m "install pybullet and opencv" d8e79722b2b0 my-ros2-full:v1.0
docker images
docker ps</code></pre>

## Result

<img src="img/截图 2026-05-07 10-05-07.png" width="800" alt="OpenCV environment verification screenshot">

## Summary

The task prepares a reusable vision environment. OpenCV and PyBullet support later perception and simulation work.

---

[Back to main archive](../README.md)
