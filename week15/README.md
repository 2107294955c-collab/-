# Week 15 - Tailscale 移动端摄像头图传

## 1. 作业说明

本周通过 Tailscale 虚拟局域网连接手机和电脑，实现移动端摄像头图传与 ArUco 标记检测。

## 2. 文件结构

<pre>
week15/
|-- README.md              # 必须
|-- img/                   # 截图、效果图
|-- code/                  # 有代码时必须
</pre>

## 3. 实验环境

- Tailscale
- Python
- HTTPS
- Mobile Camera
- ArUco

## 4. 实验步骤

1. 连接手机和电脑到 Tailscale。
2. 启动 camera_bridge.py 服务。
3. 手机浏览器访问 HTTPS 服务。
4. 授权摄像头并检测 ArUco ID。

## 5. 运行命令

<pre><code class="language-bash">
cd ~/ai-robot-class.github.io
mkdir -p week15/img
python3 camera_bridge.py
</code></pre>

## 6. 结果展示

<img src="img/result.jpeg" width="800" alt="ArUco 标记检测结果">

## 7. 学习总结

本周实验验证了虚拟局域网和移动端摄像头在机器人视觉任务中的可用性。

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
