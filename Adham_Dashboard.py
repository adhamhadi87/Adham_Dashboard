import streamlit as st
from textwrap import dedent

st.set_page_config(
    page_title="Portal Dashboard CIDB",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

DASHBOARDS = [
    {
        "title": "Prestasi Program",
        "category": "Prestasi Fizikal",
        "icon": "🚦",
        "description": "Pemantauan pencapaian fizikal program mengikut sektor, bahagian dan status traffic light.",
        "url": "https://prestasiprogram.streamlit.app/",
        "accent": "#16a34a",
        "accent_soft": "rgba(34, 197, 94, 0.14)",
        "number": "01",
    },
    {
        "title": "Dashboard JPKA",
        "category": "Kewangan & Akaun",
        "icon": "💰",
        "description": "Prestasi perbelanjaan, hasil, geran, P&L, Balance Sheet dan Cash Flow CIDB.",
        "url": "https://jpka-cidb520.streamlit.app/",
        "accent": "#2563eb",
        "accent_soft": "rgba(37, 99, 235, 0.14)",
        "number": "02",
    },
    {
        "title": "e-Filing Baucar CIDB",
        "category": "Pengurusan Dokumen",
        "icon": "📁",
        "description": "Carian, semakan dan pengurusan rekod e-Filing baucar CIDB secara dalam talian.",
        "url": "https://e-filing-baucar-cidb.streamlit.app/",
        "accent": "#7c3aed",
        "accent_soft": "rgba(124, 58, 237, 0.14)",
        "number": "03",
    },
]

st.markdown(
    """
    <style>
    #MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"],
    [data-testid="stStatusWidget"], section[data-testid="stSidebar"] {
        display: none !important;
    }

    header[data-testid="stHeader"] {
        height: 0 !important;
        min-height: 0 !important;
        background: transparent !important;
    }

    html, body, [data-testid="stAppViewContainer"], .stApp {
        min-height: 100vh !important;
    }

    .stApp {
        background:
            radial-gradient(circle at 8% 10%, rgba(191,219,254,.55), transparent 29%),
            radial-gradient(circle at 91% 12%, rgba(221,214,254,.48), transparent 30%),
            radial-gradient(circle at 50% 100%, rgba(219,234,254,.55), transparent 44%),
            linear-gradient(135deg, #f8fafc 0%, #eef4ff 48%, #f8fafc 100%) !important;
        background-attachment: fixed !important;
    }

    .block-container {
        width: 100% !important;
        max-width: 1500px !important;
        padding: .55rem 2rem .45rem !important;
        margin: 0 auto !important;
    }

    .portal-shell {
        min-height: calc(100vh - 1rem);
        display: flex;
        flex-direction: column;
        padding: 16px 20px 9px;
        border-radius: 28px;
        background: linear-gradient(135deg, rgba(255,255,255,.80), rgba(248,250,252,.60));
        border: 1px solid rgba(255,255,255,.90);
        box-shadow: 0 22px 60px rgba(15,23,42,.11), inset 0 1px 0 rgba(255,255,255,.95);
        backdrop-filter: blur(18px);
    }

    .portal-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 18px;
        padding: 3px 5px 11px;
    }

    .brand-wrap {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .brand-icon {
        width: 46px;
        height: 46px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 15px;
        font-size: 25px;
        background: linear-gradient(145deg, rgba(255,255,255,.96), rgba(219,234,254,.90));
        border: 1px solid rgba(255,255,255,.95);
        box-shadow: 0 10px 24px rgba(37,99,235,.16);
    }

    .brand-title {
        margin: 0;
        color: #172033;
        font: 900 clamp(21px, 2vw, 29px)/1.05 Arial, sans-serif;
        letter-spacing: -.6px;
    }

    .brand-subtitle {
        margin-top: 4px;
        color: #64748b;
        font: 600 12px Arial, sans-serif;
    }

    .dashboard-count {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 13px;
        border-radius: 999px;
        color: #334155;
        font: 800 12px Arial, sans-serif;
        background: rgba(255,255,255,.66);
        border: 1px solid rgba(203,213,225,.72);
        box-shadow: 0 8px 20px rgba(15,23,42,.07);
    }

    .count-dot {
        width: 9px;
        height: 9px;
        border-radius: 50%;
        background: #22c55e;
        box-shadow: 0 0 0 4px rgba(34,197,94,.13), 0 0 12px rgba(34,197,94,.55);
    }

    .intro-line {
        display: flex;
        align-items: center;
        gap: 12px;
        margin: 0 5px 12px;
    }

    .intro-line::before, .intro-line::after {
        content: "";
        height: 1px;
        flex: 1;
        background: linear-gradient(90deg, transparent, rgba(148,163,184,.42), transparent);
    }

    .intro-text {
        color: #64748b;
        font: 700 11px Arial, sans-serif;
        text-align: center;
        white-space: nowrap;
    }

    .dashboard-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 17px;
        flex: 1;
        align-items: stretch;
    }

    .dashboard-link {
        display: block;
        min-width: 0;
        height: 100%;
        text-decoration: none !important;
        color: inherit !important;
        outline: none;
    }

    .dashboard-card {
        position: relative;
        height: 100%;
        min-height: 290px;
        display: flex;
        flex-direction: column;
        padding: 21px;
        overflow: hidden;
        border-radius: 24px;
        background: linear-gradient(145deg, rgba(255,255,255,.92), rgba(248,250,252,.72));
        border: 1px solid rgba(203,213,225,.76);
        box-shadow: 0 15px 34px rgba(15,23,42,.10), inset 0 1px 0 rgba(255,255,255,.98);
        backdrop-filter: blur(15px);
        cursor: pointer;
        transition: transform .22s ease, box-shadow .22s ease, border-color .22s ease;
    }

    .dashboard-card::before {
        content: "";
        position: absolute;
        top: -85px;
        right: -75px;
        width: 190px;
        height: 190px;
        border-radius: 50%;
        background: var(--accent-soft);
        filter: blur(4px);
        transition: transform .28s ease;
    }

    .dashboard-card::after {
        content: "";
        position: absolute;
        left: 0;
        bottom: 0;
        width: 100%;
        height: 5px;
        background: linear-gradient(90deg, transparent, var(--accent), transparent);
        opacity: .76;
    }

    .dashboard-link:hover .dashboard-card {
        transform: translateY(-7px) scale(1.012);
        border-color: var(--accent);
        box-shadow: 0 26px 52px rgba(15,23,42,.16), 0 0 0 3px var(--accent-soft);
    }

    .dashboard-link:hover .dashboard-card::before {
        transform: scale(1.18);
    }

    .card-top {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 16px;
        position: relative;
        z-index: 2;
    }

    .card-icon {
        width: 56px;
        height: 56px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 18px;
        font-size: 30px;
        background: linear-gradient(145deg, rgba(255,255,255,.94), var(--accent-soft));
        border: 1px solid rgba(255,255,255,.96);
        box-shadow: 0 12px 27px var(--accent-soft);
    }

    .card-number {
        color: rgba(100,116,139,.30);
        font: 900 33px/1 Arial, sans-serif;
        letter-spacing: -1px;
    }

    .card-category {
        width: fit-content;
        margin-top: 19px;
        padding: 6px 11px;
        border-radius: 999px;
        color: var(--accent);
        font: 900 10px Arial, sans-serif;
        text-transform: uppercase;
        letter-spacing: .65px;
        background: var(--accent-soft);
        position: relative;
        z-index: 2;
    }

    .card-title {
        margin: 13px 0 8px;
        color: #1e293b;
        font: 900 clamp(18px, 1.55vw, 24px)/1.14 Arial, sans-serif;
        letter-spacing: -.35px;
        position: relative;
        z-index: 2;
    }

    .card-description {
        color: #64748b;
        font: 500 13px/1.5 Arial, sans-serif;
        position: relative;
        z-index: 2;
    }

    .card-footer {
        margin-top: auto;
        padding-top: 18px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 10px;
        position: relative;
        z-index: 2;
    }

    .open-label {
        color: var(--accent);
        font: 900 12px Arial, sans-serif;
    }

    .open-arrow {
        width: 35px;
        height: 35px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        color: white;
        font: 900 19px Arial, sans-serif;
        background: var(--accent);
        box-shadow: 0 9px 19px var(--accent-soft);
        transition: transform .20s ease;
    }

    .dashboard-link:hover .open-arrow {
        transform: translateX(4px) rotate(-4deg);
    }

    .portal-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 20px;
        padding: 11px 5px 1px;
        color: #94a3b8;
        font: 700 10px Arial, sans-serif;
    }

    .footer-right { text-align: right; }

    @media (max-width: 820px) {
        .dashboard-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .dashboard-count { display: none; }
        .portal-shell { min-height: auto; }
    }

    @media (max-width: 560px) {
        .block-container { padding: .4rem .55rem !important; }
        .portal-shell { padding: 13px; border-radius: 21px; }
        .dashboard-grid { grid-template-columns: 1fr; }
        .dashboard-card { min-height: 245px; }
        .brand-title { font-size: 20px; }
        .brand-subtitle { font-size: 10px; }
        .intro-text { white-space: normal; }
        .portal-footer { flex-direction: column; gap: 4px; text-align: center; }
        .footer-right { text-align: center; }
    }

    @media (min-width: 821px) and (max-height: 780px) {
        .block-container { padding-top: .3rem !important; padding-bottom: .25rem !important; }
        .portal-shell { min-height: calc(100vh - .6rem); padding-top: 11px; padding-bottom: 6px; }
        .portal-header { padding-bottom: 7px; }
        .brand-icon { width: 42px; height: 42px; font-size: 22px; }
        .brand-title { font-size: 22px; }
        .brand-subtitle { font-size: 10px; }
        .intro-line { margin-bottom: 8px; }
        .dashboard-card { min-height: 240px; padding: 17px; }
        .card-icon { width: 47px; height: 47px; font-size: 25px; }
        .card-number { font-size: 28px; }
        .card-category { margin-top: 13px; }
        .card-title { margin-top: 9px; font-size: 18px; }
        .card-description { font-size: 12px; line-height: 1.42; }
        .card-footer { padding-top: 12px; }
        .portal-footer { padding-top: 7px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def build_dashboard_card(dashboard: dict) -> str:
    return dedent(
        f"""
        <a
            class="dashboard-link"
            href="{dashboard['url']}"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="Buka {dashboard['title']}"
        >
            <article
                class="dashboard-card"
                style="--accent:{dashboard['accent']}; --accent-soft:{dashboard['accent_soft']};"
            >
                <div class="card-top">
                    <div class="card-icon">{dashboard['icon']}</div>
                    <div class="card-number">{dashboard['number']}</div>
                </div>

                <div class="card-category">{dashboard['category']}</div>
                <h2 class="card-title">{dashboard['title']}</h2>
                <div class="card-description">{dashboard['description']}</div>

                <div class="card-footer">
                    <div class="open-label">Klik untuk buka dashboard</div>
                    <div class="open-arrow">→</div>
                </div>
            </article>
        </a>
        """
    ).strip()


dashboard_cards_html = "\n".join(
    build_dashboard_card(dashboard)
    for dashboard in DASHBOARDS
)

portal_html = dedent(
    f"""
    <div class="portal-shell">
        <header class="portal-header">
            <div class="brand-wrap">
                <div class="brand-icon">📊</div>
                <div>
                    <h1 class="brand-title">PORTAL DASHBOARD CIDB</h1>
                    <div class="brand-subtitle">
                        Pusat Akses Dashboard Bahagian Kewangan &amp; Akaun
                    </div>
                </div>
            </div>

            <div class="dashboard-count">
                <span class="count-dot"></span>
                {len(DASHBOARDS)} Dashboard Aktif
            </div>
        </header>

        <div class="intro-line">
            <div class="intro-text">Pilih dashboard untuk membuka paparan berkaitan</div>
        </div>

        <main class="dashboard-grid">
            {dashboard_cards_html}
        </main>

        <footer class="portal-footer">
            <div>Bahagian Kewangan &amp; Akaun</div>
            <div class="footer-right">CIDB Malaysia • Portal Dashboard Dalaman</div>
        </footer>
    </div>
    """
).strip()

st.markdown(portal_html, unsafe_allow_html=True)
