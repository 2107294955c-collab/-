# Week 10 - Docker 概念与 OpenCV 实验

## 1. 作业说明

本周在 Docker 容器中安装并验证 OpenCV 与 PyBullet，学习镜像提交和环境固化。

## 2. 文件结构

<pre>
week10/
|-- README.md              # 必须
|-- img/                   # 截图、效果图
</pre>

## 3. 实验环境

- Docker
- Python
- OpenCV
- PyBullet

## 4. 实验步骤

1. 进入 ROS2 容器环境。
2. 安装 OpenCV 与 PyBullet。
3. 验证运行结果。
4. 使用 docker commit 保存镜像。

## 5. 运行命令

<pre><code class="language-bash">
docker commit -m "install pybullet and opencv" d8e79722b2b0 my-ros2-full:v1.0
docker images
docker ps
</code></pre>

## 6. 结果展示

<img src="img/截图 2026-05-07 10-05-07.png" width="800" alt="OpenCV 环境验证截图">

## 7. 学习总结

掌握了 Docker 镜像固化方法，也理解了 OpenCV 在机器人视觉实验中的基础作用。

## 8. 评分自查

| 项目 | 状态 | 说明 |
| --- | --- | --- |
| 提交 week 文件夹 | 完成 | 已建立本周目录 |
| README.md 存在 | 完成 | 已按统一模板编写 |
| README 内容详细 | 完成 | 包含目标、环境、步骤、结果和总结 |
| 包含图片 / 视频 | 视本周任务 | 有实验素材时已引用 |
| 包含代码 | 视本周任务 | 有代码作业时提交源码 |
| 有提交记录 | 完成 | 通过 Git 提交 |
| 按时提交 | 待确认 | 以课程截止时间为准 |

---

[返回总目录](../README.md)
