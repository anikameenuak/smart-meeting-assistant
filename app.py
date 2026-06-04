import streamlit as st
import requests
import pandas as pd

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="Notes Blend AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ======================
# FULL CSS REDESIGN
# ======================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@300;400;500&display=swap');

/* ── RESET & BASE ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

.stApp {
    background-color: #0a0a0f;
    background-image:
        radial-gradient(ellipse 80% 50% at 50% -10%, rgba(255, 90, 0, 0.12) 0%, transparent 60%),
        radial-gradient(ellipse 40% 30% at 90% 80%, rgba(120, 40, 255, 0.08) 0%, transparent 50%);
    font-family: 'JetBrains Mono', monospace;
    min-height: 100vh;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 4rem 4rem 4rem; max-width: 1100px; margin: auto; }

/* ── HERO SECTION ── */
.hero-wrap {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    padding: 3.5rem 0 2.5rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 3rem;
}

.hero-left {}

.hero-badge {
    display: inline-block;
    background: rgba(255, 90, 0, 0.15);
    border: 1px solid rgba(255, 90, 0, 0.35);
    color: #ff5a00;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    padding: 5px 14px;
    border-radius: 4px;
    margin-bottom: 1.2rem;
}

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(40px, 6vw, 72px);
    font-weight: 800;
    color: #f0ede8;
    line-height: 0.95;
    letter-spacing: -0.03em;
    margin-bottom: 1rem;
}

.hero-title span {
    color: #ff5a00;
}

.hero-desc {
    color: rgba(240,237,232,0.4);
    font-size: 13px;
    letter-spacing: 0.04em;
    line-height: 1.7;
    max-width: 380px;
}

.hero-right {
    text-align: right;
}

.hero-stat {
    font-family: 'Syne', sans-serif;
    font-size: 11px;
    color: rgba(240,237,232,0.25);
    letter-spacing: 0.12em;
    text-transform: uppercase;
    line-height: 2;
}

.hero-stat strong {
    display: block;
    font-size: 28px;
    font-weight: 700;
    color: rgba(240,237,232,0.7);
    letter-spacing: -0.02em;
    line-height: 1;
}

/* ── SECTION LABELS ── */
.section-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: rgba(255,90,0,0.7);
    margin-bottom: 0.75rem;
    display: flex;
    align-items: center;
    gap: 10px;
}

.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(255,90,0,0.15);
}

/* ── TEXTAREA STYLING ── */
.stTextArea label {
    display: none !important;
}

.stTextArea textarea {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 12px !important;
    color: rgba(240,237,232,0.8) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 13px !important;
    line-height: 1.8 !important;
    padding: 20px !important;
    transition: border-color 0.2s ease !important;
    caret-color: #ff5a00 !important;
}

.stTextArea textarea:focus {
    border-color: rgba(255,90,0,0.4) !important;
    box-shadow: 0 0 0 3px rgba(255,90,0,0.06) !important;
    background: rgba(255,255,255,0.04) !important;
}

.stTextArea textarea::placeholder {
    color: rgba(240,237,232,0.18) !important;
}

/* ── BUTTON ── */
.stButton > button {
    background: #ff5a00 !important;
    color: #0a0a0f !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
    padding: 14px 32px !important;
    border-radius: 8px !important;
    border: none !important;
    transition: all 0.2s ease !important;
    width: 100% !important;
}

.stButton > button:hover {
    background: #ff7a2a !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 24px rgba(255,90,0,0.3) !important;
}

.stButton > button:active {
    transform: translateY(0px) !important;
}

/* ── TIPS SIDEBAR ── */
.tips-panel {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 12px;
    padding: 20px;
    height: 100%;
}

.tips-title {
    font-family: 'Syne', sans-serif;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: rgba(240,237,232,0.35);
    margin-bottom: 16px;
}

.tip-item {
    display: flex;
    gap: 12px;
    padding: 12px 0;
    border-bottom: 1px solid rgba(255,255,255,0.04);
}

.tip-item:last-child { border-bottom: none; }

.tip-icon {
    width: 28px;
    height: 28px;
    background: rgba(255,90,0,0.1);
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 13px;
    flex-shrink: 0;
}

.tip-text {
    font-size: 12px;
    color: rgba(240,237,232,0.45);
    line-height: 1.6;
}

.tip-text strong {
    display: block;
    color: rgba(240,237,232,0.7);
    font-size: 12px;
    margin-bottom: 2px;
}

/* ── WARNING / ERROR ── */
.stAlert {
    background: rgba(255,90,0,0.08) !important;
    border: 1px solid rgba(255,90,0,0.2) !important;
    border-radius: 8px !important;
    color: rgba(240,237,232,0.7) !important;
}

/* ── SPINNER ── */
.stSpinner > div {
    border-top-color: #ff5a00 !important;
}

/* ── RESULT CARDS ── */
.result-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 28px;
    margin-bottom: 12px;
    position: relative;
    overflow: hidden;
}

.result-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 3px; height: 100%;
    background: #ff5a00;
    border-radius: 3px 0 0 3px;
}

.result-text {
    color: rgba(240,237,232,0.75);
    font-size: 14px;
    line-height: 1.9;
    font-family: 'JetBrains Mono', monospace;
}

/* ── DATAFRAME ── */
.stDataFrame {
    border-radius: 12px !important;
    overflow: hidden !important;
}

[data-testid="stDataFrame"] > div {
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    background: rgba(255,255,255,0.02) !important;
}

/* ── DOWNLOAD BUTTON ── */
.stDownloadButton > button {
    background: transparent !important;
    color: rgba(240,237,232,0.6) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 12px !important;
    letter-spacing: 0.05em !important;
    padding: 10px 24px !important;
    border-radius: 8px !important;
    transition: all 0.2s ease !important;
}

.stDownloadButton > button:hover {
    border-color: rgba(255,90,0,0.4) !important;
    color: #ff5a00 !important;
    background: rgba(255,90,0,0.05) !important;
}

/* ── DIVIDER ── */
.custom-divider {
    height: 1px;
    background: rgba(255,255,255,0.06);
    margin: 2.5rem 0;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(255,90,0,0.3); border-radius: 4px; }
</style>
""", unsafe_allow_html=True)

# ======================
# HERO
# ======================
st.markdown("""
<div class="hero-wrap">
    <div class="hero-left">
        <div class="hero-badge">⚡ AI-Powered · v2.0</div>
        <div class="hero-title">Notes<br><span>Blend</span></div>
        <div class="hero-desc">Drop your raw meeting transcript. Get structured summaries and action items in seconds.</div>
    </div>
    <div class="hero-right">
        <div class="hero-stat"><strong>~3s</strong>avg processing</div>
        <div class="hero-stat" style="margin-top:16px"><strong>GPT-4</strong>backend model</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ======================
# INPUT + TIPS COLUMNS
# ======================
col1, col2 = st.columns([3, 1], gap="large")

with col1:
    st.markdown('<div class="section-label">01 — Input Transcript</div>', unsafe_allow_html=True)
    transcript = st.text_area(
        "transcript",
        height=280,
        placeholder="Paste meeting notes, call transcript, or any unstructured text here...\n\nExample:\n  John: Let's move the launch to Friday.\n  Sarah: I'll update the deck by Thursday.\n  Mark: I need to loop in the legal team before EOD."
    )
    st.write("")
    analyze = st.button("⚡ Analyze Meeting")

with col2:
    st.markdown("""
    <div class="tips-panel">
        <div class="tips-title">How it works</div>
        <div class="tip-item">
            <div class="tip-icon">📋</div>
            <div class="tip-text"><strong>Paste transcript</strong>Any meeting notes, raw text, or call logs work.</div>
        </div>
        <div class="tip-item">
            <div class="tip-icon">⚡</div>
            <div class="tip-text"><strong>AI analyzes it</strong>Extracts key decisions and assigns owners.</div>
        </div>
        <div class="tip-item">
            <div class="tip-icon">📥</div>
            <div class="tip-text"><strong>Download report</strong>Export action items as CSV for your team.</div>
        </div>
        <div class="tip-item">
            <div class="tip-icon">🔒</div>
            <div class="tip-text"><strong>Private & fast</strong>Nothing stored. Results in under 5 seconds.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ======================
# API CALL + RESULTS
# ======================
if analyze:
    if not transcript.strip():
        st.warning("Transcript is empty. Paste some meeting text above.")
    else:
        with st.spinner("Analyzing transcript..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/analyze",
                    json={"transcript": transcript},
                    timeout=30
                )
                response.raise_for_status()
                data = response.json()

                st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

                # ── SUMMARY ──
                st.markdown('<div class="section-label">02 — Meeting Summary</div>', unsafe_allow_html=True)
                st.markdown(f"""
                <div class="result-card">
                    <div class="result-text">{data['summary']}</div>
                </div>
                """, unsafe_allow_html=True)

                st.write("")

                # ── ACTION ITEMS ──
                st.markdown('<div class="section-label">03 — Action Items</div>', unsafe_allow_html=True)
                df = pd.DataFrame(data["actions"])
                st.dataframe(df, use_container_width=True, hide_index=True)

                st.write("")

                # ── DOWNLOAD ──
                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    "↓ Export as CSV",
                    csv,
                    "meeting_actions.csv",
                    "text/csv"
                )

            except requests.exceptions.ConnectionError:
                st.error("Cannot reach backend at localhost:8000. Make sure your FastAPI server is running.")
            except Exception as e:
                st.error(f"Something went wrong: {e}")