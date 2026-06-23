#!/bin/bash
# Week 1 - Environment Setup Script
echo "=== Git Configuration ==="
git config --global user.name "student"
git config --global user.email "student@example.com"
echo "=== SSH Key Generation ==="
ssh-keygen -t ed25519 -C "student@example.com" -f ~/.ssh/id_ed25519 -N ""
echo "=== Verify ==="
git config --list
ssh -T git@github.com
echo "=== Environment Ready ==="
