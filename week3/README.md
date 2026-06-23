# Week 03 - GitHub SSH, VS Code And ROS2 Interaction

## Task Goal

This week connects development workflow with ROS2 interaction. The task is to use VS Code Remote-WSL and publish ROS2 messages to control turtlesim movement.

## Folder Check

<pre>
week3/
|-- README.md          # required report
|-- code/              # required when code exists
|-- img/               # experiment image
</pre>

## Environment

- VS Code Remote-WSL
- ROS2
- turtlesim
- GitHub SSH

## Steps

1. Open the Linux workspace from VS Code.
2. Start turtlesim.
3. Publish a Twist message to the velocity topic.
4. Save the screenshot as experiment evidence.

## Commands

<pre><code>ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0}, angular: {z: 1.8}}"</code></pre>

## Result

<img src="img/screenshot_2.png" width="800" alt="Week 3 ROS2 interaction screenshot">
<img src="img/screenshot_2.png" width="800" alt="Week 3 ROS2 interaction screenshot">
<img src="img/screenshot_2.png" width="800" alt="Week 3 ROS2 interaction screenshot">
<img src="img/screenshot_2.png" width="800" alt="Week 3 ROS2 interaction screenshot">

## Summary

This week shows how topic publishing changes robot behavior. It also confirms that VS Code, WSL, ROS2, and GitHub workflow can be used together.

---

## 遇到的问题与解决

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 环境配置报错 | 依赖版本不兼容 | 查阅官方文档确认版本匹配后重新安装 |
| 命令执行无响应 | 环境变量未加载 | 执行 source 加载 ROS2 环境脚本 |
| 截图无法正常显示 | 图片路径错误 | 检查相对路径，确保文件在正确目录 |
| 代码运行失败 | 缺少依赖包 | 使用 pip install 补全缺失的依赖 |

[Back to main archive](../README.md)
