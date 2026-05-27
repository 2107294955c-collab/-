# Week 14 - Laikago 四足机器人稳定性调试

## 1. 作业说明

本周调试 Laikago 四足机器人在 PyBullet 中的落地稳定性、关节方向和 Trot 步态控制。

## 2. 文件结构

<pre>
week14/
|-- README.md              # 必须
|-- img/                   # 截图、效果图
|-- code/                  # 推荐
</pre>

## 3. 实验环境

- Python
- PyBullet
- Laikago URDF
- Inverse Kinematics

## 4. 实验步骤

1. 排查初始姿态错误。
2. 分析前后腿关节方向差异。
3. 使用 PyBullet IK 控制足端轨迹。
4. 加入起步缓冲机制。

## 5. 运行命令

<pre><code class="language-bash">
python3 pybullet_perfect.py
</code></pre>

## 6. 结果展示

<img src="img/截图 2026-05-21 10-21-51.png" width="800" alt="Laikago 稳定性调试截图">

## 7. 学习总结

四足机器人稳定性不仅依赖步态数学模型，还与 URDF 关节方向、接触和启动控制有关。

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
