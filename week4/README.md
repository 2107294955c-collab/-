# Week 04 - Command Line And Python Simulation

## Task Goal

This week practices command-line operation, robot basics, and Python simulation thinking. The task is to move from manual command execution toward repeatable scripted robot behavior.

## Folder Check

<pre>
week4/
|-- README.md          # required report
|-- *.py               # Python homework when available
|-- images/            # recommended media
</pre>

## Environment

- Python
- ROS2 concepts
- Terminal

## Steps

1. Review command-line workflow.
2. Study simple robot motion concepts.
3. Prepare Python simulation logic.
4. Record the workflow in README form.

## Commands

<pre><code>python3 motion_script.py
ros2 topic list</code></pre>

## Result

This week documents the transition from manual terminal control to scripted motion logic.

## Summary

Python scripting helps make robot experiments repeatable. Even when the task is basic, recording commands and intended output makes the week easier to evaluate.

---

## 遇到的问题与解决

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 环境配置报错 | 依赖版本不兼容 | 查阅官方文档确认版本匹配后重新安装 |
| 命令执行无响应 | 环境变量未加载 | 执行 source 加载 ROS2 环境脚本 |
| 截图无法正常显示 | 图片路径错误 | 检查相对路径，确保文件在正确目录 |
| 代码运行失败 | 缺少依赖包 | 使用 pip install 补全缺失的依赖 |

[Back to main archive](../README.md)
