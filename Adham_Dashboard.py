import streamlit as st
from textwrap import dedent


# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Portal Dashboard CIDB",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# DASHBOARD CONFIG
# Tambah dashboard baru di sini sahaja.
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
    #MainMenu,
    footer,
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"],
    [data-testid="collapsedControl"],
    section[data-testid="stSidebar"] {
        display: none !important;
    }

    header[data-testid="stHeader"] {
        height: 0 !important;
        min-height: 0 !important;
        background: transparent !important;
    }

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
                rgba(191, 219, 254, 0.50) 0%,
                transparent 30%
            ),
            radial-gradient(
                circle at 92% 12%,
                rgba(221, 214, 254, 0.45) 0%,
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #f8fafc 0%,
                #eef4ff 50%,
                #f8fafc 100%
            ) !important;
        background-attachment: fixed !important;
    }

    .block-container {
        max-width: 1450px !important;
        padding-top: 0.8rem !important;
        padding-bottom: 0.5rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }

    /* Header */
    .portal-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 16px;
        padding: 12px 16px;
        margin-bottom: 12px;
        border-radius: 24px;
        background: rgba(255,255,255,0.68);
        border: 1px solid rgba(255,255,255,0.86);
        box-shadow:
            0 16px 38px rgba(15,23,42,0.09),
            inset 0 1px 0 rgba(255,255,255,0.95);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
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
        flex-shrink: 0;
        border-radius: 15px;
        font-size: 25px;
        background:
            linear-gradient(
                145deg,
                rgba(255,255,255,0.96),
                rgba(219,234,254,0.92)
            );
        box-shadow:
            0 10px 22px rgba(37,99,235,0.14),
            inset 0 1px 0 rgba(255,255,255,0.98);
    }

    .brand-title {
        margin: 0;
        color: #172033;
        font-family: Arial, sans-serif;
        font-size: clamp(22px, 2vw, 29px);
        font-weight: 900;
        letter-spacing: -0.5px;
        line-height: 1.05;
    }

    .brand-subtitle {
        margin-top: 3px;
        color: #64748b;
        font-family: Arial, sans-serif;
        font-size: 11px;
        font-weight: 600;
    }

    .dashboard-count {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 13px;
        border-radius: 999px;
        color: #334155;
        font-family: Arial, sans-serif;
        font-size: 11px;
        font-weight: 800;
        background: rgba(255,255,255,0.72);
        border: 1px solid rgba(203,213,225,0.72);
    }

    .count-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #22c55e;
        box-shadow:
            0 0 0 4px rgba(34,197,94,0.12),
            0 0 12px rgba(34,197,94,0.52);
    }

    .intro-text {
        margin: 0 0 12px 0;
        text-align: center;
        color: #64748b;
        font-family: Arial, sans-serif;
        font-size: 11px;
        font-weight: 700;
    }

    /* Column spacing */
    div[data-testid="stHorizontalBlock"] {
        gap: 1rem !important;
        align-items: stretch !important;
    }

    div[data-testid="column"] {
        display: flex !important;
        flex-direction: column !important;
    }

    div[data-testid="column"] > div {
        height: 100% !important;
    }

    /* Clickable card */
    .dashboard-link {
        display: block;
        height: 100%;
        text-decoration: none !important;
        color: inherit !important;
        outline: none;
    }

    .dashboard-card {
        --accent: #2563eb;
        --accent-soft: rgba(37,99,235,0.14);

        position: relative;
        min-height: 285px;
        height: 100%;
        display: flex;
        flex-direction: column;
        overflow: hidden;
        padding: 21px;
        border-radius: 24px;
        background:
            linear-gradient(
                145deg,
                rgba(255,255,255,0.91),
                rgba(248,250,252,0.73)
            );
        border: 1px solid rgba(203,213,225,0.74);
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
        top: -82px;
        right: -72px;
        width: 180px;
        height: 180px;
        border-radius: 50%;
        background: var(--accent-soft);
        transition:
            transform 0.25s ease,
            opacity 0.25s ease;
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
        opacity: 0.78;
    }

    .dashboard-link:hover .dashboard-card {
        transform: translateY(-7px) scale(1.012);
        border-color: var(--accent);
        box-shadow:
            0 26px 52px rgba(15,23,42,0.16),
            0 0 0 3px var(--accent-soft),
            inset 0 1px 0 rgba(255,255,255,0.98);
    }

    .dashboard-link:hover .dashboard-card::before {
        transform: scale(1.18);
    }

    .dashboard-link:focus-visible .dashboard-card {
        outline: 3px solid var(--accent);
        outline-offset: 4px;
    }

    .card-top {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 14px;
        position: relative;
        z-index: 2;
    }

    .card-icon {
        width: 55px;
        height: 55px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 17px;
        font-size: 29px;
        background:
            linear-gradient(
                145deg,
                rgba(255,255,255,0.95),
                var(--accent-soft)
            );
        border: 1px solid rgba(255,255,255,0.96);
        box-shadow:
            0 11px 24px var(--accent-soft),
            inset 0 1px 0 rgba(255,255,255,0.98);
    }

    .card-number {
        color: rgba(100,116,139,0.30);
        font-family: Arial, sans-serif;
        font-size: 32px;
        font-weight: 900;
        line-height: 1;
    }

    .card-category {
        width: fit-content;
        margin-top: 18px;
        padding: 6px 10px;
        border-radius: 999px;
        color: var(--accent);
        background: var(--accent-soft);
        font-family: Arial, sans-serif;
        font-size: 10px;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        position: relative;
        z-index: 2;
    }

    .card-title {
        margin: 13px 0 8px 0;
        color: #1e293b;
        font-family: Arial, sans-serif;
        font-size: clamp(18px, 1.45vw, 23px);
        font-weight: 900;
        letter-spacing: -0.3px;
        line-height: 1.14;
        position: relative;
        z-index: 2;
    }

    .card-description {
        color: #64748b;
        font-family: Arial, sans-serif;
        font-size: 12.5px;
        font-weight: 500;
        line-height: 1.5;
        position: relative;
        z-index: 2;
    }

    .card-footer {
        margin-top: auto;
        padding-top: 18px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 10px;
        position: relative;
        z-index: 2;
    }

    .open-label {
        color: var(--accent);
        font-family: Arial, sans-serif;
        font-size: 11.5px;
        font-weight: 900;
    }

    .open-arrow {
        width: 34px;
        height: 34px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 50%;
        color: #ffffff;
        background: var(--accent);
        font-family: Arial, sans-serif;
        font-size: 18px;
        font-weight: 900;
        box-shadow: 0 9px 18px var(--accent-soft);
        transition: transform 0.20s ease;
    }

    .dashboard-link:hover .open-arrow {
        transform: translateX(4px);
    }

    .portal-footer-custom {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 15px;
        margin-top: 11px;
        padding: 8px 3px 0 3px;
        color: #94a3b8;
        font-family: Arial, sans-serif;
        font-size: 10px;
        font-weight: 700;
    }

    @media (max-width: 900px) {
        .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }

        .dashboard-card {
            min-height: 265px;
            padding: 18px;
        }

        .dashboard-count {
            display: none;
        }
    }

    @media (max-width: 700px) {
        .portal-header {
            align-items: flex-start;
        }

        .brand-title {
            font-size: 20px;
        }

        .brand-subtitle {
            font-size: 10px;
        }

        .portal-footer-custom {
            flex-direction: column;
            text-align: center;
            gap: 3px;
        }
    }

    @media (min-width: 901px) and (max-height: 760px) {
        .block-container {
            padding-top: 0.4rem !important;
        }

        .portal-header {
            padding-top: 9px;
            padding-bottom: 9px;
        }

        .brand-icon {
            width: 42px;
            height: 42px;
            font-size: 22px;
        }

        .brand-title {
            font-size: 23px;
        }

        .dashboard-card {
            min-height: 235px;
            padding: 17px;
        }

        .card-icon {
            width: 47px;
            height: 47px;
            font-size: 24px;
        }

        .card-category {
            margin-top: 12px;
        }

        .card-title {
            margin-top: 9px;
            font-size: 18px;
        }

        .card-description {
            font-size: 11.5px;
        }

        .card-footer {
            padding-top: 11px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# HELPER
# =========================================================
def build_card_html(dashboard: dict) -> str:
    """Bina satu clickable dashboard card."""
    return dedent(
        f"""
        <a
            class="dashboard-link"
            href="{dashboard['url']}"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="Buka {dashboard['title']}"
        >
            <div
                class="dashboard-card"
                style="
                    --accent: {dashboard['accent']};
                    --accent-soft: {dashboard['accent_soft']};
                "
            >
                <div class="card-top">
                    <div class="card-icon">{dashboard['icon']}</div>
                    <div class="card-number">{dashboard['number']}</div>
                </div>

                <div class="card-category">
                    {dashboard['category']}
                </div>

                <div class="card-title">
                    {dashboard['title']}
                </div>

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
            </div>
        </a>
        """
    ).strip()


# =========================================================
# HEADER
# =========================================================
st.markdown(
    dedent(
        f"""
        <div class="portal-header">
            <div class="brand-wrap">
                <div class="brand-icon">📊</div>

                <div>
                    <div class="brand-title">
                        PORTAL DASHBOARD CIDB
                    </div>

                    <div class="brand-subtitle">
                        Pusat Akses Dashboard Bahagian Kewangan &amp; Akaun
                    </div>
                </div>
            </div>

            <div class="dashboard-count">
                <span class="count-dot"></span>
                {len(DASHBOARDS)} Dashboard Aktif
            </div>
        </div>
        """
    ).strip(),
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="intro-text">Pilih dashboard untuk membuka paparan berkaitan</div>',
    unsafe_allow_html=True,
)


# =========================================================
# DASHBOARD CARDS
# =========================================================
columns = st.columns(len(DASHBOARDS), gap="large")

for column, dashboard in zip(columns, DASHBOARDS):
    with column:
        st.markdown(
            build_card_html(dashboard),
            unsafe_allow_html=True,
        )


# =========================================================
# FOOTER
# =========================================================
st.markdown(
    dedent(
        """
        <div class="portal-footer-custom">
            <div>Bahagian Kewangan &amp; Akaun</div>
            <div>CIDB Malaysia • Portal Dashboard Dalaman</div>
        </div>
        """
    ).strip(),
    unsafe_allow_html=True,
)