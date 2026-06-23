# Week 05 - Linux Operations And Robot Kinematics

## Task Goal

This week combines Linux file operations with robot kinematics concepts. The key idea is that robot development requires both system-level skill and coordinate-frame understanding.

## Folder Check

<pre>
week5/
|-- README.md          # required report
|-- img/               # recording evidence
</pre>

## Environment

- Linux terminal
- GitHub Markdown
- Robot TF / coordinate-frame concepts

## Steps

1. Practice Linux commands such as permission and ownership operations.
2. Study base_link and odom relationships.
3. Record the experiment process as a video.

## Commands

<pre><code>chmod
chown
ls -la</code></pre>

## Result

<video src="img/录屏 2026-04-02 10-56-36.webm" width="800" controls>experiment recording</video>

[Open original recording](img/录屏 2026-04-02 10-56-36.webm)

## Summary

Linux permissions affect whether scripts and robot packages can run correctly. Coordinate-frame knowledge is also necessary for understanding how robots locate themselves in space.

---

n## 遇到的问题与解决

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 环境配置报错 | 依赖版本不兼容 | 查阅官方文档确认版本匹配后重新安装 |
| 命令执行无响应 | 环境变量未加载 | 执行 source 加载 ROS2 环境脚本 |
| 截图无法正常显示 | 图片路径错误 | 检查相对路径，确保文件在正确目录 |
| 代码运行失败 | 缺少依赖包 | 使用 pip install 补全缺失的依赖 |

[Back to main archive](../README.md)
