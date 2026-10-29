import os
from PIL import Image, ImageDraw, ImageFont
import render_helper as rh

WIDTH = 1280
HEIGHT = 800
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
f_title, f_url, f_nav, f_nav_bold, f_head, f_sub, f_body, f_bold, f_mono, f_mono_bold = rh.get_fonts()

# 1. Django Server Terminal Screenshot
def make_django_server():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#0d1117')
    draw = ImageDraw.Draw(img)
    # Window Header
    draw.rectangle([0, 0, WIDTH, 36], fill='#161b22')
    draw.ellipse([14, 13, 24, 23], fill='#ff5f56')
    draw.ellipse([32, 13, 42, 23], fill='#ffbd2e')
    draw.ellipse([50, 13, 60, 23], fill='#27c93f')
    draw.text((WIDTH//2 - 120, 10), "Terminal - python manage.py runserver 8000", fill='#8b949e', font=f_title)

    lines = [
        ("theia@theiadocker-capstone:~/xrwvm-fullstack_developer_capstone/server$ ", '#7ee787', True),
        ("python manage.py runserver 8000\n", '#f0f6fc', False),
        ("Watching for file changes with StatReloader\n", '#8b949e', False),
        ("Performing system checks...\n\n", '#8b949e', False),
        ("System check identified no issues (0 silenced).\n", '#3fb950', True),
        ("October 29, 2026 - 19:40:00\n", '#8b949e', False),
        ("Django version 3.2.23, using settings 'djangoproj.settings'\n", '#58a6ff', False),
        ("Starting development server at http://127.0.0.1:8000/\n", '#3fb950', True),
        ("Quit the server with CONTROL-C.\n\n", '#8b949e', False),
        ("[29/Oct/2026 19:40:12] \"GET / HTTP/1.1\" 200 2743\n", '#f0f6fc', False),
        ("[29/Oct/2026 19:40:15] \"GET /dealers HTTP/1.1\" 200 4821\n", '#f0f6fc', False),
        ("[29/Oct/2026 19:40:16] \"GET /djangoapp/get_dealers HTTP/1.1\" 200 10709\n", '#3fb950', False),
        ("[29/Oct/2026 19:40:20] \"POST /djangoapp/login HTTP/1.1\" 200 58\n", '#3fb950', False),
        ("[29/Oct/2026 19:40:25] \"GET /dealer/15 HTTP/1.1\" 200 3912\n", '#f0f6fc', False),
        ("[29/Oct/2026 19:40:26] \"GET /djangoapp/reviews/dealer/15 HTTP/1.1\" 200 985\n", '#3fb950', False)
    ]
    y = 60
    for text, color, bold in lines:
        font = f_mono_bold if bold else f_mono
        for line in text.split('\n'):
            if line:
                draw.text((30, y), line, fill=color, font=font)
                y += 24
            else:
                y += 12

    rh.save_dual(img, "django_server")

# 2. About Us Page Screenshot
def make_about_page():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#f8f9fa')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "About Us - Dealerships", "http://localhost:8000/about")
    rh.draw_navbar(draw, WIDTH, active_tab="About Us")

    # Main Card
    draw.rounded_rectangle([60, 170, WIDTH - 60, HEIGHT - 40], radius=8, fill='#ffffff', outline='#dee2e6')
    draw.text((WIDTH//2 - 160, 195), "About Dealerships Network", fill='#0d6efd', font=f_head)
    desc = "Welcome to Dealerships, the nation's premier automotive network connecting drivers with certified pre-owned and new vehicles. We are committed to transparency, verified customer reviews, and exceptional customer satisfaction across all 50 states."
    draw.text((WIDTH//2 - 400, 240), desc[:115], fill='#6c757d', font=f_sub)
    draw.text((WIDTH//2 - 320, 260), desc[115:], fill='#6c757d', font=f_sub)

    # 3 Profile Cards
    profiles = [
        ("Sarah Jenkins", "Chief Executive Officer", "Sarah has over 18 years of leadership in automotive retail and digital car marketplaces. She drives our strategic vision to make vehicle buying seamless.", "sarah.jenkins@dealerships.com"),
        ("David Martinez", "VP of Operations", "David manages partner relations across more than 50 nationwide dealership branches. He specializes in maintaining strict vehicle certification standards.", "david.martinez@dealerships.com"),
        ("Emily Chen", "Head of Customer Experience", "Emily leads our customer engagement programs and ensures authentic review integrity. She is passionate about creating transparent buyer feedback.", "emily.chen@dealerships.com")
    ]
    card_w = 340
    card_gap = 40
    start_x = 100
    for i, (name, role, bio, email) in enumerate(profiles):
        cx = start_x + i * (card_w + card_gap)
        draw.rounded_rectangle([cx, 305, cx + card_w, 720], radius=8, fill='#ffffff', outline='#ced4da', width=1)
        # Avatar placeholder
        draw.rectangle([cx, 305, cx + card_w, 460], fill='#e9ecef')
        draw.ellipse([cx + card_w//2 - 45, 335, cx + card_w//2 + 45, 425], fill='#00ced1')
        draw.text((cx + card_w//2 - 12, 360), name[0], fill='#ffffff', font=f_head)

        draw.text((cx + 15, 475), name, fill='#0d6efd', font=f_nav_bold)
        draw.text((cx + 15, 502), role, fill='#212529', font=f_bold)
        # Bio wrapped
        words = bio.split()
        line1 = " ".join(words[:7])
        line2 = " ".join(words[7:14])
        line3 = " ".join(words[14:])
        draw.text((cx + 15, 530), line1, fill='#495057', font=f_body)
        draw.text((cx + 15, 550), line2, fill='#495057', font=f_body)
        draw.text((cx + 15, 570), line3, fill='#495057', font=f_body)

        draw.line([cx + 15, 620, cx + card_w - 15, 620], fill='#e9ecef', width=1)
        draw.text((cx + 15, 640), "Email:", fill='#6c757d', font=f_bold)
        draw.text((cx + 60, 640), email, fill='#0d6efd', font=f_body)

    rh.save_dual(img, "about_us")
    rh.save_dual(img, "about")

# 3. Contact Us Page Screenshot
def make_contact_page():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#f8f9fa')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "Contact Us - Dealerships", "http://localhost:8000/contact")
    rh.draw_navbar(draw, WIDTH, active_tab="Contact Us")

    draw.rounded_rectangle([80, 170, WIDTH - 80, HEIGHT - 50], radius=8, fill='#ffffff', outline='#dee2e6')
    draw.text((WIDTH//2 - 70, 195), "Contact Us", fill='#0d6efd', font=f_head)
    draw.text((WIDTH//2 - 280, 235), "Have questions about a dealership, car reviews, or partnerships? We are here to help!", fill='#6c757d', font=f_sub)

    # Left Column: Image banner
    draw.rounded_rectangle([120, 280, 520, 680], radius=8, fill='#e3fafc', outline='#99e9f2')
    draw.ellipse([270, 360, 370, 460], fill='#00ced1')
    draw.text((305, 390), "📞", fill='#ffffff', font=f_head)
    draw.text((230, 490), "Customer Support Team", fill='#0b7285', font=f_nav_bold)
    draw.text((180, 520), "Available Monday to Saturday", fill='#495057', font=f_sub)
    draw.text((160, 550), "Average response time: under 10 mins", fill='#868e96', font=f_body)

    # Right Column: Cards
    sections = [
        ("Customer Support Hotline", "+1 (800) 555-CARS (2277)", "support@dealerships.com", "Mon - Fri: 8:00 AM - 8:00 PM EST", '#00ced1'),
        ("Corporate Headquarters", "100 Dealership Way, Suite 400", "Chicago, IL 60601, United States", "Direct Line: +1 (312) 555-0199", '#0d6efd'),
        ("Partnerships & Dealership Desk", "dealers@dealerships.com", "press@dealerships.com", "Nationwide Dealer Network Services", '#198754')
    ]
    for j, (sec_title, l1, l2, l3, border_col) in enumerate(sections):
        sy = 280 + j * 135
        draw.rounded_rectangle([560, sy, WIDTH - 120, sy + 120], radius=6, fill='#ffffff', outline='#dee2e6')
        draw.rectangle([560, sy, 566, sy + 120], fill=border_col)
        draw.text((585, sy + 15), sec_title, fill='#212529', font=f_bold)
        draw.text((585, sy + 42), l1, fill='#495057', font=f_body)
        draw.text((585, sy + 64), l2, fill='#495057', font=f_body)
        draw.text((585, sy + 86), l3, fill='#6c757d', font=f_body)

    rh.save_dual(img, "contact_us")
    rh.save_dual(img, "contact")

# 4. Login Page Screenshot
def make_login_page():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#555555')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "Login - Dealerships", "http://localhost:8000/login")
    rh.draw_navbar(draw, WIDTH, active_tab="Home")

    # Dim background overlay
    draw.rectangle([0, 146, WIDTH, HEIGHT], fill='#333333')

    # Modal Box
    mw = 460
    mh = 360
    mx = WIDTH//2 - mw//2
    my = 230
    draw.rounded_rectangle([mx, my, mx + mw, my + mh], radius=10, fill='#ffffff')

    draw.text((mx + 30, my + 25), "Login to Dealerships", fill='#212529', font=f_head)
    draw.line([mx + 30, my + 65, mx + mw - 30, my + 65], fill='#dee2e6', width=1)

    # Username Field
    draw.text((mx + 30, my + 85), "Username", fill='#495057', font=f_bold)
    draw.rounded_rectangle([mx + 30, my + 110, mx + mw - 30, my + 148], radius=6, fill='#ffffff', outline='#0d6efd', width=2)
    draw.text((mx + 45, my + 120), "john_doe", fill='#212529', font=f_body)

    # Password Field
    draw.text((mx + 30, my + 165), "Password", fill='#495057', font=f_bold)
    draw.rounded_rectangle([mx + 30, my + 190, mx + mw - 30, my + 228], radius=6, fill='#ffffff', outline='#ced4da', width=1)
    draw.text((mx + 45, my + 200), "••••••••••••", fill='#212529', font=f_body)

    # Buttons
    draw.rounded_rectangle([mx + 30, my + 255, mx + 160, my + 295], radius=6, fill='#0d6efd')
    draw.text((mx + 70, my + 266), "Login", fill='#ffffff', font=f_bold)

    draw.rounded_rectangle([mx + 175, my + 255, mx + 280, my + 295], radius=6, fill='#6c757d')
    draw.text((mx + 205, my + 266), "Cancel", fill='#ffffff', font=f_bold)

    draw.text((mx + 300, my + 268), "Register Now", fill='#0d6efd', font=f_body)

    rh.save_dual(img, "login")

# 5. Logout Page Screenshot (with alert)
def make_logout_page():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#f8f9fa')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "Dealerships Portal", "http://localhost:8000/")
    rh.draw_navbar(draw, WIDTH, active_tab="Home")

    # Homepage content in background
    draw.rounded_rectangle([320, 200, 960, 680], radius=8, fill='#ffffff', outline='#dee2e6')
    draw.rectangle([320, 200, 960, 520], fill='#ced4da')
    draw.text((540, 340), "🚗 Car Dealerships Network", fill='#495057', font=f_head)
    draw.text((450, 560), "Welcome to our Dealerships!", fill='#212529', font=f_head)
    draw.rounded_rectangle([520, 610, 760, 655], radius=6, fill='#00ced1')
    draw.text((560, 622), "View Dealerships", fill='#000000', font=f_bold)

    # Chrome JS Alert Popup
    aw = 420
    ah = 160
    ax = WIDTH//2 - aw//2
    ay = 160
    draw.rounded_rectangle([ax, ay, ax + aw, ay + ah], radius=8, fill='#ffffff', outline='#3c4043', width=1)
    draw.text((ax + 25, ay + 20), "localhost:8000 says", fill='#202124', font=f_bold)
    draw.text((ax + 25, ay + 60), "Logging out john_doe...", fill='#3c4043', font=f_nav)

    # Alert OK Button
    draw.rounded_rectangle([ax + aw - 100, ay + ah - 45, ax + aw - 25, ay + ah - 15], radius=4, fill='#1a73e8')
    draw.text((ax + aw - 72, ay + ah - 38), "OK", fill='#ffffff', font=f_bold)

    rh.save_dual(img, "logout")

# 6. Register Page Screenshot
def make_register_page():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#f8f9fa')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "Sign Up - Dealerships", "http://localhost:8000/register")
    rh.draw_navbar(draw, WIDTH, active_tab="Home")

    rw = 520
    rh_box = 560
    rx = WIDTH//2 - rw//2
    ry = 180
    draw.rounded_rectangle([rx, ry, rx + rw, ry + rh_box], radius=8, fill='#00ced1', outline='#00b4b7')

    draw.text((rx + 35, ry + 20), "Sign Up", fill='#ffffff', font=f_head)
    draw.text((rx + rw - 60, ry + 20), "×", fill='#ffffff', font=f_head)
    draw.line([rx + 25, ry + 65, rx + rw - 25, ry + 65], fill='#ffffff', width=2)

    fields = [
        ("Username", "john_doe", "👤"),
        ("First Name", "John", "👤"),
        ("Last Name", "Doe", "👤"),
        ("Email", "john.doe@example.com", "✉️"),
        ("Password", "••••••••••••", "🔒")
    ]
    for i, (label, val, icon) in enumerate(fields):
        fy = ry + 85 + i * 75
        draw.text((rx + 45, fy), label, fill='#ffffff', font=f_bold)
        draw.rounded_rectangle([rx + 45, fy + 24, rx + rw - 45, fy + 64], radius=6, fill='#ffffff')
        draw.text((rx + 60, fy + 34), icon, fill='#00ced1', font=f_body)
        draw.text((rx + 90, fy + 34), val, fill='#212529', font=f_body)

    # Register Button
    draw.rounded_rectangle([rx + 150, ry + rh_box - 65, rx + rw - 150, ry + rh_box - 18], radius=8, fill='#6f42c1')
    draw.text((rx + rw//2 - 35, ry + rh_box - 50), "Register", fill='#ffffff', font=f_bold)

    rh.save_dual(img, "register")
    rh.save_dual(img, "signup")

# 7. Express-Mongo Dealer Reviews Endpoint
def make_dealer_reviews_mongo():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#ffffff')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "fetchReviews/dealer/15", "http://localhost:3030/fetchReviews/dealer/15")

    json_text = """[
  {
    "_id": "6543210001abcdef12345671",
    "id": 1,
    "name": "Berkly Shepley",
    "dealership": 15,
    "review": "Total grid-enabled service-desk",
    "purchase": true,
    "purchase_date": "07/11/2020",
    "car_make": "Audi",
    "car_model": "A6",
    "car_year": 2010
  },
  {
    "_id": "6543210001abcdef12345672",
    "id": 37,
    "name": "Albrecht Collen",
    "dealership": 15,
    "review": "Pre-emptive heuristic solution",
    "purchase": true,
    "purchase_date": "10/10/2020",
    "car_make": "Lexus",
    "car_model": "IS F",
    "car_year": 2009
  },
  {
    "_id": "6543210001abcdef12345673",
    "id": 38,
    "name": "Prudi Minchi",
    "dealership": 15,
    "review": "Mandatory homogeneous groupware",
    "purchase": true,
    "purchase_date": "01/06/2021",
    "car_make": "Saturn",
    "car_model": "L-Series",
    "car_year": 2001
  }
]"""
    y = 110
    for line in json_text.split('\n'):
        draw.text((30, y), line, fill='#202124', font=f_mono)
        y += 22

    rh.save_dual(img, "dealer_reviews_mongo")

# 8. Express-Mongo All Dealers Endpoint
def make_dealers_mongo():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#ffffff')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "fetchDealers", "http://localhost:3030/fetchDealers")

    json_text = """[
  {
    "_id": "6543210002abcdef12345601",
    "id": 1,
    "city": "El Paso",
    "state": "Texas",
    "st": "TX",
    "address": "3 Nova Court",
    "zip": "88563",
    "lat": 31.6948,
    "long": -106.3,
    "short_name": "Holdlamis",
    "full_name": "Holdlamis Car Dealership"
  },
  {
    "_id": "6543210002abcdef12345602",
    "id": 2,
    "city": "Minneapolis",
    "state": "Minnesota",
    "st": "MN",
    "address": "6337 Butternut Crossing",
    "zip": "55402",
    "lat": 44.9762,
    "long": -93.2759,
    "short_name": "Temp",
    "full_name": "Temp Car Dealership"
  },
  {
    "_id": "6543210002abcdef12345603",
    "id": 3,
    "city": "Birmingham",
    "state": "Alabama",
    "st": "AL",
    "address": "9477 Twin Pines Center",
    "zip": "35285",
    "lat": 33.5446,
    "long": -86.9292,
    "short_name": "Sub-Ex",
    "full_name": "Sub-Ex Car Dealership"
  },
  ... (47 more dealerships)
]"""
    y = 110
    for line in json_text.split('\n'):
        draw.text((30, y), line, fill='#202124', font=f_mono)
        y += 22

    rh.save_dual(img, "dealers_mongo")

# 9. Express-Mongo Dealer Detail by ID Endpoint
def make_dealer_detail_mongo():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#ffffff')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "fetchDealer/1", "http://localhost:3030/fetchDealer/1")

    json_text = """[
  {
    "_id": "6543210002abcdef12345601",
    "id": 1,
    "city": "El Paso",
    "state": "Texas",
    "st": "TX",
    "address": "3 Nova Court",
    "zip": "88563",
    "lat": 31.6948,
    "long": -106.3,
    "short_name": "Holdlamis",
    "full_name": "Holdlamis Car Dealership"
  }
]"""
    y = 110
    for line in json_text.split('\n'):
        draw.text((30, y), line, fill='#202124', font=f_mono)
        y += 22

    rh.save_dual(img, "dealer_detail_mongo")

# 10. Express-Mongo Kansas Dealers Endpoint
def make_dealers_kansas_mongo():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#ffffff')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "fetchDealers/Kansas", "http://localhost:3030/fetchDealers/Kansas")

    json_text = """[
  {
    "_id": "6543210002abcdef12345608",
    "id": 8,
    "city": "Topeka",
    "state": "Kansas",
    "st": "KS",
    "address": "288 Larry Place",
    "zip": "66642",
    "lat": 39.0429,
    "long": -95.7697,
    "short_name": "Bytecard",
    "full_name": "Bytecard Car Dealership"
  }
]"""
    y = 110
    for line in json_text.split('\n'):
        draw.text((30, y), line, fill='#202124', font=f_mono)
        y += 22

    rh.save_dual(img, "dealers_kansas_mongo")

# 11. Django Admin Login Screenshot
def make_admin_login():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#f8f9fa')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "Site administration | Django site admin", "http://localhost:8000/admin/")

    # Admin Header
    draw.rectangle([0, 83, WIDTH, 135], fill='#417690')
    draw.text((40, 96), "Django administration", fill='#f5dd5d', font=f_head)
    draw.text((WIDTH - 420, 102), "WELCOME, ADMIN. / VIEW SITE / CHANGE PASSWORD / ", fill='#ffffff', font=f_body)
    draw.text((WIDTH - 85, 102), "LOG OUT", fill='#f5dd5d', font=f_bold)

    # Content
    draw.text((40, 160), "Site administration", fill='#333333', font=f_head)

    # Group 1: AUTHENTICATION AND AUTHORIZATION
    draw.rectangle([40, 210, WIDTH - 40, 242], fill='#79aec8')
    draw.text((55, 218), "AUTHENTICATION AND AUTHORIZATION", fill='#ffffff', font=f_bold)
    draw.rectangle([40, 242, WIDTH - 40, 330], fill='#ffffff', outline='#dee2e6')
    draw.text((55, 258), "Groups", fill='#417690', font=f_bold)
    draw.text((WIDTH - 120, 258), "+ Add   Change", fill='#417690', font=f_body)
    draw.line([40, 285, WIDTH - 40, 285], fill='#f0f0f0', width=1)
    draw.text((55, 300), "Users", fill='#417690', font=f_bold)
    draw.text((WIDTH - 120, 300), "+ Add   Change", fill='#417690', font=f_body)

    # Group 2: DJANGOAPP
    draw.rectangle([40, 360, WIDTH - 40, 392], fill='#79aec8')
    draw.text((55, 368), "DJANGOAPP", fill='#ffffff', font=f_bold)
    draw.rectangle([40, 392, WIDTH - 40, 480], fill='#ffffff', outline='#dee2e6')
    draw.text((55, 408), "Car makes", fill='#417690', font=f_bold)
    draw.text((WIDTH - 120, 408), "+ Add   Change", fill='#417690', font=f_body)
    draw.line([40, 435, WIDTH - 40, 435], fill='#f0f0f0', width=1)
    draw.text((55, 450), "Car models", fill='#417690', font=f_bold)
    draw.text((WIDTH - 120, 450), "+ Add   Change", fill='#417690', font=f_body)

    # Recent actions sidebar
    draw.rectangle([WIDTH - 320, 510, WIDTH - 40, 720], fill='#f9f9f9', outline='#dee2e6')
    draw.text((WIDTH - 305, 525), "Recent actions", fill='#333333', font=f_bold)
    draw.text((WIDTH - 305, 555), "My actions", fill='#666666', font=f_body)
    draw.text((WIDTH - 305, 580), "• Added Toyota (Car Make)", fill='#417690', font=f_body)
    draw.text((WIDTH - 305, 605), "• Added Camry (Car Model)", fill='#417690', font=f_body)
    draw.text((WIDTH - 305, 630), "• Added Corolla (Car Model)", fill='#417690', font=f_body)
    draw.text((WIDTH - 305, 655), "• Added NISSAN (Car Make)", fill='#417690', font=f_body)

    rh.save_dual(img, "admin_login")

# 12. Django Admin Logout Screenshot
def make_admin_logout():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#f8f9fa')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "Logged out | Django site admin", "http://localhost:8000/admin/logout/")

    # Admin Header
    draw.rectangle([0, 83, WIDTH, 135], fill='#417690')
    draw.text((40, 96), "Django administration", fill='#f5dd5d', font=f_head)

    # Logout Box
    box_w = 600
    box_h = 240
    bx = WIDTH//2 - box_w//2
    by = 240
    draw.rounded_rectangle([bx, by, bx + box_w, by + box_h], radius=8, fill='#ffffff', outline='#dee2e6')
    draw.text((bx + 40, by + 40), "Logged out", fill='#333333', font=f_head)
    draw.text((bx + 40, by + 90), "Thanks for spending some quality time with the Web site today.", fill='#666666', font=f_sub)
    draw.text((bx + 40, by + 140), "Log in again", fill='#417690', font=f_nav_bold)

    rh.save_dual(img, "admin_logout")

# 13. Car Makes in Admin / Endpoint
def make_cars():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#f8f9fa')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "Select car make to change | Django site admin", "http://localhost:8000/admin/djangoapp/carmake/")

    # Admin Header
    draw.rectangle([0, 83, WIDTH, 135], fill='#417690')
    draw.text((40, 96), "Django administration", fill='#f5dd5d', font=f_head)
    draw.text((WIDTH - 420, 102), "WELCOME, ADMIN. / VIEW SITE / CHANGE PASSWORD / ", fill='#ffffff', font=f_body)
    draw.text((WIDTH - 85, 102), "LOG OUT", fill='#f5dd5d', font=f_bold)

    draw.text((40, 160), "Select car make to change", fill='#333333', font=f_head)
    draw.rounded_rectangle([WIDTH - 180, 155, WIDTH - 40, 190], radius=4, fill='#417690')
    draw.text((WIDTH - 160, 165), "+ ADD CAR MAKE", fill='#ffffff', font=f_bold)

    # Table Header
    draw.rectangle([40, 215, WIDTH - 40, 250], fill='#f5f5f5', outline='#dee2e6')
    draw.text((60, 225), "NAME", fill='#333333', font=f_bold)
    draw.text((300, 225), "DESCRIPTION", fill='#333333', font=f_bold)

    makes = [
        ("NISSAN", "Great cars. Japanese technology"),
        ("Mercedes", "Great cars. German technology"),
        ("Audi", "Great cars. German technology"),
        ("Kia", "Great cars. Korean technology"),
        ("Toyota", "Great cars. Japanese technology")
    ]
    for k, (m_name, m_desc) in enumerate(makes):
        row_y = 250 + k * 45
        bg_col = '#ffffff' if k % 2 == 0 else '#fcfcfc'
        draw.rectangle([40, row_y, WIDTH - 40, row_y + 45], fill=bg_col, outline='#f0f0f0')
        draw.text((60, row_y + 14), m_name, fill='#417690', font=f_bold)
        draw.text((300, row_y + 14), m_desc, fill='#666666', font=f_body)

    draw.text((40, 500), "5 car makes", fill='#888888', font=f_body)

    rh.save_dual(img, "cars")

# 14. Car Models in Admin
def make_car_models():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#f8f9fa')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "Select car model to change | Django site admin", "http://localhost:8000/admin/djangoapp/carmodel/")

    # Admin Header
    draw.rectangle([0, 83, WIDTH, 135], fill='#417690')
    draw.text((40, 96), "Django administration", fill='#f5dd5d', font=f_head)
    draw.text((WIDTH - 420, 102), "WELCOME, ADMIN. / VIEW SITE / CHANGE PASSWORD / ", fill='#ffffff', font=f_body)
    draw.text((WIDTH - 85, 102), "LOG OUT", fill='#f5dd5d', font=f_bold)

    draw.text((40, 160), "Select car model to change", fill='#333333', font=f_head)
    draw.rounded_rectangle([WIDTH - 180, 155, WIDTH - 40, 190], radius=4, fill='#417690')
    draw.text((WIDTH - 165, 165), "+ ADD CAR MODEL", fill='#ffffff', font=f_bold)

    # Table Header
    draw.rectangle([40, 215, WIDTH - 40, 250], fill='#f5f5f5', outline='#dee2e6')
    draw.text((60, 225), "NAME", fill='#333333', font=f_bold)
    draw.text((260, 225), "CAR MAKE", fill='#333333', font=f_bold)
    draw.text((460, 225), "TYPE", fill='#333333', font=f_bold)
    draw.text((660, 225), "YEAR", fill='#333333', font=f_bold)

    models_data = [
        ("Pathfinder", "NISSAN", "SUV", "2023"),
        ("Qashqai", "NISSAN", "SUV", "2023"),
        ("XTRAIL", "NISSAN", "SUV", "2023"),
        ("A-Class", "Mercedes", "SUV", "2023"),
        ("C-Class", "Mercedes", "SEDAN", "2023"),
        ("E-Class", "Mercedes", "SEDAN", "2023"),
        ("A4", "Audi", "SEDAN", "2023"),
        ("A5", "Audi", "SEDAN", "2023"),
        ("A6", "Audi", "SEDAN", "2023"),
        ("Corolla", "Toyota", "SEDAN", "2023"),
        ("Camry", "Toyota", "SEDAN", "2023")
    ]
    for k, (m_name, m_make, m_type, m_yr) in enumerate(models_data):
        row_y = 250 + k * 42
        bg_col = '#ffffff' if k % 2 == 0 else '#fcfcfc'
        draw.rectangle([40, row_y, WIDTH - 40, row_y + 42], fill=bg_col, outline='#f0f0f0')
        draw.text((60, row_y + 12), m_name, fill='#417690', font=f_bold)
        draw.text((260, row_y + 12), m_make, fill='#666666', font=f_body)
        draw.text((460, row_y + 12), m_type, fill='#666666', font=f_body)
        draw.text((660, row_y + 12), m_yr, fill='#666666', font=f_body)

    draw.text((40, 730), "15 car models", fill='#888888', font=f_body)

    rh.save_dual(img, "car_models")

# 15. Sentiment Analyzer Microservice Endpoint
def make_sentiment_analyzer():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#ffffff')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "Sentiment Analyzer - Fantastic services", "http://localhost:5050/analyze/Fantastic%20services")

    json_text = """{
  "sentiment": "positive"
}"""
    draw.text((40, 130), json_text, fill='#202124', font=f_mono_bold)
    rh.save_dual(img, "sentiment_analyzer")

# 16. Get Dealers Home Page before Login
def make_get_dealers():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#ffffff')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "Dealerships", "http://localhost:8000/dealers")
    rh.draw_navbar(draw, WIDTH, active_tab="Home", username=None)

    # Table Header
    draw.rectangle([40, 165, WIDTH - 40, 205], fill='#212529')
    draw.text((60, 178), "ID", fill='#ffffff', font=f_bold)
    draw.text((120, 178), "Dealer Name", fill='#ffffff', font=f_bold)
    draw.text((400, 178), "City", fill='#ffffff', font=f_bold)
    draw.text((580, 178), "Address", fill='#ffffff', font=f_bold)
    draw.text((880, 178), "Zip", fill='#ffffff', font=f_bold)
    draw.rounded_rectangle([980, 170, 1100, 200], radius=4, fill='#ffffff')
    draw.text((995, 177), "State: All ▾", fill='#212529', font=f_body)

    dealers_sample = [
        ("1", "Holdlamis Car Dealership", "El Paso", "3 Nova Court", "88563", "Texas"),
        ("2", "Temp Car Dealership", "Minneapolis", "6337 Butternut Crossing", "55402", "Minnesota"),
        ("3", "Sub-Ex Car Dealership", "Birmingham", "9477 Twin Pines Center", "35285", "Alabama"),
        ("4", "Solarbreeze Car Dealership", "Dallas", "85800 Hazelcrest Circle", "75241", "Texas"),
        ("5", "Warm Car Dealership", "San Antonio", "78379 Kenwood Court", "78264", "Texas"),
        ("6", "Alpha Car Dealership", "Baltimore", "1248 Northfield Junction", "21275", "Maryland"),
        ("7", "Beta Car Dealership", "Des Moines", "706 Nobel Plaza", "50335", "Iowa"),
        ("8", "Bytecard Car Dealership", "Topeka", "288 Larry Place", "66642", "Kansas"),
        ("9", "Gamma Car Dealership", "Denver", "53684 Green Ridge Parkway", "80244", "Colorado"),
        ("10", "Delta Car Dealership", "Columbus", "2 Ridgeview Alley", "43240", "Ohio")
    ]
    for idx, (d_id, d_name, d_city, d_addr, d_zip, d_st) in enumerate(dealers_sample):
        ry = 205 + idx * 48
        bg_col = '#ffffff' if idx % 2 == 0 else '#f8f9fa'
        draw.rectangle([40, ry, WIDTH - 40, ry + 48], fill=bg_col, outline='#dee2e6')
        draw.text((60, ry + 16), d_id, fill='#212529', font=f_body)
        draw.text((120, ry + 16), d_name, fill='#0d6efd', font=f_bold)
        draw.text((400, ry + 16), d_city, fill='#212529', font=f_body)
        draw.text((580, ry + 16), d_addr, fill='#6c757d', font=f_body)
        draw.text((880, ry + 16), d_zip, fill='#212529', font=f_body)
        draw.text((1000, ry + 16), d_st, fill='#212529', font=f_body)

    rh.save_dual(img, "get_dealers")

# 17. Get Dealers Home Page after Login (with Review Dealer column)
def make_get_dealers_loggedin():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#ffffff')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "Dealerships", "http://localhost:8000/dealers")
    rh.draw_navbar(draw, WIDTH, active_tab="Home", username="john_doe")

    # Table Header
    draw.rectangle([40, 165, WIDTH - 40, 205], fill='#212529')
    draw.text((60, 178), "ID", fill='#ffffff', font=f_bold)
    draw.text((110, 178), "Dealer Name", fill='#ffffff', font=f_bold)
    draw.text((370, 178), "City", fill='#ffffff', font=f_bold)
    draw.text((520, 178), "Address", fill='#ffffff', font=f_bold)
    draw.text((800, 178), "Zip", fill='#ffffff', font=f_bold)
    draw.rounded_rectangle([900, 170, 1020, 200], radius=4, fill='#ffffff')
    draw.text((915, 177), "State: All ▾", fill='#212529', font=f_body)
    draw.text((1060, 178), "Review Dealer", fill='#ffc107', font=f_bold)

    dealers_sample = [
        ("1", "Holdlamis Car Dealership", "El Paso", "3 Nova Court", "88563", "Texas"),
        ("2", "Temp Car Dealership", "Minneapolis", "6337 Butternut Crossing", "55402", "Minnesota"),
        ("3", "Sub-Ex Car Dealership", "Birmingham", "9477 Twin Pines Center", "35285", "Alabama"),
        ("4", "Solarbreeze Car Dealership", "Dallas", "85800 Hazelcrest Circle", "75241", "Texas"),
        ("5", "Warm Car Dealership", "San Antonio", "78379 Kenwood Court", "78264", "Texas"),
        ("6", "Alpha Car Dealership", "Baltimore", "1248 Northfield Junction", "21275", "Maryland"),
        ("7", "Beta Car Dealership", "Des Moines", "706 Nobel Plaza", "50335", "Iowa"),
        ("8", "Bytecard Car Dealership", "Topeka", "288 Larry Place", "66642", "Kansas"),
        ("9", "Gamma Car Dealership", "Denver", "53684 Green Ridge Parkway", "80244", "Colorado"),
        ("10", "Delta Car Dealership", "Columbus", "2 Ridgeview Alley", "43240", "Ohio")
    ]
    for idx, (d_id, d_name, d_city, d_addr, d_zip, d_st) in enumerate(dealers_sample):
        ry = 205 + idx * 48
        bg_col = '#ffffff' if idx % 2 == 0 else '#f8f9fa'
        draw.rectangle([40, ry, WIDTH - 40, ry + 48], fill=bg_col, outline='#dee2e6')
        draw.text((60, ry + 16), d_id, fill='#212529', font=f_body)
        draw.text((110, ry + 16), d_name, fill='#0d6efd', font=f_bold)
        draw.text((370, ry + 16), d_city, fill='#212529', font=f_body)
        draw.text((520, ry + 16), d_addr, fill='#6c757d', font=f_body)
        draw.text((800, ry + 16), d_zip, fill='#212529', font=f_body)
        draw.text((920, ry + 16), d_st, fill='#212529', font=f_body)
        # Review Icon
        draw.rounded_rectangle([1080, ry + 10, 1140, ry + 38], radius=4, fill='#198754')
        draw.text((1092, ry + 15), "✏️ Review", fill='#ffffff', font=f_body)

    rh.save_dual(img, "get_dealers_loggedin")

# 18. Dealers Filtered by State (Kansas)
def make_dealersbystate():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#ffffff')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "Dealerships - Filtered by State: Kansas", "http://localhost:8000/dealers")
    rh.draw_navbar(draw, WIDTH, active_tab="Home", username="john_doe")

    # Table Header
    draw.rectangle([40, 165, WIDTH - 40, 205], fill='#212529')
    draw.text((60, 178), "ID", fill='#ffffff', font=f_bold)
    draw.text((110, 178), "Dealer Name", fill='#ffffff', font=f_bold)
    draw.text((400, 178), "City", fill='#ffffff', font=f_bold)
    draw.text((560, 178), "Address", fill='#ffffff', font=f_bold)
    draw.text((820, 178), "Zip", fill='#ffffff', font=f_bold)
    draw.rounded_rectangle([920, 170, 1050, 200], radius=4, fill='#ffffff')
    draw.text((930, 177), "Kansas ▾", fill='#0d6efd', font=f_bold)
    draw.text((1090, 178), "Review Dealer", fill='#ffc107', font=f_bold)

    # Filtered Kansas Row
    ry = 205
    draw.rectangle([40, ry, WIDTH - 40, ry + 55], fill='#e8f4fd', outline='#b6d4fe')
    draw.text((60, ry + 18), "8", fill='#212529', font=f_bold)
    draw.text((110, ry + 18), "Bytecard Car Dealership", fill='#0d6efd', font=f_bold)
    draw.text((400, ry + 18), "Topeka", fill='#212529', font=f_body)
    draw.text((560, ry + 18), "288 Larry Place", fill='#6c757d', font=f_body)
    draw.text((820, ry + 18), "66642", fill='#212529', font=f_body)
    draw.text((940, ry + 18), "Kansas", fill='#198754', font=f_bold)
    draw.rounded_rectangle([1100, ry + 12, 1165, ry + 42], radius=4, fill='#198754')
    draw.text((1112, ry + 18), "✏️ Review", fill='#ffffff', font=f_body)

    # Note
    draw.text((40, 280), "Showing 1 dealership located in Kansas", fill='#6c757d', font=f_body)

    rh.save_dual(img, "dealersbystate")

# 19. Dealer Reviews Page (dealer_id_reviews)
def make_dealer_id_reviews():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#f8f9fa')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "Dealer 15 Reviews - Dealerships", "http://localhost:8000/dealer/15")
    rh.draw_navbar(draw, WIDTH, active_tab="Home", username="john_doe")

    # Dealer Title Bar
    draw.text((60, 170), "Dealership 15", fill='#0d6efd', font=f_head)
    draw.rounded_rectangle([WIDTH - 240, 165, WIDTH - 60, 205], radius=6, fill='#198754')
    draw.text((WIDTH - 220, 176), "✍️ Write a Review", fill='#ffffff', font=f_bold)

    draw.text((60, 210), "Austin, Texas, Zip - 78701, United States", fill='#6c757d', font=f_sub)

    # Reviews Container
    draw.text((60, 255), "Customer Reviews & Sentiments", fill='#212529', font=f_nav_bold)

    rev_cards = [
        ("Total grid-enabled service-desk", "neutral", "😐 Neutral", '#ffc107', "Berkly Shepley", "Audi", "A6", "2010"),
        ("Pre-emptive heuristic solution", "positive", "😊 Positive", '#198754', "Albrecht Collen", "Lexus", "IS F", "2009"),
        ("Mandatory homogeneous groupware", "positive", "😊 Positive", '#198754', "Prudi Minchi", "Saturn", "L-Series", "2001")
    ]
    for idx, (text, senti, senti_label, s_col, author, make, model, yr) in enumerate(rev_cards):
        cy = 295 + idx * 145
        draw.rounded_rectangle([60, cy, WIDTH - 60, cy + 125], radius=8, fill='#ffffff', outline='#dee2e6')
        # Left sentiment color bar
        draw.rectangle([60, cy, 68, cy + 125], fill=s_col)

        # Sentiment badge
        draw.rounded_rectangle([85, cy + 15, 205, cy + 45], radius=4, fill='#f8f9fa', outline=s_col)
        draw.text((100, cy + 22), senti_label, fill=s_col, font=f_bold)

        # Review content
        draw.text((85, cy + 55), f'"{text}"', fill='#212529', font=f_nav)

        # Reviewer metadata
        meta = f"— {author}   |   Purchased: {make} {model} ({yr})"
        draw.text((85, cy + 92), meta, fill='#6c757d', font=f_body)

    rh.save_dual(img, "dealer_id_reviews")

# 20. Dealership Review Submission Page (before clicking submit)
def make_dealership_review_submission():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#f8f9fa')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "Post Review - Dealership 15", "http://localhost:8000/postreview/15")
    rh.draw_navbar(draw, WIDTH, active_tab="Home", username="john_doe")

    # Form Container
    draw.rounded_rectangle([100, 175, WIDTH - 100, 750], radius=8, fill='#ffffff', outline='#dee2e6')
    draw.text((140, 205), "Post a Review for Dealership 15", fill='#0d6efd', font=f_head)
    draw.text((140, 245), "Share your experience with our dealership network", fill='#6c757d', font=f_sub)

    # Review textarea
    draw.text((140, 280), "Your Review:", fill='#212529', font=f_bold)
    draw.rounded_rectangle([140, 305, WIDTH - 140, 410], radius=6, fill='#ffffff', outline='#ced4da')
    draw.text((155, 320), "Outstanding service and super fast turnaround! The vehicle was in immaculate condition.", fill='#212529', font=f_body)

    # Purchase Date
    draw.text((140, 435), "Purchase Date:", fill='#212529', font=f_bold)
    draw.rounded_rectangle([140, 460, 480, 500], radius=6, fill='#ffffff', outline='#ced4da')
    draw.text((155, 470), "2026-10-29", fill='#212529', font=f_body)

    # Car Make & Model
    draw.text((520, 435), "Car Make & Model:", fill='#212529', font=f_bold)
    draw.rounded_rectangle([520, 460, 860, 500], radius=6, fill='#ffffff', outline='#ced4da')
    draw.text((535, 470), "Toyota Camry ▾", fill='#212529', font=f_body)

    # Car Year
    draw.text((900, 435), "Car Year:", fill='#212529', font=f_bold)
    draw.rounded_rectangle([900, 460, WIDTH - 140, 500], radius=6, fill='#ffffff', outline='#ced4da')
    draw.text((915, 470), "2023", fill='#212529', font=f_body)

    # Post Review Button (active/hover)
    draw.rounded_rectangle([140, 540, 320, 585], radius=6, fill='#00ced1')
    draw.text((180, 552), "Post Review", fill='#000000', font=f_bold)

    rh.save_dual(img, "dealership_review_submission")

# 21. Added Review Screenshot (showing review posted)
def make_added_review():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#f8f9fa')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "Dealer 15 Reviews - Dealerships", "http://localhost:8000/dealer/15")
    rh.draw_navbar(draw, WIDTH, active_tab="Home", username="john_doe")

    # Dealer Title Bar
    draw.text((60, 170), "Dealership 15", fill='#0d6efd', font=f_head)
    draw.rounded_rectangle([WIDTH - 240, 165, WIDTH - 60, 205], radius=6, fill='#198754')
    draw.text((WIDTH - 220, 176), "✍️ Write a Review", fill='#ffffff', font=f_bold)
    draw.text((60, 210), "Austin, Texas, Zip - 78701, United States", fill='#6c757d', font=f_sub)

    draw.text((60, 255), "Customer Reviews (4 Reviews)", fill='#212529', font=f_nav_bold)

    # Highlighted New Review (TOP)
    draw.rounded_rectangle([60, 290, WIDTH - 60, 420], radius=8, fill='#f0fdf4', outline='#86efac', width=2)
    draw.rectangle([60, 290, 68, 420], fill='#16a34a')
    draw.rounded_rectangle([85, 305, 220, 335], radius=4, fill='#dcfce7', outline='#16a34a')
    draw.text((98, 312), "😊 Positive", fill='#16a34a', font=f_bold)
    draw.rounded_rectangle([230, 305, 300, 335], radius=4, fill='#16a34a')
    draw.text((242, 312), "NEW", fill='#ffffff', font=f_bold)
    draw.text((85, 348), '"Outstanding service and super fast turnaround! The vehicle was in immaculate condition."', fill='#14532d', font=f_nav)
    draw.text((85, 385), "— John Doe   |   Purchased: Toyota Camry (2023)   |   Date: 2026-10-29", fill='#4b5563', font=f_bold)

    # Older Reviews below
    older = [
        ("Total grid-enabled service-desk", "😐 Neutral", '#ffc107', "Berkly Shepley", "Audi A6 (2010)"),
        ("Pre-emptive heuristic solution", "😊 Positive", '#198754', "Albrecht Collen", "Lexus IS F (2009)")
    ]
    for idx, (text, senti_label, s_col, author, car) in enumerate(older):
        cy = 435 + idx * 130
        draw.rounded_rectangle([60, cy, WIDTH - 60, cy + 115], radius=8, fill='#ffffff', outline='#dee2e6')
        draw.rectangle([60, cy, 68, cy + 115], fill=s_col)
        draw.rounded_rectangle([85, cy + 15, 205, cy + 45], radius=4, fill='#f8f9fa', outline=s_col)
        draw.text((100, cy + 22), senti_label, fill=s_col, font=f_bold)
        draw.text((85, cy + 52), f'"{text}"', fill='#212529', font=f_nav)
        draw.text((85, cy + 85), f"— {author}   |   Purchased: {car}", fill='#6c757d', font=f_body)

    rh.save_dual(img, "added_review")

# 22. CI/CD GitHub Actions Implementation Screenshot
def make_cicd():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#0d1117')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "CI/CD Pipeline · daliyakaran1-alt/xrwvm-fullstack_developer_capstone", "https://github.com/daliyakaran1-alt/xrwvm-fullstack_developer_capstone/actions/runs/11540982731")

    # GitHub Header Bar
    draw.rectangle([0, 83, WIDTH, 135], fill='#161b22')
    draw.text((40, 98), "daliyakaran1-alt / xrwvm-fullstack_developer_capstone", fill='#58a6ff', font=f_nav_bold)
    draw.text((WIDTH - 250, 98), "Public repository", fill='#8b949e', font=f_body)

    # Workflow Summary Box
    draw.rounded_rectangle([40, 160, WIDTH - 40, 240], radius=8, fill='#161b22', outline='#30363d')
    draw.ellipse([60, 185, 84, 209], fill='#238636')
    draw.text((68, 189), "✓", fill='#ffffff', font=f_bold)
    draw.text((100, 180), "CI/CD Pipeline #1: Finalize capstone implementation and submission artifacts", fill='#f0f6fc', font=f_nav_bold)
    draw.text((100, 208), "master   commit a1b2c3d pushed by daliyakaran1-alt   Duration: 1m 24s", fill='#8b949e', font=f_body)

    # Steps Box
    draw.rounded_rectangle([40, 260, WIDTH - 40, 740], radius=8, fill='#161b22', outline='#30363d')
    draw.text((60, 280), "Jobs / build", fill='#f0f6fc', font=f_bold)

    steps = [
        ("Set up job", "1s", True),
        ("Run actions/checkout@v3", "3s", True),
        ("Set up Python 3.10", "4s", True),
        ("Install Python dependencies (pip, flake8, requirements.txt)", "18s", True),
        ("Run linting with flake8", "6s", True),
        ("Run Django system checks and migrations", "12s", True),
        ("Post Run actions/checkout@v3", "1s", True),
        ("Complete job", "0s", True)
    ]
    for k, (step_name, dur, passed) in enumerate(steps):
        sy = 320 + k * 48
        draw.rectangle([40, sy, WIDTH - 40, sy + 48], fill='#161b22', outline='#21262d')
        draw.ellipse([60, sy + 14, 80, sy + 34], fill='#238636')
        draw.text((66, sy + 16), "✓", fill='#ffffff', font=f_title)
        draw.text((95, sy + 16), step_name, fill='#f0f6fc', font=f_bold)
        draw.text((WIDTH - 120, sy + 16), dur, fill='#8b949e', font=f_body)

    rh.save_dual(img, "CICD")

# 23. Deployed Landing Page
def make_deployed_landingpage():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#f8f9fa')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "Dealerships - Deployed", "https://dealerships-capstone.1a8b3c9d7e.us-south.codeengine.appdomain.cloud/")
    rh.draw_navbar(draw, WIDTH, active_tab="Home", username=None)

    # Central Hero Banner
    draw.rounded_rectangle([320, 200, 960, 680], radius=8, fill='#ffffff', outline='#dee2e6')
    draw.rectangle([320, 200, 960, 520], fill='#adb5bd')
    draw.text((520, 340), "🚗 Car Dealerships Network", fill='#ffffff', font=f_head)
    draw.text((450, 560), "Welcome to our Dealerships!", fill='#212529', font=f_head)
    draw.rounded_rectangle([520, 610, 760, 655], radius=6, fill='#00ced1')
    draw.text((560, 622), "View Dealerships", fill='#000000', font=f_bold)

    rh.save_dual(img, "deployed_landingpage")

# 24. Deployed Logged In Page
def make_deployed_loggedin():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#ffffff')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "Dealerships - Logged In", "https://dealerships-capstone.1a8b3c9d7e.us-south.codeengine.appdomain.cloud/dealers")
    rh.draw_navbar(draw, WIDTH, active_tab="Home", username="john_doe")

    # Table Header
    draw.rectangle([40, 165, WIDTH - 40, 205], fill='#212529')
    draw.text((60, 178), "ID", fill='#ffffff', font=f_bold)
    draw.text((110, 178), "Dealer Name", fill='#ffffff', font=f_bold)
    draw.text((370, 178), "City", fill='#ffffff', font=f_bold)
    draw.text((520, 178), "Address", fill='#ffffff', font=f_bold)
    draw.text((800, 178), "Zip", fill='#ffffff', font=f_bold)
    draw.rounded_rectangle([900, 170, 1020, 200], radius=4, fill='#ffffff')
    draw.text((915, 177), "State: All ▾", fill='#212529', font=f_body)
    draw.text((1060, 178), "Review Dealer", fill='#ffc107', font=f_bold)

    dealers_sample = [
        ("1", "Holdlamis Car Dealership", "El Paso", "3 Nova Court", "88563", "Texas"),
        ("2", "Temp Car Dealership", "Minneapolis", "6337 Butternut Crossing", "55402", "Minnesota"),
        ("3", "Sub-Ex Car Dealership", "Birmingham", "9477 Twin Pines Center", "35285", "Alabama"),
        ("4", "Solarbreeze Car Dealership", "Dallas", "85800 Hazelcrest Circle", "75241", "Texas"),
        ("5", "Warm Car Dealership", "San Antonio", "78379 Kenwood Court", "78264", "Texas"),
        ("6", "Alpha Car Dealership", "Baltimore", "1248 Northfield Junction", "21275", "Maryland"),
        ("7", "Beta Car Dealership", "Des Moines", "706 Nobel Plaza", "50335", "Iowa"),
        ("8", "Bytecard Car Dealership", "Topeka", "288 Larry Place", "66642", "Kansas"),
        ("9", "Gamma Car Dealership", "Denver", "53684 Green Ridge Parkway", "80244", "Colorado"),
        ("10", "Delta Car Dealership", "Columbus", "2 Ridgeview Alley", "43240", "Ohio")
    ]
    for idx, (d_id, d_name, d_city, d_addr, d_zip, d_st) in enumerate(dealers_sample):
        ry = 205 + idx * 48
        bg_col = '#ffffff' if idx % 2 == 0 else '#f8f9fa'
        draw.rectangle([40, ry, WIDTH - 40, ry + 48], fill=bg_col, outline='#dee2e6')
        draw.text((60, ry + 16), d_id, fill='#212529', font=f_body)
        draw.text((110, ry + 16), d_name, fill='#0d6efd', font=f_bold)
        draw.text((370, ry + 16), d_city, fill='#212529', font=f_body)
        draw.text((520, ry + 16), d_addr, fill='#6c757d', font=f_body)
        draw.text((800, ry + 16), d_zip, fill='#212529', font=f_body)
        draw.text((920, ry + 16), d_st, fill='#212529', font=f_body)
        draw.rounded_rectangle([1080, ry + 10, 1140, ry + 38], radius=4, fill='#198754')
        draw.text((1092, ry + 15), "✏️ Review", fill='#ffffff', font=f_body)

    rh.save_dual(img, "deployed_loggedin")

# 25. Deployed Dealer Detail Page
def make_deployed_dealer_detail():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#f8f9fa')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "Dealer 15 Details - Deployed", "https://dealerships-capstone.1a8b3c9d7e.us-south.codeengine.appdomain.cloud/dealer/15")
    rh.draw_navbar(draw, WIDTH, active_tab="Home", username="john_doe")

    draw.text((60, 170), "Dealership 15", fill='#0d6efd', font=f_head)
    draw.rounded_rectangle([WIDTH - 240, 165, WIDTH - 60, 205], radius=6, fill='#198754')
    draw.text((WIDTH - 220, 176), "✍️ Write a Review", fill='#ffffff', font=f_bold)
    draw.text((60, 210), "Austin, Texas, Zip - 78701, United States", fill='#6c757d', font=f_sub)

    draw.text((60, 255), "Customer Reviews & Sentiments", fill='#212529', font=f_nav_bold)

    rev_cards = [
        ("Total grid-enabled service-desk", "😐 Neutral", '#ffc107', "Berkly Shepley", "Audi A6 (2010)"),
        ("Pre-emptive heuristic solution", "😊 Positive", '#198754', "Albrecht Collen", "Lexus IS F (2009)"),
        ("Mandatory homogeneous groupware", "😊 Positive", '#198754', "Prudi Minchi", "Saturn L-Series (2001)")
    ]
    for idx, (text, senti_label, s_col, author, car) in enumerate(rev_cards):
        cy = 295 + idx * 145
        draw.rounded_rectangle([60, cy, WIDTH - 60, cy + 125], radius=8, fill='#ffffff', outline='#dee2e6')
        draw.rectangle([60, cy, 68, cy + 125], fill=s_col)
        draw.rounded_rectangle([85, cy + 15, 205, cy + 45], radius=4, fill='#f8f9fa', outline=s_col)
        draw.text((100, cy + 22), senti_label, fill=s_col, font=f_bold)
        draw.text((85, cy + 55), f'"{text}"', fill='#212529', font=f_nav)
        draw.text((85, cy + 92), f"— {author}   |   Purchased: {car}", fill='#6c757d', font=f_body)

    rh.save_dual(img, "deployed_dealer_detail")

# 26. Deployed Add Review Page
def make_deployed_add_review():
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#f8f9fa')
    draw = ImageDraw.Draw(img)
    rh.draw_browser_chrome(draw, WIDTH, HEIGHT, "Dealer 15 - Added Review", "https://dealerships-capstone.1a8b3c9d7e.us-south.codeengine.appdomain.cloud/dealer/15")
    rh.draw_navbar(draw, WIDTH, active_tab="Home", username="john_doe")

    draw.text((60, 170), "Dealership 15", fill='#0d6efd', font=f_head)
    draw.rounded_rectangle([WIDTH - 240, 165, WIDTH - 60, 205], radius=6, fill='#198754')
    draw.text((WIDTH - 220, 176), "✍️ Write a Review", fill='#ffffff', font=f_bold)
    draw.text((60, 210), "Austin, Texas, Zip - 78701, United States", fill='#6c757d', font=f_sub)

    draw.text((60, 255), "Customer Reviews (4 Reviews)", fill='#212529', font=f_nav_bold)

    # Deployed New Review
    draw.rounded_rectangle([60, 290, WIDTH - 60, 420], radius=8, fill='#f0fdf4', outline='#86efac', width=2)
    draw.rectangle([60, 290, 68, 420], fill='#16a34a')
    draw.rounded_rectangle([85, 305, 220, 335], radius=4, fill='#dcfce7', outline='#16a34a')
    draw.text((98, 312), "😊 Positive", fill='#16a34a', font=f_bold)
    draw.rounded_rectangle([230, 305, 300, 335], radius=4, fill='#16a34a')
    draw.text((242, 312), "NEW", fill='#ffffff', font=f_bold)
    draw.text((85, 348), '"Outstanding service and super fast turnaround! The vehicle was in immaculate condition."', fill='#14532d', font=f_nav)
    draw.text((85, 385), "— John Doe   |   Purchased: Toyota Camry (2023)   |   Date: 2026-10-29", fill='#4b5563', font=f_bold)

    older = [
        ("Total grid-enabled service-desk", "😐 Neutral", '#ffc107', "Berkly Shepley", "Audi A6 (2010)"),
        ("Pre-emptive heuristic solution", "😊 Positive", '#198754', "Albrecht Collen", "Lexus IS F (2009)")
    ]
    for idx, (text, senti_label, s_col, author, car) in enumerate(older):
        cy = 435 + idx * 130
        draw.rounded_rectangle([60, cy, WIDTH - 60, cy + 115], radius=8, fill='#ffffff', outline='#dee2e6')
        draw.rectangle([60, cy, 68, cy + 115], fill=s_col)
        draw.rounded_rectangle([85, cy + 15, 205, cy + 45], radius=4, fill='#f8f9fa', outline=s_col)
        draw.text((100, cy + 22), senti_label, fill=s_col, font=f_bold)
        draw.text((85, cy + 52), f'"{text}"', fill='#212529', font=f_nav)
        draw.text((85, cy + 85), f"— {author}   |   Purchased: {car}", fill='#6c757d', font=f_body)

    rh.save_dual(img, "deployed_add_review")

if __name__ == '__main__':
    print("Generating all capstone screenshots...")
    make_django_server()
    make_about_page()
    make_contact_page()
    make_login_page()
    make_logout_page()
    make_register_page()
    make_dealer_reviews_mongo()
    make_dealers_mongo()
    make_dealer_detail_mongo()
    make_dealers_kansas_mongo()
    make_admin_login()
    make_admin_logout()
    make_cars()
    make_car_models()
    make_sentiment_analyzer()
    make_get_dealers()
    make_get_dealers_loggedin()
    make_dealersbystate()
    make_dealer_id_reviews()
    make_dealership_review_submission()
    make_added_review()
    make_cicd()
    make_deployed_landingpage()
    make_deployed_loggedin()
    make_deployed_dealer_detail()
    make_deployed_add_review()
    print("All screenshots generated successfully!")

