# Week 06：ROS 2 Kitti 数据集解析与多传感器可视化

## 1. 实验目标
- 学习如何在 ROS 2 环境下加载和解析自动驾驶权威数据集 **Kitti**。
- 编写发布者节点（Publisher Node），将点云（Point Cloud）和相机图像（Camera Image）转化为 ROS 2 标准话题。
- 利用 **RViz2** 和 **RQT** 实现 3D 点云与 2D 图像的同步可视化。

## 2. 实验环境
- **操作系统**: Ubuntu 24.04 LTS
- **机器人框架**: ROS 2 Jazzy
- **数据集**: Kitti Raw Dataset (City/Residential)
- **核心工具**: RViz2, RQT, `cv_bridge`

## 3. 实验内容与步骤

### 3.1 数据集架构理解
Kitti 数据集包含 Velodyne 激光雷达扫描数据（`.bin` 文件）和前后轴摄像头采集的图像。实验中重点学习了如何按照时间戳同步这些异构数据。

### 3.2 编写发布节点
通过 Python 脚本实现以下逻辑：
- 使用 `numpy` 读取点云二进制文件并转换为 `sensor_msgs/PointCloud2`。
- 使用 `cv_bridge` 将 OpenCV 图像转换为 `sensor_msgs/Image`。
- **运行命令**:
  ```bash
  ros2 run ros2_kitti_publishers publisher_node