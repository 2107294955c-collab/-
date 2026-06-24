# Week 14 Project Summary

## Project Name

Mobile Web Control and Maze Exploration Robot Demo

## Main Goal

This project connects a browser-based control panel with a Python robot-control server. The system demonstrates how a phone can send movement commands to a robot simulation and how maze exploration logic can be organized into separate reusable modules.

## Delivered Files

| File | Purpose |
| --- | --- |
| `index.html` | Mobile web control panel with movement buttons |
| `server.py` | Long-running Python server that receives web commands and controls the robot |
| `maze.py` | Maze map, obstacle layout, and collision-related logic |
| `explorer.py` | Automatic exploration and path-planning logic |
| `agent.py` | AI agent control helper |
| `turtlesim_auto.mp4` | Recorded project demonstration |
| `week14_XXXX.pdf` | Final PDF project report |
| `docker-compose.yml` | Container orchestration file |
| `turtlesim_web_bridge.py` | ROS2 turtlesim web bridge backup implementation |
| `turtlesim_maze.py` | turtlesim maze implementation |
| `turtlesim_explorer.py` | turtlesim exploration implementation |
| `turtlesim_index.html` | turtlesim web control page |

## System Flow

```txt
Phone browser
  -> index.html
  -> server.py
  -> robot control commands
  -> maze.py map constraints
  -> explorer.py automatic exploration
```

## Demonstration Evidence

- Demo video: [turtlesim_auto.mp4](turtlesim_auto.mp4)
- PDF report: [week14_XXXX.pdf](week14_XXXX.pdf)
- Screenshot evidence: [img/](img/)

## Scoring Checklist

- [x] Mobile or browser control interface exists.
- [x] Server-side command receiver exists.
- [x] Robot control code is included.
- [x] Maze logic is included.
- [x] Exploration logic is included.
- [x] Demo video is included.
- [x] PDF report is included.
- [x] README links all core deliverables.

## Reflection

The most important lesson from this project is that a robot demonstration needs more than a single script. The control interface, server, robot simulation, maze logic, exploration algorithm, screenshots, video, and report all need to work together so that another person can understand and evaluate the result. The final repository now keeps those materials in one place and makes the project easier to inspect.
