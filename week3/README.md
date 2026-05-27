# Week 03 - GitHub SSH、VS Code 与 ROS2 交互

## 1. 作业说明

本周练习 VS Code Remote-WSL 开发流程，并通过 ROS2 topic 命令控制 turtlesim。

## 2. 文件结构

<pre>
week3/
|-- README.md              # 必须
|-- img/                   # 实验截图
|-- code/                  # 有代码时必须
</pre>

## 3. 实验环境

- VS Code Remote-WSL
- ROS2
- Git
- turtlesim

## 4. 实验步骤

1. 使用 VS Code 连接 WSL。
2. 启动 turtlesim 节点。
3. 发布 Twist 消息控制小乌龟运动。
4. 截图记录实验结果。

## 5. 运行命令

<pre><code class="language-bash">
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0}, angular: {z: 1.8}}"
</code></pre>

## 6. 结果展示

<img src="img/粘贴的图像.png" width="800" alt="Week 3 ROS2 实验截图">

## 7. 学习总结

通过本周实验理解了 ROS2 topic 的发布机制，以及 VS Code 远程开发的便利性。

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
