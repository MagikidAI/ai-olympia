#!/usr/bin/env python3
"""完整翻译脚本 - 第五轮翻译"""
with open('index.html', 'r') as f:
    content = f.read()

translations = {
    # 按钮
    "中文": "中/EN",

    # 标签
    "国际顶级": "International Top",
    "国际级": "International",
    "太空级": "Space Level",
    "科研级": "Research Level",
    "国家级": "National Level",
    "全球 hackathon": "Global Hackathon",
    "工业级平台": "Industrial Platform",

    # 年龄和类型标签
    "14–19岁": "Age 14-19",
    "国际赛": "Intl Competition",
    "24 节课时": "24 Training Hours",
    "14–18岁": "Age 14-18",
    "高中/大学预科": "High School/Pre-College",
    "高中": "High School",
    "18 节课时": "18 Training Hours",
    "15岁以上": "Age 15+",
    "研究与大学水平": "Research & College Level",
    "12 节课时": "12 Training Hours",
    "13–18岁": "Age 13-18",
    "国家级": "National Level",
    "14岁以上": "Age 14+",
}

for cn, en in translations.items():
    content = content.replace(cn, en)

with open('index.html', 'w') as f:
    f.write(content)

print("✅ 第五轮翻译完成！")
