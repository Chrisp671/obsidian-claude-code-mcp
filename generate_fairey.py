# generate_fairey.py

gStr = '#8EC540'
pStr = '#9867C1'
dStr = '#32373C'

def get_svg_base(title, contents, desc=""):
    return {
        "title": title,
        "desc": desc,
        "svg": f"""<svg viewBox="0 0 24 24" fill="none" class="svg-icon" stroke-linejoin="round" stroke-linecap="round">
            {contents}
        </svg>"""
    }

# Halftone pattern generator for reuse
half_green = f'<pattern id="htG" width="3" height="3" patternUnits="userSpaceOnUse"><circle cx="1.5" cy="1.5" r="1" fill="{gStr}"/></pattern>'
half_purple = f'<pattern id="htP" width="4" height="4" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.5" fill="{pStr}"/></pattern>'
half_slate = f'<pattern id="htD" width="2" height="2" patternUnits="userSpaceOnUse"><rect width="1" height="1" fill="{dStr}"/></pattern>'

# 20 Variations
variations = []

# 1. The Classic Halftone
variations.append(get_svg_base(
    "1. The Classic Halftone",
    f"""<defs>{half_green}</defs>
    <path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="url(#htG)" stroke-width="6" stroke-linecap="square" />
    <path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{pStr}" stroke-width="2" stroke-linecap="square">
        <animate attributeName="stroke-dasharray" values="0 60; 60 0; 0 60" dur="4s" repeatCount="indefinite" />
    </path>""",
    "Heavy purple outline containing a thick green halftone pattern."
))

# 2. The Propaganda Sunburst
variations.append(get_svg_base(
    "2. The Propaganda Sunburst",
    f"""
    <g stroke="{dStr}" stroke-width="1.5">
        <line x1="12" y1="12" x2="0" y2="0" /><line x1="12" y1="12" x2="12" y2="0" /><line x1="12" y1="12" x2="24" y2="0" />
        <line x1="12" y1="12" x2="24" y2="12" /><line x1="12" y1="12" x2="24" y2="24" /><line x1="12" y1="12" x2="12" y2="24" />
        <line x1="12" y1="12" x2="0" y2="24" /><line x1="12" y1="12" x2="0" y2="12" />
        <animateTransform attributeName="transform" type="rotate" from="0 12 12" to="360 12 12" dur="15s" repeatCount="indefinite" />
    </g>
    <path d="M 4 5 L 20 5 L 4 19 L 20 19" stroke="{pStr}" stroke-width="6" stroke-linecap="square" />
    <path d="M 4 5 L 20 5 L 4 19 L 20 19" stroke="{gStr}" stroke-width="2" stroke-dasharray="8 4" stroke-linecap="square">
         <animate attributeName="stroke-dashoffset" from="12" to="0" dur="0.5s" repeatCount="indefinite" />
    </path>""",
    "Rotating constructivist beams behind a sharp stencil Z."
))

# 3. The Obey Drop
variations.append(get_svg_base(
    "3. The Obey Drop",
    f"""<path d="M 6 8 L 20 8 L 6 20 L 20 20" stroke="{pStr}" stroke-width="5" stroke-linecap="square" />
    <path d="M 4 6 L 18 6 L 4 18 L 18 18" stroke="{gStr}" stroke-width="5" stroke-linecap="square" stroke-dasharray="60">
        <animate attributeName="stroke-dashoffset" values="60;0;0;60;60" dur="3s" keyTimes="0; 0.3; 0.7; 1; 1" repeatCount="indefinite" />
    </path>""",
    "Huge, brutalist solid drop shadow with animated foreground."
))

# 4. The Stencil Cut
variations.append(get_svg_base(
    "4. The Stencil Cut",
    f"""<path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{gStr}" stroke-width="6" stroke-linecap="square" stroke-dasharray="4 2" />
    <path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{pStr}" stroke-width="2" stroke-linecap="square" stroke-dasharray="4 2" stroke-dashoffset="6">
        <animate attributeName="stroke-dashoffset" from="12" to="0" dur="0.5s" repeatCount="indefinite" />
    </path>""",
    "Fragmented gaps imitating a spray-paint stencil bridge."
))

# 5. The Distressed Print (Misregistration)
variations.append(get_svg_base(
    "5. The Distressed Print",
    f"""<path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{pStr}" stroke-width="4" stroke-linecap="square" opacity="0.8">
        <animateTransform attributeName="transform" type="translate" values="0.5,0.5; -0.5,0; 0,-0.5; 0.5,0.5" dur="0.15s" repeatCount="indefinite" />
    </path>
    <path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{gStr}" stroke-width="4" stroke-linecap="square" opacity="0.8">
        <animateTransform attributeName="transform" type="translate" values="-0.5,-0.5; 0.5,0; 0,0.5; -0.5,-0.5" dur="0.2s" repeatCount="indefinite" />
    </path>""",
    "Lithographic misregistration jitter effect, pure green and purple."
))

# 6. The Repeating Echo
variations.append(get_svg_base(
    "6. The Repeating Echo",
    f"""
    <path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{dStr}" stroke-width="8" stroke-linecap="square" />
    <path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{pStr}" stroke-width="4" stroke-linecap="square" />
    <path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{gStr}" stroke-width="1" stroke-linecap="square" stroke-dasharray="10 5">
        <animate attributeName="stroke-dashoffset" from="15" to="0" dur="0.5s" repeatCount="indefinite" />
    </path>""",
    "Concentric sharp borders radiating inward like a target."
))

# 7. The Constructivist Gear
variations.append(get_svg_base(
    "7. The Constructivist Gear",
    f"""
    <circle cx="12" cy="12" r="10" stroke="{dStr}" stroke-width="3" stroke-dasharray="2 2" />
    <polygon points="12,2 14,8 20,8 15,12 17,18 12,14 7,18 9,12 4,8 10,8" fill="{gStr}" opacity="0.2">
        <animateTransform attributeName="transform" type="rotate" from="0 12 12" to="360 12 12" dur="6s" repeatCount="indefinite" />
    </polygon>
    <path d="M 6 8 L 18 8 L 6 16 L 18 16" stroke="{pStr}" stroke-width="4" stroke-linecap="square" />""",
    "Harsh star/gear motif spinning behind the rigid stencil."
))

# 8. The Overprint Halftone
variations.append(get_svg_base(
    "8. The Overprint Halftone",
    f"""<defs>{half_green}{half_purple}</defs>
    <path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="url(#htG)" stroke-width="8" stroke-linecap="square" />
    <path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="url(#htP)" stroke-width="4" stroke-linecap="square">
        <animate attributeName="stroke-dasharray" values="60 0; 0 60; 60 0" dur="3s" repeatCount="indefinite" />
    </path>""",
    "Two halftone screens overlapping to create dynamic moiré."
))

# 9. The Isometric Block
variations.append(get_svg_base(
    "9. The Isometric Block",
    f"""
    <path d="M 4 8 L 18 8 L 4 20 L 18 20" stroke="{dStr}" stroke-width="6" stroke-linecap="square" />
    <path d="M 5 7 L 19 7 L 5 19 L 19 19" stroke="{pStr}" stroke-width="4" stroke-linecap="square" />
    <path d="M 6 6 L 20 6 L 6 18 L 20 18" stroke="{gStr}" stroke-width="2" stroke-linecap="square" stroke-dasharray="60">
        <animate attributeName="stroke-dashoffset" values="60;0;0;60;60" dur="3s" keyTimes="0;0.3;0.7;1;1" repeatCount="indefinite" />
    </path>""",
    "Faux 3D rigid block structure heavily stacked."
))

# 10. The Snapping Animation
variations.append(get_svg_base(
    "10. The Snapping Propaganda",
    f"""<path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{pStr}" stroke-width="4" stroke-linecap="square" stroke-dasharray="64" stroke-dashoffset="64">
        <animate attributeName="stroke-dashoffset" values="64;48;32;16;0;0;64" dur="1s" calcMode="discrete" repeatCount="indefinite" />
    </path>
    <path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{gStr}" stroke-width="2" stroke-linecap="square" stroke-dasharray="64" stroke-dashoffset="64">
        <animate attributeName="stroke-dashoffset" values="64;64;48;32;16;0;0;64" dur="1s" calcMode="discrete" repeatCount="indefinite" />
    </path>""",
    "No smooth interpolation. Harsh, stop-motion discrete snaps."
))

# 11. The Halftone Track Laser
variations.append(get_svg_base(
    "11. The Halftone Track",
    f"""<defs>{half_purple}</defs>
    <polygon points="4,6 20,6 4,18 20,18" stroke="url(#htP)" stroke-width="4" stroke-linejoin="miter" />
    <path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{gStr}" stroke-width="6" stroke-linecap="square" stroke-dasharray="6 60">
        <animate attributeName="stroke-dashoffset" from="66" to="0" dur="1.5s" repeatCount="indefinite" />
    </path>""",
    "Heavy solid green block sliding over a purple halftone grid."
))

# 12. The Cutout Void
variations.append(get_svg_base(
    "12. The Cutout Void",
    f"""<rect x="2" y="2" width="20" height="20" fill="{dStr}" />
    <path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="#1a1a1a" stroke-width="4" stroke-linecap="square" />
    <path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{gStr}" stroke-width="4" stroke-linecap="square" stroke-dasharray="8 60">
        <animate attributeName="stroke-dashoffset" from="68" to="0" dur="1s" repeatCount="indefinite" />
    </path>
    <path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{pStr}" stroke-width="4" stroke-linecap="square" stroke-dasharray="2 66">
        <animate attributeName="stroke-dashoffset" from="68" to="0" dur="1s" repeatCount="indefinite" />
    </path>""",
    "A solid background with the Z punched out as a void, filling with color."
))

# 13. The Offset Echo Laser
variations.append(get_svg_base(
    "13. Offset Echo Laser",
    f"""
    <path d="M 4 5 L 20 5 L 4 17 L 20 17" stroke="{dStr}" stroke-width="3" stroke-linecap="square" stroke-dasharray="10 60">
        <animate attributeName="stroke-dashoffset" from="70" to="0" dur="1.5s" repeatCount="indefinite" />
    </path>
    <path d="M 5 7 L 21 7 L 5 19 L 21 19" stroke="{pStr}" stroke-width="3" stroke-linecap="square" stroke-dasharray="10 60">
        <animate attributeName="stroke-dashoffset" from="70" to="0" dur="1.5s" repeatCount="indefinite" />
    </path>
    <path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{gStr}" stroke-width="3" stroke-linecap="square" stroke-dasharray="10 60">
        <animate attributeName="stroke-dashoffset" from="70" to="0" dur="1.5s" repeatCount="indefinite" />
    </path>""",
    "3 solid, hard-edged laser bars running parallel and overlapping."
))

# 14. The Halftone Scan
variations.append(get_svg_base(
    "14. The Halftone Scan",
    f"""<defs>{half_green}</defs>
    <rect x="0" y="0" width="24" height="24" fill="url(#htG)" />
    <path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{pStr}" stroke-width="6" stroke-linecap="square" stroke-dasharray="60">
        <animate attributeName="stroke-dashoffset" values="60; 0; 0; 60; 60" dur="4s" keyTimes="0; 0.25; 0.6; 0.85; 1" repeatCount="indefinite" />
    </path>""",
    "Solid purple bar erasing the green halftone background."
))

# 15. The Block Bounce
variations.append(get_svg_base(
    "15. The Block Bounce",
    f"""<polygon points="4,6 20,6 4,18 20,18" stroke="{pStr}" stroke-width="3" stroke-linecap="square" />
    <path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{gStr}" stroke-width="8" stroke-linecap="square" stroke-dasharray="4 64">
        <animate attributeName="stroke-dashoffset" from="68" to="0" dur="0.8s" repeatCount="indefinite" calcMode="discrete" values="68; 52; 34; 16; 0" />
    </path>""",
    "A massive square block snapping rigidly corner-to-corner."
))

# 16. The Stencil Reveal
variations.append(get_svg_base(
    "16. The Stencil Reveal",
    f"""<defs>{half_purple}</defs>
    <path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="url(#htP)" stroke-width="6" stroke-linecap="square" />
    <path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{gStr}" stroke-width="6" stroke-linecap="square" stroke-dasharray="60" stroke-dashoffset="60">
        <animate attributeName="stroke-dashoffset" values="60; 0; 0; -60; -60" dur="3s" keyTimes="0;0.3;0.6;0.9;1" repeatCount="indefinite" />
    </path>""",
    "Solid green block retracts to reveal purple halftone underneath."
))

# 17. The Retro Pulse
variations.append(get_svg_base(
    "17. The Retro Pulse",
    f"""<defs>{half_green}</defs>
    <path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="url(#htG)" stroke-width="6" stroke-linecap="square" />
    <path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{pStr}" stroke-width="6" stroke-linecap="square">
        <animate attributeName="opacity" values="1;0;1" dur="0.2s" calcMode="discrete" repeatCount="indefinite" />
    </path>""",
    "Hyper-aggressive frame-by-frame color swap (strobe)."
))

# 18. The Propaganda Shift
variations.append(get_svg_base(
    "18. The Propaganda Shift",
    f"""<path d="M 5 6 L 19 6 L 5 18 L 19 18" stroke="{gStr}" stroke-width="6" stroke-linecap="square">
        <animate attributeName="stroke" values="{gStr}; {pStr}; {gStr}" dur="1s" calcMode="discrete" repeatCount="indefinite" />
        <animate attributeName="stroke-dasharray" values="60; 30 30; 60" dur="1s" calcMode="discrete" repeatCount="indefinite" />
    </path>""",
    "Shape and color mutate jaggedly on a rigid timer loop."
))

# 19. The Worn Edge
variations.append(get_svg_base(
    "19. The Worn Edge",
    f"""<polygon points="5,5 19,5 19,7 7,7 17,17 19,17 19,19 5,19 5,17 15,17 5,7" fill="{pStr}" />
    <path d="M 6 6 L 18 6 L 6 18 L 18 18" stroke="{gStr}" stroke-width="2" stroke-dasharray="4 60">
        <animate attributeName="stroke-dashoffset" from="64" to="0" dur="1s" repeatCount="indefinite" />
    </path>""",
    "Polygon base imitating torn paper edges. Small laser passes inside."
))

# 20. The Triple Overprint
variations.append(get_svg_base(
    "20. The Triple Overprint",
    f"""
    <path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{dStr}" stroke-width="8" stroke-dasharray="8 8">
        <animate attributeName="stroke-dashoffset" from="16" to="0" dur="1s" repeatCount="indefinite" />
    </path>
    <path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{pStr}" stroke-width="4" stroke-dasharray="12 12">
        <animate attributeName="stroke-dashoffset" from="24" to="0" dur="1.5s" repeatCount="indefinite" />
    </path>
    <path d="M 4 6 L 20 6 L 4 18 L 20 18" stroke="{gStr}" stroke-width="2" stroke-dasharray="24 24">
        <animate attributeName="stroke-dashoffset" from="48" to="0" dur="2s" repeatCount="indefinite" />
    </path>""",
    "Three differing dashed strokes moving at different modulo speeds."
))

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The Fairey Collection: Obsidian Native</title>
    <style>
        body {{ background: #1a1a1a; color: #fff; font-family: sans-serif; padding: 40px; margin: 0; }}
        h1 {{ text-align: center; color: #ccc; margin-bottom: 50px; text-transform: uppercase; letter-spacing: 2px;}}
        .grid {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 40px; max-width: 1400px; margin: 0 auto;}}
        
        .mockup-container {{ display: flex; flex-direction: column; align-items: center; }}
        .mockup-title {{ margin-bottom: 5px; color: {pStr}; font-weight: bold; text-align: center; font-size: 0.9rem; max-width: 250px; line-height: 1.2; text-transform: uppercase;}}
        .mockup-desc {{ margin-bottom: 15px; color: #888; text-align: center; font-size: 0.75rem; max-width: 250px; line-height: 1.3;}}
        
        .obsidian-window {{ 
            width: 250px; 
            height: 200px; 
            background: #2D2D2D; 
            border-radius: 8px; 
            border: 1px solid #444; 
            display: flex;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        }}
        
        .ribbon {{
            width: 48px;
            background: #1E1E1E;
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
        
        .svg-icon {{ width: 24px; height: 24px; }}
        .target-icon {{ background: rgba(142, 197, 64, 0.1); border: 1px solid rgba(142, 197, 64, 0.3); }}
        .target-icon:hover {{ background: rgba(142, 197, 64, 0.2); }}
        
        .obsidian-content {{
            flex-grow: 1;
            padding: 20px;
            background: #2D2D2D;
        }}
        
        .dummy-text {{ height: 10px; background: #3e3e3e; border-radius: 4px; margin-bottom: 15px; width: 100%; }}
        .dummy-text.short {{ width: 60%; }}
    </style>
</head>
<body>
    <h1>"OBEY" The Grid - Shepard Fairey Collection</h1>
    <div class="grid">
"""

for item in variations:
    html += f"""
    <div class="mockup-container">
        <div class="mockup-title">{item['title']}</div>
        <div class="mockup-desc">{item['desc']}</div>
        <div class="obsidian-window">
            <div class="ribbon">
                <div class="ribbon-item">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
                </div>
                <div class="ribbon-item">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                </div>
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

html += """
    </div>
</body>
</html>
"""

with open("preview_fairey.html", "w") as f:
    f.write(html)
