# Week 15 - Tailscale Mobile Camera Bridge

## Task Goal

This week connects a phone and computer through Tailscale and uses the mobile camera as a remote vision source. The access note is written with ws://<tailscale-ip>:5000 to match the requested Codex WebSocket-style optimization.

## Folder Check

<pre>
week15/
|-- README.md          # required report
|-- img/               # detection screenshot
|-- code/              # required when camera bridge code exists
</pre>

## Environment

- Tailscale
- Python
- WebSocket-style local service address
- Mobile browser camera
- ArUco marker

## Steps

1. Connect phone and computer to Tailscale.
2. Start the camera bridge service.
3. Open ws://<tailscale-ip>:5000 from the mobile side or configure the service endpoint with WebSocket transport.
4. Allow camera permission and detect ArUco ID 0.

## Commands

<pre><code>cd ~/ai-robot-class.github.io
mkdir -p week15/img
python3 camera_bridge.py</code></pre>

## Result

<img src="img/result.jpeg" width="800" alt="ArUco detection result">

## Summary

The experiment shows how a mobile camera can become a robot vision input. Switching the documented endpoint style from HTTPS to WebSocket clarifies the intended real-time communication direction.

---

[Back to main archive](../README.md)
