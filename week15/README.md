# Week 15 — Week14 Project Archive & Final Summary

## Task Goal

Archive the complete Week14 robot dog (PyBullet) and turtle maze (TurtleSim) project code and final project report into Week15 as the course capstone deliverable.

## Folder Check

<pre>
week15/
|-- README.md                   # required report
|-- img/                        # screenshots
|-- Week14_项目报告.docx         # Week14 project report
|-- server.py                   # PyBullet robot dog simulation server
|-- agent.py                    # AI agent decision controller
|-- maze.py                     # Maze map generation
|-- explorer.py                 # Autonomous maze explorer
|-- index.html                  # Robot dog web control UI
|-- docker-compose.yml          # Docker container orchestration
|-- turtlesim_web_bridge.py     # TurtleSim ROS2 web bridge
|-- turtlesim_maze.py           # Turtle maze map
|-- turtlesim_explorer.py       # Turtle maze explorer
|-- turtlesim_index.html        # Turtle control web UI
</pre>

## Environment

- **Track A — PyBullet Robot Dog**
  - Python 3.12 + PyBullet + aiohttp
  - WSL2 Ubuntu 24.04 + Docker Engine
  - DeepSeek API (Agent mode)
  - Tailscale (mobile remote control)
- **Track B — TurtleSim Maze**
  - ROS2 Humble (Docker container)
  - TurtleSim + custom maze/explorer modules
  - Web bridge for browser control

## Architecture

```
Mobile Web Controller → Tailscale → WSL2 → Docker(ROS2) / PyBullet → Robot Motion
```

- Port 8765: Track A robot dog web controller
- Port 8080: Track B turtle controller
- Port 6080: noVNC remote desktop
- `PYBULLET_GUI=0`: DIRECT mode (low resource usage)

## Key Commands

<pre><code># Start PyBullet simulation (Agent mode)
wsl -d Ubuntu-24.04 -u root bash -c "cd /mnt/d/ai-robotics-course/week14_starters/pybullet_dog && DEEPSEEK_API_KEY=sk-xxx PYBULLET_GUI=0 python3 server.py"

# Start Docker containers (TurtleSim Track B)
wsl -d Ubuntu-24.04 -u root bash -c "service docker start && cd /mnt/d/ai-robotics-course/week14_starters/docker && docker compose up -d"

# View PyBullet logs
wsl -d Ubuntu-24.04 -u root bash -c "cat /tmp/pybullet_wsl.log"</code></pre>

## Result

- Full project code archived for both Track A (PyBullet robot dog) and Track B (TurtleSim maze)
- Project report: `Week14_项目报告.docx`
- Mobile remote control via Tailscale IP `100.66.42.5:8765`

## Summary

This project established a complete pipeline from mobile web controller to simulated robot: Tailscale networking → WSL2 VM → Docker/ROS2 → PyBullet physics simulation. Key challenges solved include Windows-WSL2 port forwarding (bypassed Docker, ran PyBullet directly in WSL), container dependency persistence after rebuild, and PyBullet GUI resource overhead (switched to DIRECT mode).

---

n## 遇到的问题与解决

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 环境配置报错 | 依赖版本不兼容 | 查阅官方文档确认版本匹配后重新安装 |
| 命令执行无响应 | 环境变量未加载 | 执行 source 加载 ROS2 环境脚本 |
| 截图无法正常显示 | 图片路径错误 | 检查相对路径，确保文件在正确目录 |
| 代码运行失败 | 缺少依赖包 | 使用 pip install 补全缺失的依赖 |

[Back to main archive](../README.md)
