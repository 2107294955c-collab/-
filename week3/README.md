# Week 03: GitHub SSH、VS Code 与 ROS 2 交互

## 1. 实验目标
- 掌握通过 VS Code 远程连接并编辑 WSL 环境中的文件。
- 练习 Git 的分支管理与版本回退。
- 在 ROS 2 环境中测试节点通信。

## 2. 实验内容
### 2.1 远程开发
通过 Remote-WSL 插件，在 VS Code 中直接操作 Ubuntu 文件系统。

### 2.2 节点控制
运行了 `turtlesim` 节点，并尝试通过命令行发布速度指令。

## 3. 实验截图
<img src="img/粘贴的图像.png" width="800" alt="Week 3 截图">

## 4. 运行命令
```bash
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
