# Week 03：ROS 2 话题发布与小乌龟运动控制

## 1. 实验目标
- 学习如何通过命令行工具手动发布话题消息（`ros2 topic pub`）。
- 掌握 `geometry_msgs/msg/Twist` 消息结构，实现对机器人运动的精准控制。
- 观察不同线速度（Linear）与角速度（Angular）组合下小乌龟的运动轨迹。

## 2. 实验环境
- **操作系统**: Ubuntu 24.04 LTS
- **机器人框架**: ROS 2 Jazzy
- **核心工具**: Turtlesim, Terminal

## 3. 实验内容与步骤

### 3.1 手动发布控制指令
不再仅依赖键盘控制，而是通过终端命令直接向 `/turtle1/cmd_vel` 话题发送指令：
```bash
ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"