"""
generate_banner.py
Generates java-journey-banner.svg with the current day auto-calculated
from your START_DATE. Commit this file to your GitHub profile repo root.
"""

from datetime import date

# ── CONFIG ──────────────────────────────────────────────────────────────────
START_DATE   = date(2025, 5, 6)   
TOTAL_DAYS   = 70
OUTPUT_FILE  = "java-journey-banner.svg"
# ────────────────────────────────────────────────────────────────────────────

today       = date.today()
current_day = min((today - START_DATE).days + 1, TOTAL_DAYS)
current_day = max(current_day, 1)

pct_done      = current_day / TOTAL_DAYS
pct_remaining = round((1 - pct_done) * 100, 1)

BAR_X     = 100
BAR_W     = 660
BAR_Y     = 175
BAR_H     = 16
BAR_R     = 8

filled_w  = max(int(pct_done * BAR_W), BAR_H)
cup_x     = BAR_X + filled_w - 6
cup_y     = BAR_Y - 14

svg = f"""<svg viewBox="0 0 860 220" xmlns="http://www.w3.org/2000/svg" width="860" height="220">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%"   style="stop-color:#0d1117"/>
      <stop offset="100%" style="stop-color:#161b22"/>
    </linearGradient>
    <linearGradient id="progressGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   style="stop-color:#f89820"/>
      <stop offset="100%" style="stop-color:#ff6b35"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <linearGradient id="shimmer" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   style="stop-color:rgba(255,255,255,0)"/>
      <stop offset="50%"  style="stop-color:rgba(255,255,255,0.15)"/>
      <stop offset="100%" style="stop-color:rgba(255,255,255,0)"/>
      <animateTransform attributeName="gradientTransform" type="translate"
        from="-1 0" to="1 0" dur="2s" repeatCount="indefinite"/>
    </linearGradient>
    <clipPath id="progressClip">
      <rect x="{BAR_X}" y="{BAR_Y}" width="{BAR_W}" height="{BAR_H}" rx="{BAR_R}"/>
    </clipPath>
  </defs>

  <rect width="860" height="220" rx="16" fill="url(#bg)"/>
  <rect width="860" height="220" rx="16" fill="none" stroke="#f89820" stroke-width="1.5" stroke-opacity="0.35"/>
  <rect x="0" y="0" width="860" height="3" rx="2" fill="url(#progressGrad)" opacity="0.9"/>

  <path d="M20 40 L20 18 L42 18"   fill="none" stroke="#f89820" stroke-width="1.5" stroke-opacity="0.5"/>
  <path d="M840 40 L840 18 L818 18" fill="none" stroke="#f89820" stroke-width="1.5" stroke-opacity="0.5"/>
  <path d="M20 180 L20 202 L42 202" fill="none" stroke="#f89820" stroke-width="1.5" stroke-opacity="0.5"/>
  <path d="M840 180 L840 202 L818 202" fill="none" stroke="#f89820" stroke-width="1.5" stroke-opacity="0.5"/>

  <text x="430" y="38" text-anchor="middle"
        font-family="Georgia, serif" font-style="italic"
        font-size="12.5" fill="#8b949e" letter-spacing="0.3">
    "Every expert was once a beginner. Every pro was once an amateur."
  </text>

  <text x="430" y="82" text-anchor="middle"
        font-family="'Trebuchet MS', Impact, sans-serif"
        font-size="36" font-weight="900"
        fill="#f89820" filter="url(#glow)" letter-spacing="2">
    &#x2615; THE COMPLETE JAVA MASTERCLASS
  </text>

  <text x="180" y="148" text-anchor="middle" font-family='Courier New', monospace" font-size="12" fill="#8b949e">STARTED</text>
  <text x="180" y="163" text-anchor="middle" font-family="'Courier New', monospace" font-size="14" font-weight="bold" fill="#f89820">Day 1</text>

  <text x="430" y="148" text-anchor="middle" font-family="'Courier New', monospace" font-size="12" fill="#8b949e">TODAY</text>
  <text x="430" y="163" text-anchor="middle" font-family="'Courier New', monospace" font-size="14" font-weight="bold" fill="#ffffff">Day {current_day} / {TOTAL_DAYS}</text>

  <text x="680" y="148" text-anchor="middle" font-family="'Courier New', monospace" font-size="12" fill="#8b949e">TARGET</text>
  <text x="680" y="163" text-anchor="middle" font-family="'Courier New', monospace" font-size="14" font-weight="bold" fill="#f89820">Day {TOTAL_DAYS}</text>

  <line x1="295" y1="140" x2="295" y2="168" stroke="#30363d" stroke-width="1"/>
  <line x1="565" y1="140" x2="565" y2="168" stroke="#30363d" stroke-width="1"/>

  <rect x="{BAR_X}" y="{BAR_Y}" width="{BAR_W}" height="{BAR_H}" rx="{BAR_R}" fill="#21262d"/>
  <rect x="{BAR_X}" y="{BAR_Y}" width="{filled_w}" height="{BAR_H}" rx="{BAR_R}" fill="url(#progressGrad)"/>
  <rect x="{BAR_X}" y="{BAR_Y}" width="{filled_w}" height="{BAR_H}" rx="{BAR_R}" fill="url(#shimmer)" clip-path="url(#progressClip)"/>

  <g transform="translate({cup_x}, {cup_y})">
    <ellipse cx="0" cy="-10" rx="3" ry="4" fill="#8b949e" opacity="0">
      <animate attributeName="opacity" values="0;0.6;0" dur="1.5s" begin="0s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="-10;-22;-32" dur="1.5s" begin="0s" repeatCount="indefinite"/>
      <animate attributeName="rx" values="3;5;3" dur="1.5s" begin="0s" repeatCount="indefinite"/>
    </ellipse>
    <ellipse cx="6" cy="-10" rx="3" ry="4" fill="#8b949e" opacity="0">
      <animate attributeName="opacity" values="0;0.5;0" dur="1.5s" begin="0.5s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="-10;-24;-34" dur="1.5s" begin="0.5s" repeatCount="indefinite"/>
      <animate attributeName="rx" values="2;4;2" dur="1.5s" begin="0.5s" repeatCount="indefinite"/>
    </ellipse>
    <ellipse cx="-5" cy="-10" rx="2.5" ry="3.5" fill="#8b949e" opacity="0">
      <animate attributeName="opacity" values="0;0.4;0" dur="1.5s" begin="1s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="-10;-21;-31" dur="1.5s" begin="1s" repeatCount="indefinite"/>
    </ellipse>
    <path d="M-12 0 L-10 14 Q0 17 10 14 L12 0 Z" fill="#f89820"/>
    <rect x="-13" y="-2" width="26" height="5" rx="2.5" fill="#ff8c00"/>
    <ellipse cx="0" cy="-0.5" rx="10" ry="3" fill="#5c3317"/>
    <path d="M12 2 Q20 2 20 8 Q20 14 12 12" fill="none" stroke="#ff8c00" stroke-width="2.5" stroke-linecap="round"/>
    <text x="0" y="10" text-anchor="middle" font-family="'Courier New', monospace" font-weight="900" font-size="8" fill="#fff" opacity="0.9">JAVA</text>
  </g>

  <text x="430" y="208" text-anchor="middle"
        font-family="'Courier New', monospace"
        font-size="12" fill="#8b949e" letter-spacing="1">
    Day {current_day} / {TOTAL_DAYS} · {pct_remaining}% remaining ☕
  </text>
</svg>"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"Banner generated: Day {current_day}/{TOTAL_DAYS} ({pct_remaining}% remaining)")
