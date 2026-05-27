# AI Robot Homework Archive

<div align="center">

<pre>
+------------------------------------------------------------+
|                 AI ROBOT HOMEWORK ARCHIVE                 |
|        monochrome weekly logs / code / media evidence      |
+------------------------------------------------------------+
</pre>

**2107294955c-collab · AI Robot course repository**

</div>

---

## Repository Purpose

This repository keeps the AI Robot course work in a clear homework archive. The structure is optimized for review: every submitted week has its own folder, every folder has a README, and the README explains the task, environment, commands, evidence, and learning result. The design is intentionally black and white so the repository looks like a clean lab record rather than a decorative landing page.

## Submission Structure

<pre>
ai-robot-homework/
|-- README.md              # main overview
|-- week1/
|   |-- README.md          # required weekly report
|   |-- screenshots/       # recommended when screenshots exist
|-- week3/
|   |-- README.md          # required weekly report
|   |-- code/              # required when source code exists
|   |-- images/            # screenshots or output images
|-- week4/
|   |-- README.md          # required weekly report
|   |-- *.py               # Python homework when available
|   |-- images/            # experiment media
|-- ...
|-- week14/
|   |-- README.md          # simulation/debug report
|   |-- img/               # result screenshots
|-- week15/
|   |-- README.md          # remote camera report
|   |-- img/               # detection result
</pre>

## Review-Oriented Improvements

- Weekly README files are expanded into report-style records instead of short placeholders.
- Existing screenshots and videos are linked from their matching week pages.
- Weeks with code-oriented work include command sections and code-file expectations.
- Remote camera notes use a WebSocket-style access pattern, written as ws://<tailscale-ip>:5000, to match the requested Codex optimization.
- Empty weeks are documented honestly as archive or organization weeks instead of being left blank.

## Week Index

| Week | Topic | Evidence | Link |
| --- | --- | --- | --- |
| week1 | Environment setup and tool installation | README | [Open](./week1) |
| week2 | Ubuntu 24.04 and ROS2 environment | README | [Open](./week2) |
| week3 | GitHub SSH, VS Code, ROS2 interaction | Image | [Open](./week3) |
| week4 | Command line, robot basics, Python simulation | README | [Open](./week4) |
| week5 | Linux operations and robot kinematics | Video | [Open](./week5) |
| week6 | KITTI dataset and multi-sensor visualization | Image | [Open](./week6) |
| week7 | Markdown and GitHub organization | README | [Open](./week7) |
| week8 | Docker ROS2 desktop container | Image | [Open](./week8) |
| week10 | Docker and OpenCV experiment | Image | [Open](./week10) |
| week11 | Screenshot archive and verification | Image | [Open](./week11) |
| week14 | Laikago stability debugging | Image | [Open](./week14) |
| week15 | Tailscale mobile camera bridge | Image | [Open](./week15) |

## How To Review

1. Open the week folder from the index.
2. Read the weekly README from top to bottom.
3. Check the linked screenshot, video, or command output.
4. Review commit history to confirm regular submission progress.
