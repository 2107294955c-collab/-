# Week 07 - Markdown And GitHub Organization

## Task Goal

This week improves repository organization. The task is to make every week easier to inspect by using a consistent README structure and clear folder layout.

## Folder Check

<pre>
week7/
|-- README.md          # required report
</pre>

## Environment

- GitHub
- Markdown
- Git
- VS Code

## Steps

1. Review folder naming.
2. Practice Markdown headings, tables, lists, and command blocks.
3. Update week pages with consistent sections.
4. Commit the changes.

## Commands

<pre><code>git status
git add .
git commit -m update-weekly-notes
git push origin main</code></pre>

## Result

The repository becomes easier to evaluate because each week follows a predictable report structure.

## Summary

Good documentation is part of the homework. A clear README helps the reviewer find goals, commands, screenshots, code, and conclusions quickly.

---

## 遇到的问题与解决

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 环境配置报错 | 依赖版本不兼容 | 查阅官方文档确认版本匹配后重新安装 |
| 命令执行无响应 | 环境变量未加载 | 执行 source 加载 ROS2 环境脚本 |
| 截图无法正常显示 | 图片路径错误 | 检查相对路径，确保文件在正确目录 |
| 代码运行失败 | 缺少依赖包 | 使用 pip install 补全缺失的依赖 |

[Back to main archive](../README.md)

## 延伸思考

规范的 Markdown 格式不仅有助于课程评分，更是技术文档写作的基本功。统一的目录结构让评审者能快速定位实验目标、命令、截图和总结，减少沟通成本。
