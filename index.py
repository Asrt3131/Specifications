import streamlit as st
import streamlit.components.v1 as components

# تنظیمات صفحه Streamlit
st.set_page_config(page_title="Ali Obaidi | Portfolio", page_icon="🌌", layout="wide")

# استایل‌های مخفی کردن منوی پیش‌فرض استریم‌لیت برای اینکه سایت خودمان تمام صفحه باشد
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
        iframe {height: 100vh !important; width: 100vw !important; border: none;}
    </style>
""", unsafe_allow_html=True)

# داده‌های پروژه‌ها
projects = [
    {"title": "SMS Spam Detector", "live": "https://sms-spam-detector-kb98vmxzj65ttuffy6h56dsyvu55.streamlit.app/", "github": "https://github.com/Asrt3131/sms-spam-detector.git"},
    {"title": "House Price Prediction", "live": "https://house-price-prediction-acuccze543baay6rn4354syp34bgbq.streamlit.app/", "github": "https://github.com/Asrt3131/house-price-prediction.git"},
    {"title": "Persian RAG Chatbot", "live": "https://persian-rag-chatbot-amtzeujabqdazrzcvnrew5.streamlit.app/", "github": "https://github.com/Asrt3131/persian-rag-chatbot.git"},
    {"title": "Medical-Legal RAG", "live": "https://medical-legal-rag-f8whusetlraqtgxt8lwiam.streamlit.app/", "github": "https://github.com/Asrt3131/medical-legal-rag.git"},
    {"title": "AI Agent Tool Calling", "live": "https://ai-agent-tool-calling-f6rdca8iuuhukcwe7lrnl5.streamlit.app/", "github": "https://github.com/Asrt3131/ai-agent-tool-calling.git"},
    {"title": "Realtime Vision YOLOv8", "live": "https://realtime-vision-yolov8-mediapipe-emyqrahh3wfbgyvvycvcfq.streamlit.app/", "github": "https://github.com/Asrt3131/realtime-vision-yolov8-mediapipe.git"},
    {"title": "ML API Project", "live": "https://ml-api-project-8xte3fdm8ft2see9qzezu9.streamlit.app/", "github": "https://github.com/Asrt3131/ml-api-project.git"},
    {"title": "Data Dashboard", "live": "https://data-dashboard-srt343-z8hpwmaamvsucqn5jc5a4c.streamlit.app/", "github": "https://github.com/Asrt3131/data-dashboard-srt343.git"}
]

# ساخت قالب HTML به صورت داینامیک برای تزریق در Streamlit
def get_html_content():
    # تولید کدهای HTML کارت‌های پروژه
    projects_html = ""
    for p in projects:
        projects_html += f"""
        <div class="project-card">
            <img src="https://images.unsplash.com/photo-1555949963-aa79dcee981c?auto=format&fit=crop&w=400&q=80" class="project-img" alt="{p['title']}">
            <div class="project-content">
                <h3 class="project-title">{p['title']}</h3>
                <div class="project-btns">
                    <a href="{p['live']}" target="_blank" class="btn btn-live">🚀 مشاهده و اجرای پروژه</a>
                    <a href="{p['github']}" target="_blank" class="btn btn-data">📁 لینک داده‌های گیت‌هاب</a>
                </div>
            </div>
        </div>
        """

    html_code = f"""
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Vazirmatn:wght@300;500;800&display=swap" rel="stylesheet">
        <style>
            :root {{
                --bg-color: #050510;
                --cyan: #00f3ff;
                --pink: #ff00ea;
                --purple: #8a2be2;
                --text-color: #e0e0e0;
            }}
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                font-family: 'Vazirmatn', sans-serif;
                background-color: var(--bg-color);
                color: var(--text-color);
                overflow-x: hidden;
                min-height: 100vh;
            }}
            #canvas-bg {{
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                z-index: -1; background: radial-gradient(circle at center, #11111a 0%, #050510 100%);
            }}
            
            /* صفحه انتخاب زبان */
            .lang-overlay {{
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background: rgba(5,5,16,0.95); display: flex; flex-direction: column; 
                align-items: center; justify-content: center; z-index: 1000; backdrop-filter: blur(10px);
            }}
            .lang-overlay h1 {{
                font-size: 2rem; margin-bottom: 40px; text-align: center;
                background: linear-gradient(90deg, var(--cyan), var(--pink));
                -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                animation: pulse 2s infinite alternate; font-family: 'Orbitron', sans-serif;
            }}
            .lang-btns {{ display: flex; gap: 20px; flex-wrap: wrap; justify-content: center; }}
            .lang-btn {{
                padding: 15px 40px; font-size: 1.2rem; font-weight: bold;
                background: rgba(255,255,255,0.05); border: 2px solid var(--cyan); color: var(--cyan);
                border-radius: 50px; cursor: pointer; text-decoration: none;
                transition: 0.3s; box-shadow: 0 0 10px rgba(0,243,255,0.2);
            }}
            .lang-btn:hover {{
                background: var(--cyan); color: var(--bg-color);
                box-shadow: 0 0 20px var(--cyan); transform: scale(1.05);
            }}

            /* محتوای اصلی */
            .container {{ max-width: 1200px; margin: 0 auto; padding: 40px 20px; }}
            .profile-header {{
                display: flex; align-items: center; gap: 40px;
                background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);
                padding: 40px; border-radius: 24px; backdrop-filter: blur(15px);
                margin-bottom: 60px; position: relative; overflow: hidden;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5); animation: fadeInUp 1s ease;
            }}
            .profile-header::before {{
                content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
                background: conic-gradient(from 0deg, transparent, transparent, var(--cyan), transparent, transparent, var(--pink), transparent);
                animation: rotate 10s linear infinite; z-index: -1; opacity: 0.3;
            }}
            .profile-img-container {{
                position: relative; width: 180px; height: 180px; border-radius: 50%;
                padding: 4px; background: linear-gradient(45deg, var(--cyan), var(--pink));
                box-shadow: 0 0 25px var(--cyan); animation: float 4s ease-in-out infinite; flex-shrink: 0;
            }}
            .profile-img {{
                width: 100%; height: 100%; border-radius: 50%;
                object-fit: cover; object-position: center 20%; transition: opacity 0.5s ease; background-color: #222;
            }}
            .profile-info h1 {{
                font-size: 2.5rem; margin-bottom: 10px;
                background: linear-gradient(90deg, #fff, var(--cyan));
                -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            }}
            .profile-info p {{ font-size: 1.1rem; margin-bottom: 8px; color: #aaa; }}
            .profile-info .badges {{ display: flex; gap: 10px; flex-wrap: wrap; margin-top: 15px; }}
            .badge {{
                background: rgba(255,0,234,0.15); border: 1px solid var(--pink);
                padding: 6px 15px; border-radius: 20px; font-size: 0.9rem;
                color: var(--pink); box-shadow: 0 0 10px rgba(255,0,234,0.2);
            }}
            .social-links {{ display: flex; gap: 10px; margin-top: 25px; flex-wrap: wrap; }}
            .social-links a {{
                display: flex; align-items: center; gap: 8px; color: #fff; text-decoration: none;
                font-size: 0.9rem; background: rgba(255,255,255,0.05); padding: 8px 15px;
                border-radius: 10px; transition: 0.3s; border: 1px solid rgba(255,255,255,0.1);
            }}
            .social-links a:hover {{
                background: var(--purple); border-color: var(--purple);
                box-shadow: 0 0 15px var(--purple); transform: translateY(-3px);
            }}
            .section-title {{
                text-align: center; font-size: 2.2rem; margin-bottom: 40px;
                background: linear-gradient(90deg, var(--pink), var(--cyan));
                -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            }}
            .projects-grid {{
                display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 30px;
            }}
            .project-card {{
                background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);
                border-radius: 20px; overflow: hidden; transition: 0.4s;
                backdrop-filter: blur(10px); display: flex; flex-direction: column;
            }}
            .project-card:hover {{
                transform: translateY(-10px); border-color: var(--cyan);
                box-shadow: 0 15px 30px rgba(0,243,255,0.15);
            }}
            .project-img {{ width: 100%; height: 200px; object-fit: cover; border-bottom: 1px solid rgba(255,255,255,0.1); }}
            .project-content {{ padding: 25px; display: flex; flex-direction: column; flex-grow: 1; }}
            .project-title {{ font-size: 1.3rem; margin-bottom: 20px; color: #fff; text-align: center; font-weight: bold; }}
            .project-btns {{ display: flex; flex-direction: column; gap: 10px; margin-top: auto; }}
            .btn {{
                text-align: center; padding: 12px; border-radius: 12px;
                text-decoration: none; font-weight: bold; transition: 0.3s;
                display: flex; justify-content: center; align-items: center; gap: 8px; font-size: 0.95rem;
            }}
            .btn-live {{ background: linear-gradient(90deg, var(--cyan), #0088ff); color: #000; }}
            .btn-live:hover {{ box-shadow: 0 0 20px var(--cyan); transform: scale(1.02); }}
            .btn-data {{ background: transparent; border: 1px solid var(--pink); color: var(--pink); }}
            .btn-data:hover {{ background: var(--pink); color: #fff; box-shadow: 0 0 20px var(--pink); transform: scale(1.02); }}
            @keyframes fadeInUp {{ from {{ opacity: 0; transform: translateY(30px); }} to {{ opacity: 1; transform: translateY(0); }} }}
            @keyframes float {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-10px); }} }}
            @keyframes rotate {{ from {{ transform: rotate(0deg); }} to {{ transform: rotate(360deg); }} }}
            @keyframes pulse {{ from {{ opacity: 0.7; }} to {{ opacity: 1; filter: drop-shadow(0 0 10px var(--pink)); }} }}
            @media (max-width: 768px) {{
                .profile-header {{ flex-direction: column; text-align: center; padding: 30px 20px; gap: 20px; }}
                .social-links {{ justify-content: center; }}
                .profile-info h1 {{ font-size: 2rem; }}
            }}
        </style>
    </head>
    <body>
        <canvas id="canvas-bg"></canvas>

        <div class="container">
            <header class="profile-header">
                <div class="profile-img-container">
                    <!-- نام عکس‌ها باید دقیقا img1.jpg تا img6.jpg باشد -->
                    <img src="app/static/img1.jpg" id="myProfilePic" alt="Ali Obaidi" class="profile-img" onerror="this.src='https://ui-avatars.com/api/?name=Ali+Obaidi&background=0D8ABC&color=fff&size=200'">
                </div>
                
                <div class="profile-info">
                    <h1>علی عبیدی</h1>
                    <p>مهندس هوش مصنوعی و توسعه‌دهنده وب</p>
                    <div class="badges">
                        <span class="badge">متولد ۲۰۰۶</span>
                        <span class="badge">بیش از ۸ پروژه</span>
                    </div>
                    
                    <div class="social-links">
                        <a href="https://instagram.com/A_srt343" target="_blank">📸 @A_srt343</a>
                        <a href="https://instagram.com/project_srt343" target="_blank">💼 اینستاگرام پروژه‌ها</a>
                        <a href="https://t.me/A_srt343" target="_blank">✈️ Telegram</a>
                        <a href="https://wa.me/A_srt343" target="_blank">💬 WhatsApp</a>
                        <a href="https://github.com/Asrt3131" target="_blank">💻 GitHub</a>
                    </div>
                </div>
            </header>

            <h2 class="section-title">✦ پروژه‌های کهکشانی ✦</h2>
            
            <div class="projects-grid">
                {projects_html}
            </div>
        </div>

        <script>
            // انیمیشن ستاره‌ها
            const canvas = document.getElementById('canvas-bg');
            const ctx = canvas.getContext('2d');
            let width, height, stars = [];
            function initCanvas() {{
                width = canvas.width = window.innerWidth;
                height = canvas.height = window.innerHeight;
                stars = [];
                for (let i = 0; i < 200; i++) {{
                    stars.push({{ x: Math.random() * width, y: Math.random() * height, radius: Math.random() * 1.5, speed: Math.random() * 0.5 + 0.1, alpha: Math.random() }});
                }}
            }}
            function animateStars() {{
                ctx.clearRect(0, 0, width, height);
                stars.forEach(star => {{
                    ctx.beginPath(); ctx.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
                    ctx.fillStyle = `rgba(255, 255, 255, ${{star.alpha}})`; ctx.fill();
                    star.y += star.speed; if (star.y > height) {{ star.y = 0; star.x = Math.random() * width; }}
                    star.alpha += (Math.random() - 0.5) * 0.05; if(star.alpha < 0.1) star.alpha = 0.1; if(star.alpha > 0.8) star.alpha = 0.8;
                }});
                requestAnimationFrame(animateStars);
            }}
            window.addEventListener('resize', initCanvas);
            initCanvas(); animateStars();

            // اسلایدر عکس پروفایل
            const myPhotos = ['app/static/img1.jpg', 'app/static/img2.jpg', 'app/static/img3.jpg', 'app/static/img4.jpg', 'app/static/img5.jpg', 'app/static/img6.jpg'];
            let currentPhotoIndex = 0;
            const profilePic = document.getElementById('myProfilePic');
            if(profilePic) {{
                setInterval(() => {{
                    profilePic.style.opacity = '0';
                    setTimeout(() => {{
                        currentPhotoIndex = (currentPhotoIndex + 1) % myPhotos.length;
                        profilePic.src = myPhotos[currentPhotoIndex];
                        profilePic.style.opacity = '1';
                    }}, 500); 
                }}, 5000); 
            }}
        </script>
    </body>
    </html>
    """
    return html_code

# رندر کردن قالب در استریم‌لیت
components.html(get_html_content(), height=2000, scrolling=True)
