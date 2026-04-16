# Week 02：Ubuntu 24.04 环境搭建与 ROS 2 初探

## 1. 实验目标
- 在本地设备上安装并配置最新的 **Ubuntu 24.04 LTS** 操作系统。
- 完成 **ROS 2 (Jazzy Jalisco)** 环境的安装与工作空间配置。
- 运行经典的 **Turtlesim (小乌龟)** 案例，验证 ROS 2 节点的发布与订阅机制。

## 2. 实验环境
- **操作系统**: Ubuntu 24.04 LTS
- **机器人框架**: ROS 2 Jazzy
- **核心工具**: Terminal, VS Code

## 3. 实验内容与步骤

### 3.1 环境安装
配置了 Ubuntu 软件源，并完成了 ROS 2 桌面版的完整安装。
设置环境变量以确保每次打开终端都能自动加载 ROS 2 环境：
```bash
source /opt/ros/jazzy/setup.bash