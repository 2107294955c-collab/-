# Week 14 - Laikago Stability Debugging

## Task Goal

This week focuses on Laikago quadruped stability in PyBullet. The work investigates orientation, leg polarity, inverse kinematics, and startup control.

## Folder Check

<pre>
week14/
|-- README.md          # required report
|-- img/               # result screenshots
|-- code/              # recommended when source exists
</pre>

## Environment

- Python
- PyBullet
- Laikago URDF
- Inverse kinematics

## Steps

1. Diagnose unstable landing and joint conflicts.
2. Check robot orientation and front/back leg polarity.
3. Use PyBullet inverse kinematics for foot targets.
4. Add startup buffering to reduce sudden force.

## Commands

<pre><code>python3 pybullet_perfect.py</code></pre>

## Result

<img src="img/screenshot_2.png" width="800" alt="Laikago stability screenshot">
<img src="img/screenshot_2.png" width="800" alt="Laikago stability screenshot">
<img src="img/screenshot_2.png" width="800" alt="Laikago stability screenshot">
<img src="img/screenshot_2.png" width="800" alt="Laikago stability screenshot">

## Summary

Quadruped stability depends on control logic and physical contact. This week documents practical debugging beyond simple waveform movement.

---

## 遇到的问题与解决

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 环境配置报错 | 依赖版本不兼容 | 查阅官方文档确认版本匹配后重新安装 |
| 命令执行无响应 | 环境变量未加载 | 执行 source 加载 ROS2 环境脚本 |
| 截图无法正常显示 | 图片路径错误 | 检查相对路径，确保文件在正确目录 |
| 代码运行失败 | 缺少依赖包 | 使用 pip install 补全缺失的依赖 |

---

## Week15 Project Archive (Merged)

### Project Files

| 文件 | 说明 |
|------|------|
| `Week14_项目报告.pdf` | 完整项目文档 |
| `server.py` | PyBullet 仿真服务器 |
| `agent.py` | AI Agent 控制器 |
| `maze.py` | 迷宫地图生成 |
| `explorer.py` | 迷宫自主探索 |
| `index.html` | 网页控制面板 |
| `docker-compose.yml` | Docker 编排 |
| `turtlesim_web_bridge.py` | ROS2 Web 桥接 |
| `turtlesim_maze.py` | 乌龟迷宫 |
| `turtlesim_explorer.py` | 乌龟探索 |
| `turtlesim_index.html` | 乌龟网页控制 |

### 系统架构

手机网页 → Tailscale → WSL2 → Docker/ROS2 → PyBullet 仿真

| 端口 | 服务 |
|------|------|
| 8765 | 机器狗 Web 控制器 |
| 8080 | 乌龟控制器 |
| 6080 | noVNC 桌面 |

### 遇到的问题与解决

| 问题 | 解决方案 |
|------|----------|
| WSL2 端口不通 | 配置端口转发 |
| 容器重建后依赖丢失 | 固化至 Dockerfile |
| PyBullet GUI 资源占用高 | 切换 DIRECT 模式 |

[Back to main archive](../README.md)
