#!/usr/bin/env python3
"""
合并中英文双语版本，添加切换按钮
"""
import re

# 读取两个版本
with open('index-en.html', 'r') as f:
    en_content = f.read()

with open('index.html', 'r') as f:
    cn_content = f.read()

# 创建合并版本 - 基于中文版，添加切换功能
merged = cn_content

# 1. 在<head>标签内添加切换脚本样式
toggle_script = '''
<style>
.lang-switcher {
  display: flex;
  background: rgba(255,255,255,0.1);
  border-radius: 20px;
  padding: 2px;
  gap: 2px;
}
.lang-btn {
  padding: 6px 14px;
  border: none;
  border-radius: 18px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  background: transparent;
  color: var(--text-dim);
}
.lang-btn.active {
  background: linear-gradient(135deg, var(--gold), #FFA000);
  color: #000;
}
</style>
<script>
const i18n = {
  // 导航
  nav_home: { zh: '首页', en: 'Home' },
  nav_course: { zh: '课程体系', en: 'Curriculum' },
  nav_schedule: { zh: '课程安排', en: 'Schedule' },
  nav_students: { zh: '学员成就', en: 'Students' },
  nav_competitions: { zh: '竞赛荣誉', en: 'Competitions' },
  nav_enroll: { zh: '立即报名', en: 'Enroll Now' },
  
  // Hero
  hero_badge: { zh: '🎓 MAGIKID 2026 精英计划', en: '🎓 MAGIKID 2026 Elite Program' },
  hero_title: { zh: 'MAGIKID AI 竞赛班', en: 'MAGIKID AI Competition Class' },
  hero_sub: { zh: '通往常春藤与斯坦福的AI竞技之路', en: 'Your Path to Ivy League & Stanford via AI Competition' },
  hero_desc: { zh: '培养下一代AI领袖，从这里开始', en: 'Cultivating Next-Gen AI Leaders' },
  hero_cta: { zh: '开启AI之旅', en: 'Start Your AI Journey' },
  hero_stats_students: { zh: '优秀学员', en: 'Elite Students' },
  hero_stats_medals: { zh: '国际奖项', en: 'Intl Medals' },
  hero_stats_top: { zh: '顶尖录取', en: 'Top Admissions' },
  hero_stats_nasa: { zh: 'NASA挑战', en: 'NASA Challenges' },
  
  // 课程体系
  course_title: { zh: '🚀 课程体系', en: '🚀 Curriculum System' },
  course_sub: { zh: '5阶段递进式AI精英培养', en: '5-Stage Progressive AI Elite Training' },
  course_explore: { zh: '探索者', en: 'Explorer' },
  course_innovator: { zh: '创新者', en: 'Innovator' },
  course_challenger: { zh: '挑战者', en: 'Challenger' },
  course_master: { zh: '大师', en: 'Master' },
  course_specialist: { zh: '专家', en: 'Specialist' },
  
  // 赛道表格
  track_title: { zh: '🎯 赛道 · 赛事 · 核心课程', en: '🎯 Track · Competition · Core Curriculum' },
  track_a: { zh: '赛道A：算法与奥赛类', en: 'Track A: Algorithm & Olympiad' },
  track_b: { zh: '赛道B：具身智能与机器人类', en: 'Track B: Embodied Intelligence & Robotics' },
  track_c: { zh: '赛道C：系统集成与黑客松类', en: 'Track C: System Integration & Hackathons' },
  track_col1: { zh: '赛道分类', en: 'Track' },
  track_col2: { zh: '目标赛事', en: 'Target Competitions' },
  track_col3: { zh: '核心依赖课程阶段', en: 'Prerequisite Courses' },
  track_col4: { zh: 'MAGIKID成就', en: 'MAGIKID Achievements' },
  
  // 学员荣耀
  gallery_title: { zh: '🌟 学员荣耀 2026', en: '🌟 Student Glory 2026' },
  gallery_world: { zh: '🏆 World Stage', en: '🏆 World Stage' },
  gallery_students: { zh: 'MAGIKID 赛队 · 全球 AI 竞赛现场', en: 'MAGIKID Teams · Global AI Competition' },
  gallery_achieve: { zh: '🏅 Achievement', en: '🏅 Achievement' },
  
  // 底部
  footer_join: { zh: '加入我们', en: 'Join Us' },
  footer_contact: { zh: '联系我们', en: 'Contact Us' },
  footer_location: { zh: '加州·硅谷 | 德州·达拉斯', en: 'California · Silicon Valley | Texas · Dallas' },
  footer_rights: { zh: '© 2026 MAGIKID Lab. All Rights Reserved.', en: '© 2026 MAGIKID Lab. All Rights Reserved.' },
  footer_note: { zh: 'MAGIKID Lab 保留法律追究权利', en: 'MAGIKID Lab reserves all legal rights' },
  
  // 移动端导航
  mob_home: { zh: '首页', en: 'Home' },
  mob_course: { zh: '课程', en: 'Course' },
  mob_students: { zh: '学员', en: 'Students' },
  mob_comp: { zh: '竞赛', en: 'Comp' },
  mob_enroll: { zh: '报名', en: 'Enroll' },
};

let currentLang = 'zh';

function switchLang(lang) {
  currentLang = lang;
  document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';
  
  // 更新按钮状态
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === lang);
  });
  
  // 更新所有带data-i18n的元素
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.dataset.i18n;
    if (i18n[key] && i18n[key][lang]) {
      el.textContent = i18n[key][lang];
    }
  });
  
  // 更新带data-i18n-html的元素（支持HTML）
  document.querySelectorAll('[data-i18n-html]').forEach(el => {
    const key = el.dataset.i18nHtml;
    if (i18n[key] && i18n[key][lang]) {
      el.innerHTML = i18n[key][lang];
    }
  });
  
  // 存储选择
  localStorage.setItem('magikid-lang', lang);
}

document.addEventListener('DOMContentLoaded', () => {
  // 恢复语言选择
  const saved = localStorage.getItem('magikid-lang');
  if (saved) {
    switchLang(saved);
  }
});
</script>
'''

# 在</head>前插入
merged = merged.replace('</head>', toggle_script + '</head>')

# 2. 在导航栏CTA前添加语言切换
nav_switch = '''
<div class="lang-switcher">
  <button class="lang-btn active" data-lang="zh" onclick="switchLang('zh')">中文</button>
  <button class="lang-btn" data-lang="en" onclick="switchLang('en')">EN</button>
</div>
'''
merged = merged.replace('<a href="#enroll" class="nav-cta"', nav_switch + '<a href="#enroll" class="nav-cta"')

# 3. 给关键文本添加data-i18n属性
# Hero section
merged = merged.replace('MAGIKID AI 竞赛班', '<span data-i18n="hero_title">MAGIKID AI 竞赛班</span>')
merged = merged.replace('通往常春藤与斯坦福的AI竞技之路', '<span data-i18n="hero_sub">通往常春藤与斯坦福的AI竞技之路</span>')
merged = merged.replace('培养下一代AI领袖，从这里开始', '<span data-i18n="hero_desc">培养下一代AI领袖，从这里开始</span>')
merged = merged.replace('开启AI之旅', '<span data-i18n="hero_cta">开启AI之旅</span>')

# 课程体系
merged = merged.replace('🚀 课程体系', '<span data-i18n="course_title">🚀 课程体系</span>')
merged = merged.replace('5阶段递进式AI精英培养', '<span data-i18n="course_sub">5阶段递进式AI精英培养</span>')

# 赛道表格标题
merged = merged.replace('🎯 赛道 · 赛事 · 核心课程', '<span data-i18n="track_title">🎯 赛道 · 赛事 · 核心课程</span>')

# 赛道名称
merged = merged.replace('赛道A：算法与奥赛类', '<span data-i18n="track_a">赛道A：算法与奥赛类</span>')
merged = merged.replace('赛道B：具身智能与机器人类', '<span data-i18n="track_b">赛道B：具身智能与机器人类</span>')
merged = merged.replace('赛道C：系统集成与黑客松类', '<span data-i18n="track_c">赛道C：系统集成与黑客松类</span>')

# 课程阶段
merged = merged.replace('探索者', '<span data-i18n="course_explore">探索者</span>')
merged = merged.replace('创新者', '<span data-i18n="course_innovator">创新者</span>')
merged = merged.replace('挑战者', '<span data-i18n="course_challenger">挑战者</span>')
merged = merged.replace('大师', '<span data-i18n="course_master">大师</span>')
merged = merged.replace('专家', '<span data-i18n="course_specialist">专家</span>')

# 表格列标题
merged = merged.replace('>赛道分类<', '><span data-i18n="track_col1">赛道分类</span><')
merged = merged.replace('>目标赛事<', '><span data-i18n="track_col2">目标赛事</span><')
merged = merged.replace('>核心依赖课程阶段<', '><span data-i18n="track_col3">核心依赖课程阶段</span><')
merged = merged.replace('>MAGIKID成就<', '><span data-i18n="track_col4">MAGIKID成就</span><')

# 学员荣耀
merged = merged.replace('🌟 学员荣耀 2026', '<span data-i18n="gallery_title">🌟 学员荣耀 2026</span>')
merged = merged.replace('🏆 World Stage', '<span data-i18n="gallery_world">🏆 World Stage</span>')
merged = merged.replace('MAGIKID 赛队 · 全球 AI 竞赛现场', '<span data-i18n="gallery_students">MAGIKID 赛队 · 全球 AI 竞赛现场</span>')

# 导航链接
merged = merged.replace('>首页<', '><span data-i18n="nav_home">首页</span><')
merged = merged.replace('>课程体系<', '><span data-i18n="nav_course">课程体系</span><')
merged = merged.replace('>课程安排<', '><span data-i18n="nav_schedule">课程安排</span><')
merged = merged.replace('>学员成就<', '><span data-i18n="nav_students">学员成就</span><')
merged = merged.replace('>竞赛荣誉<', '><span data-i18n="nav_competitions">竞赛荣誉</span><')
merged = merged.replace('>立即报名<', '><span data-i18n="nav_enroll">立即报名</span><')

# 底部
merged = merged.replace('加入我们', '<span data-i18n="footer_join">加入我们</span>')
merged = merged.replace('联系我们', '<span data-i18n="footer_contact">联系我们</span>')
merged = merged.replace('加州·硅谷 | 德州·达拉斯', '<span data-i18n="footer_location">加州·硅谷 | 德州·达拉斯</span>')
merged = merged.replace('MAGIKID Lab 保留法律追究权利', '<span data-i18n="footer_note">MAGIKID Lab 保留法律追究权利</span>')

# Hero统计数字标签
merged = merged.replace('>优秀学员<', '><span data-i18n="hero_stats_students">优秀学员</span><')
merged = merged.replace('>国际奖项<', '><span data-i18n="hero_stats_medals">国际奖项</span><')
merged = merged.replace('>顶尖录取<', '><span data-i18n="hero_stats_top">顶尖录取</span><')
merged = merged.replace('>NASA挑战<', '><span data-i18n="hero_stats_nasa">NASA挑战</span><')

# 移动端导航
merged = merged.replace('首页', '<span data-i18n="mob_home">首页</span>')
merged = merged.replace('课程', '<span data-i18n="mob_course">课程</span>')
merged = merged.replace('学员', '<span data-i18n="mob_students">学员</span>')
merged = merged.replace('竞赛', '<span data-i18n="mob_comp">竞赛</span>')
merged = merged.replace('报名', '<span data-i18n="mob_enroll">报名</span>')

# 保存
with open('index.html', 'w') as f:
    f.write(merged)

print("✅ 合并完成！已生成双语切换版本: index.html")
print("📍 预览: http://localhost:8899")
