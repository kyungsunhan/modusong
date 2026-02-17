import re
import streamlit as st
import streamlit.components.v1 as components

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="🐰 Rainbow Bunny Music",
    page_icon="🐰",
    layout="centered"
)

# ----------------------------
# Fixed YouTube URL
# ----------------------------
FIXED_URL = "https://youtu.be/l_ZHgg3g0NQ?si=S-mVoCc_Pj_ohUu8"


# ----------------------------
# Extract video id
# ----------------------------
def extract_video_id(url: str) -> str | None:
    patterns = [
        r"youtu\.be/([A-Za-z0-9_-]{11})",
        r"v=([A-Za-z0-9_-]{11})",
        r"youtube\.com/shorts/([A-Za-z0-9_-]{11})",
        r"youtube\.com/embed/([A-Za-z0-9_-]{11})",
    ]
    for p in patterns:
        m = re.search(p, url)
        if m:
            return m.group(1)
    return None


# ----------------------------
# Rainbow + Bunny Theme
# ----------------------------
THEME = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;900&display=swap');

html, body, [class*="css"] {
  font-family: 'Nunito', sans-serif;
}

.stApp {
  background: linear-gradient(135deg,
    rgba(255,120,168,0.35),
    rgba(255,196,92,0.35),
    rgba(255,255,140,0.35),
    rgba(140,255,170,0.35),
    rgba(140,210,255,0.35),
    rgba(180,160,255,0.35)
  );
  background-size: 400% 400%;
  animation: rainbow 14s ease infinite;
}

@keyframes rainbow {
  0% {background-position:0% 50%;}
  50% {background-position:100% 50%;}
  100% {background-position:0% 50%;}
}

.card {
  background: rgba(255,255,255,0.75);
  border-radius: 28px;
  padding: 20px;
  box-shadow: 0 15px 40px rgba(0,0,0,0.1);
  margin-bottom: 18px;
}

.title {
  text-align:center;
  font-size:36px;
  font-weight:900;
  background: linear-gradient(
    90deg,#ff4fa0,#ffb000,#53f69b,#4aa8ff,#a56bff
  );
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
}

.sub {
  text-align:center;
  font-size:14px;
  opacity:0.8;
}

.player {
  border-radius:22px;
  overflow:hidden;
  border:2px solid white;
  box-shadow:0 12px 30px rgba(0,0,0,0.12);
}
</style>
"""

st.markdown(THEME, unsafe_allow_html=True)

# ----------------------------
# Bunny Icon (SVG)
# ----------------------------
BUNNY = """
<svg width="60" height="60" viewBox="0 0 128 128">
<circle cx="64" cy="72" r="38" fill="#fff"/>
<circle cx="50" cy="68" r="5" fill="#333"/>
<circle cx="78" cy="68" r="5" fill="#333"/>
<path d="M64 76 C60 76,58 80,64 82 C70 80,68 76,64 76 Z" fill="#ff6aa8"/>
</svg>
"""

# ----------------------------
# Header
# ----------------------------
st.markdown(
    f"""
<div class="card">
  <div style="text-align:center">{BUNNY}</div>
  <div class="title">🐰 Rainbow Bunny Music 🌈</div>
  <div class="sub">토끼와 함께 음악을 들어요 🎵</div>
</div>
""",
    unsafe_allow_html=True
)

# ----------------------------
# Controls
# ----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    autoplay = st.toggle("🚀 자동재생", False)

with col2:
    loop = st.toggle("🔁 반복재생", False)

with col3:
    start = st.number_input("⏱ 시작(초)", 0, value=0)

st.markdown("</div>", unsafe_allow_html=True)


# ----------------------------
# Player
# ----------------------------
video_id = extract_video_id(FIXED_URL)

if not video_id:
    st.error("고정된 유튜브 링크 오류")
    st.stop()

params = {
    "start": str(int(start)),
    "autoplay": "1" if autoplay else "0",
    "loop": "1" if loop else "0",
    "playlist": video_id if loop else "",
    "controls": "1",
    "rel": "0",
}

query = "&".join([f"{k}={v}" for k, v in params.items()])

embed_url = f"https://www.youtube.com/embed/{video_id}?{query}"


st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 🎧 지금 음악 재생중이에요")

html = f"""
<div class="player">
  <iframe
    width="100%"
    height="280"
    src="{embed_url}"
    frameborder="0"
    allow="autoplay; encrypted-media"
    allowfullscreen>
  </iframe>
</div>
"""

components.html(html, height=310)

st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------
# Footer
# ----------------------------
st.caption("🐰 Made with Streamlit · Rainbow Theme 🌈")
