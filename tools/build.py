"""Generate every SVG component of the profile README in one visual system.

Run:  python tools/build.py
Edit the CONTENT block, re-run, commit. hero.svg and footer.svg are hand-made
and left untouched.
"""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

# ---- palette -------------------------------------------------------------
MIDNIGHT, DARKWINE, BURGUNDY = "#10070C", "#190B12", "#451126"
WINE, ROSE, PALE, IVORY = "#701A3D", "#C77B9B", "#E5B5C7", "#F8F0F3"
SERIF = "Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif"
MONO = "ui-monospace, 'SF Mono', Menlo, Consolas, monospace"
SANS = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
W = 1000  # logical width of every full-width component

# ---- content -------------------------------------------------------------
SECTIONS = [
    ("01", "Hello", "WHO I AM"),
    ("02", "Achievements", "VERIFIED AGAINST MY CV"),
    ("03", "Projects", "ALL FROM THIS ACCOUNT"),
    ("04", "Skills", "GROUPED BY WHAT THEY'RE FOR"),
    ("05", "Contributions", "LIVE DATA FROM GITHUB"),
    ("06", "Experience", "ONE LINE EACH"),
    ("07", "Contact", "SAY HELLO"),
]

INTRO = [
    "I'm Abhishek, an Engineering Management master's student at Politecnico di Torino, with a B.Sc. in Computer "
    "Engineering from the same place. I like the seam between engineering and business: taking something technical, "
    "understanding who it is for, and shipping it.",
    "Before this I built a VR property-visualisation platform as a Technical Management Trainee at OpenSky VR Italia, "
    "and spent a year and a half as a Junior Data Analyst at Fibzio turning SQL and Power BI into decisions. "
    "On the side I lead the Politecnico Indian Students Association, which reaches more than a thousand students. "
    "In 2026 I stood on three hackathon podiums.",
]

STATS = [
    ("3", "hackathon podiums in 2026"),
    ("1,000+", "students reached as PISA president"),
    ("40%", "faster reporting at Fibzio"),
    ("~30%", "faster property demos at OpenSky VR"),
]

PODIUM = [
    ("1st", "LOKI Urban Monitoring Hackathon", "404: Pothole Not Found · Oct 2026",
     "cityX: an AI civic-intelligence platform that turns street reports into actionable incidents, with "
     "geospatial analysis, duplicate detection and risk-based prioritisation."),
    ("2nd", "Automation Hackathon", "Mar 2026",
     "An AI supply-chain risk platform built in five hours. ScrapeGraphAI and LLMs profile 1,000+ vendors "
     "and flag geopolitical, weather and logistics risks on cargo routes."),
    ("1st", "Therness Hackathon", "Feb 2026",
     "1,551 welding samples across thermal video, audio and sensor data, detected and classified into "
     "six defect categories."),
]

CERTS = ["INSIDE LVMH Certificate", "McKinsey Forward Program", "CS50 · Harvard"]

PROJECTS = [
    ("Hand-drawn 3D portfolio", "portfolio", "https://iamsammy-ak.github.io/portfolio/",
     "A portfolio you walk through: paper-tear loader, a sketched building, a corridor with doors to four rooms. "
     "Every drawing is procedural canvas, no image files.", "three.js · GSAP · Canvas 2D"),
    ("ms-project-mcp", "ms-project-mcp", "",
     "Microsoft Project desktop has no public API. This MCP server hands it to AI agents as 51 typed tools over COM: "
     "tasks, WBS, dependencies, resources, baselines, earned value.", "Python · MCP · COM automation"),
    ("OmniPilot", "omni-pilot", "",
     "An AI SOC copilot: threat analysis, Italian NIS2 / ACN compliance reports, honeypot deception and "
     "plain-English security Q&A in one console.", "Next.js 15 · TypeScript"),
    ("M&A Synergy Simulator", "SynergySimulator", "https://synergy-simulator.vercel.app",
     "Client-side financial model for merger deals: premiums, pro-forma financials, accretion / dilution, "
     "ownership splits and 2D sensitivity heatmaps.", "React · TypeScript"),
    ("RetailPulse BI", "retailpulse", "",
     "End-to-end BI delivery for a mock retailer: star-schema SQL Server model, DAX measures, an executive "
     "Power BI dashboard, testing and documentation.", "SQL Server · DAX · Power BI"),
    ("StockVault", "StockVault", "",
     "A stock-trading platform with portfolio tracking, live quotes from Yahoo Finance, watchlists, "
     "stop-loss orders and candlestick charts.", "Flask · SQLite · Plotly"),
    ("Smart Stop", "smart-stop", "",
     "Lets hearing-impaired passengers identify an arriving bus. Two Raspberry Pis talk over MQTT: a "
     "touchscreen at the stop, an LCD and buzzer on the bus.", "Python · Raspberry Pi · MQTT"),
    ("CineSphere", "CineSphere", "",
     "A social network for cinephiles: film logging via TMDB, spoiler-safe reviews, reactions, follows "
     "and a unified feed.", "ASP.NET Core 8 · CQRS · Next.js · PostgreSQL"),
    ("RateMyDorm Italy", "ratemyDorm", "",
     "Crowdsourced reviews of student residences across Italian universities, with a campus map and "
     "side-by-side comparison.", "Next.js 14 · TypeScript · Leaflet"),
]

SKILLS = [
    ("Data & analytics", ["SQL", "MS SQL", "PostgreSQL", "Power BI", "DAX", "Excel", "FP&A"]),
    ("AI & engineering", ["Python", "AI / ML", "MATLAB", "Docker", "MCP", "ScrapeGraphAI", "LLM tooling"]),
    ("Web", ["TypeScript", "React", "Angular", "Next.js", "three.js", "Flask", "ASP.NET Core"]),
    ("Product & delivery", ["Project management", "Market research", "Startup research", "JIRA", "Trello", "Asana", "Notion", "Figma"]),
    ("People", ["Public speaking", "Entrepreneurship", "Volunteer teams of 10+", "Budgets & sponsorship"]),
    ("Languages", ["Hindi · native", "English · professional", "Italian · beginner"]),
]

TIMELINE = [
    ("2025 – now", "M.Sc. Engineering Management", "Politecnico di Torino", "Focus: business solutions and finance", True),
    ("Jan – Jun 2025", "Technical Management Trainee", "OpenSky VR Italia",
     "React, Angular, Matterport, LiDAR · MVP in six months · ~30% faster property presentations", False),
    ("Sep 2023 – Dec 2024", "Junior Data Analyst", "Fibzio",
     "SQL, Power BI, FP&A · 40% faster reporting · 20% fewer incidents · +25% client satisfaction", False),
    ("Apr 2023 – now", "President", "Politecnico Indian Students Association",
     "Strategy and events for 1,000+ students · Red Bull-sponsored chess tournament, 400+ players", True),
    ("May – Jul 2024", "Logistics Coordinator", "Torino 2025 FISU Games", "5+ venues, inspections, on-site execution", False),
    ("Nov 2022 – Jun 2023", "Marketing Manager", "AIESEC", "Led a volunteer team of 10+", False),
    ("2022 – 2025", "B.Sc. Computer Engineering", "Politecnico di Torino", "", False),
]

BUTTONS = [
    ("btn-portfolio", "3D portfolio", "iamsammy-ak.github.io/portfolio"),
    ("btn-linkedin", "LinkedIn", "in/sammy4bhishek"),
    ("btn-github", "GitHub", "iamsammy-ak"),
    ("btn-email", "Email", "kumarabhishekk363@gmail.com"),
    ("btn-cv", "Curriculum vitae", "PDF"),
]

# ---- helpers -------------------------------------------------------------
def e(s):
    return escape(s, quote=True)


def wrap(text, max_px, size, factor):
    """Greedy word-wrap using an average glyph width = size * factor."""
    cw = size * factor
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if len(t) * cw <= max_px or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def svg(name, w, h, body, title, defs="", radius=18):
    uid = name.replace("-", "")
    doc = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="{uid}-t">
  <title id="{uid}-t">{e(title)}</title>
  <defs>
    <linearGradient id="{uid}-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{DARKWINE}"/><stop offset="1" stop-color="#23091A"/>
    </linearGradient>
    <linearGradient id="{uid}-rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{ROSE}"/><stop offset="1" stop-color="{ROSE}" stop-opacity="0"/>
    </linearGradient>
    <pattern id="{uid}-dots" width="8" height="8" patternUnits="userSpaceOnUse">
      <circle cx="4" cy="4" r="0.6" fill="{ROSE}" fill-opacity="0.12"/>
    </pattern>
    <clipPath id="{uid}-clip"><rect width="{w}" height="{h}" rx="{radius}"/></clipPath>
    {defs}
  </defs>
  <g clip-path="url(#{uid}-clip)">
{body}
  </g>
</svg>
"""
    (OUT / f"{name}.svg").write_text(doc, encoding="utf-8")
    return name


def panel(uid, w, h, x=0, y=0, rx=18, fill=None, stroke=True):
    f = fill or f"url(#{uid}-bg)"
    s = f' stroke="{WINE}" stroke-opacity="0.8" stroke-width="1"' if stroke else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{f}"{s}/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="url(#{uid}-dots)"/>')


def text(x, y, s, size, fill, family=SANS, weight=None, anchor=None, italic=False, spacing=None, opacity=None):
    a = []
    if weight: a.append(f'font-weight="{weight}"')
    if anchor: a.append(f'text-anchor="{anchor}"')
    if italic: a.append('font-style="italic"')
    if spacing is not None: a.append(f'letter-spacing="{spacing}"')
    if opacity is not None: a.append(f'fill-opacity="{opacity}"')
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{fill}" {" ".join(a)}>{e(s)}</text>'


def chip(x, y, label, size=13, pad=12, h=28, fill=BURGUNDY, stroke=WINE, color=PALE):
    w = round(len(label) * size * 0.62 + pad * 2)
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{fill}" stroke="{stroke}" stroke-width="1"/>'
            + text(x + w / 2, y + h / 2 + size * 0.36, label, size, color, MONO, anchor="middle"), w)


# ---- components ----------------------------------------------------------
def section_headers():
    for num, title, eyebrow in SECTIONS:
        name = f"h-{title.lower()}"
        uid = name.replace("-", "")
        tw = len(title) * 30 * 0.56
        x_rule = 70 + tw + 24
        body = f"""
    {text(0, 44, num, 15, ROSE, MONO, spacing=3)}
    {text(50, 44, title, 30, IVORY, SERIF, weight=700)}
    <rect x="{x_rule:.0f}" y="38" width="{W - x_rule - 260:.0f}" height="1" fill="url(#{uid}-rule)">
      <animate attributeName="width" values="0;{W - x_rule - 260:.0f}" dur="1.6s" fill="freeze"/>
    </rect>
    <circle cx="{x_rule:.0f}" cy="38.5" r="2.5" fill="{PALE}"/>
    {text(W, 44, eyebrow, 11, ROSE, MONO, anchor="end", spacing=2.5)}
    <rect x="0" y="62" width="{W}" height="1" fill="{WINE}" fill-opacity="0.5"/>"""
        svg(name, W, 72, body, f"{num} {title}", radius=0)


def intro():
    name, uid = "intro", "intro"
    size, lh, pad = 17, 28, 40
    lines = []
    for p in INTRO:
        lines += wrap(p, W - pad * 2 - 40, size, 0.5)
        lines.append("")
    lines = lines[:-1]
    h = pad * 2 + lh * len(lines) - 6
    body = [panel(uid, W, h), f'<rect x="0" y="0" width="4" height="{h}" fill="{ROSE}"/>']
    y = pad + size
    for ln in lines:
        if ln:
            body.append(text(pad + 20, y, ln, size, IVORY, SERIF, opacity=0.92))
        y += lh
    svg(name, W, h, "\n".join(body), " ".join(INTRO))


def stats():
    name, uid = "stats", "stats"
    n, gap, h = len(STATS), 20, 140
    tw = (W - gap * (n - 1)) / n
    body = []
    for i, (big, small) in enumerate(STATS):
        x = i * (tw + gap)
        body.append(panel(uid, tw, h, x, 0, 16))
        body.append(f'<rect x="{x + 24}" y="0" width="56" height="3" rx="1.5" fill="{ROSE}">'
                    f'<animate attributeName="width" values="56;110;56" dur="{4 + i}s" repeatCount="indefinite"/></rect>')
        body.append(text(x + 24, 72, big, 46, PALE, SERIF, weight=700))
        for j, ln in enumerate(wrap(small, tw - 48, 13, 0.6)):
            body.append(text(x + 24, 100 + j * 18, ln.upper(), 11, ROSE, MONO, spacing=1.8))
    svg(name, W, h, "\n".join(body), "; ".join(f"{b} {s}" for b, s in STATS), radius=0)


def podium():
    name, uid = "podium", "podium"
    n, gap, h = 3, 20, 262
    cw = (W - gap * (n - 1)) / n
    defs = (f'<radialGradient id="{uid}-medal" cx="0.35" cy="0.3" r="0.8">'
            f'<stop offset="0" stop-color="{PALE}"/><stop offset="1" stop-color="{WINE}"/></radialGradient>'
            f'<filter id="{uid}-glow" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="6"/></filter>')
    body = []
    for i, (place, event, when, desc) in enumerate(PODIUM):
        x = i * (cw + gap)
        body.append(panel(uid, cw, h, x, 0, 18))
        mx, my = x + 46, 46
        body.append(f'<circle cx="{mx}" cy="{my}" r="22" fill="{ROSE}" filter="url(#{uid}-glow)" opacity="0.55">'
                    f'<animate attributeName="opacity" values="0.3;0.7;0.3" dur="{3 + i}s" repeatCount="indefinite"/></circle>')
        body.append(f'<circle cx="{mx}" cy="{my}" r="22" fill="url(#{uid}-medal)" stroke="{PALE}" stroke-width="1"/>')
        body.append(text(mx, my + 5, place, 14, MIDNIGHT, SERIF, weight=700, anchor="middle"))
        body.append(text(x + 82, 42, "HACKATHON", 10, ROSE, MONO, spacing=2.5))
        body.append(text(x + 82, 60, when.upper(), 10, PALE, MONO, spacing=1.5, opacity=0.9))
        y = 104
        for ln in wrap(event, cw - 56, 21, 0.58):
            body.append(text(x + 28, y, ln, 21, IVORY, SERIF, weight=700)); y += 26
        y += 6
        for ln in wrap(desc, cw - 56, 13.5, 0.44)[:5]:
            body.append(text(x + 28, y, ln, 13.5, IVORY, SANS, opacity=0.8)); y += 19
    svg(name, W, h, "\n".join(body), "; ".join(f"{p} {ev} {w}" for p, ev, w, _ in PODIUM), defs, radius=0)


def certs():
    name, uid = "certs", "certs"
    h = 64
    body = [panel(uid, W, h, 0, 0, 14), text(24, 38, "CERTIFICATES", 11, ROSE, MONO, spacing=2.5)]
    x = 150
    for c in CERTS:
        s, w = chip(x, 17, c, 13, 16, 30)
        body.append(s); x += w + 12
    svg(name, W, h, "\n".join(body), "Certificates: " + ", ".join(CERTS))


def projects():
    h = 118
    for i, (title, repo, live, desc, stack) in enumerate(PROJECTS, 1):
        name = f"p-{repo.lower()}"
        uid = name.replace("-", "")
        body = [panel(uid, W, h, 0, 0, 16), f'<rect x="0" y="0" width="5" height="{h}" fill="{ROSE}"/>',
                text(W - 24, 32, f"{i:02d}", 13, ROSE, MONO, anchor="end", spacing=2),
                text(36, 40, title, 22, IVORY, SERIF, weight=700)]
        tx = 36 + len(title) * 22 * 0.66 + 14
        if live:
            s, w = chip(tx, 20, "LIVE ↗", 10, 10, 22, WINE, PALE, IVORY)
            body.append(s)
            tx += w + 10
        body.append(text(tx + 2, 40, repo, 12, ROSE, MONO, opacity=0.9))
        y = 66
        for ln in wrap(desc, W - 36 - 300, 14, 0.5)[:2]:
            body.append(text(36, y, ln, 14, IVORY, SANS, opacity=0.82)); y += 19
        body.append(text(W - 24, 100, stack.upper(), 10.5, PALE, MONO, anchor="end", spacing=1.5, opacity=0.85))
        svg(name, W, h, "\n".join(body), f"{title}: {desc} Built with {stack}.")


def skills():
    name, uid = "skills", "skills"
    cols, gap, colw = 2, 20, (W - 20) / 2

    def layout(items):
        """Return chip positions (relative) and the number of rows used."""
        pos, x, row = [], 24, 0
        for it in items:
            w = round(len(it) * 12 * 0.62 + 24)
            if x + w > colw - 20:
                x, row = 24, row + 1
            pos.append((x, row, it)); x += w + 8
        return pos, row + 1

    laid = [layout(items) for _, items in SKILLS]
    row_h = []
    for r in range(0, len(SKILLS), cols):
        rows_used = max(n for _, n in laid[r:r + cols])
        row_h.append(48 + rows_used * 32 + 10)
    h = sum(row_h) + gap * (len(row_h) - 1)
    body, cy = [], 0
    for i, (group, items) in enumerate(SKILLS):
        r, c = divmod(i, cols)
        if c == 0 and r > 0:
            cy += row_h[r - 1] + gap
        cx, rh = c * (colw + gap), row_h[r]
        body.append(panel(uid, colw, rh, cx, cy, 16))
        body.append(text(cx + 24, cy + 32, group.upper(), 11, ROSE, MONO, spacing=2.5))
        for x, row, it in laid[i][0]:
            s, _ = chip(cx + x, cy + 48 + row * 32, it, 12, 12, 26)
            body.append(s)
    svg(name, W, h, "\n".join(body), "; ".join(f"{g}: {', '.join(i)}" for g, i in SKILLS), radius=0)


def timeline():
    name, uid = "timeline", "timeline"
    rh, top = 66, 28
    h = top + rh * len(TIMELINE) + 10
    lx = 236
    body = [panel(uid, W, h), f'<rect x="{lx}" y="{top}" width="1" height="{h - top - 20}" fill="{WINE}"/>']
    for i, (when, role, org, note, now) in enumerate(TIMELINE):
        y = top + i * rh + 22
        body.append(text(lx - 22, y + 2, when.upper(), 11, ROSE, MONO, anchor="end", spacing=1.5))
        if now:
            body.append(f'<circle cx="{lx + 0.5}" cy="{y - 3}" r="5" fill="{PALE}" opacity="0.5">'
                        f'<animate attributeName="r" values="5;12" dur="2.4s" repeatCount="indefinite"/>'
                        f'<animate attributeName="opacity" values="0.5;0" dur="2.4s" repeatCount="indefinite"/></circle>')
        body.append(f'<circle cx="{lx + 0.5}" cy="{y - 3}" r="4.5" fill="{PALE if now else DARKWINE}" stroke="{PALE}" stroke-width="1.2"/>')
        body.append(text(lx + 28, y + 3, role, 19, IVORY, SERIF, weight=700))
        ox = lx + 28 + len(role) * 19 * 0.66 + 12
        body.append(text(ox, y + 3, org, 12, PALE, MONO, opacity=0.9))
        if note:
            body.append(text(lx + 28, y + 25, note, 13, IVORY, SANS, opacity=0.68))
    svg(name, W, h, "\n".join(body), "; ".join(f"{w}: {r}, {o}" for w, r, o, _, _ in TIMELINE))


def buttons():
    for name, label, sub in BUTTONS:
        uid = name.replace("-", "")
        w = round(max(len(label) * 15 * 0.58, len(sub) * 10 * 0.62) + 62)
        h = 58
        body = [panel(uid, w, h, 0, 0, 14),
                text(18, 26, label, 15, IVORY, SERIF, weight=700),
                text(18, 43, sub, 10, ROSE, MONO, spacing=0.6),
                f'<circle cx="{w - 26}" cy="29" r="13" fill="{BURGUNDY}" stroke="{WINE}"/>',
                f'<path d="M{w - 31} 29h10m-4 -4l4 4l-4 4" fill="none" stroke="{PALE}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
                f'<animateTransform attributeName="transform" type="translate" values="0 0;2 0;0 0" dur="1.8s" repeatCount="indefinite"/></path>']
        svg(name, w, h, "\n".join(body), f"{label} ({sub})")


def divider():
    name, uid = "divider", "divider"
    body = (f'<rect x="0" y="9" width="{W}" height="1" fill="url(#{uid}-rule)"/>'
            f'<circle cx="0" cy="9.5" r="3" fill="{PALE}"><animate attributeName="cx" values="0;{W}" dur="6s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="1;0" dur="6s" repeatCount="indefinite"/></circle>')
    svg(name, W, 20, body, "divider", radius=0)


if __name__ == "__main__":
    for fn in (section_headers, intro, stats, podium, certs, projects, skills, timeline, buttons, divider):
        fn()
    print("wrote", sorted(p.name for p in OUT.glob("*.svg")))
