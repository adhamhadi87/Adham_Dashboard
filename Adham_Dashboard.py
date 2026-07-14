import streamlit as st
import streamlit.components.v1 as components
from html import escape


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
# STREAMLIT CHROME / PAGE CSS
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
        min-height: 100vh !important;
    }

    .block-container {
        max-width: 1500px !important;
        padding-top: 0.45rem !important;
        padding-bottom: 0 !important;
        padding-left: 1.1rem !important;
        padding-right: 1.1rem !important;
    }

    iframe {
        border: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# BUILD CARD HTML
# =========================================================
def build_card(dashboard: dict) -> str:
    title = escape(dashboard["title"])
    category = escape(dashboard["category"])
    description = escape(dashboard["description"])
    url = escape(dashboard["url"], quote=True)
    icon = escape(dashboard["icon"])
    number = escape(dashboard["number"])
    accent = escape(dashboard["accent"])
    accent_soft = escape(dashboard["accent_soft"])

    return f"""
    <a
        class="dashboard-link"
        href="{url}"
        target="_blank"
        rel="noopener noreferrer"
        aria-label="Buka {title}"
    >
        <div
            class="dashboard-card"
            style="
                --accent:{accent};
                --accent-soft:{accent_soft};
            "
        >
            <div class="card-top">
                <div class="card-icon">{icon}</div>
                <div class="card-number">{number}</div>
            </div>

            <div class="card-category">{category}</div>

            <div class="card-title">{title}</div>

            <div class="card-description">{description}</div>

            <div class="card-footer">
                <div class="open-label">Klik untuk buka dashboard</div>
                <div class="open-arrow">→</div>
            </div>
        </div>
    </a>
    """


cards_html = "\n".join(build_card(item) for item in DASHBOARDS)


# =========================================================
# FULL HTML COMPONENT
# =========================================================
portal_html = f"""
<!DOCTYPE html>
<html lang="ms">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
    * {{
        box-sizing: border-box;
    }}

    html,
    body {{
        margin: 0;
        padding: 0;
        width: 100%;
        min-height: 100%;
        font-family: Arial, Helvetica, sans-serif;
        background: transparent;
        color: #1e293b;
        overflow-x: hidden;
    }}

    body {{
        padding: 8px;
    }}

    .portal-shell {{
        min-height: calc(100vh - 16px);
        display: flex;
        flex-direction: column;
        padding: 14px 18px 9px 18px;
        border-radius: 28px;
        background:
            linear-gradient(
                135deg,
                rgba(255,255,255,0.82),
                rgba(248,250,252,0.64)
            );
        border: 1px solid rgba(255,255,255,0.90);
        box-shadow:
            0 22px 58px rgba(15,23,42,0.10),
            inset 0 1px 0 rgba(255,255,255,0.96);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
    }}

    .portal-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 18px;
        padding: 3px 4px 12px 4px;
    }}

    .brand-wrap {{
        display: flex;
        align-items: center;
        gap: 12px;
        min-width: 0;
    }}

    .brand-icon {{
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
    }}

    .brand-title {{
        margin: 0;
        color: #172033;
        font-size: clamp(21px, 2vw, 29px);
        font-weight: 900;
        letter-spacing: -0.5px;
        line-height: 1.05;
    }}

    .brand-subtitle {{
        margin-top: 4px;
        color: #64748b;
        font-size: 11px;
        font-weight: 600;
    }}

    .dashboard-count {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        flex-shrink: 0;
        padding: 8px 13px;
        border-radius: 999px;
        color: #334155;
        font-size: 11px;
        font-weight: 800;
        background: rgba(255,255,255,0.72);
        border: 1px solid rgba(203,213,225,0.72);
    }}

    .count-dot {{
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #22c55e;
        box-shadow:
            0 0 0 4px rgba(34,197,94,0.12),
            0 0 12px rgba(34,197,94,0.52);
    }}

    .intro-line {{
        display: flex;
        align-items: center;
        gap: 12px;
        margin: 0 3px 11px 3px;
    }}

    .intro-line::before,
    .intro-line::after {{
        content: "";
        flex: 1;
        height: 1px;
        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(148,163,184,0.42),
                transparent
            );
    }}

    .intro-text {{
        color: #64748b;
        font-size: 11px;
        font-weight: 700;
        text-align: center;
        white-space: nowrap;
    }}

    .dashboard-grid {{
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 17px;
        flex: 1;
        align-items: stretch;
    }}

    .dashboard-link {{
        display: block;
        min-width: 0;
        height: 100%;
        text-decoration: none;
        color: inherit;
        outline: none;
    }}

    .dashboard-card {{
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
                rgba(255,255,255,0.93),
                rgba(248,250,252,0.75)
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
    }}

    .dashboard-card::before {{
        content: "";
        position: absolute;
        top: -82px;
        right: -72px;
        width: 180px;
        height: 180px;
        border-radius: 50%;
        background: var(--accent-soft);
        transition: transform 0.25s ease;
    }}

    .dashboard-card::after {{
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
    }}

    .dashboard-link:hover .dashboard-card {{
        transform: translateY(-7px) scale(1.012);
        border-color: var(--accent);
        box-shadow:
            0 26px 52px rgba(15,23,42,0.16),
            0 0 0 3px var(--accent-soft),
            inset 0 1px 0 rgba(255,255,255,0.98);
    }}

    .dashboard-link:hover .dashboard-card::before {{
        transform: scale(1.18);
    }}

    .dashboard-link:focus-visible .dashboard-card {{
        outline: 3px solid var(--accent);
        outline-offset: 4px;
    }}

    .card-top {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 14px;
        position: relative;
        z-index: 2;
    }}

    .card-icon {{
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
    }}

    .card-number {{
        color: rgba(100,116,139,0.30);
        font-size: 32px;
        font-weight: 900;
        line-height: 1;
    }}

    .card-category {{
        width: fit-content;
        margin-top: 18px;
        padding: 6px 10px;
        border-radius: 999px;
        color: var(--accent);
        background: var(--accent-soft);
        font-size: 10px;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        position: relative;
        z-index: 2;
    }}

    .card-title {{
        margin: 13px 0 8px 0;
        color: #1e293b;
        font-size: clamp(18px, 1.45vw, 23px);
        font-weight: 900;
        letter-spacing: -0.3px;
        line-height: 1.14;
        position: relative;
        z-index: 2;
    }}

    .card-description {{
        color: #64748b;
        font-size: 12.5px;
        font-weight: 500;
        line-height: 1.5;
        position: relative;
        z-index: 2;
    }}

    .card-footer {{
        margin-top: auto;
        padding-top: 18px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 10px;
        position: relative;
        z-index: 2;
    }}

    .open-label {{
        color: var(--accent);
        font-size: 11.5px;
        font-weight: 900;
    }}

    .open-arrow {{
        width: 34px;
        height: 34px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        border-radius: 50%;
        color: #ffffff;
        background: var(--accent);
        font-size: 18px;
        font-weight: 900;
        box-shadow: 0 9px 18px var(--accent-soft);
        transition: transform 0.20s ease;
    }}

    .dashboard-link:hover .open-arrow {{
        transform: translateX(4px);
    }}

    .portal-footer {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 15px;
        padding: 11px 3px 0 3px;
        color: #94a3b8;
        font-size: 10px;
        font-weight: 700;
    }}

    @media (max-width: 900px) {{
        .dashboard-grid {{
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }}

        .dashboard-count {{
            display: none;
        }}

        .dashboard-card {{
            min-height: 265px;
        }}
    }}

    @media (max-width: 620px) {{
        body {{
            padding: 4px;
        }}

        .portal-shell {{
            padding: 12px;
            border-radius: 20px;
        }}

        .dashboard-grid {{
            grid-template-columns: 1fr;
        }}

        .portal-header {{
            align-items: flex-start;
        }}

        .brand-title {{
            font-size: 20px;
        }}

        .brand-subtitle {{
            font-size: 10px;
        }}

        .intro-text {{
            white-space: normal;
        }}

        .portal-footer {{
            flex-direction: column;
            gap: 3px;
            text-align: center;
        }}
    }}

    @media (min-width: 901px) and (max-height: 760px) {{
        .portal-shell {{
            padding-top: 10px;
            padding-bottom: 6px;
        }}

        .portal-header {{
            padding-bottom: 8px;
        }}

        .brand-icon {{
            width: 42px;
            height: 42px;
            font-size: 22px;
        }}

        .brand-title {{
            font-size: 23px;
        }}

        .dashboard-card {{
            min-height: 235px;
            padding: 17px;
        }}

        .card-icon {{
            width: 47px;
            height: 47px;
            font-size: 24px;
        }}

        .card-category {{
            margin-top: 12px;
        }}

        .card-title {{
            margin-top: 9px;
            font-size: 18px;
        }}

        .card-description {{
            font-size: 11.5px;
        }}

        .card-footer {{
            padding-top: 11px;
        }}
    }}
</style>
</head>

<body>
    <div class="portal-shell">

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

        <div class="intro-line">
            <div class="intro-text">
                Pilih dashboard untuk membuka paparan berkaitan
            </div>
        </div>

        <div class="dashboard-grid">
            {cards_html}
        </div>

        <div class="portal-footer">
            <div>Bahagian Kewangan &amp; Akaun</div>
            <div>CIDB Malaysia • Portal Dashboard Dalaman</div>
        </div>

    </div>
</body>
</html>
"""


# =========================================================
# RENDER
# Height fixed untuk muat satu skrin monitor biasa.
# scrolling=True sebagai fallback jika skrin lebih rendah.
# =========================================================
components.html(
    portal_html,
    height=690,
    scrolling=True,
)
