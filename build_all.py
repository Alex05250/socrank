# -*- coding: utf-8 -*-
import json
import os

BASE_DIR = r"C:\Users\21458\Desktop\socrank"
with open(os.path.join(BASE_DIR, "final_chips.json"), "r", encoding="utf-8") as f:
    chips = json.load(f)

# Sortings
peak_sorted = sorted(chips, key=lambda x: x["overall"], reverse=True)
daily_sorted = sorted(chips, key=lambda x: x["daily_score"], reverse=True)

peak_ranks = {c["id"]: i + 1 for i, c in enumerate(peak_sorted)}
daily_ranks = {c["id"]: i + 1 for i, c in enumerate(daily_sorted)}

phone_count = len([c for c in chips if c["device_type"] == "phone"])
tablet_count = len([c for c in chips if c["device_type"] == "tablet"])
total_count = len(chips)
apple_count = len([c for c in chips if c["brand"] == "Apple"])
qc_count = len([c for c in chips if c["brand"] == "Qualcomm"])
mtk_count = len([c for c in chips if c["brand"] == "MediaTek"])
hisi_count = len([c for c in chips if c["brand"] == "HiSilicon"])
sam_count = len([c for c in chips if c["brand"] == "Samsung"])
goog_count = len([c for c in chips if c["brand"] == "Google"])
mi_count = len([c for c in chips if c["brand"] == "Xiaomi"])

# Cache-buster for data.js. A count-only token stays identical across data-only
# edits (e.g. filling in process/GPU), so browsers and the Pages CDN keep serving
# the stale dataset. Bind the version to the build time instead.
from datetime import datetime
data_version = f"{total_count}c-{datetime.now().strftime('%Y%m%d%H%M%S')}"

def get_navbar(active_page):
    home_act = "active" if active_page == "home" else ""
    daily_act = "active" if active_page == "daily" else ""
    peak_act = "active" if active_page == "peak" else ""

    return f"""
  <header class="site-header">
    <div class="nav-container">
      <a href="index.html" class="nav-brand">
        <span class="brand-icon">⚡</span>
        <span class="brand-title">SocRank</span>
        <span class="brand-badge">双轨综合天梯</span>
      </a>
      <nav class="nav-links">
        <a href="index.html" class="nav-item {home_act}">
          <span class="nav-icon">🏠</span> 首页概览
        </a>
        <a href="daily.html" class="nav-item {daily_act}">
          <span class="nav-icon">⚡</span> 日常流畅模式
        </a>
        <a href="peak.html" class="nav-item {peak_act}">
          <span class="nav-icon">🚀</span> 极限性能模式
        </a>
        <a href="https://github.com/Alex05250/socrank" target="_blank" rel="noopener" class="nav-item nav-gh">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
          GitHub
        </a>
      </nav>
    </div>
  </header>
"""

COMMON_CSS = """
    :root {
      --bg: #0b0f19;
      --card-bg: rgba(22, 30, 49, 0.72);
      --card-border: rgba(255, 255, 255, 0.08);
      --card-hover-border: rgba(56, 189, 248, 0.35);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --accent: #38bdf8;
      --accent-grad: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%);
      --daily-grad: linear-gradient(135deg, #10b981 0%, #06b6d4 100%);
      --peak-grad: linear-gradient(135deg, #f43f5e 0%, #fb923c 100%);
      --daily-accent: #10b981;
      --peak-accent: #f43f5e;
      --apple: #a855f7;
      --qualcomm: #ef4444;
      --mediatek: #f59e0b;
      --hisilicon: #ec4899;
      --samsung: #3b82f6;
      --google: #10b981;
      --xiaomi: #f97316;
      --other: #64748b;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    }

    body {
      background-color: var(--bg);
      background-image: 
        radial-gradient(at 0% 0%, rgba(56, 189, 248, 0.08) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(129, 140, 248, 0.07) 0px, transparent 50%),
        radial-gradient(at 50% 50%, rgba(15, 23, 42, 0.5) 0px, transparent 100%);
      background-attachment: fixed;
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    .site-header {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(11, 15, 25, 0.85);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--card-border);
      padding: 0 20px;
    }

    .nav-container {
      max-width: 1200px;
      margin: 0 auto;
      height: 64px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }

    .nav-brand {
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: inherit;
    }

    .brand-icon {
      font-size: 22px;
      filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.5));
    }

    .brand-title {
      font-size: 20px;
      font-weight: 800;
      letter-spacing: -0.5px;
      background: var(--accent-grad);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .brand-badge {
      font-size: 11px;
      background: rgba(255, 255, 255, 0.08);
      color: var(--text-muted);
      padding: 2px 8px;
      border-radius: 20px;
      border: 1px solid var(--card-border);
      font-weight: 500;
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .nav-item {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      border-radius: 8px;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 13px;
      font-weight: 500;
      transition: all 0.2s;
      border: 1px solid transparent;
    }

    .nav-item:hover {
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.05);
    }

    .nav-item.active {
      color: #fff;
      background: rgba(56, 189, 248, 0.12);
      border-color: rgba(56, 189, 248, 0.3);
      font-weight: 600;
    }

    .nav-gh {
      color: var(--text-dim);
      border: 1px solid var(--card-border);
      margin-left: 6px;
    }

    .nav-gh:hover {
      border-color: rgba(255, 255, 255, 0.2);
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 24px 16px 60px;
      flex: 1;
      width: 100%;
    }

    .mode-header {
      text-align: center;
      margin-bottom: 24px;
      position: relative;
    }

    .mode-tag-top {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
      margin-bottom: 12px;
    }

    .mode-tag-daily {
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }

    .mode-tag-peak {
      background: rgba(244, 63, 94, 0.15);
      color: #fb7185;
      border: 1px solid rgba(244, 63, 94, 0.3);
    }

    .page-title {
      font-size: 30px;
      font-weight: 800;
      letter-spacing: -0.5px;
      margin-bottom: 8px;
    }

    .page-title.daily-title {
      background: var(--daily-grad);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .page-title.peak-title {
      background: var(--peak-grad);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .page-desc {
      color: var(--text-muted);
      font-size: 14px;
      line-height: 1.6;
      max-width: 800px;
      margin: 0 auto;
    }

    .mode-switch-bar {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 12px 18px;
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      font-size: 13px;
      backdrop-filter: blur(12px);
    }

    .mode-switch-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s;
    }

    .btn-to-daily {
      background: rgba(16, 185, 129, 0.2);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.4);
    }
    .btn-to-daily:hover {
      background: rgba(16, 185, 129, 0.35);
      transform: translateX(2px);
    }

    .btn-to-peak {
      background: rgba(244, 63, 94, 0.2);
      color: #fb7185;
      border: 1px solid rgba(244, 63, 94, 0.4);
    }
    .btn-to-peak:hover {
      background: rgba(244, 63, 94, 0.35);
      transform: translateX(2px);
    }

    .formula-banner {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 14px 18px;
      margin-bottom: 20px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      font-size: 13px;
      backdrop-filter: blur(12px);
    }

    .formula-tag {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.04);
      padding: 5px 10px;
      border-radius: 6px;
      border: 1px solid rgba(255, 255, 255, 0.05);
    }

    .formula-tag b {
      color: var(--accent);
    }

    .controls {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 16px 18px;
      margin-bottom: 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      backdrop-filter: blur(12px);
    }

    .control-top-row {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
      justify-content: space-between;
    }

    .search-box {
      position: relative;
      flex: 1;
      min-width: 240px;
    }

    .search-box input {
      width: 100%;
      background: rgba(11, 15, 25, 0.85);
      border: 1px solid var(--card-border);
      border-radius: 8px;
      padding: 10px 14px;
      color: var(--text-main);
      font-size: 13px;
      outline: none;
      transition: all 0.2s;
    }

    .search-box input:focus {
      border-color: var(--accent);
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2);
    }

    .filter-row {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 10px;
      font-size: 12px;
    }

    .filter-label {
      color: var(--text-dim);
      font-weight: 600;
      width: 60px;
      flex-shrink: 0;
    }

    .filter-group {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }

    .filter-btn {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--card-border);
      color: var(--text-muted);
      padding: 5px 12px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s;
      user-select: none;
    }

    .filter-btn:hover {
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.09);
    }

    .filter-btn.active {
      background: var(--accent);
      color: #0b0f19;
      border-color: var(--accent);
      font-weight: 700;
    }

    .sort-group {
      display: flex;
      gap: 8px;
      align-items: center;
      font-size: 13px;
      color: var(--text-muted);
    }

    .sort-select {
      background: rgba(11, 15, 25, 0.85);
      border: 1px solid var(--card-border);
      border-radius: 8px;
      padding: 8px 12px;
      color: var(--text-main);
      font-size: 13px;
      outline: none;
      cursor: pointer;
    }

    .list-wrapper {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .chip-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 14px 18px;
      display: grid;
      grid-template-columns: 44px 250px 1fr 100px;
      align-items: center;
      gap: 16px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      cursor: pointer;
      backdrop-filter: blur(12px);
    }

    .chip-card:hover {
      border-color: var(--card-hover-border);
      transform: translateY(-1px);
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }

    .chip-card.baseline {
      border: 1px dashed rgba(236, 72, 153, 0.5);
      background: rgba(236, 72, 153, 0.05);
    }

    .rank-num {
      font-size: 16px;
      font-weight: 800;
      color: var(--text-dim);
      text-align: center;
      line-height: 1;
    }

    .rank-1 { color: #fbbf24; text-shadow: 0 0 10px rgba(251, 191, 36, 0.5); font-size: 20px; }
    .rank-2 { color: #94a3b8; text-shadow: 0 0 10px rgba(148, 163, 184, 0.5); font-size: 18px; }
    .rank-3 { color: #d97706; text-shadow: 0 0 10px rgba(217, 119, 6, 0.5); font-size: 18px; }

    .chip-info {
      display: flex;
      flex-direction: column;
      gap: 4px;
      overflow: hidden;
    }

    .chip-name-row {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }

    .chip-name {
      font-size: 15px;
      font-weight: 700;
      color: var(--text-main);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .brand-badge {
      font-size: 10px;
      padding: 1px 6px;
      border-radius: 4px;
      font-weight: 600;
      letter-spacing: 0.2px;
    }

    .brand-Apple { background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.3); }
    .brand-Qualcomm { background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); }
    .brand-MediaTek { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }
    .brand-HiSilicon { background: rgba(236, 72, 153, 0.15); color: #f472b6; border: 1px solid rgba(236, 72, 153, 0.3); }
    .brand-Samsung { background: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.3); }
    .brand-Google { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); }
    .brand-Xiaomi { background: rgba(249, 115, 22, 0.15); color: #fb923c; border: 1px solid rgba(249, 115, 22, 0.3); }

    .device-badge {
      font-size: 10px;
      padding: 1px 5px;
      border-radius: 4px;
      font-weight: 600;
    }

    .badge-tablet-only {
      background: rgba(168, 85, 247, 0.2);
      color: #e9d5ff;
      border: 1px solid rgba(168, 85, 247, 0.4);
    }

    .badge-phone-only {
      background: rgba(56, 189, 248, 0.12);
      color: #7dd3fc;
      border: 1px solid rgba(56, 189, 248, 0.25);
    }

    .chip-meta {
      font-size: 12px;
      color: var(--text-dim);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .year-tag {
      color: var(--text-muted);
    }

    .bars-container {
      display: flex;
      flex-direction: column;
      gap: 6px;
      min-width: 0;
    }

    .bar-item {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .bar-label {
      font-size: 11px;
      color: var(--text-dim);
      width: 60px;
      text-align: right;
      flex-shrink: 0;
    }

    .bar-track {
      flex: 1;
      height: 6px;
      background: rgba(255, 255, 255, 0.06);
      border-radius: 4px;
      overflow: hidden;
      position: relative;
    }

    .bar-fill {
      height: 100%;
      border-radius: 4px;
      transition: width 0.4s ease;
    }

    .bar-fill.overall-daily {
      background: var(--daily-grad);
    }

    .bar-fill.overall-peak {
      background: var(--peak-grad);
    }

    .bar-fill.cpu-single {
      background: linear-gradient(90deg, #38bdf8 0%, #818cf8 100%);
    }

    .bar-fill.cpu-multi {
      background: linear-gradient(90deg, #f59e0b 0%, #ef4444 100%);
    }

    .bar-fill.cpu {
      background: linear-gradient(90deg, #38bdf8 0%, #3b82f6 100%);
    }

    .bar-fill.gpu {
      background: linear-gradient(90deg, #10b981 0%, #06b6d4 100%);
    }

    .bar-val {
      font-size: 11px;
      font-weight: 600;
      color: var(--text-muted);
      width: 44px;
      text-align: right;
      font-variant-numeric: tabular-nums;
      flex-shrink: 0;
    }

    .score-box {
      text-align: right;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    .score-main {
      font-size: 22px;
      font-weight: 800;
      line-height: 1.1;
      font-variant-numeric: tabular-nums;
    }

    .score-main.daily-score-color {
      color: #34d399;
    }

    .score-main.peak-score-color {
      color: #fb7185;
    }

    .score-unit {
      font-size: 11px;
      color: var(--text-dim);
      margin-top: 2px;
    }

    .chip-drawer {
      grid-column: 1 / -1;
      display: none;
      padding-top: 12px;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      margin-top: 8px;
    }

    .chip-card.expanded .chip-drawer {
      display: block;
    }

    .detail-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 12px;
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.6;
    }

    .detail-card {
      background: rgba(11, 15, 25, 0.5);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 8px;
      padding: 10px 14px;
    }

    .detail-card strong {
      display: block;
      color: var(--text-main);
      margin-bottom: 4px;
      font-size: 12px;
    }

    footer {
      text-align: center;
      padding: 30px 20px;
      color: var(--text-dim);
      font-size: 13px;
      border-top: 1px solid var(--card-border);
      background: rgba(11, 15, 25, 0.6);
      margin-top: auto;
    }

    footer a {
      color: var(--accent);
      text-decoration: none;
    }

    @media (max-width: 860px) {
      .chip-card {
        grid-template-columns: 36px 1fr 80px;
        gap: 10px;
        padding: 12px 14px;
      }
      .bars-container {
        grid-column: 1 / -1;
        order: 3;
        margin-top: 4px;
      }
      .score-box {
        order: 2;
      }
      .score-main {
        font-size: 18px;
      }
      .nav-links .nav-icon {
        display: none;
      }
      .nav-brand .brand-badge {
        display: none;
      }
      .filter-label {
        width: 100%;
        margin-bottom: 2px;
      }
    }
"""

def get_filter_controls(mode):
    return f"""
    <div class="controls">
      <div class="control-top-row">
        <div class="search-box">
          <input type="text" id="searchInput" placeholder="搜索型号、厂商或平台版本 (如 天玑 9400 平板, 骁龙 8 Gen 3, iPad M4)...">
        </div>
        <div class="sort-group">
          <span>排序:</span>
          <select class="sort-select" id="sortSelect">
            {"<option value='daily'>日常综合评分 (高到低)</option>" if mode == "daily" else "<option value='overall'>极限综合评分 (高到低)</option>"}
            {"<option value='cpu'>CPU 性能 (高到低)</option>" if mode == "peak" else ""}
            <option value="gb6s">GB6 单核 (高到低)</option>
            <option value="gb6m">GB6 多核 (高到低)</option>
            <option value="gpu">GPU 性能 (高到低)</option>
            <option value="year">发布年份 (新到旧)</option>
          </select>
        </div>
      </div>

      <div class="filter-row">
        <div class="filter-label">设备形态:</div>
        <div class="filter-group" id="deviceFilters">
          <button class="filter-btn active" data-device="all">🌐 全形态通榜 ({total_count})</button>
          <button class="filter-btn" data-device="phone">📱 智能手机 ({phone_count})</button>
          <button class="filter-btn" data-device="tablet">📟 平板 / 跨界 ({tablet_count})</button>
        </div>
      </div>

      <div class="filter-row">
        <div class="filter-label">厂商平台:</div>
        <div class="filter-group" id="brandFilters">
          <button class="filter-btn active" data-brand="all">全部厂商</button>
          <button class="filter-btn" data-brand="Apple">苹果</button>
          <button class="filter-btn" data-brand="Qualcomm">高通骁龙</button>
          <button class="filter-btn" data-brand="MediaTek">联发科天玑</button>
          <button class="filter-btn" data-brand="HiSilicon">华为麒麟</button>
          <button class="filter-btn" data-brand="Samsung">三星 Exynos</button>
          <button class="filter-btn" data-brand="Google">谷歌 Tensor</button>
          <button class="filter-btn" data-brand="Xiaomi">小米玄戒</button>
        </div>
      </div>
    </div>
"""

# Daily JS Logic
daily_js = """
    let currentDevice = 'all';
    let currentFilter = 'all';
    let currentSort = 'daily';
    let searchQuery = '';

    const listContainer = document.getElementById('chipList');
    const searchInput = document.getElementById('searchInput');
    const deviceFilters = document.getElementById('deviceFilters');
    const brandFilters = document.getElementById('brandFilters');
    const sortSelect = document.getElementById('sortSelect');

    function renderList() {
      const data = window.CHIPS_DATA || [];
      const maxDaily = Math.max(...data.map(c => c.daily_score));
      const maxS = Math.max(...data.map(c => c.gb6s_norm));
      const maxM = Math.max(...data.map(c => c.gb6m_norm));
      const maxGPU = Math.max(...data.map(c => c.gpu_score));

      let filtered = data.filter(chip => {
        // 设备形态过滤
        let matchDevice = (currentDevice === 'all') || (chip.device_type === currentDevice);

        // 品牌过滤
        const matchBrand = (currentFilter === 'all') || (chip.brand === currentFilter);

        // 搜索 (无缝支持中英文、去空格匹配及形态别名)
        const q = searchQuery.trim().toLowerCase().replace(/\s+/g, '');
        const haystack = (chip.name_cn + ' ' + chip.name + ' ' + chip.brand_cn + ' ' + chip.brand + ' ' + (chip.gpu || '') + ' ' + (chip.year || '') + ' ' + (chip.device_type === 'tablet' ? '平板 跨界' : '手机')).toLowerCase().replace(/\s+/g, '');
        const matchSearch = !q || haystack.includes(q);

        return matchDevice && matchBrand && matchSearch;
      });

      filtered.sort((a, b) => {
        if (currentSort === 'daily') return b.daily_score - a.daily_score;
        if (currentSort === 'gb6s') return b.gb6s - a.gb6s;
        if (currentSort === 'gb6m') return b.gb6m - a.gb6m;
        if (currentSort === 'gpu') return b.gpu_score - a.gpu_score;
        if (currentSort === 'year') return (b.year || 0) - (a.year || 0);
        return 0;
      });

      listContainer.innerHTML = '';
      if (filtered.length === 0) {
        listContainer.innerHTML = '<div style="text-align:center; padding: 40px; color: var(--text-muted);">未找到符合条件的芯片</div>';
        return;
      }

      filtered.forEach((chip, index) => {
        const isBaseline = chip.id === "hisilicon-kirin-9000";
        const rankClass = index === 0 ? 'rank-1' : (index === 1 ? 'rank-2' : (index === 2 ? 'rank-3' : ''));
        
        let deviceBadge = chip.device_type === 'tablet' 
          ? '<span class="device-badge badge-tablet-only">📟 平板端</span>'
          : '<span class="device-badge badge-phone-only">📱 手机端</span>';

        const card = document.createElement('div');
        card.className = `chip-card ${isBaseline ? 'baseline' : ''}`;
        card.innerHTML = `
          <div class="rank-num ${rankClass}">${index + 1}</div>
          <div class="chip-info">
            <div class="chip-name-row">
              <span class="chip-name" title="${chip.name_cn} (${chip.name})">${chip.name_cn}</span>
              <span class="brand-badge brand-${chip.brand}">${chip.brand_cn}</span>
              ${deviceBadge}
              ${isBaseline ? '<span style="font-size:10px; background:#ec4899; color:#fff; padding:1px 5px; border-radius:3px; font-weight:bold;">100基准</span>' : ''}
            </div>
            <div class="chip-meta">
              <span class="year-tag">${chip.year ? chip.year + '年' : '年份待核'}</span>
              <span>•</span>
              <span>${chip.process || '工艺未知'}</span>
              <span>•</span>
              <span>${chip.gpu || 'GPU 未知'}</span>
            </div>
          </div>
          <div class="bars-container">
            <div class="bar-item">
              <span class="bar-label">日常综合</span>
              <div class="bar-track">
                <div class="bar-fill overall-daily" style="width: ${(chip.daily_score / maxDaily * 100).toFixed(1)}%"></div>
              </div>
              <span class="bar-val">${chip.daily_score.toFixed(1)}</span>
            </div>
            <div class="bar-item">
              <span class="bar-label">单核 60%</span>
              <div class="bar-track">
                <div class="bar-fill cpu-single" style="width: ${(chip.gb6s_norm / maxS * 100).toFixed(1)}%"></div>
              </div>
              <span class="bar-val">${chip.gb6s_norm.toFixed(1)}</span>
            </div>
            <div class="bar-item">
              <span class="bar-label">多核 20%</span>
              <div class="bar-track">
                <div class="bar-fill cpu-multi" style="width: ${(chip.gb6m_norm / maxM * 100).toFixed(1)}%"></div>
              </div>
              <span class="bar-val">${chip.gb6m_norm.toFixed(1)}</span>
            </div>
            <div class="bar-item">
              <span class="bar-label">GPU 20%</span>
              <div class="bar-track">
                <div class="bar-fill gpu" style="width: ${(chip.gpu_score / maxGPU * 100).toFixed(1)}%"></div>
              </div>
              <span class="bar-val">${chip.gpu_score.toFixed(1)}</span>
            </div>
          </div>
          <div class="score-box">
            <div class="score-main daily-score-color">${chip.daily_score.toFixed(1)}</div>
            <div class="score-unit">日常流畅指数</div>
          </div>
          <div class="chip-drawer">
            <div class="detail-grid">
              <div class="detail-card">
                <strong>CPU 体验基准 (权重 80%)</strong>
                单核实测: ${chip.gb6s} 分 (归一化 ${chip.gb6s_norm} 分 · 权 60%)<br>
                多核实测: ${chip.gb6m} 分 (归一化 ${chip.gb6m_norm} 分 · 权 20%)<br>
                <em>大核瞬时爆发主导秒开与滑动掉帧率</em>
              </div>
              <div class="detail-card">
                <strong>GPU 图形基准 (权重 20%)</strong>
                ${chip.wle_raw ? `3DMark WLE 原生: ${chip.wle_raw} 分<br>` : ''}
                ${chip.snl_raw ? `3DMark SNL: ${chip.snl_raw} 分<br>` : ''}
                WLE 当量: ${Math.round(chip.wle_equiv)} 分 (${chip.gpu_method})<br>
                GPU 归一化分: ${chip.gpu_score} 分 (权 20%)
              </div>
              <div class="detail-card">
                <strong>形态与计算拆解</strong>
                ${chip.platform_note ? `<b>平台调校:</b> ${chip.platform_note}<br>` : ''}
                加权公式: ${chip.gb6s_norm}×0.6 + ${chip.gb6m_norm}×0.2 + ${chip.gpu_score}×0.2<br>
                = <strong>${chip.daily_score}</strong> 分 (基准 华为麒麟9000(手机) = 100.0)
              </div>
            </div>
          </div>
        `;

        card.addEventListener('click', () => {
          card.classList.toggle('expanded');
        });

        listContainer.appendChild(card);
      });
    }

    deviceFilters.addEventListener('click', (e) => {
      if (e.target.classList.contains('filter-btn')) {
        deviceFilters.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
        e.target.classList.add('active');
        currentDevice = e.target.dataset.device;
        renderList();
      }
    });

    brandFilters.addEventListener('click', (e) => {
      if (e.target.classList.contains('filter-btn')) {
        brandFilters.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
        e.target.classList.add('active');
        currentFilter = e.target.dataset.brand;
        renderList();
      }
    });

    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value;
      renderList();
    });

    sortSelect.addEventListener('change', (e) => {
      currentSort = e.target.value;
      renderList();
    });

    renderList();
"""

daily_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>日常流畅模式 (Daily Fluidity) - 移动端 SoC 综合天梯榜</title>
  <style>
{COMMON_CSS}
  </style>
</head>
<body>
{get_navbar('daily')}

  <div class="container">
    <div class="mode-header">
      <div class="mode-tag-top mode-tag-daily">🍃 贴近真实日常 · 拒绝烤机虚标</div>
      <h1 class="page-title daily-title">日常流畅模式 (Daily Fluidity Profile)</h1>
      <p class="page-desc">以单核大核瞬时爆发为核心，真实反映应用冷启动、手势打断与滑动掉帧表现。全面细分「手机端」与「平板端」真实跑分释放差距。</p>
    </div>

    <div class="mode-switch-bar">
      <span>🔥 想要查看全核满载、极客烤机与 3DMark 图形极限压榨？</span>
      <a href="peak.html" class="mode-switch-btn btn-to-peak">切换至 极限性能模式 →</a>
    </div>

    <div class="formula-banner">
      <div class="formula-tag"><b>基准</b> 华为麒麟 9000 (手机) = 100 分</div>
      <div class="formula-tag"><b>综合权重</b> GB6 单核 60% + GB6 多核 20% + GPU 20%</div>
      <div class="formula-tag"><b>单核锚点</b> 贴合 3.5W~5W 日用甜点区</div>
      <div class="formula-tag"><b>收录范围</b> 手机 & 平板细分核心 ({total_count}款)</div>
    </div>

{get_filter_controls('daily')}

    <div class="list-wrapper" id="chipList">
      <!-- Generated by JS -->
    </div>
  </div>

  <footer>
    <p>SocRank 数据源基于主流跑分实测及实验室样本归一化整理 · <a href="https://github.com/Alex05250/socrank" target="_blank">GitHub 开源</a></p>
  </footer>

  <script src="data.js?v={data_version}"></script>
  <script>
{daily_js}
  </script>
</body>
</html>
"""

# Peak JS Logic
peak_js = """
    let currentDevice = 'all';
    let currentFilter = 'all';
    let currentSort = 'overall';
    let searchQuery = '';

    const listContainer = document.getElementById('chipList');
    const searchInput = document.getElementById('searchInput');
    const deviceFilters = document.getElementById('deviceFilters');
    const brandFilters = document.getElementById('brandFilters');
    const sortSelect = document.getElementById('sortSelect');

    function renderList() {
      const data = window.CHIPS_DATA || [];
      const maxOverall = Math.max(...data.map(c => c.overall));
      const maxCPU = Math.max(...data.map(c => c.cpu_score));
      const maxGPU = Math.max(...data.map(c => c.gpu_score));

      let filtered = data.filter(chip => {
        // 设备形态过滤
        let matchDevice = (currentDevice === 'all') || (chip.device_type === currentDevice);

        // 品牌过滤
        const matchBrand = (currentFilter === 'all') || (chip.brand === currentFilter);

        // 搜索 (无缝支持中英文、去空格匹配及形态别名)
        const q = searchQuery.trim().toLowerCase().replace(/\s+/g, '');
        const haystack = (chip.name_cn + ' ' + chip.name + ' ' + chip.brand_cn + ' ' + chip.brand + ' ' + (chip.gpu || '') + ' ' + (chip.year || '') + ' ' + (chip.device_type === 'tablet' ? '平板 跨界' : '手机')).toLowerCase().replace(/\s+/g, '');
        const matchSearch = !q || haystack.includes(q);

        return matchDevice && matchBrand && matchSearch;
      });

      filtered.sort((a, b) => {
        if (currentSort === 'overall') return b.overall - a.overall;
        if (currentSort === 'cpu') return b.cpu_score - a.cpu_score;
        if (currentSort === 'gpu') return b.gpu_score - a.gpu_score;
        if (currentSort === 'gb6s') return b.gb6s - a.gb6s;
        if (currentSort === 'gb6m') return b.gb6m - a.gb6m;
        if (currentSort === 'year') return (b.year || 0) - (a.year || 0);
        return 0;
      });

      listContainer.innerHTML = '';
      if (filtered.length === 0) {
        listContainer.innerHTML = '<div style="text-align:center; padding: 40px; color: var(--text-muted);">未找到符合条件的芯片</div>';
        return;
      }

      filtered.forEach((chip, index) => {
        const isBaseline = chip.id === "hisilicon-kirin-9000";
        const rankClass = index === 0 ? 'rank-1' : (index === 1 ? 'rank-2' : (index === 2 ? 'rank-3' : ''));
        
        let deviceBadge = chip.device_type === 'tablet' 
          ? '<span class="device-badge badge-tablet-only">📟 平板端</span>'
          : '<span class="device-badge badge-phone-only">📱 手机端</span>';

        const card = document.createElement('div');
        card.className = `chip-card ${isBaseline ? 'baseline' : ''}`;
        card.innerHTML = `
          <div class="rank-num ${rankClass}">${index + 1}</div>
          <div class="chip-info">
            <div class="chip-name-row">
              <span class="chip-name" title="${chip.name_cn} (${chip.name})">${chip.name_cn}</span>
              <span class="brand-badge brand-${chip.brand}">${chip.brand_cn}</span>
              ${deviceBadge}
              ${isBaseline ? '<span style="font-size:10px; background:#ec4899; color:#fff; padding:1px 5px; border-radius:3px; font-weight:bold;">100基准</span>' : ''}
            </div>
            <div class="chip-meta">
              <span class="year-tag">${chip.year ? chip.year + '年' : '年份待核'}</span>
              <span>•</span>
              <span>${chip.process || '工艺未知'}</span>
              <span>•</span>
              <span>${chip.gpu || 'GPU 未知'}</span>
            </div>
          </div>
          <div class="bars-container">
            <div class="bar-item">
              <span class="bar-label">极限综合</span>
              <div class="bar-track">
                <div class="bar-fill overall-peak" style="width: ${(chip.overall / maxOverall * 100).toFixed(1)}%"></div>
              </div>
              <span class="bar-val">${chip.overall.toFixed(1)}</span>
            </div>
            <div class="bar-item">
              <span class="bar-label">CPU 60%</span>
              <div class="bar-track">
                <div class="bar-fill cpu" style="width: ${(chip.cpu_score / maxCPU * 100).toFixed(1)}%"></div>
              </div>
              <span class="bar-val">${chip.cpu_score.toFixed(1)}</span>
            </div>
            <div class="bar-item">
              <span class="bar-label">GPU 40%</span>
              <div class="bar-track">
                <div class="bar-fill gpu" style="width: ${(chip.gpu_score / maxGPU * 100).toFixed(1)}%"></div>
              </div>
              <span class="bar-val">${chip.gpu_score.toFixed(1)}</span>
            </div>
          </div>
          <div class="score-box">
            <div class="score-main peak-score-color">${chip.overall.toFixed(1)}</div>
            <div class="score-unit">极限性能指数</div>
          </div>
          <div class="chip-drawer">
            <div class="detail-grid">
              <div class="detail-card">
                <strong>CPU Geekbench 6 详情 (60% 综合权重)</strong>
                单核: ${chip.gb6s} 分 · 多核: ${chip.gb6m} 分<br>
                CPU 归一化分: ${chip.cpu_score} 分 (单30% + 多70%)
              </div>
              <div class="detail-card">
                <strong>GPU 图形测试详情 (40% 综合权重)</strong>
                ${chip.wle_raw ? `3DMark WLE 原生: ${chip.wle_raw} 分<br>` : ''}
                ${chip.snl_raw ? `3DMark Steel Nomad Light: ${chip.snl_raw} 分<br>` : ''}
                WLE 当量: ${Math.round(chip.wle_equiv)} 分 (${chip.gpu_method})<br>
                GPU 归一化分: ${chip.gpu_score} 分
              </div>
              <div class="detail-card">
                <strong>形态与极限性能计算拆解</strong>
                ${chip.platform_note ? `<b>平台调校:</b> ${chip.platform_note}<br>` : ''}
                极限公式: ${chip.cpu_score} × 0.60 + ${chip.gpu_score} × 0.40<br>
                = <strong>${chip.overall}</strong> 分 (基准 华为麒麟9000(手机) = 100.0)
              </div>
            </div>
          </div>
        `;

        card.addEventListener('click', () => {
          card.classList.toggle('expanded');
        });

        listContainer.appendChild(card);
      });
    }

    deviceFilters.addEventListener('click', (e) => {
      if (e.target.classList.contains('filter-btn')) {
        deviceFilters.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
        e.target.classList.add('active');
        currentDevice = e.target.dataset.device;
        renderList();
      }
    });

    brandFilters.addEventListener('click', (e) => {
      if (e.target.classList.contains('filter-btn')) {
        brandFilters.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
        e.target.classList.add('active');
        currentFilter = e.target.dataset.brand;
        renderList();
      }
    });

    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value;
      renderList();
    });

    sortSelect.addEventListener('change', (e) => {
      currentSort = e.target.value;
      renderList();
    });

    renderList();
"""

peak_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>极限性能模式 (Peak Performance) - 移动端 SoC 综合天梯榜</title>
  <style>
{COMMON_CSS}
  </style>
</head>
<body>
{get_navbar('peak')}

  <div class="container">
    <div class="mode-header">
      <div class="mode-tag-top mode-tag-peak">🔥 极致性能释放 · 极客压榨天花板</div>
      <h1 class="page-title peak-title">极限性能模式 (Peak Performance Profile)</h1>
      <p class="page-desc">展现芯片在全核狂飙、极限游戏与 3DMark 烤机下的绝对算力释放，衡量芯片架构与制程的极限物理天花板。支持手机与平板独立筛选。</p>
    </div>

    <div class="mode-switch-bar">
      <span>⚡ 想要更贴近被动散热日常使用、应用秒开与滑动掉帧表现？</span>
      <a href="daily.html" class="mode-switch-btn btn-to-daily">切换至 日常流畅模式 →</a>
    </div>

    <div class="formula-banner">
      <div class="formula-tag"><b>基准</b> 华为麒麟 9000 (手机) = 100 分</div>
      <div class="formula-tag"><b>综合权重</b> CPU 60% + GPU 40%</div>
      <div class="formula-tag"><b>CPU 内部</b> 单核 30% + 多核 70% (GB6)</div>
      <div class="formula-tag"><b>GPU 测标</b> 3DMark WLE (新架构按 SNL 当量折算)</div>
      <div class="formula-tag"><b>收录范围</b> 手机 & 平板细分核心 ({total_count}款)</div>
    </div>

{get_filter_controls('peak')}

    <div class="list-wrapper" id="chipList">
      <!-- Generated by JS -->
    </div>
  </div>

  <footer>
    <p>SocRank 数据源基于主流跑分实测及实验室样本归一化整理 · <a href="https://github.com/Alex05250/socrank" target="_blank">GitHub 开源</a></p>
  </footer>

  <script src="data.js?v={data_version}"></script>
  <script>
{peak_js}
  </script>
</body>
</html>
"""

# Portal index.html
focus_cids = [
    "apple-a20-pro",
    "apple-m5-ipad",
    "xiaomi-xring-o3-tablet",
    "xiaomi-xring-o3",
    "apple-m4-ipad",
    "mediatek-dimensity-9400-tablet",
    "mediatek-dimensity-9400",
    "qualcomm-snapdragon-8-gen-3-tablet",
    "qualcomm-snapdragon-8-gen-3",
    "hisilicon-kirin-9050-pro",
    "apple-a17-pro",
    "apple-a17-pro-tablet",
    "apple-a15-bionic",
    "apple-a15-bionic-tablet",
    "hisilicon-kirin-9030",
    "hisilicon-kirin-9000",
    "hisilicon-kirin-9000-tablet"
]

table_rows = []
for cid in focus_cids:
    c = next(x for x in chips if x["id"] == cid)
    pr = peak_ranks[cid]
    dr = daily_ranks[cid]
    diff = pr - dr
    if diff > 0:
        shift_badge = f'<span style="color:#34d399; font-weight:700;">↑ +{diff} (日常跃升)</span>'
    elif diff < 0:
        shift_badge = f'<span style="color:#fb7185; font-weight:600;">↓ {abs(diff)} (烤机挤水)</span>'
    else:
        shift_badge = '<span style="color:#94a3b8;">= 锚定持平</span>'
    
    is_base = c['id'] == "hisilicon-kirin-9000"
    tr_style = 'style="background:rgba(236,72,153,0.06);"' if is_base else ""
    base_badge = '<span style="font-size:10px; background:#ec4899; color:#fff; padding:1px 5px; border-radius:3px; font-weight:bold; margin-left:4px;">100基准</span>' if is_base else ''

    device_tag = '<span class="device-badge badge-tablet-only" style="margin-left:4px;">📟 平板</span>' if c['device_type'] == 'tablet' else '<span class="device-badge badge-phone-only" style="margin-left:4px;">📱 手机</span>'

    table_rows.append(f"""
        <tr {tr_style}>
          <td style="padding:12px 14px; font-weight:700; white-space:nowrap;">
            {c['name_cn']}
            <span class="brand-badge brand-{c['brand']}" style="margin-left:6px;">{c['brand_cn']}</span>
            {device_tag}
            {base_badge}
          </td>
          <td style="padding:12px 14px; text-align:center;">#{dr} (<b style="color:#34d399;">{c['daily_score']}</b>)</td>
          <td style="padding:12px 14px; text-align:center;">#{pr} (<b style="color:#fb7185;">{c['overall']}</b>)</td>
          <td style="padding:12px 14px; text-align:center;">{shift_badge}</td>
          <td style="padding:12px 14px; color:var(--text-dim); font-size:12px;">GB6单: {c['gb6s']} · 多: {c['gb6m']} · 当量: {round(c['wle_equiv'])}</td>
        </tr>
    """)

table_html = "\n".join(table_rows)

index_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SocRank 移动与平板 SoC 双轨综合性能天梯榜</title>
  <style>
{COMMON_CSS}

    .hero {{
      text-align: center;
      padding: 40px 10px 30px;
      max-width: 900px;
      margin: 0 auto;
    }}

    .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
      background: rgba(56, 189, 248, 0.12);
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.3);
      margin-bottom: 16px;
    }}

    .hero-title {{
      font-size: 38px;
      font-weight: 800;
      letter-spacing: -1px;
      line-height: 1.2;
      margin-bottom: 16px;
      background: linear-gradient(135deg, #ffffff 30%, #94a3b8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .hero-sub {{
      font-size: 16px;
      line-height: 1.7;
      color: var(--text-muted);
      max-width: 780px;
      margin: 0 auto 36px;
    }}

    .portal-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 24px;
      margin-bottom: 48px;
    }}

    .portal-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 18px;
      padding: 28px 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      backdrop-filter: blur(16px);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      overflow: hidden;
    }}

    .portal-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
    }}

    .portal-card.card-daily::before {{
      background: var(--daily-grad);
    }}

    .portal-card.card-peak::before {{
      background: var(--peak-grad);
    }}

    .portal-card:hover {{
      transform: translateY(-4px);
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.4);
    }}

    .portal-card.card-daily:hover {{
      border-color: rgba(16, 185, 129, 0.4);
    }}

    .portal-card.card-peak:hover {{
      border-color: rgba(244, 63, 94, 0.4);
    }}

    .portal-header {{
      margin-bottom: 18px;
    }}

    .portal-badge {{
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 6px;
      margin-bottom: 12px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .badge-daily {{
      background: rgba(16, 185, 129, 0.2);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.4);
    }}

    .badge-peak {{
      background: rgba(244, 63, 94, 0.2);
      color: #fb7185;
      border: 1px solid rgba(244, 63, 94, 0.4);
    }}

    .portal-title {{
      font-size: 24px;
      font-weight: 800;
      margin-bottom: 8px;
    }}

    .portal-formula {{
      font-size: 13px;
      color: var(--accent);
      font-weight: 600;
      margin-bottom: 12px;
    }}

    .portal-desc {{
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.6;
      margin-bottom: 20px;
    }}

    .preview-list {{
      background: rgba(11, 15, 25, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 12px;
      padding: 12px 16px;
      margin-bottom: 24px;
    }}

    .preview-title {{
      font-size: 11px;
      font-weight: 700;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
    }}

    .preview-item {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 5px 0;
      font-size: 13px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.03);
    }}

    .preview-item:last-child {{
      border-bottom: none;
    }}

    .preview-score {{
      font-weight: 700;
      font-variant-numeric: tabular-nums;
    }}

    .portal-btn {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 12px 20px;
      border-radius: 10px;
      text-decoration: none;
      font-size: 14px;
      font-weight: 700;
      transition: all 0.2s;
    }}

    .btn-daily-cta {{
      background: var(--daily-grad);
      color: #0b0f19;
      box-shadow: 0 4px 16px rgba(16, 185, 129, 0.3);
    }}
    .btn-daily-cta:hover {{
      box-shadow: 0 6px 20px rgba(16, 185, 129, 0.5);
      filter: brightness(1.1);
    }}

    .btn-peak-cta {{
      background: var(--peak-grad);
      color: #fff;
      box-shadow: 0 4px 16px rgba(244, 63, 94, 0.3);
    }}
    .btn-peak-cta:hover {{
      box-shadow: 0 6px 20px rgba(244, 63, 94, 0.5);
      filter: brightness(1.1);
    }}

    .section-block {{
      margin-bottom: 48px;
    }}

    .section-title {{
      font-size: 22px;
      font-weight: 800;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .methods-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
    }}

    .method-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 20px;
      backdrop-filter: blur(12px);
    }}

    .method-icon {{
      font-size: 26px;
      margin-bottom: 12px;
    }}

    .method-card h3 {{
      font-size: 16px;
      font-weight: 700;
      margin-bottom: 8px;
      color: var(--text-main);
    }}

    .method-card p {{
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.6;
    }}

    .table-container {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      overflow-x: auto;
      backdrop-filter: blur(12px);
    }}

    .comp-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
    }}

    .comp-table th {{
      background: rgba(255, 255, 255, 0.04);
      padding: 12px 14px;
      text-align: left;
      font-weight: 600;
      color: var(--text-dim);
      border-bottom: 1px solid var(--card-border);
    }}

    .comp-table td {{
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
    }}

    .comp-table tr:hover {{
      background: rgba(255, 255, 255, 0.02);
    }}
  </style>
</head>
<body>
{get_navbar('home')}

  <div class="container">
    <section class="hero">
      <div class="hero-badge">移动与平板 SoC 双轨评测体系 · 2026 深度细分 {total_count} 款核心</div>
      <h1 class="hero-title">移动端 SoC 综合性能天梯榜</h1>
      <p class="hero-sub">拒绝 15W 烤机虚标 · 还原「日常流畅 4W 甜点」与「极限性能压榨」的双重视角。<br>同一芯片精准拆分「手机端 vs 平板端」实测 · 真实还原机身散热模具与硬件调校反差。</p>
    </section>

    <!-- Dual Mode Cards -->
    <div class="portal-grid">
      <!-- Daily Card -->
      <div class="portal-card card-daily">
        <div>
          <div class="portal-header">
            <span class="portal-badge badge-daily">👑 推荐日常购机参考</span>
            <h2 class="portal-title">日常流畅模式</h2>
            <div class="portal-formula">GB6 单核 60% + GB6 多核 20% + GPU 20%</div>
            <p class="portal-desc">
              日常 App 秒开、手势打断与滑动抗掉帧 90% 依赖单大核瞬间爆发（Burst）。挤掉 15W 全核烤机水分，真实反映温控甜点区流畅度。提供手机与平板专属独立筛选。
            </p>
          </div>
          <div class="preview-list">
            <div class="preview-title">全形态日常榜 TOP 3 领跑者</div>
            <div class="preview-item">
              <span>1. 苹果 M5 (iPad) <span style="font-size:11px; color:#c084fc;">[📟平板]</span></span>
              <span class="preview-score" style="color:#34d399;">383.7 分</span>
            </div>
            <div class="preview-item">
              <span>2. 小米玄戒 O3 <span style="font-size:11px; color:#fb923c;">[📱手机]</span></span>
              <span class="preview-score" style="color:#34d399;">369.0 分</span>
            </div>
            <div class="preview-item">
              <span>3. 苹果 M4 (iPad) <span style="font-size:11px; color:#c084fc;">[📟平板]</span></span>
              <span class="preview-score" style="color:#34d399;">332.5 分</span>
            </div>
          </div>
        </div>
        <a href="daily.html" class="portal-btn btn-daily-cta">
          进入日常流畅天梯榜 ({total_count}款) →
        </a>
      </div>

      <!-- Peak Card -->
      <div class="portal-card card-peak">
        <div>
          <div class="portal-header">
            <span class="portal-badge badge-peak">🔥 极客跑分与游戏天花板</span>
            <h2 class="portal-title">极限性能模式</h2>
            <div class="portal-formula">CPU 60% (单30/多70) + GPU 40%</div>
            <p class="portal-desc">
              展现芯片在不计功耗、主动散热或高压重载游戏时的全核狂飙与 3DMark 极限图形光追释放能力，反映芯片微架构与半导体制程的最高理论物理天花板。
            </p>
          </div>
          <div class="preview-list">
            <div class="preview-title">全形态极限榜 TOP 3 领跑者</div>
            <div class="preview-item">
              <span>1. 小米玄戒 O3 <span style="font-size:11px; color:#fb923c;">[📱手机]</span></span>
              <span class="preview-score" style="color:#fb7185;">445.8 分</span>
            </div>
            <div class="preview-item">
              <span>2. 苹果 M5 (iPad) <span style="font-size:11px; color:#c084fc;">[📟平板]</span></span>
              <span class="preview-score" style="color:#fb7185;">442.1 分</span>
            </div>
            <div class="preview-item">
              <span>3. 苹果 M4 (iPad) <span style="font-size:11px; color:#c084fc;">[📟平板]</span></span>
              <span class="preview-score" style="color:#fb7185;">374.9 分</span>
            </div>
          </div>
        </div>
        <a href="peak.html" class="portal-btn btn-peak-cta">
          进入极限性能天梯榜 ({total_count}款) →
        </a>
      </div>
    </div>

    <!-- Methodology Section -->
    <section class="section-block">
      <h2 class="section-title">💡 双轨设计哲学与形态细分解构</h2>
      <div class="methods-grid">
        <div class="method-card">
          <div class="method-icon">⚖️</div>
          <h3>同一芯片「手机 vs 平板」的真实分化</h3>
          <p>
            同为天玑 9400 或骁龙 8 Gen 3，在 11~13 寸平板金属大背板（持续耐受 10W~15W）下的全核与 GPU 释放显著超越小屏手机；而在苹果端，iPad mini 7 的 A17 Pro 甚至物理屏蔽了 1 个 GPU 核心，iPad mini 6 的 A15 官方下调了主频。细分后才能彻底杜绝跑分混淆。
          </p>
        </div>
        <div class="method-card">
          <div class="method-icon">📟</div>
          <h3>平板专属大核心的降维压制</h3>
          <p>
            iPad M 系列与高通骁龙 X Elite 拥有 128-bit 显存位宽（带宽超 100GB/s）与更大芯片 Die 面积。通过「设备形态筛选器」，既可在手机榜维持纯粹公平，又可在通榜观察跨界压制。
          </p>
        </div>
        <div class="method-card">
          <div class="method-icon">⚡</div>
          <h3>为什么日常模式以「单核 60%」为轴心？</h3>
          <p>
            微信滑动、动效打断、网页冷启均属于 200ms~800ms 的瞬时脉冲（Burst）。Geekbench 6 单核满载功耗天然落在 3.5W~5.5W，是硅片在稳态甜点区最干净、最无水分的真实体验代理指标。
          </p>
        </div>
      </div>
    </section>

    <!-- Comparison Table -->
    <section class="section-block">
      <h2 class="section-title">📊 手机 vs 平板实测反差与跨界对比</h2>
      <p style="color:var(--text-muted); font-size:13px; margin-bottom:14px;">
        同一芯片在「手机端」与「平板端」的实际释放对比（如天玑 9400、骁龙 8G3、苹果 A17 Pro/A15）：
      </p>
      <div class="table-container">
        <table class="comp-table">
          <thead>
            <tr>
              <th>芯片型号与平台版本</th>
              <th style="text-align:center;">日常流畅排名 (分)</th>
              <th style="text-align:center;">极限性能排名 (分)</th>
              <th style="text-align:center;">模式反差变动</th>
              <th>实测核心数据 (GB6 / 3DMark当量)</th>
            </tr>
          </thead>
          <tbody>
{table_html}
          </tbody>
        </table>
      </div>
    </section>

    <!-- Platforms Section -->
    <section class="section-block" style="text-align:center;">
      <h2 class="section-title" style="justify-content:center;">🌐 覆盖 {total_count} 款主流移动与平板芯片</h2>
      <p style="color:var(--text-muted); font-size:13px; margin-bottom:16px;">智能手机专精 ({phone_count}款) · 平板与跨界专精 ({tablet_count}款) · 统一中文平台标注与基准归一化</p>
      <div style="display:flex; flex-wrap:wrap; justify-content:center; gap:8px;">
        <span class="brand-badge brand-Apple" style="padding:4px 10px; font-size:12px;">苹果 Apple (含 iPad M系列 / {apple_count}款)</span>
        <span class="brand-badge brand-Qualcomm" style="padding:4px 10px; font-size:12px;">高通骁龙 Qualcomm (含 X Elite / {qc_count}款)</span>
        <span class="brand-badge brand-MediaTek" style="padding:4px 10px; font-size:12px;">联发科天玑 Dimensity ({mtk_count}款)</span>
        <span class="brand-badge brand-HiSilicon" style="padding:4px 10px; font-size:12px;">华为麒麟 Kirin ({hisi_count}款)</span>
        <span class="brand-badge brand-Samsung" style="padding:4px 10px; font-size:12px;">三星 Exynos ({sam_count}款)</span>
        <span class="brand-badge brand-Google" style="padding:4px 10px; font-size:12px;">谷歌 Tensor ({goog_count}款)</span>
        <span class="brand-badge brand-Xiaomi" style="padding:4px 10px; font-size:12px;">小米玄戒 Xring ({mi_count}款)</span>
      </div>
    </section>
  </div>

  <footer>
    <p>SocRank 移动与平板 SoC 综合天梯榜 · 基于主流跑分实测与当量归一化整理 · <a href="https://github.com/Alex05250/socrank" target="_blank">GitHub 开源仓库</a></p>
  </footer>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "daily.html"), "w", encoding="utf-8") as f:
    f.write(daily_content)

with open(os.path.join(BASE_DIR, "peak.html"), "w", encoding="utf-8") as f:
    f.write(peak_content)

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_content)

with open(os.path.join(BASE_DIR, "data.js"), "w", encoding="utf-8") as f:
    f.write("window.CHIPS_DATA = " + json.dumps(chips, ensure_ascii=False) + ";\n")

print(f"SUCCESS: Rebuilt index.html, daily.html, peak.html, data.js with {total_count} chips (Phones: {phone_count}, Tablets: {tablet_count}).")
