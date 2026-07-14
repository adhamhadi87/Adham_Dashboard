import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Portal Dashboard CIDB",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# DASHBOARD DATA
# Tambah dashboard baru dalam senarai ini sahaja.
# =========================================================
DASHBOARDS = [
    {
        "title": "Prestasi Program",
        "category": "Prestasi Fizikal",
        "icon": "🚦",
        "description": (
            "Pemantauan pencapaian fizikal program mengikut sektor, "
            "bahagian dan status traffic light."
        ),
        "url": "https://prestasiprogram.streamlit.app/",
        "accent": "#16a34a",
        "accent_soft": "rgba(34, 197, 94, 0.14)",
        "number": "01",
    },
    {
        "title": "Dashboard JPKA",
        "category": "Kewangan & Akaun",
        "icon": "💰",
        "description": (
            "Prestasi perbelanjaan, hasil, geran, P&L, "
            "Balance Sheet dan Cash Flow CIDB."
        ),
        "url": "https://jpka-cidb520.streamlit.app/",
        "accent": "#2563eb",
        "accent_soft": "rgba(37, 99, 235, 0.14)",
        "number": "02",
    },
    {
        "title": "e-Filing Baucar CIDB",
        "category": "Pengurusan Dokumen",
        "icon": "📁",
        "description": (
            "Carian, semakan dan pengurusan rekod "
            "e-Filing baucar CIDB secara dalam talian."
        ),
        "url": "https://e-filing-baucar-cidb.streamlit.app/",
        "accent": "#7c3aed",
        "accent_soft": "rgba(124, 58, 237, 0.14)",
        "number": "03",
    },
]


# =========================================================
# GLOBAL CSS
# =========================================================
st.markdown(
    """
    <style>

    /* ==========================================
       HIDE STREAMLIT ELEMENTS
    ========================================== */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header[data-testid="stHeader"] {
        height: 0 !important;
        min-height: 0 !important;
        background: transparent !important;
    }

    [data-testid="stToolbar"] {
        display: none !important;
    }

    [data-testid="stDecoration"] {
        display: none !important;
    }

    [data-testid="stStatusWidget"] {
        display: none !important;
    }

    section[data-testid="stSidebar"] {
        display: none !important;
    }

    button[data-testid="stBaseButton-headerNoPadding"] {
        display: none !important;
    }


    /* ==========================================
       PAGE BACKGROUND
    ========================================== */

    html,
    body,
    [data-testid="stAppViewContainer"],
    .stApp {
        min-height: 100vh !important;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 8% 10%,
                rgba(191, 219, 254, 0.55) 0%,
                transparent 29%
            ),
            radial-gradient(
                circle at 91% 12%,
                rgba(221, 214, 254, 0.48) 0%,
                transparent 30%
            ),
            radial-gradient(
                circle at 50% 100%,
                rgba(219, 234, 254, 0.55) 0%,
                transparent 44%
            ),
            linear-gradient(
                135deg,
                #f8fafc 0%,
                #eef4ff 48%,
                #f8fafc 100%
            ) !important;

        background-attachment: fixed !important;
    }


    /* ==========================================
       MAIN CONTAINER
    ========================================== */

    .block-container {
        width: 100% !important;
        max-width: 1500px !important;

        padding-top: 0.65rem !important;
        padding-bottom: 0.55rem !important;
        padding-left: 2.2rem !important;
        padding-right: 2.2rem !important;

        margin-left: auto !important;
        margin-right: auto !important;
    }


    /* ==========================================
       PORTAL SHELL
    ========================================== */

    .portal-shell {
        min-height: calc(100vh - 1.2rem);

        display: flex;
        flex-direction: column;

        padding: 18px 22px 10px 22px;

        border-radius: 30px;

        background:
            linear-gradient(
                135deg,
                rgba(255, 255, 255, 0.78),
                rgba(248, 250, 252, 0.58)
            );

        border: 1px solid rgba(255, 255, 255, 0.88);

        box-shadow:
            0 22px 60px rgba(15, 23, 42, 0.11),
            inset 0 1px 0 rgba(255, 255, 255, 0.95);

        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
    }


    /* ==========================================
       HEADER
    ========================================== */

    .portal-header {
        display: flex;
        justify-content: space-between;
        align-items: center;

        gap: 20px;

        padding: 4px 6px 13px 6px;
    }

    .brand-wrap {
        display: flex;
        align-items: center;
        gap: 13px;
    }

    .brand-icon {
        width: 48px;
        height: 48px;

        display: flex;
        align-items: center;
        justify-content: center;

        flex-shrink: 0;

        border-radius: 16px;

        font-size: 26px;

        background:
            linear-gradient(
                145deg,
                rgba(255,255,255,0.95),
                rgba(219,234,254,0.90)
            );

        border: 1px solid rgba(255,255,255,0.95);

        box-shadow:
            0 10px 24px rgba(37,99,235,0.16),
            inset 0 1px 0 rgba(255,255,255,0.98);
    }

    .brand-title {
        margin: 0;

        color: #172033;

        font-family: Arial, sans-serif;
        font-size: clamp(21px, 2vw, 30px);
        font-weight: 900;

        letter-spacing: -0.6px;
        line-height: 1.05;
    }

    .brand-subtitle {
        margin-top: 4px;

        color: #64748b;

        font-family: Arial, sans-serif;
        font-size: 12px;
        font-weight: 600;
    }

    .dashboard-count {
        display: inline-flex;
        align-items: center;
        gap: 8px;

        padding: 9px 14px;

        border-radius: 999px;

        color: #334155;

        font-family: Arial, sans-serif;
        font-size: 12px;
        font-weight: 800;

        background: rgba(255,255,255,0.64);

        border: 1px solid rgba(203,213,225,0.72);

        box-shadow:
            0 8px 20px rgba(15,23,42,0.07),
            inset 0 1px 0 rgba(255,255,255,0.92);

        backdrop-filter: blur(12px);
    }

    .count-dot {
        width: 9px;
        height: 9px;

        border-radius: 50%;

        background: #22c55e;

        box-shadow:
            0 0 0 4px rgba(34,197,94,0.13),
            0 0 12px rgba(34,197,94,0.55);
    }


    /* ==========================================
       INTRO LINE
    ========================================== */

    .intro-line {
        display: flex;
        align-items: center;
        gap: 12px;

        margin: 0 6px 14px 6px;
    }

    .intro-line::before,
    .intro-line::after {
        content: "";

        height: 1px;
        flex: 1;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(148,163,184,0.42),
                transparent
            );
    }

    .intro-text {
        color: #64748b;

        font-family: Arial, sans-serif;
        font-size: 11px;
        font-weight: 700;

        text-align: center;
        white-space: nowrap;
    }


    /* ==========================================
       CARD GRID
    ========================================== */

    .dashboard-grid {
        display: grid;

        grid-template-columns:
            repeat(3, minmax(0, 1fr));

        gap: 18px;

        flex: 1;
        align-items: stretch;
    }


    /* ==========================================
       CLICKABLE LINK
    ========================================== */

    .dashboard-link {
        display: block;

        min-width: 0;
        height: 100%;

        text-decoration: none !important;
        color: inherit !important;

        outline: none;
    }


    /* ==========================================
       DASHBOARD CARD
    ========================================== */

    .dashboard-card {
        --accent: #2563eb;
        --accent-soft: rgba(37, 99, 235, 0.14);

        position: relative;

        height: 100%;
        min-height: 300px;

        display: flex;
        flex-direction: column;

        padding: 22px;

        overflow: hidden;

        border-radius: 25px;

        background:
            linear-gradient(
                145deg,
                rgba(255,255,255,0.91),
                rgba(248,250,252,0.71)
            );

        border: 1px solid rgba(203,213,225,0.76);

        box-shadow:
            0 15px 34px rgba(15,23,42,0.10),
            inset 0 1px 0 rgba(255,255,255,0.98);

        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);

        cursor: pointer;

        transition:
            transform 0.22s ease,
            box-shadow 0.22s ease,
            border-color 0.22s ease;
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

        transition:
            transform 0.28s ease,
            opacity 0.28s ease;
    }

    .dashboard-card::after {
        content: "";

        position: absolute;
        left: 0;
        bottom: 0;

        width: 100%;
        height: 5px;

        background:
            linear-gradient(
                90deg,
                transparent,
                var(--accent),
                transparent
            );

        opacity: 0.76;
    }

    .dashboard-link:hover .dashboard-card {
        transform:
            translateY(-7px)
            scale(1.012);

        border-color: var(--accent);

        box-shadow:
            0 26px 52px rgba(15,23,42,0.16),
            0 0 0 3px var(--accent-soft),
            inset 0 1px 0 rgba(255,255,255,0.98);
    }

    .dashboard-link:hover .dashboard-card::before {
        transform: scale(1.18);
        opacity: 0.95;
    }

    .dashboard-link:focus-visible .dashboard-card {
        outline: 3px solid var(--accent);
        outline-offset: 4px;
    }


    /* ==========================================
       CARD TOP
    ========================================== */

    .card-top {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;

        gap: 16px;

        position: relative;
        z-index: 2;
    }

    .card-icon {
        width: 58px;
        height: 58px;

        display: flex;
        align-items: center;
        justify-content: center;

        flex-shrink: 0;

        border-radius: 18px;

        font-size: 31px;

        background:
            linear-gradient(
                145deg,
                rgba(255,255,255,0.94),
                var(--accent-soft)
            );

        border: 1px solid rgba(255,255,255,0.96);

        box-shadow:
            0 12px 27px var(--accent-soft),
            inset 0 1px 0 rgba(255,255,255,0.98);
    }

    .card-number {
        color: rgba(100,116,139,0.30);

        font-family: Arial, sans-serif;
        font-size: 34px;
        font-weight: 900;

        letter-spacing: -1px;
        line-height: 1;
    }


    /* ==========================================
       CARD CONTENT
    ========================================== */

    .card-category {
        width: fit-content;

        margin-top: 21px;
        padding: 6px 11px;

        border-radius: 999px;

        color: var(--accent);

        font-family: Arial, sans-serif;
        font-size: 10px;
        font-weight: 900;

        text-transform: uppercase;
        letter-spacing: 0.65px;

        background: var(--accent-soft);

        position: relative;
        z-index: 2;
    }

    .card-title {
        margin: 14px 0 8px 0;

        color: #1e293b;

        font-family: Arial, sans-serif;
        font-size: clamp(18px, 1.55vw, 24px);
        font-weight: 900;

        letter-spacing: -0.35px;
        line-height: 1.14;

        position: relative;
        z-index: 2;
    }

    .card-description {
        color: #64748b;

        font-family: Arial, sans-serif;
        font-size: 13px;
        font-weight: 500;

        line-height: 1.55;

        position: relative;
        z-index: 2;
    }


    /* ==========================================
       CARD FOOTER
    ========================================== */

    .card-footer {
        margin-top: auto;
        padding-top: 20px;

        display: flex;
        align-items: center;
        justify-content: space-between;

        gap: 10px;

        position: relative;
        z-index: 2;
    }

    .open-label {
        color: var(--accent);

        font-family: Arial, sans-serif;
        font-size: 12px;
        font-weight: 900;
    }

    .open-arrow {
        width: 35px;
        height: 35px;

        display: flex;
        align-items: center;
        justify-content: center;

        flex-shrink: 0;

        border-radius: 50%;

        color: white;

        font-family: Arial, sans-serif;
        font-size: 19px;
        font-weight: 900;

        background: var(--accent);

        box-shadow:
            0 9px 19px var(--accent-soft);

        transition:
            transform 0.20s ease,
            box-shadow 0.20s ease;
    }

    .dashboard-link:hover .open-arrow {
        transform:
            translateX(4px)
            rotate(-4deg);

        box-shadow:
            0 12px 24px var(--accent-soft);
    }


    /* ==========================================
       FOOTER
    ========================================== */

    .portal-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;

        gap: 20px;

        padding: 13px 5px 1px 5px;

        color: #94a3b8;

        font-family: Arial, sans-serif;
        font-size: 10px;
        font-weight: 700;
    }

    .footer-right {
        text-align: right;
    }


    /* ==========================================
       RESPONSIVE — MEDIUM SCREEN
    ========================================== */

    @media (max-width: 1050px) {

        .block-container {
            padding-left: 1.1rem !important;
            padding-right: 1.1rem !important;
        }

        .dashboard-grid {
            gap: 13px;
        }

        .dashboard-card {
            min-height: 280px;
            padding: 18px;
        }

        .card-title {
            font-size: 18px;
        }

        .card-description {
            font-size: 12px;
        }
    }


    /* ==========================================
       RESPONSIVE — TABLET
    ========================================== */

    @media (max-width: 820px) {

        .portal-shell {
            min-height: auto;
        }

        .dashboard-grid {
            grid-template-columns:
                repeat(2, minmax(0, 1fr));
        }

        .dashboard-card {
            min-height: 285px;
        }

        .dashboard-count {
            display: none;
        }

        .portal-footer {
            flex-direction: column;
            gap: 4px;
            text-align: center;
        }

        .footer-right {
            text-align: center;
        }
    }


    /* ==========================================
       RESPONSIVE — MOBILE
    ========================================== */

    @media (max-width: 560px) {

        .block-container {
            padding-top: 0.4rem !important;
            padding-left: 0.55rem !important;
            padding-right: 0.55rem !important;
        }

        .portal-shell {
            padding: 13px;
            border-radius: 21px;
        }

        .dashboard-grid {
            grid-template-columns: 1fr;
        }

        .dashboard-card {
            min-height: 245px;
        }

        .brand-icon {
            width: 43px;
            height: 43px;
            font-size: 23px;
        }

        .brand-title {
            font-size: 20px;
        }

        .brand-subtitle {
            font-size: 10px;
        }

        .intro-text {
            white-space: normal;
        }
    }


    /* ==========================================
       SHORT LAPTOP HEIGHT
       Kurangkan ketinggian supaya muat satu skrin.
    ========================================== */

    @media (min-width: 821px) and (max-height: 780px) {

        .block-container {
            padding-top: 0.35rem !important;
            padding-bottom: 0.3rem !important;
        }

        .portal-shell {
            min-height: calc(100vh - 0.7rem);
            padding-top: 12px;
            padding-bottom: 7px;
        }

        .portal-header {
            padding-bottom: 8px;
        }

        .brand-icon {
            width: 43px;
            height: 43px;
            font-size: 23px;
        }

        .brand-title {
            font-size: 23px;
        }

        .brand-subtitle {
            font-size: 10px;
        }

        .intro-line {
            margin-bottom: 9px;
        }

        .dashboard-card {
            min-height: 245px;
            padding: 18px;
        }

        .card-icon {
            width: 48px;
            height: 48px;
            font-size: 26px;
        }

        .card-number {
            font-size: 29px;
        }

        .card-category {
            margin-top: 14px;
        }

        .card-title {
            margin-top: 10px;
            font-size: 19px;
        }

        .card-description {
            font-size: 12px;
            line-height: 1.45;
        }

        .card-footer {
            padding-top: 13px;
        }

        .portal-footer {
            padding-top: 8px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# BUILD DASHBOARD CARD HTML
# =========================================================
def build_dashboard_card(dashboard: dict) -> str:
    """
    Bina satu kad dashboard yang seluruh kawasannya boleh diklik.
    """

    return f"""
    <a
        class="dashboard-link"
        href="{dashboard['url']}"
        target="_blank"
        rel="noopener noreferrer"
        aria-label="Buka {dashboard['title']}"
    >
        <article
            class="dashboard-card"
            style="
                --accent: {dashboard['accent']};
                --accent-soft: {dashboard['accent_soft']};
            "
        >
            <div class="card-top">
                <div class="card-icon">
                    {dashboard['icon']}
                </div>

                <div class="card-number">
                    {dashboard['number']}
                </div>
            </div>

            <div class="card-category">
                {dashboard['category']}
            </div>

            <h2 class="card-title">
                {dashboard['title']}
            </h2>

            <div class="card-description">
                {dashboard['description']}
            </div>

            <div class="card-footer">
                <div class="open-label">
                    Klik untuk buka dashboard
                </div>

                <div class="open-arrow">
                    →
                </div>
            </div>
        </article>
    </a>
    """


# =========================================================
# GENERATE ALL CARDS
# =========================================================
dashboard_cards_html = "\n".join(
    build_dashboard_card(dashboard)
    for dashboard in DASHBOARDS
)


# =========================================================
# MAIN PORTAL
# =========================================================
portal_html = f"""
<div class="portal-shell">

    <header class="portal-header">

        <div class="brand-wrap">
            <div class="brand-icon">
                📊
            </div>

            <div>
                <h1 class="brand-title">
                    PORTAL DASHBOARD CIDB
                </h1>

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
        <div class="intro-text">
            Pilih dashboard untuk membuka paparan berkaitan
        </div>
    </div>

    <main class="dashboard-grid">
        {dashboard_cards_html}
    </main>

    <footer class="portal-footer">
        <div>
            Bahagian Kewangan &amp; Akaun
        </div>

        <div class="footer-right">
            CIDB Malaysia • Portal Dashboard Dalaman
        </div>
    </footer>

</div>
"""

st.markdown(
    portal_html,
    unsafe_allow_html=True
)