# Week 02 - Ubuntu 24.04 与 ROS2 初探

## 1. 作业说明

本周完成 Ubuntu 24.04 与 ROS2 Jazzy 环境配置，并通过 turtlesim 验证 ROS2 基础环境。

## 2. 文件结构

<pre>
week2/
|-- README.md              # 必须
|-- screenshots/           # 推荐
</pre>

## 3. 实验环境

- Ubuntu 24.04 LTS
- ROS2 Jazzy
- Terminal
- VS Code

## 4. 实验步骤

1. 配置 Ubuntu 软件源。
2. 安装 ROS2 Jazzy 桌面环境。
3. 加载 ROS2 环境变量。
4. 运行 turtlesim 验证环境。

## 5. 运行命令

<pre><code class="language-bash">
source /opt/ros/jazzy/setup.bash
ros2 run turtlesim turtlesim_node
</code></pre>

## 6. 结果展示

ROS2 环境可正常运行，为后续话题通信和仿真实验打下基础。

## 7. 学习总结

掌握了 ROS2 环境配置流程，并理解了 source 环境变量的重要性。

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
