#!/usr/bin/env python3
"""修复表格课程名称翻译"""
with open('index.html', 'r') as f:
    content = f.read()

translations = {
    # 课程名称
    "🤖 机器手交互 · AI 逻辑启蒙": "🤖 Robot Hand Interaction · AI Logic Basics",
    "🐕 机器狗感知 · OpenCV 视觉": "🐕 Robot Dog Perception · OpenCV Vision",
    "🎯 AI 奥林匹克冲刺年": "🎯 AI Olympiad Sprint Year",
    "🐕 机器狗感知 · OpenCV 视觉工程": "🐕 Robot Dog Perception · OpenCV Vision",
    "🏅 AI 奥林匹克冲刺年 · IOAI 全真模拟": "🏅 AI Olympiad Sprint · IOAI Full Simulation",
}

for cn, en in translations.items():
    content = content.replace(cn, en)

with open('index.html', 'w') as f:
    f.write(content)

print("✅ 表格课程名称翻译完成！")
