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

n## 遇到的问题与解决

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 环境配置报错 | 依赖版本不兼容 | 查阅官方文档确认版本匹配后重新安装 |
| 命令执行无响应 | 环境变量未加载 | 执行 source 加载 ROS2 环境脚本 |
| 截图无法正常显示 | 图片路径错误 | 检查相对路径，确保文件在正确目录 |
| 代码运行失败 | 缺少依赖包 | 使用 pip install 补全缺失的依赖 |

[Back to main archive](../README.md)
## 延伸思考

ROS2 环境搭建是整个课程的基石。后续的话题通信、可视化、Docker 容器化都依赖于此。在 WSL2 中运行 ROS2 兼顾了 Windows 日常使用的便利性和 Linux 开发环境的原生支持。
