# Week 14 - Laikago Stability Debugging

## Task Goal

This week focuses on Laikago quadruped stability in PyBullet. The work investigates orientation, leg polarity, inverse kinematics, and startup control.

## Folder Check

<pre>
week14/
|-- README.md          # required report
|-- img/               # result screenshots
|-- code/              # recommended when source exists
</pre>

## Environment

- Python
- PyBullet
- Laikago URDF
- Inverse kinematics

## Steps

1. Diagnose unstable landing and joint conflicts.
2. Check robot orientation and front/back leg polarity.
3. Use PyBullet inverse kinematics for foot targets.
4. Add startup buffering to reduce sudden force.

## Commands

<pre><code>python3 pybullet_perfect.py</code></pre>

## Result

<img src="img/截图 2026-05-21 10-21-51.png" width="800" alt="Laikago stability screenshot">

## Summary

Quadruped stability depends on control logic and physical contact. This week documents practical debugging beyond simple waveform movement.

---

[Back to main archive](../README.md)
