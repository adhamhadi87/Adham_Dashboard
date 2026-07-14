import streamlit as st
import streamlit.components.v1 as components
from html import escape


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
        "description": "Pemantauan pencapaian fizikal program dan status traffic light.",
        "url": "https://prestasiprogram.streamlit.app/",
        "accent": "#16a34a",
        "accent_soft": "rgba(34,197,94,0.14)",
        "number": "01",
    },
    {
        "title": "Dashboard JPKA",
        "category": "Kewangan & Akaun",
        "icon": "💰",
        "description": "Prestasi perbelanjaan, hasil, geran, P&L dan kedudukan kewangan.",
        "url": "https://jpka-cidb520.streamlit.app/",
        "accent": "#2563eb",
        "accent_soft": "rgba(37,99,235,0.14)",
        "number": "02",
    },
    {
        "title": "e-Filing Baucar CIDB",
        "category": "Pengurusan Dokumen",
        "icon": "📁",
        "description": "Carian, semakan dan pengurusan rekod e-Filing baucar CIDB.",
        "url": "https://e-filing-baucar-cidb.streamlit.app/",
        "accent": "#7c3aed",
        "accent_soft": "rgba(124,58,237,0.14)",
        "number": "03",
    },
]


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
        min-height: 100vh !important;
        background:
            radial-gradient(circle at 8% 10%, rgba(191,219,254,0.48), transparent 30%),
            radial-gradient(circle at 92% 12%, rgba(221,214,254,0.42), transparent 30%),
            linear-gradient(135deg, #f8fafc 0%, #eef4ff 50%, #f8fafc 100%) !important;
    }

    .block-container {
        max-width: 1600px !important;
        padding: 0.35rem 0.75rem 0 !important;
    }

    iframe {
        border: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


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
    <a class="dashboard-link"
       href="{url}"
       target="_blank"
       rel="noopener noreferrer"
       aria-label="Buka {title}">
        <div class="dashboard-card"
             style="--accent:{accent}; --accent-soft:{accent_soft};">

            <div class="card-top">
                <div class="card-icon">{icon}</div>
                <div class="card-number">{number}</div>
            </div>

            <div class="card-category">{category}</div>
            <div class="card-title">{title}</div>
            <div class="card-description">{description}</div>

            <div class="card-footer">
                <span class="open-label">Buka dashboard</span>
                <span class="open-arrow">→</span>
            </div>
        </div>
    </a>
    """


cards_html = "\n".join(build_card(item) for item in DASHBOARDS)


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

html, body {{
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
    padding: 6px;
}}

.portal-shell {{
    min-height: calc(100vh - 12px);
    display: flex;
    flex-direction: column;
    padding: 11px 14px 7px;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(255,255,255,0.82), rgba(248,250,252,0.64));
    border: 1px solid rgba(255,255,255,0.90);
    box-shadow:
        0 18px 48px rgba(15,23,42,0.09),
        inset 0 1px 0 rgba(255,255,255,0.96);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
}}

.portal-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 14px;
    padding: 2px 3px 9px;
}}

.brand-wrap {{
    display: flex;
    align-items: center;
    gap: 10px;
    min-width: 0;
}}

.brand-icon {{
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    border-radius: 13px;
    font-size: 21px;
    background: linear-gradient(145deg, rgba(255,255,255,0.96), rgba(219,234,254,0.92));
    box-shadow:
        0 8px 18px rgba(37,99,235,0.13),
        inset 0 1px 0 rgba(255,255,255,0.98);
}}

.brand-title {{
    color: #172033;
    font-size: clamp(19px, 1.7vw, 25px);
    font-weight: 900;
    letter-spacing: -0.4px;
    line-height: 1.05;
}}

.brand-subtitle {{
    margin-top: 3px;
    color: #64748b;
    font-size: 10px;
    font-weight: 600;
}}

.dashboard-count {{
    display: inline-flex;
    align-items: center;
    gap: 7px;
    flex-shrink: 0;
    padding: 7px 11px;
    border-radius: 999px;
    color: #334155;
    font-size: 10px;
    font-weight: 800;
    background: rgba(255,255,255,0.72);
    border: 1px solid rgba(203,213,225,0.72);
}}

.count-dot {{
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #22c55e;
    box-shadow: 0 0 0 3px rgba(34,197,94,0.12);
}}

.intro-line {{
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 0 2px 9px;
}}

.intro-line::before,
.intro-line::after {{
    content: "";
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(148,163,184,0.38), transparent);
}}

.intro-text {{
    color: #64748b;
    font-size: 10px;
    font-weight: 700;
    text-align: center;
    white-space: nowrap;
}}

/* Auto-fit: dashboard baru akan turun ke baris seterusnya secara automatik */
.dashboard-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 13px;
    align-items: stretch;
    flex: 1;
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
    min-height: 195px;
    height: 100%;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    padding: 15px;
    border-radius: 19px;
    background: linear-gradient(145deg, rgba(255,255,255,0.93), rgba(248,250,252,0.75));
    border: 1px solid rgba(203,213,225,0.76);
    box-shadow:
        0 11px 25px rgba(15,23,42,0.09),
        inset 0 1px 0 rgba(255,255,255,0.98);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    cursor: pointer;
    transition: transform 0.20s ease, box-shadow 0.20s ease, border-color 0.20s ease;
}}

.dashboard-card::before {{
    content: "";
    position: absolute;
    top: -65px;
    right: -58px;
    width: 140px;
    height: 140px;
    border-radius: 50%;
    background: var(--accent-soft);
    transition: transform 0.22s ease;
}}

.dashboard-card::after {{
    content: "";
    position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, transparent, var(--accent), transparent);
    opacity: 0.78;
}}

.dashboard-link:hover .dashboard-card {{
    transform: translateY(-5px) scale(1.008);
    border-color: var(--accent);
    box-shadow:
        0 20px 38px rgba(15,23,42,0.14),
        0 0 0 2px var(--accent-soft),
        inset 0 1px 0 rgba(255,255,255,0.98);
}}

.dashboard-link:hover .dashboard-card::before {{
    transform: scale(1.14);
}}

.card-top {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 10px;
    position: relative;
    z-index: 2;
}}

.card-icon {{
    width: 42px;
    height: 42px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    border-radius: 13px;
    font-size: 22px;
    background: linear-gradient(145deg, rgba(255,255,255,0.95), var(--accent-soft));
    border: 1px solid rgba(255,255,255,0.96);
    box-shadow:
        0 8px 17px var(--accent-soft),
        inset 0 1px 0 rgba(255,255,255,0.98);
}}

.card-number {{
    color: rgba(100,116,139,0.28);
    font-size: 25px;
    font-weight: 900;
    line-height: 1;
}}

.card-category {{
    width: fit-content;
    margin-top: 11px;
    padding: 4px 8px;
    border-radius: 999px;
    color: var(--accent);
    background: var(--accent-soft);
    font-size: 8.5px;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 0.45px;
    position: relative;
    z-index: 2;
}}

.card-title {{
    margin: 9px 0 5px;
    color: #1e293b;
    font-size: 17px;
    font-weight: 900;
    letter-spacing: -0.25px;
    line-height: 1.12;
    position: relative;
    z-index: 2;
}}

.card-description {{
    color: #64748b;
    font-size: 10.5px;
    font-weight: 500;
    line-height: 1.42;
    position: relative;
    z-index: 2;
}}

.card-footer {{
    margin-top: auto;
    padding-top: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 8px;
    position: relative;
    z-index: 2;
}}

.open-label {{
    color: var(--accent);
    font-size: 9.5px;
    font-weight: 900;
}}

.open-arrow {{
    width: 27px;
    height: 27px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    border-radius: 50%;
    color: #ffffff;
    background: var(--accent);
    font-size: 14px;
    font-weight: 900;
    box-shadow: 0 6px 13px var(--accent-soft);
    transition: transform 0.18s ease;
}}

.dashboard-link:hover .open-arrow {{
    transform: translateX(3px);
}}

.portal-footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    padding: 8px 2px 0;
    color: #94a3b8;
    font-size: 9px;
    font-weight: 700;
}}

@media (min-width: 1450px) {{
    .dashboard-grid {{
        grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    }}
}}

@media (max-width: 900px) {{
    .dashboard-grid {{
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    }}

    .dashboard-count {{
        display: none;
    }}
}}

@media (max-width: 560px) {{
    body {{
        padding: 3px;
    }}

    .portal-shell {{
        padding: 10px;
        border-radius: 18px;
    }}

    .dashboard-grid {{
        grid-template-columns: 1fr;
    }}

    .dashboard-card {{
        min-height: 180px;
    }}

    .brand-title {{
        font-size: 18px;
    }}

    .brand-subtitle {{
        font-size: 9px;
    }}

    .intro-text {{
        white-space: normal;
    }}

    .portal-footer {{
        flex-direction: column;
        gap: 2px;
        text-align: center;
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
                <div class="brand-title">PORTAL DASHBOARD CIDB</div>
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


components.html(
    portal_html,
    height=720,
    scrolling=True,
)
