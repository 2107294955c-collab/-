# Week 10: Docker 概念与 OpenCV 实验报告

## 实验内容
本周的主要任务是配置 ROS2 容器环境，并安装必要的库：
1. **Docker 操作**：学习了镜像的查看、提交与保存。
2. **环境安装**：在容器内安装了 `pybullet` 和 `opencv-python`。
3. **环境固化**：使用 `docker commit` 命令保存了修改后的镜像。

## 实验截图
### OpenCV 环境验证
<img src="img/截图 2026-05-07 10-05-07.png" width="600">

## 运行命令总结
```bash
# 提交镜像
docker commit -m "install pybullet and opencv" d8e79722b2b0 my-ros2-full:v1.0
