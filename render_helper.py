import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_fonts():
    try:
        f_title = ImageFont.truetype('segoeui.ttf', 13)
        f_url = ImageFont.truetype('segoeui.ttf', 13)
        f_nav = ImageFont.truetype('segoeui.ttf', 16)
        f_nav_bold = ImageFont.truetype('segoeuib.ttf', 16)
        f_head = ImageFont.truetype('segoeuib.ttf', 24)
        f_sub = ImageFont.truetype('segoeui.ttf', 14)
        f_body = ImageFont.truetype('segoeui.ttf', 13)
        f_bold = ImageFont.truetype('segoeuib.ttf', 13)
        f_mono = ImageFont.truetype('consola.ttf', 13)
        f_mono_bold = ImageFont.truetype('consolab.ttf', 13)
    except:
        f_default = ImageFont.load_default()
        return (f_default,) * 10
    return f_title, f_url, f_nav, f_nav_bold, f_head, f_sub, f_body, f_bold, f_mono, f_mono_bold

def draw_browser_chrome(draw, width, height, title, url):
    f_title, f_url = get_fonts()[:2]
    # Window Header
    draw.rectangle([0, 0, width, 40], fill='#dfe1e5')
    # Window Buttons
    draw.ellipse([14, 15, 26, 27], fill='#ed6a5f')
    draw.ellipse([34, 15, 46, 27], fill='#f5bf4f')
    draw.ellipse([54, 15, 66, 27], fill='#62c554')

    # Tab
    draw.rounded_rectangle([80, 8, 300, 40], radius=8, fill='#ffffff')
    draw.text((105, 14), title[:25], fill='#3c4043', font=f_title)
    draw.text((280, 14), "×", fill='#5f6368', font=f_title)

    # Address Bar Area
    draw.rectangle([0, 40, width, 82], fill='#ffffff')
    draw.line([0, 82, width, 82], fill='#dadce0', width=1)

    # Nav controls (back, forward, refresh)
    draw.text((18, 52), "←", fill='#5f6368', font=f_url)
    draw.text((45, 52), "→", fill='#b0b3b8', font=f_url)
    draw.text((72, 52), "↻", fill='#5f6368', font=f_url)

    # URL input box
    draw.rounded_rectangle([105, 47, width - 60, 75], radius=14, fill='#f1f3f4')
    draw.text((120, 52), "🔒", fill='#1e8e3e', font=f_url)
    draw.text((142, 52), url, fill='#202124', font=f_url)

    # Extensions / profile icon
    draw.ellipse([width - 40, 50, width - 20, 70], fill='#0d6efd')
    draw.text((width - 33, 52), "A", fill='#ffffff', font=f_title)

def draw_navbar(draw, width, active_tab="Home", username=None):
    f_nav, f_nav_bold = get_fonts()[2:4]
    draw.rectangle([0, 83, width, 145], fill='#00ced1') # darkturquoise
    draw.text((40, 98), "Dealerships", fill='#000000', font=f_nav_bold)

    tabs = [("Home", 220), ("About Us", 300), ("Contact Us", 400)]
    for name, x in tabs:
        font = f_nav_bold if name == active_tab else f_nav
        fill = '#000000' if name == active_tab else '#333333'
        draw.text((x, 102), name, fill=fill, font=font)
        if name == active_tab:
            draw.line([x, 126, x + int(draw.textlength(name, font=font)), 126], fill='#000000', width=2)

    # Right side: Login/Register or Username/Logout
    if username:
        draw.text((width - 240, 102), username, fill='#000000', font=f_nav_bold)
        draw.rounded_rectangle([width - 120, 96, width - 40, 132], radius=4, fill='#dc3545')
        draw.text((width - 105, 104), "Logout", fill='#ffffff', font=f_nav)
    else:
        draw.rounded_rectangle([width - 200, 96, width - 125, 132], radius=4, fill='#0d6efd')
        draw.text((width - 185, 104), "Login", fill='#ffffff', font=f_nav)
        draw.rounded_rectangle([width - 110, 96, width - 35, 132], radius=4, fill='#198754')
        draw.text((width - 100, 104), "Register", fill='#ffffff', font=f_nav)

def save_dual(img, name):
    png_path = os.path.join(BASE_DIR, f"{name}.png")
    jpg_path = os.path.join(BASE_DIR, f"{name}.jpeg")
    img.save(png_path, 'PNG')
    img.save(jpg_path, 'JPEG', quality=95)
    print(f"Generated {name}.png and {name}.jpeg")

print("Rendering helper initialized")
