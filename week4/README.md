# Week 04：PyBullet 仿真环境搭建与四足机器人加载

## 1. 实验目标
- 学习并安装 **PyBullet** 物理仿真引擎。
- 掌握加载机器人描述文件（URDF）的基本流程。
- 在仿真环境中初始化四足机器人模型，并观察其默认物理状态。

## 2. 实验环境
- **操作系统**: Ubuntu 24.04 LTS
- **仿真引擎**: PyBullet (Bullet Physics)
- **编程语言**: Python 3
- **参考课件**: 《ai_robot_0325.pptx》第 56 页

## 3. 实验内容与步骤

### 3.1 PyBullet 环境配置
在终端中完成了物理引擎库的安装与验证：
```bash
pip install pybullet