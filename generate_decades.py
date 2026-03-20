# generate_decades.py

gStr = '#8EC540'
pStr = '#9867C1'
dStr = '#32373C'

def get_neon_base(i, strokes, dash, anim, filters, extra=''):
    return f"""<svg viewBox="0 0 24 24" fill="none" stroke-linejoin="round" stroke-linecap="round">
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
    return f"""<svg viewBox="0 0 24 24" fill="none" stroke-linejoin="round" stroke-linecap="round">
        <defs>{filters}</defs>
        {extra}
        <polygon points="4,6 20,6 4,18 20,18" {trackStroke} />
        {shadow_html}
        <path d="M 4 6 L 20 6 L 4 18 L 20 18" {laserStrokes} {laserDash}>
            <animate attributeName="stroke-dashoffset" from="68" to="0" dur="1.5s" repeatCount="indefinite" />
        </path>
    </svg>"""

neon_builds = [
    { "title": "70s: Milton Glaser (Psychedelic Flow)", "desc": "Flowing, curving offset strokes overlaying each other.", "svg": get_neon_base(1, f'stroke="{gStr}" stroke-width="4"', 'stroke-dasharray="60" stroke-dashoffset="60"', '60; 0; 0; 60; 60', '', f'<path d="M 5 7 L 18 7 L 4 19 L 19 19" stroke="{pStr}" stroke-width="3" stroke-dasharray="60" stroke-dashoffset="60" opacity="0.8"><animate attributeName="stroke-dashoffset" values="60; 0; 0; 60; 60" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite" /></path>') },
    { "title": "70s: Roger Dean (Organic Aura)", "desc": "Ethereal, glowing, organic line work.", "svg": get_neon_base(2, f'stroke="{gStr}" stroke-width="2" filter="url(#glow2)"', 'stroke-dasharray="60" stroke-dashoffset="60"', '60; 0; 0; 60; 60', f'<filter id="glow2"><feGaussianBlur stdDeviation="3" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>', f'<path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{pStr}" stroke-width="8" opacity="0.4" stroke-linecap="round" filter="url(#glow2)" stroke-dasharray="60" stroke-dashoffset="60"><animate attributeName="stroke-dashoffset" values="60; 0; 0; 60; 60" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite" /></path>') },
    { "title": "80s: Neville Brody (Industrial Blocks)", "desc": "Heavy, rigorous geometric segments.", "svg": get_neon_base(3, f'stroke="{gStr}" stroke-width="6" stroke-linecap="square" stroke-dasharray="4 4"', 'stroke-dashoffset="60"', '60; 0; 0; 60; 60', '', f'<path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{pStr}" stroke-width="6" stroke-dasharray="4 4" stroke-dashoffset="64" stroke-linecap="square"><animate attributeName="stroke-dashoffset" values="64; 4; 4; 64; 64" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite" /></path>') },
    { "title": "80s: David Carson (Deconstructed Grunge)", "desc": "Fragmented, overlapping, rule-breaking layouts.", "svg": get_neon_base(4, f'stroke="{gStr}" stroke-width="3" stroke-dasharray="10 5 15 5"', 'stroke-dashoffset="60"', '60; 0; 0; 60; 60', '', f'<path d="M 5 5 L 20 6 L 4 18 L 20 19" stroke="{pStr}" stroke-width="2" stroke-dasharray="60" stroke-dashoffset="60"><animate attributeName="stroke-dashoffset" values="60; 0; 0; 60; 60" dur="3.8s" repeatCount="indefinite" /></path>') },
    { "title": "90s: Stefan Sagmeister (Visceral Raw)", "desc": "Violent, emotional scratch-marks.", "svg": f'<svg viewBox="0 0 24 24" fill="none" stroke-linejoin="round" stroke-linecap="round"><path d="M 5 7 L 19 6 M 4 5 L 20 8 M 5 17 L 19 19 M 4 16 L 20 17 M 19 6 L 5 18 M 20 6 L 4 18" stroke="{pStr}" stroke-width="1.5" stroke-dasharray="40"><animate attributeName="stroke-dashoffset" values="40; 0; 0; 40; 40" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite" /></path><path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{gStr}" stroke-width="2" stroke-dasharray="60" stroke-dashoffset="60"><animate attributeName="stroke-dashoffset" values="60; 0; 0; 60; 60" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite" /></path></svg>' },
    { "title": "90s: Chris Ashworth (Swiss Grit Barcode)", "desc": "Barcode-like vertical stripes masking a gradient.", "svg": get_neon_base(6, f'stroke="url(#grad6)" stroke-width="4" mask="url(#stripes6)"', 'stroke-dasharray="60" stroke-dashoffset="60"', '60; 0; 0; 60; 60', f'<linearGradient id="grad6"><stop offset="0%" stop-color="{gStr}"/><stop offset="100%" stop-color="{pStr}"/></linearGradient><mask id="stripes6"><rect x="0" y="0" width="24" height="24" fill="url(#pattern6)"/></mask><pattern id="pattern6" width="2" height="2" patternUnits="userSpaceOnUse"><rect width="1" height="2" fill="white"/></pattern>') },
    { "title": "00s: Shepard Fairey (Stencil Contrast)", "desc": "Stark stencils with halftone shading.", "svg": get_neon_base(7, f'stroke="{pStr}" stroke-width="3" filter="url(#drop7)"', 'stroke-dasharray="60" stroke-dashoffset="60"', '60; 0; 0; 60; 60', f'<filter id="drop7"><feDropShadow dx="2" dy="2" stdDeviation="0" flood-color="{gStr}"/></filter>') },
    { "title": "00s: Joshua Davis (Generative Vectors)", "desc": "Code-driven, intersecting geometric thin lines.", "svg": f'<svg viewBox="0 0 24 24" fill="none"><path d="M 5 4 L 19 8 L 5 16 L 19 20" stroke="{gStr}" stroke-width="1" stroke-dasharray="60"><animate attributeName="stroke-dashoffset" values="60; 0; 0; 60; 60" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite"/></path><path d="M 5 8 L 19 4 L 5 20 L 19 16" stroke="{pStr}" stroke-width="1" stroke-dasharray="60"><animate attributeName="stroke-dashoffset" values="60; 0; 0; 60; 60" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite"/></path><path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{gStr}" stroke-width="2" stroke-dasharray="60"><animate attributeName="stroke-dashoffset" values="60; 0; 0; 60; 60" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite"/></path></svg>' },
    { "title": "10s: Beeple (Volumetric Glow)", "desc": "Intense 3D-feeling bloom & rim lighting.", "svg": get_neon_base(9, f'stroke="{gStr}" stroke-width="5" filter="url(#bloom9)"', 'stroke-dasharray="60" stroke-dashoffset="60"', '60; 0; 0; 60; 60', f'<filter id="bloom9"><feGaussianBlur stdDeviation="3" result="blur"/><feComponentTransfer><feFuncA type="linear" slope="3"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>', f'<path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{pStr}" stroke-width="2" stroke-dasharray="60" stroke-dashoffset="60"><animate attributeName="stroke-dashoffset" values="60; 0; 0; 60; 60" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite" /></path>') },
    { "title": "20s: Refik Anadol (Data Fluid)", "desc": "Liquid, morphing, sweeping colored fluid gradient.", "svg": get_neon_base(10, f'stroke="url(#fluid10)" stroke-width="5" stroke-linecap="round"', 'stroke-dasharray="60" stroke-dashoffset="60"', '60; 0; 0; 60; 60', f'<linearGradient id="fluid10" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="{gStr}"/><stop offset="50%" stop-color="{pStr}"/><stop offset="100%" stop-color="{gStr}"/><animateTransform attributeName="transform" type="translate" values="-1,-1;1,1;-1,-1" dur="2s" repeatCount="indefinite"/></linearGradient>') }
]

tracing_lasers = [
    { "title": "70s: Milton Glaser", "desc": "Triple-weaver curved green/purple lasers.", "svg": get_laser_base(11, f'stroke="{dStr}" stroke-width="4"', f'stroke="{gStr}" stroke-width="2"', f'stroke="{pStr}" stroke-width="2"', 'stroke-dasharray="8 60"', 'stroke-dasharray="12 56" stroke-dashoffset="2"', '', f'<path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{gStr}" stroke-dasharray="16 52" stroke-dashoffset="4" stroke-width="1"><animate attributeName="stroke-dashoffset" from="72" to="4" dur="1.5s" repeatCount="indefinite" /></path>') },
    { "title": "70s: Roger Dean", "desc": "A glowing green orb dragging a flowing purple aura mist.", "svg": get_laser_base(12, f'stroke="{dStr}" stroke-width="4"', f'stroke="{gStr}" stroke-width="4" stroke-linecap="round"', f'stroke="{pStr}" stroke-width="6" filter="url(#glow12)"', 'stroke-dasharray="2 66"', 'stroke-dasharray="20 48" stroke-dashoffset="2"', f'<filter id="glow12"><feGaussianBlur stdDeviation="3" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>') },
    { "title": "80s: Neville Brody", "desc": "A heavy square laser leaving rigid purple trails.", "svg": get_laser_base(13, f'stroke="{dStr}" stroke-width="4"', f'stroke="{gStr}" stroke-width="6" stroke-linecap="square"', f'stroke="{pStr}" stroke-width="4" stroke-dasharray="4 4"', 'stroke-dasharray="6 62"', 'stroke-dasharray="30 38" stroke-dashoffset="6"', '') },
    { "title": "80s: David Carson", "desc": "Glitching, stuttering, chaotic green/purple laser segments.", "svg": get_laser_base(14, f'stroke="{dStr}" stroke-width="4"', f'stroke="{gStr}" stroke-width="3"', f'stroke="{pStr}" stroke-width="2"', 'stroke-dasharray="4 10 2 52"', 'stroke-dasharray="8 6 4 50" stroke-dashoffset="6"', '') },
    { "title": "90s: Stefan Sagmeister", "desc": "Violent scribbles acting as a racing laser head.", "svg": f'<svg viewBox="0 0 24 24" fill="none" stroke-linejoin="round" stroke-linecap="round"><polygon points="4,6 20,6 4,18 20,18" stroke="{dStr}" stroke-width="4"/><path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{pStr}" stroke-width="8" stroke-dasharray="2 66"><animate attributeName="stroke-dashoffset" from="68" to="0" dur="1.5s" repeatCount="indefinite" /><animate attributeName="stroke-width" values="8;2;6;10;4;8" dur="0.2s" repeatCount="indefinite" /></path><path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{gStr}" stroke-width="2" stroke-dasharray="8 60"><animate attributeName="stroke-dashoffset" from="68" to="0" dur="1.5s" repeatCount="indefinite" /></path></svg>' },
    { "title": "90s: Chris Ashworth", "desc": "Laser prints thick and thin barcode tracking dashed lines.", "svg": get_laser_base(16, f'stroke="{dStr}" stroke-width="4"', f'stroke="{gStr}" stroke-width="4" stroke-dasharray="1 2 3 2"', f'stroke="{pStr}" stroke-width="4" stroke-dasharray="1 4 2 2"', 'stroke-dasharray="8 60"', 'stroke-dasharray="16 52" stroke-dashoffset="8"', '') },
    { "title": "00s: Shepard Fairey", "desc": "Iconic stenciled laser cut with sharp, heavy drop shadow.", "svg": get_laser_base(17, f'stroke="{dStr}" stroke-width="4"', f'stroke="{gStr}" stroke-width="4" stroke-linecap="square" filter="url(#drop17)"', f'stroke="{pStr}" stroke-width="2"', 'stroke-dasharray="8 60"', 'stroke-dasharray="16 52" stroke-dashoffset="8"', f'<filter id="drop17"><feDropShadow dx="2" dy="2" stdDeviation="0" flood-color="#000"/></filter>') },
    { "title": "00s: Joshua Davis", "desc": "Generative geometry; laser head spawns vector spikes.", "svg": f'<svg viewBox="0 0 24 24" fill="none" stroke-linejoin="round"><polygon points="4,6 20,6 4,18 20,18" stroke="{dStr}" stroke-width="4"/><g><animateTransform attributeName="transform" type="translate" values="-1,-1;1,1;-1,-1" dur="0.1s" repeatCount="indefinite"/><path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{pStr}" stroke-width="8" stroke-dasharray="2 66"><animate attributeName="stroke-dashoffset" from="68" to="0" dur="1.5s" repeatCount="indefinite" /></path></g><path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{gStr}" stroke-width="2" stroke-dasharray="8 60"><animate attributeName="stroke-dashoffset" from="68" to="0" dur="1.5s" repeatCount="indefinite" /></path></svg>' },
    { "title": "10s: Beeple", "desc": "Thick, blindingly bright volumetric green/purple lens flare.", "svg": get_laser_base(19, f'stroke="{dStr}" stroke-width="4"', f'stroke="{gStr}" stroke-width="6" filter="url(#bloom19)"', f'stroke="{pStr}" stroke-width="4" filter="url(#bloom19)"', 'stroke-dasharray="6 62"', 'stroke-dasharray="24 44" stroke-dashoffset="6"', f'<filter id="bloom19"><feGaussianBlur stdDeviation="3" result="blur"/><feComponentTransfer><feFuncA type="linear" slope="4"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>') },
    { "title": "20s: Refik Anadol", "desc": "Swirling, continuous liquid data fluid transitioning states.", "svg": f'<svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round"><linearGradient id="fluid10L" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="{gStr}"/><stop offset="50%" stop-color="{pStr}"/><stop offset="100%" stop-color="{gStr}"/><animateTransform attributeName="transform" type="translate" values="-1,-1;1,1;-1,-1" dur="1s" repeatCount="indefinite"/></linearGradient><path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{dStr}" stroke-width="4"/><path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="url(#fluid10L)" stroke-width="5" stroke-dasharray="12 56"><animate attributeName="stroke-dashoffset" from="68" to="0" dur="1.5s" repeatCount="indefinite" /></path></svg>' }
]

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The Decades Collection (Brand Colors Only)</title>
    <style>
        body {{ background: #050505; color: #fff; font-family: sans-serif; padding: 40px; margin: 0; }}
        h1 {{ text-align: center; color: {gStr}; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 2px;}}
        .header-sub {{ text-align: center; color: #888; margin-bottom: 50px; font-weight: bold; letter-spacing: 1px; }}
        h2 {{ border-bottom: 2px solid #333; padding-bottom: 10px; margin-top: 60px; color: {pStr}; }}
        .grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 30px; max-width: 1200px; margin: 0 auto;}}
        .card {{ background: #111; border: 1px solid #222; border-radius: 12px; padding: 30px; display: flex; flex-direction: column; align-items: center; transition: transform 0.2s, border-color 0.2s; }}
        .card:hover {{ transform: translateY(-5px); border-color: {gStr}; box-shadow: 0 5px 20px rgba(152, 103, 193, 0.2);}}
        .icon-box {{ width: 140px; height: 140px; margin-bottom: 20px; color: #fff; display: flex; align-items: center; justify-content: center; }}
        .title {{ font-size: 1.1rem; font-weight: 900; text-align: center; margin-bottom: 10px; color: #fff; line-height: 1.3; text-transform: uppercase; letter-spacing: 1px; }}
        .desc {{ font-size: 0.9rem; color: #aaa; text-align: center; line-height: 1.5; }}
    </style>
</head>
<body>
    <h1>Zenith Bridge: The Decades Collection</h1>
    <div class="header-sub">Strictly GREEN & PURPLE | 70s to 20s Artist Inspirations</div>
    
    <h2>The Build: Decades Collection</h2>
    <div class="grid">
"""

for item in neon_builds:
    html += f'<div class="card"><div class="icon-box">{item["svg"]}</div><div class="title">{item["title"]}</div><div class="desc">{item["desc"]}</div></div>\n'

html += """
    </div>

    <h2>The Laser: Decades Collection</h2>
    <div class="grid">
"""

for item in tracing_lasers:
    html += f'<div class="card"><div class="icon-box">{item["svg"]}</div><div class="title">{item["title"]}</div><div class="desc">{item["desc"]}</div></div>\n'

html += """
    </div>
</body>
</html>
"""

with open("preview_decades.html", "w") as f:
    f.write(html)
