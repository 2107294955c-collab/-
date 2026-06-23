# Week 01 - Environment Setup And Tool Installation

## Task Goal

This week prepares the course workflow. The main task is to make sure GitHub, VS Code, Git, and SSH are ready before the robot experiments begin. A working toolchain is important because every later week depends on stable editing, committing, and pushing.

## Folder Check

<pre>
week1/
|-- README.md          # required report
|-- screenshots/       # recommended when setup images exist
</pre>

## Work Completed

1. Created or prepared the GitHub account used for the course.
2. Installed VS Code as the main editor for Markdown and code files.
3. Configured Git identity and repository access.
4. Prepared SSH authentication so future submissions can be pushed more smoothly.

## Commands

<pre><code>git config --global user.name your-name
git config --global user.email your-email@example.com
ssh-keygen -t ed25519
git status</code></pre>

## Result

The local environment is ready for weekly homework submission. The repository can now be used as a structured course archive.

## Summary

The most important result of this week is not a robot demo, but a reliable submission workflow. With GitHub, Git, VS Code, and SSH prepared, later ROS2 and simulation tasks can be documented and submitted with less friction.

---

n## 遇到的问题与解决

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 环境配置报错 | 依赖版本不兼容 | 查阅官方文档确认版本匹配后重新安装 |
| 命令执行无响应 | 环境变量未加载 | 执行 source 加载 ROS2 环境脚本 |
| 截图无法正常显示 | 图片路径错误 | 检查相对路径，确保文件在正确目录 |
| 代码运行失败 | 缺少依赖包 | 使用 pip install 补全缺失的依赖 |

[Back to main archive](../README.md)
