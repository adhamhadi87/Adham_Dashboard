import streamlit as st

st.set_page_config(
    page_title="Portal Dashboard CIDB",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# CSS
# =====================================================
st.markdown(
    """
    <style>
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(191, 219, 254, 0.40),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 15%,
                rgba(233, 213, 255, 0.40),
                transparent 28%
            ),
            linear-gradient(
                135deg,
                #f8fafc 0%,
                #eef2ff 50%,
                #f8fafc 100%
            );
    }

    .hero {
        padding: 32px 28px;
        margin-bottom: 28px;
        border-radius: 28px;
        text-align: center;
        background: rgba(255, 255, 255, 0.70);
        border: 1px solid rgba(255, 255, 255, 0.90);
        box-shadow: 0 20px 50px rgba(15, 23, 42, 0.10);
        backdrop-filter: blur(16px);
    }

    .hero-icon {
        font-size: 45px;
        margin-bottom: 8px;
    }

    .hero-title {
        margin: 0;
        color: #1e293b;
        font-size: 34px;
        font-weight: 900;
    }

    .hero-subtitle {
        margin-top: 8px;
        color: #64748b;
        font-size: 15px;
    }

    .dashboard-card {
        min-height: 255px;
        padding: 25px;
        border-radius: 24px;
        background: rgba(255, 255, 255, 0.80);
        border: 1px solid rgba(203, 213, 225, 0.75);
        box-shadow:
            0 16px 38px rgba(15, 23, 42, 0.10),
            inset 0 1px 0 rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(14px);
        transition: all 0.20s ease;
        margin-bottom: 12px;
    }

    .dashboard-card:hover {
        transform: translateY(-5px);
        box-shadow:
            0 24px 48px rgba(15, 23, 42, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.95);
    }

    .dashboard-badge {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 999px;
        margin-bottom: 16px;
        background: #eef2ff;
        color: #4338ca;
        font-size: 12px;
        font-weight: 800;
    }

    .dashboard-icon {
        font-size: 42px;
        margin-bottom: 12px;
    }

    .dashboard-title {
        margin: 0 0 12px 0;
        color: #1e293b;
        font-size: 22px;
        font-weight: 900;
    }

    .dashboard-description {
        color: #64748b;
        font-size: 14px;
        line-height: 1.65;
        min-height: 70px;
    }

    div[data-testid="stLinkButton"] a {
        width: 100%;
        border-radius: 999px;
        padding: 0.65rem 1rem;
        background: linear-gradient(
            135deg,
            #2563eb,
            #4f46e5
        );
        border: none;
        color: white;
        font-weight: 800;
        box-shadow: 0 10px 22px rgba(37, 99, 235, 0.25);
    }

    div[data-testid="stLinkButton"] a:hover {
        transform: translateY(-1px);
        box-shadow: 0 14px 26px rgba(37, 99, 235, 0.35);
    }

    .footer-text {
        text-align: center;
        color: #94a3b8;
        font-size: 12px;
        margin-top: 35px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# HERO
# =====================================================
st.markdown(
    """
    <div class="hero">
        <div class="hero-icon">📊</div>
        <h1 class="hero-title">PORTAL DASHBOARD CIDB</h1>
        <div class="hero-subtitle">
            Pusat akses dashboard prestasi, kewangan dan e-Filing baucar
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =====================================================
# DASHBOARD CARDS
# =====================================================
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown(
        """
        <div class="dashboard-card">
            <div class="dashboard-badge">Prestasi Program</div>
            <div class="dashboard-icon">🚦</div>
            <h2 class="dashboard-title">Prestasi Program</h2>
            <div class="dashboard-description">
                Pemantauan pencapaian fizikal program mengikut sektor,
                bahagian dan status traffic light.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "Buka Dashboard Prestasi",
        "https://prestasiprogram.streamlit.app/",
        icon="🚀",
        use_container_width=True
    )

with col2:
    st.markdown(
        """
        <div class="dashboard-card">
            <div class="dashboard-badge">Kewangan & Akaun</div>
            <div class="dashboard-icon">💰</div>
            <h2 class="dashboard-title">Dashboard JPKA</h2>
            <div class="dashboard-description">
                Prestasi perbelanjaan, hasil, geran, P&L,
                Balance Sheet dan Cash Flow CIDB.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "Buka Dashboard JPKA",
        "https://jpka-cidb520.streamlit.app/",
        icon="🚀",
        use_container_width=True
    )

with col3:
    st.markdown(
        """
        <div class="dashboard-card">
            <div class="dashboard-badge">e-Filing</div>
            <div class="dashboard-icon">📁</div>
            <h2 class="dashboard-title">e-Filing Baucar CIDB</h2>
            <div class="dashboard-description">
                Carian, semakan dan pengurusan rekod
                e-Filing baucar CIDB secara dalam talian.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "Buka e-Filing Baucar",
        "https://e-filing-baucar-cidb.streamlit.app/",
        icon="🚀",
        use_container_width=True
    )

st.markdown(
    """
    <div class="footer-text">
        Bahagian Kewangan & Akaun • CIDB Malaysia
    </div>
    """,
    unsafe_allow_html=True
)