# generate_obsidian.py

gStr = '#8EC540'
pStr = '#9867C1'
dStr = '#32373C'

def get_neon_base(i, strokes, dash, anim, filters, extra=''):
    return f"""<svg viewBox="0 0 24 24" fill="none" class="svg-icon" stroke-linejoin="round" stroke-linecap="round">
        <defs>{filters}</defs>
        {extra}
        <path d="M 5 6 L 19 6 L 5 18 L 19 18" {strokes} {dash}>
            <animate attributeName="stroke-dashoffset" values="{anim}" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite" />
        </path>
    </svg>"""

def get_laser_base(i, trackStroke, laserStrokes, shadowStrokes, laserDash, shadowDash, filters, extra=''):
    shadow_html = ''
    if shadowStrokes:
        shadow_html = f"""<path d="M 4 6 L 20 6 L 4 18 L 20 18" {shadowStrokes} {shadowDash}>
            <animate attributeName="stroke-dashoffset" from="76" to="8" dur="1.5s" repeatCount="indefinite" />
        </path>"""
    return f"""<svg viewBox="0 0 24 24" fill="none" class="svg-icon" stroke-linejoin="round" stroke-linecap="round">
        <defs>{filters}</defs>
        {extra}
        <polygon points="4,6 20,6 4,18 20,18" {trackStroke} />
        {shadow_html}
        <path d="M 4 6 L 20 6 L 4 18 L 20 18" {laserStrokes} {laserDash}>
            <animate attributeName="stroke-dashoffset" from="68" to="0" dur="1.5s" repeatCount="indefinite" />
        </path>
    </svg>"""

neon_builds = [
    { "title": "Build 1 (70s Glaser)", "svg": get_neon_base(1, f'stroke="{gStr}" stroke-width="4"', 'stroke-dasharray="60" stroke-dashoffset="60"', '60; 0; 0; 60; 60', '', f'<path d="M 5 7 L 18 7 L 4 19 L 19 19" stroke="{pStr}" stroke-width="3" stroke-dasharray="60" stroke-dashoffset="60" opacity="0.8"><animate attributeName="stroke-dashoffset" values="60; 0; 0; 60; 60" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite" /></path>') },
    { "title": "Build 2 (70s Dean)", "svg": get_neon_base(2, f'stroke="{gStr}" stroke-width="2" filter="url(#glow2)"', 'stroke-dasharray="60" stroke-dashoffset="60"', '60; 0; 0; 60; 60', f'<filter id="glow2"><feGaussianBlur stdDeviation="3" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>', f'<path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{pStr}" stroke-width="8" opacity="0.4" stroke-linecap="round" filter="url(#glow2)" stroke-dasharray="60" stroke-dashoffset="60"><animate attributeName="stroke-dashoffset" values="60; 0; 0; 60; 60" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite" /></path>') },
    { "title": "Build 3 (80s Brody)", "svg": get_neon_base(3, f'stroke="{gStr}" stroke-width="6" stroke-linecap="square" stroke-dasharray="4 4"', 'stroke-dashoffset="60"', '60; 0; 0; 60; 60', '', f'<path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{pStr}" stroke-width="6" stroke-dasharray="4 4" stroke-dashoffset="64" stroke-linecap="square"><animate attributeName="stroke-dashoffset" values="64; 4; 4; 64; 64" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite" /></path>') },
    { "title": "Build 4 (80s Carson)", "svg": get_neon_base(4, f'stroke="{gStr}" stroke-width="3" stroke-dasharray="10 5 15 5"', 'stroke-dashoffset="60"', '60; 0; 0; 60; 60', '', f'<path d="M 5 5 L 20 6 L 4 18 L 20 19" stroke="{pStr}" stroke-width="2" stroke-dasharray="60" stroke-dashoffset="60"><animate attributeName="stroke-dashoffset" values="60; 0; 0; 60; 60" dur="3.8s" repeatCount="indefinite" /></path>') },
    { "title": "Build 5 (90s Sagmeister)", "svg": f'<svg viewBox="0 0 24 24" fill="none" class="svg-icon" stroke-linejoin="round" stroke-linecap="round"><path d="M 5 7 L 19 6 M 4 5 L 20 8 M 5 17 L 19 19 M 4 16 L 20 17 M 19 6 L 5 18 M 20 6 L 4 18" stroke="{pStr}" stroke-width="1.5" stroke-dasharray="40"><animate attributeName="stroke-dashoffset" values="40; 0; 0; 40; 40" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite" /></path><path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{gStr}" stroke-width="2" stroke-dasharray="60" stroke-dashoffset="60"><animate attributeName="stroke-dashoffset" values="60; 0; 0; 60; 60" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite" /></path></svg>' },
    { "title": "Build 6 (90s Ashworth)", "svg": get_neon_base(6, f'stroke="url(#grad6)" stroke-width="4" mask="url(#stripes6)"', 'stroke-dasharray="60" stroke-dashoffset="60"', '60; 0; 0; 60; 60', f'<linearGradient id="grad6"><stop offset="0%" stop-color="{gStr}"/><stop offset="100%" stop-color="{pStr}"/></linearGradient><mask id="stripes6"><rect x="0" y="0" width="24" height="24" fill="url(#pattern6)"/></mask><pattern id="pattern6" width="2" height="2" patternUnits="userSpaceOnUse"><rect width="1" height="2" fill="white"/></pattern>') },
    { "title": "Build 7 (00s Fairey)", "svg": get_neon_base(7, f'stroke="{pStr}" stroke-width="3" filter="url(#drop7)"', 'stroke-dasharray="60" stroke-dashoffset="60"', '60; 0; 0; 60; 60', f'<filter id="drop7"><feDropShadow dx="2" dy="2" stdDeviation="0" flood-color="{gStr}"/></filter>') },
    { "title": "Build 8 (00s Davis)", "svg": f'<svg viewBox="0 0 24 24" fill="none" class="svg-icon"><path d="M 5 4 L 19 8 L 5 16 L 19 20" stroke="{gStr}" stroke-width="1" stroke-dasharray="60"><animate attributeName="stroke-dashoffset" values="60; 0; 0; 60; 60" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite"/></path><path d="M 5 8 L 19 4 L 5 20 L 19 16" stroke="{pStr}" stroke-width="1" stroke-dasharray="60"><animate attributeName="stroke-dashoffset" values="60; 0; 0; 60; 60" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite"/></path><path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{gStr}" stroke-width="2" stroke-dasharray="60"><animate attributeName="stroke-dashoffset" values="60; 0; 0; 60; 60" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite"/></path></svg>' },
    { "title": "Build 9 (10s Beeple)", "svg": get_neon_base(9, f'stroke="{gStr}" stroke-width="5" filter="url(#bloom9)"', 'stroke-dasharray="60" stroke-dashoffset="60"', '60; 0; 0; 60; 60', f'<filter id="bloom9"><feGaussianBlur stdDeviation="3" result="blur"/><feComponentTransfer><feFuncA type="linear" slope="3"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>', f'<path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{pStr}" stroke-width="2" stroke-dasharray="60" stroke-dashoffset="60"><animate attributeName="stroke-dashoffset" values="60; 0; 0; 60; 60" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite" /></path>') },
    { "title": "Build 10 (20s Anadol)", "svg": get_neon_base(10, f'stroke="url(#fluid10)" stroke-width="5" stroke-linecap="round"', 'stroke-dasharray="60" stroke-dashoffset="60"', '60; 0; 0; 60; 60', f'<linearGradient id="fluid10" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="{gStr}"/><stop offset="50%" stop-color="{pStr}"/><stop offset="100%" stop-color="{gStr}"/><animateTransform attributeName="transform" type="translate" values="-1,-1;1,1;-1,-1" dur="2s" repeatCount="indefinite"/></linearGradient>') }
]

tracing_lasers = [
    { "title": "Laser 1 (70s Glaser)", "svg": get_laser_base(11, f'stroke="{dStr}" stroke-width="4"', f'stroke="{gStr}" stroke-width="2"', f'stroke="{pStr}" stroke-width="2"', 'stroke-dasharray="8 60"', 'stroke-dasharray="12 56" stroke-dashoffset="2"', '', f'<path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{gStr}" stroke-dasharray="16 52" stroke-dashoffset="4" stroke-width="1"><animate attributeName="stroke-dashoffset" from="72" to="4" dur="1.5s" repeatCount="indefinite" /></path>') },
    { "title": "Laser 2 (70s Dean)", "svg": get_laser_base(12, f'stroke="{dStr}" stroke-width="4"', f'stroke="{gStr}" stroke-width="4" stroke-linecap="round"', f'stroke="{pStr}" stroke-width="6" filter="url(#glow12)"', 'stroke-dasharray="2 66"', 'stroke-dasharray="20 48" stroke-dashoffset="2"', f'<filter id="glow12"><feGaussianBlur stdDeviation="3" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>') },
    { "title": "Laser 3 (80s Brody)", "svg": get_laser_base(13, f'stroke="{dStr}" stroke-width="4"', f'stroke="{gStr}" stroke-width="6" stroke-linecap="square"', f'stroke="{pStr}" stroke-width="4" stroke-dasharray="4 4"', 'stroke-dasharray="6 62"', 'stroke-dasharray="30 38" stroke-dashoffset="6"', '') },
    { "title": "Laser 4 (80s Carson)", "svg": get_laser_base(14, f'stroke="{dStr}" stroke-width="4"', f'stroke="{gStr}" stroke-width="3"', f'stroke="{pStr}" stroke-width="2"', 'stroke-dasharray="4 10 2 52"', 'stroke-dasharray="8 6 4 50" stroke-dashoffset="6"', '') },
    { "title": "Laser 5 (90s Sagmeister)", "svg": f'<svg viewBox="0 0 24 24" fill="none" class="svg-icon" stroke-linejoin="round" stroke-linecap="round"><polygon points="4,6 20,6 4,18 20,18" stroke="{dStr}" stroke-width="4"/><path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{pStr}" stroke-width="8" stroke-dasharray="2 66"><animate attributeName="stroke-dashoffset" from="68" to="0" dur="1.5s" repeatCount="indefinite" /><animate attributeName="stroke-width" values="8;2;6;10;4;8" dur="0.2s" repeatCount="indefinite" /></path><path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{gStr}" stroke-width="2" stroke-dasharray="8 60"><animate attributeName="stroke-dashoffset" from="68" to="0" dur="1.5s" repeatCount="indefinite" /></path></svg>' },
    { "title": "Laser 6 (90s Ashworth)", "svg": get_laser_base(16, f'stroke="{dStr}" stroke-width="4"', f'stroke="{gStr}" stroke-width="4" stroke-dasharray="1 2 3 2"', f'stroke="{pStr}" stroke-width="4" stroke-dasharray="1 4 2 2"', 'stroke-dasharray="8 60"', 'stroke-dasharray="16 52" stroke-dashoffset="8"', '') },
    { "title": "Laser 7 (00s Fairey)", "svg": get_laser_base(17, f'stroke="{dStr}" stroke-width="4"', f'stroke="{gStr}" stroke-width="4" stroke-linecap="square" filter="url(#drop17)"', f'stroke="{pStr}" stroke-width="2"', 'stroke-dasharray="8 60"', 'stroke-dasharray="16 52" stroke-dashoffset="8"', f'<filter id="drop17"><feDropShadow dx="2" dy="2" stdDeviation="0" flood-color="#000"/></filter>') },
    { "title": "Laser 8 (00s Davis)", "svg": f'<svg viewBox="0 0 24 24" fill="none" class="svg-icon" stroke-linejoin="round"><polygon points="4,6 20,6 4,18 20,18" stroke="{dStr}" stroke-width="4"/><g><animateTransform attributeName="transform" type="translate" values="-1,-1;1,1;-1,-1" dur="0.1s" repeatCount="indefinite"/><path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{pStr}" stroke-width="8" stroke-dasharray="2 66"><animate attributeName="stroke-dashoffset" from="68" to="0" dur="1.5s" repeatCount="indefinite" /></path></g><path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{gStr}" stroke-width="2" stroke-dasharray="8 60"><animate attributeName="stroke-dashoffset" from="68" to="0" dur="1.5s" repeatCount="indefinite" /></path></svg>' },
    { "title": "Laser 9 (10s Beeple)", "svg": get_laser_base(19, f'stroke="{dStr}" stroke-width="4"', f'stroke="{gStr}" stroke-width="6" filter="url(#bloom19)"', f'stroke="{pStr}" stroke-width="4" filter="url(#bloom19)"', 'stroke-dasharray="6 62"', 'stroke-dasharray="24 44" stroke-dashoffset="6"', f'<filter id="bloom19"><feGaussianBlur stdDeviation="3" result="blur"/><feComponentTransfer><feFuncA type="linear" slope="4"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>') },
    { "title": "Laser 10 (20s Anadol)", "svg": f'<svg viewBox="0 0 24 24" fill="none" class="svg-icon" stroke-linecap="round" stroke-linejoin="round"><linearGradient id="fluid10L" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="{gStr}"/><stop offset="50%" stop-color="{pStr}"/><stop offset="100%" stop-color="{gStr}"/><animateTransform attributeName="transform" type="translate" values="-1,-1;1,1;-1,-1" dur="1s" repeatCount="indefinite"/></linearGradient><path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{dStr}" stroke-width="4"/><path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="url(#fluid10L)" stroke-width="5" stroke-dasharray="12 56"><animate attributeName="stroke-dashoffset" from="68" to="0" dur="1.5s" repeatCount="indefinite" /></path></svg>' }
]

def render_obsidian_mock(item):
    return f"""
    <div class="mockup-container">
        <div class="mockup-title">{item['title']}</div>
        <div class="obsidian-window">
            <div class="ribbon">
                <!-- Obsidian standard icons (static placeholders) -->
                <div class="ribbon-item">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
                </div>
                <div class="ribbon-item">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                </div>
                <!-- Custom Zenith Bridge SVG Icon -->
                <div class="ribbon-item target-icon" title="Zenith Bridge">
                    {item['svg']}
                </div>
                <div class="ribbon-item">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
                </div>
            </div>
            <div class="obsidian-content">
                <div class="dummy-text"></div>
                <div class="dummy-text short"></div>
                <div class="dummy-text"></div>
            </div>
        </div>
    </div>
"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Obsidian Native View - The Decades Collection</title>
    <style>
        body {{ background: #1a1a1a; color: #fff; font-family: sans-serif; padding: 40px; margin: 0; }}
        h1 {{ text-align: center; color: #ccc; margin-bottom: 50px; text-transform: uppercase; letter-spacing: 2px;}}
        .grid {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 40px; max-width: 1400px; margin: 0 auto;}}
        
        .mockup-container {{ display: flex; flex-direction: column; align-items: center; }}
        .mockup-title {{ margin-bottom: 10px; color: {gStr}; font-weight: bold; text-align: center; font-size: 0.9rem; }}
        
        .obsidian-window {{ 
            width: 250px; 
            height: 200px; 
            background: #2D2D2D; /* Obsidian secondary background */
            border-radius: 8px; 
            border: 1px solid #444; 
            display: flex;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        }}
        
        .ribbon {{
            width: 48px;
            background: #1E1E1E; /* Obsidian ribbon background */
            border-right: 1px solid #333;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding-top: 10px;
        }}
        
        .ribbon-item {{
            width: 36px;
            height: 36px;
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 8px;
            color: #888;
            cursor: pointer;
            transition: background 0.1s, color 0.1s;
        }}
        
        .ribbon-item:hover {{
            background: rgba(255, 255, 255, 0.08);
            color: #e0e0e0;
        }}
        
        .svg-icon {{
            width: 24px;
            height: 24px;
        }}

        .target-icon {{
            background: rgba(142, 197, 64, 0.1); 
            border: 1px solid rgba(142, 197, 64, 0.3);
        }}
        .target-icon:hover {{
            background: rgba(142, 197, 64, 0.2); 
        }}
        
        .obsidian-content {{
            flex-grow: 1;
            padding: 20px;
            background: #2D2D2D; /* Main workspace area */
        }}
        
        .dummy-text {{
            height: 10px;
            background: #3e3e3e;
            border-radius: 4px;
            margin-bottom: 15px;
            width: 100%;
        }}
        .dummy-text.short {{
            width: 60%;
        }}
        
        .section-title {{
            grid-column: 1 / -1;
            text-align: center;
            color: {pStr};
            margin-top: 40px;
            border-bottom: 1px solid #333;
            padding-bottom: 10px;
        }}
    </style>
</head>
<body>
    <h1>Obsidian Native View Preview</h1>
    
    <div class="grid">
        <h2 class="section-title">The Build Variations</h2>
"""

for item in neon_builds:
    html += render_obsidian_mock(item)

html += """
        <h2 class="section-title">The Laser Variations</h2>
"""

for item in tracing_lasers:
    html += render_obsidian_mock(item)

html += """
    </div>
</body>
</html>
"""

with open("preview_obsidian.html", "w") as f:
    f.write(html)
