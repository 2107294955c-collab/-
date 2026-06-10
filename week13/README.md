# Week 13：四足机器人入门与期末项目实施

## 一、实验基本信息

课程：AI Robotics  
主题：四足机器人入门、PyBullet 仿真、期末项目整理  
工具：Python、PyBullet、GitHub Pages  

---

## 二、实验目标

本周是课程最后阶段，重点是理解四足机器人的基本结构、运动控制思想，并完成期末项目的核心功能整理。

本周完成内容：

1. 了解四足机器人结构与运动特点。
2. 理解四足机器人相比轮式机器人的优势。
3. 使用 Python 模拟四足机器人运动状态。
4. 整理期末项目开发检查清单。
5. 对前面课程内容进行总结和收尾。

---

## 三、理论整理

### 1. 为什么需要四足机器人？

轮式机器人在平地上速度快、效率高，但是面对楼梯、碎石、山地等复杂地形时容易受限制。四足机器人通过腿部运动可以跨越障碍，适合巡检、救援、山地探索等场景。

### 2. 四足机器人的基本结构

四足机器人通常有四条腿：

- LF：Left Front，左前腿
- RF：Right Front，右前腿
- LH：Left Hind，左后腿
- RH：Right Hind，右后腿

每条腿通常包含多个关节，例如髋关节、大腿关节和小腿关节。

### 3. 四足机器人控制思想

四足机器人控制需要考虑：

- 身体平衡
- 步态规划
- 足端接触
- 关节角度控制
- IMU 姿态反馈

现代四足机器人常结合模型预测控制、强化学习和仿真训练，实现更稳定的运动能力。

---

## 四、项目开发整理

### 1. 项目基础搭建

- [x] 建立课程作业仓库
- [x] 整理 Week2 到 Week13 的实验页面
- [x] 配置 GitHub Pages 页面结构
- [x] 添加每周实验截图

### 2. 核心功能实现

- [x] ROS2 turtlesim 控制实验
- [x] Python 运动学仿真
- [x] RViz Marker 可视化
- [x] ArUco 视觉识别
- [x] Docker ROS2 桌面容器实验
- [x] OpenCV 图像处理实验

### 3. 测试与完善

- [x] 检查图片路径
- [x] 检查 README 链接
- [x] 检查每周文件夹结构
- [x] 整理最终提交内容

---

## 五、仿真实验

本周使用 Python 编写简化的四足机器人步态模拟程序。  
程序模拟四条腿在不同时间步下的支撑状态，用于理解四足机器人的步态切换思想。

运行命令：

```bash
python3 quadruped_project_demo.py
cd ~/ai_robotics_record/week13
python3 quadruped_project_demo.py

cd ~/ai_robotics_record/week13
python3 quadruped_project_demo.py
cd ~/ai_robotics_record/week13
python3 quadruped_project_demo.py、
cd ~/ai_robotics_record
mkdir -p week13/img
cat > week13/quadruped_project_demo.py <<'EOF'
import time

print("Week 13：四足机器人步态模拟")
print("--------------------------------")

print("四足机器人基本结构：")
print("LF：左前腿")
print("RF：右前腿")
print("LH：左后腿")
print("RH：右后腿")

print("--------------------------------")
print("开始模拟 Trot 对角步态")

for step in range(1, 7):
    print(f"Step {step}")

    if step % 2 == 1:
        print("支撑腿：LF 左前腿 + RH 右后腿")
        print("摆动腿：RF 右前腿 + LH 左后腿")
    else:
        print("支撑腿：RF 右前腿 + LH 左后腿")
        print("摆动腿：LF 左前腿 + RH 右后腿")

    print("身体保持平衡，进入下一步")
    print("--------------------------------")
    time.sleep(0.3)

print("四足机器人步态模拟完成")
print("项目核心功能测试完成")
