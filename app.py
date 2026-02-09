#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Flynn 50/50 Matrix Dashboard
─────────────────────────────
C-Level Gegenüberstellung: Extraktiver Kapitalismus vs. Regenerative Ökonomie
Basierend auf dem Flynn Handbook — Mathematisch vollständige 50/50 Framework-Klasse.

Autor:  Societal Business Think Tank
Stack:  Streamlit · yfinance · Plotly
"""

import math
import numpy as np
import pandas as pd

def _sf(v, default=0.0):
    """Safe float: NaN / None / empty → default."""
    try:
        f = float(v if v is not None else default)
        return default if math.isnan(f) else f
    except (TypeError, ValueError):
        return default
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from translations import T, LANGUAGES

# ─── Translation helper ──────────────────────────────────────────────────────
def t(key: str, **kwargs) -> str:
    """Return translated string for the current session language.
    Supports {placeholder} substitution via **kwargs."""
    lang = st.session_state.get("lang", "en")
    entry = T.get(key, {})
    text = entry.get(lang, entry.get("en", f"[{key}]"))
    if kwargs:
        try:
            text = text.format(**kwargs)
        except (KeyError, IndexError):
            pass
    return text

# ─── yfinance mit Graceful-Fallback ──────────────────────────────────────────
try:
    import yfinance as yf
    YF_AVAILABLE = True
except ImportError:
    YF_AVAILABLE = False

# ═══════════════════════════════════════════════════════════════════════════════
#  PAGE CONFIG & THEME
# ═══════════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Flynn 50/50 Matrix Dashboard",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS (dark pro look) ─────────────────────────────────────────────
st.markdown("""
<style>
    /* ── Global ── */
    .stApp {
        background: linear-gradient(160deg, #0a0e17 0%, #101829 50%, #0d1522 100%);
        color: #c9d6e3;
    }
    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background: #0c1220 !important;
        border-right: 1px solid #1a2744;
    }
    section[data-testid="stSidebar"] .stMarkdown h1,
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3 {
        color: #7eb8ff;
    }
    /* ── Metric cards ── */
    div[data-testid="stMetric"] {
        background: rgba(14,26,50,0.6);
        border: 1px solid #1a2744;
        border-radius: 12px;
        padding: 16px 20px;
    }
    div[data-testid="stMetric"] label {
        color: #6b8ab5 !important;
        font-size: 0.82rem !important;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }
    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #e0ecff !important;
        font-weight: 700;
    }
    /* ── Headings ── */
    h1 { color: #a0c4ff !important; }
    h2 { color: #7eb8ff !important; }
    h3 { color: #5fa8ff !important; }
    /* ── Slider labels ── */
    .stSlider label { color: #8fadc9 !important; }
    /* ── Dividers ── */
    hr { border-color: #1a2744 !important; }
    /* ── Info/status boxes ── */
    .dashboard-badge {
        display: inline-block;
        background: linear-gradient(135deg, #162a50, #1a3a6e);
        border: 1px solid #2a5090;
        border-radius: 8px;
        padding: 6px 14px;
        font-size: 0.78rem;
        color: #7eb8ff;
        margin-bottom: 10px;
    }
    .kpi-row {
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
        margin: 10px 0 20px 0;
    }
    .kpi-card {
        flex: 1;
        min-width: 160px;
        background: rgba(14,26,50,0.55);
        border: 1px solid #1a2744;
        border-radius: 12px;
        padding: 18px 20px;
        text-align: center;
    }
    .kpi-card .kpi-label {
        font-size: 0.72rem;
        color: #5a7ea3;
        text-transform: uppercase;
        letter-spacing: 0.07em;
        margin-bottom: 4px;
    }
    .kpi-card .kpi-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: #e0ecff;
    }
    .kpi-card .kpi-sub {
        font-size: 0.72rem;
        color: #446a8f;
        margin-top: 2px;
    }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
#  DATA LAYER — yfinance (Historische Kurse + Income Statements)
#  Die 5 groessten boersennotierten Asset Manager nach AUM
# ═══════════════════════════════════════════════════════════════════════════════

TICKERS = ["BLK", "STT", "IVZ", "BEN", "TROW"]
NAMES = {
    "BLK":  "BlackRock Inc.",
    "STT":  "State Street Corp.",
    "IVZ":  "Invesco Ltd.",
    "BEN":  "Franklin Templeton",
    "TROW": "T. Rowe Price",
}
# One colour per ticker (consistent across all charts)
TICKER_COLORS = {
    "BLK":  "#6ea8fe",   # blue
    "STT":  "#fbbf24",   # gold
    "IVZ":  "#c084fc",   # purple
    "BEN":  "#f472b6",   # pink
    "TROW": "#34d399",   # teal
}

# ══════════════════════════════════════════════════════════════════
#  COMPREHENSIVE EXTERNALITY MODEL
#  Costs based on REVENUE (entire business activity), NOT just NI!
#  These are the REAL costs that the extractive system hides.
# ══════════════════════════════════════════════════════════════════
EXT_CATEGORIES = {
    # ── EHI-driven (Ecological) ──
    "Klima & CO2":            {"rate": 0.12, "index": "ehi", "color": "#ff6b6b", "icon": "\U0001F321"},
    "Biodiversitaetsverlust": {"rate": 0.06, "index": "ehi", "color": "#cc4444", "icon": "\U0001F33F"},
    "Wasser & Boden":         {"rate": 0.04, "index": "ehi", "color": "#aa3333", "icon": "\U0001F4A7"},
    # ── HRI-driven (Social) ──
    "Gesundheitsschaeden":    {"rate": 0.06, "index": "hri", "color": "#ff8c42", "icon": "\U0001F3E5"},
    "Soziale Ungleichheit":   {"rate": 0.08, "index": "hri", "color": "#e07020", "icon": "\u2696"},
    "Arbeitnehmerausbeutung": {"rate": 0.04, "index": "hri", "color": "#c06010", "icon": "\u26D3"},
    # ── IRI-driven (Institutional) ──
    "Systemisches Risiko":    {"rate": 0.07, "index": "iri", "color": "#fbbf24", "icon": "\U0001F4A3"},
    "Regulat. Erfassung":     {"rate": 0.03, "index": "iri", "color": "#d4a017", "icon": "\U0001F3DB"},
}
EXT_CAT_NAMES = list(EXT_CATEGORIES.keys())
# Total max rate at full degradation (all indices=0): sum of all rates = 0.50 of Revenue

# ═══════════════════════════════════════════════════════════════════════════════
#  30-YEAR RETROPOLATION: Estimated combined Revenue for Big 5 Asset Managers
#  The extractive system didn't start in 2021 — it has been running for DECADES.
#  Source: Industry AUM & Revenue data (World Bank, McKinsey, annual reports)
# ═══════════════════════════════════════════════════════════════════════════════
_RETRO_COMBINED_REVENUE = {
    # ── Mid-90s: asset management industry was ~$20T AUM globally ──
    1996: 18.0e9, 1997: 20.5e9, 1998: 22.0e9, 1999: 26.0e9, 2000: 28.0e9,
    # ── Dot-com bust, then recovery ──
    2001: 24.0e9, 2002: 22.0e9, 2003: 25.0e9, 2004: 29.0e9, 2005: 33.0e9,
    # ── Boom before GFC ──
    2006: 38.0e9, 2007: 42.0e9,
    # ── Global Financial Crisis — the system's cancer exposed ──
    2008: 30.0e9, 2009: 32.0e9,
    # ── QE-fueled recovery: AUM exploded ──
    2010: 37.0e9, 2011: 39.0e9, 2012: 42.0e9, 2013: 47.0e9, 2014: 50.0e9,
    # ── Bull market: asset managers print money ──
    2015: 52.0e9, 2016: 53.0e9, 2017: 57.0e9, 2018: 55.0e9,
    # ── Pre-COVID peak + COVID ──
    2019: 60.0e9, 2020: 58.0e9,
}
RETRO_START = min(_RETRO_COMBINED_REVENUE.keys())  # 1996


@st.cache_data(ttl=3600, show_spinner=False)
def fetch_annual_history() -> pd.DataFrame:
    """
    Pull REAL annual data for all TICKERS: stock price + net income + revenue.
    Returns a DataFrame indexed by year with columns per ticker.
    """
    rows: dict[int, dict] = {}

    for tick in TICKERS:
        t = yf.Ticker(tick)

        # ── Stock price history (annual close) ──
        try:
            hist = t.history(period="6y", interval="3mo")
            if hist is not None and not hist.empty:
                hist.index = (
                    hist.index.tz_localize(None)
                    if hist.index.tz is None
                    else hist.index.tz_convert(None)
                )
                annual = hist.groupby(hist.index.year)["Close"].last()
                for yr, price in annual.items():
                    rows.setdefault(yr, {})[f"{tick}_price"] = float(price)
        except Exception:
            pass

        # ── Income statement (annual net income + revenue) ──
        try:
            inc = t.income_stmt
            if inc is not None and not inc.empty:
                if "Net Income" in inc.index:
                    for col_ts, val in inc.loc["Net Income"].items():
                        rows.setdefault(col_ts.year, {})[f"{tick}_netincome"] = float(val)
                if "Total Revenue" in inc.index:
                    for col_ts, val in inc.loc["Total Revenue"].items():
                        rows.setdefault(col_ts.year, {})[f"{tick}_revenue"] = float(val)
        except Exception:
            pass

    df = pd.DataFrame.from_dict(rows, orient="index").sort_index()
    df.index.name = "Jahr"

    # Fill forward gaps
    for tick in TICKERS:
        for sfx in ("_price", "_netincome", "_revenue"):
            col = f"{tick}{sfx}"
            if col in df.columns:
                df[col] = df[col].ffill()

    # Combined columns
    ni_cols  = [f"{t}_netincome" for t in TICKERS if f"{t}_netincome" in df.columns]
    rev_cols = [f"{t}_revenue"   for t in TICKERS if f"{t}_revenue"   in df.columns]
    df["Combined_NI"]      = df[ni_cols].sum(axis=1)  if ni_cols  else 0
    df["Combined_Revenue"]  = df[rev_cols].sum(axis=1) if rev_cols else 0

    return df


# ── Fallback if yfinance completely fails ──
_fb = {
    "BLK":  {2021: (727, 5.90e9, 19.37e9), 2022: (565, 5.18e9, 17.87e9), 2023: (736, 5.50e9, 17.86e9), 2024: (1049, 6.37e9, 20.41e9), 2025: (1056, 6.80e9, 21.50e9)},
    "STT":  {2021: (93, 2.07e9, 11.96e9),  2022: (78, 2.77e9, 12.35e9),  2023: (77, 1.95e9, 11.95e9),  2024: (98, 2.18e9, 12.63e9),  2025: (132, 2.35e9, 13.10e9)},
    "IVZ":  {2021: (24, 1.39e9, 6.89e9),   2022: (18, 0.54e9, 6.05e9),   2023: (17, 0.52e9, 5.73e9),   2024: (18, 0.58e9, 6.02e9),   2025: (19, 0.62e9, 6.20e9)},
    "BEN":  {2021: (32, 1.83e9, 8.43e9),   2022: (25, 1.30e9, 8.28e9),   2023: (25, 0.87e9, 7.85e9),   2024: (22, 0.95e9, 8.10e9),   2025: (21, 1.00e9, 8.30e9)},
    "TROW": {2021: (198, 3.08e9, 7.67e9),  2022: (110, 1.55e9, 6.49e9),  2023: (109, 1.65e9, 6.46e9),  2024: (118, 1.90e9, 7.08e9),  2025: (115, 2.00e9, 7.30e9)},
}
FALLBACK_DATA: dict[int, dict] = {}
for _tick, _years in _fb.items():
    for _yr, (_p, _ni, _rev) in _years.items():
        FALLBACK_DATA.setdefault(_yr, {})
        FALLBACK_DATA[_yr][f"{_tick}_price"]     = _p
        FALLBACK_DATA[_yr][f"{_tick}_netincome"] = _ni
        FALLBACK_DATA[_yr][f"{_tick}_revenue"]   = _rev


@st.cache_data(ttl=3600, show_spinner=False)
def get_historical_data() -> pd.DataFrame:
    """Get real historical data, fall back to hardcoded if yfinance fails."""
    if YF_AVAILABLE:
        try:
            df = fetch_annual_history()
            if df is not None and not df.empty and len(df) >= 3:
                return df
        except Exception:
            pass

    # Fallback
    df = pd.DataFrame.from_dict(FALLBACK_DATA, orient="index").sort_index()
    df.index.name = "Jahr"
    ni_cols  = [f"{t}_netincome" for t in TICKERS if f"{t}_netincome" in df.columns]
    rev_cols = [f"{t}_revenue"   for t in TICKERS if f"{t}_revenue"   in df.columns]
    df["Combined_NI"]     = df[ni_cols].sum(axis=1)
    df["Combined_Revenue"] = df[rev_cols].sum(axis=1)
    return df


def _available_tickers(df: pd.DataFrame) -> list[str]:
    """Return the subset of TICKERS that actually have data."""
    return [t for t in TICKERS if f"{t}_price" in df.columns]


# ═══════════════════════════════════════════════════════════════════════════════
#  MATHEMATICAL ENGINE — Dual-Path Simulation
#  Historical years: real data  |  Future years: projected + Flynn model
# ═══════════════════════════════════════════════════════════════════════════════

def run_full_simulation(
    hist_df: pd.DataFrame,
    proj_years: int,
    growth_rate: float,
    gamma: float,
    dr_0: float,
    beta: float,
    ehi_0: float,
    hri_0: float,
    iri_0: float,
    q_b_share: float,
    ext_degrad: float,
) -> pd.DataFrame:
    """
    Build a complete timeline:
    - PAST (historical): Real stock prices, net income, revenue
    - FUTURE (projected): Extractive path (degradation) vs Flynn path (regeneration)
    """
    records = []
    hist_years = sorted(hist_df.index.tolist())
    current_year = hist_years[-1] if hist_years else 2025
    first_real_year = hist_years[0] if hist_years else 2021
    last_ni = _sf(hist_df.loc[current_year, "Combined_NI"], 12e9) if current_year in hist_df.index else 12e9
    avail = _available_tickers(hist_df)

    # ── Per-ticker NI shares for projection distribution ──
    ni_shares: dict[str, float] = {}
    total_last = 0
    for tk in avail:
        v = _sf(hist_df.loc[current_year].get(f"{tk}_netincome", 0))
        ni_shares[tk] = v
        total_last += v
    for tk in avail:
        ni_shares[tk] = ni_shares[tk] / total_last if total_last else 1.0 / len(avail)

    # ═══════════════════════════════════════════════
    #  PHASE 0: Retropolation (1996 – year before real data)
    #  No real stock data, but ESTIMATED Revenue to calculate
    #  the externality debt that was ALREADY accumulating.
    #  The cancer didn't start in 2021 — it started DECADES ago.
    # ═══════════════════════════════════════════════
    cum_ext_cost = 0.0
    cum_flynn_created = 0.0

    retro_years = sorted([y for y in _RETRO_COMBINED_REVENUE if y < first_real_year])
    for yr in retro_years:
        retro_rev = _RETRO_COMBINED_REVENUE[yr]
        rec: dict = {"Jahr": yr, "Phase": "Retropolation"}

        # Per-ticker: distribute revenue proportionally (estimate)
        for tk in TICKERS:
            rec[f"{tk} Kurs"] = 0
            rec[f"{tk} Net Income"] = 0
            rec[f"{tk} Revenue"] = retro_rev / len(TICKERS)

        # Externalities from estimated revenue
        # Indices were WORSE in the past (less ESG, less regulation)
        years_ago = current_year - yr
        retro_ehi = max(0.10, ehi_0 - 0.005 * years_ago)  # worse the further back
        retro_hri = max(0.15, hri_0 - 0.004 * years_ago)
        retro_iri = max(0.20, iri_0 - 0.003 * years_ago)
        idx_map_retro = {"ehi": retro_ehi, "hri": retro_hri, "iri": retro_iri}

        retro_ext_cost = 0.0
        for cat_name, cat_cfg in EXT_CATEGORIES.items():
            cat_cost = cat_cfg["rate"] * retro_rev * (1 - idx_map_retro[cat_cfg["index"]])
            rec[f"Ext. {cat_name}"] = cat_cost
            retro_ext_cost += cat_cost

        cum_ext_cost += retro_ext_cost
        retro_ni_est = retro_rev * 0.15  # rough NI/Rev ratio

        rec.update({
            "Surplus (S)": retro_ni_est, "Revenue": retro_rev,
            "Ext. Marktwert": retro_ni_est, "Ext. Externalities": retro_ext_cost,
            "Ext. True Value": retro_ni_est - retro_ext_cost,
            "Ext. Kum. Externalities": cum_ext_cost,
            "Ext. Kum. Wertvernichtung": -cum_ext_cost,
            "Ext. EHI": retro_ehi, "Ext. HRI": retro_hri, "Ext. IRI": retro_iri,
            "Flynn Retained": 0, "Matrix-Kapital (Q)": 0,
            "Flynn Matrix Value": 0,
            "Flynn Kum. Wertschoepfung": 0,
            "Flynn EHI": retro_ehi, "Flynn HRI": retro_hri, "Flynn IRI": retro_iri,
            "MW_Total": 0, "Matrix-Metamorphose": 0,
            "Dialyse-Durchsatz": 0, "Dialyse-Rate (DR)": 0,
            "Alpha": 1, "Delta (abs)": 0, "Delta (%)": 0,
            "Kum. Schere (abs)": -cum_ext_cost,
            "Flynn Ext. Kosten": retro_ext_cost,
            "Flynn Jahres-Aufbau": 0,
            "Netto-Systemsaldo": -cum_ext_cost,
        })
        records.append(rec)

    # ═══════════════════════════════════════════════
    #  PHASE 1: Historical years (REAL data)
    #  Externalities were ALREADY accumulating!
    #  cum_ext_cost carries the 30-year retropolated debt!
    #  Flynn did NOT exist yet → no value creation
    # ═══════════════════════════════════════════════
    # cum_ext_cost already seeded from Phase 0 retropolation!

    for yr in hist_years:
        row = hist_df.loc[yr]
        rec: dict = {"Jahr": yr, "Phase": "Historisch"}

        comb_ni = 0.0
        comb_rev = 0.0
        for tk in TICKERS:
            p  = _sf(row.get(f"{tk}_price", 0))
            ni = _sf(row.get(f"{tk}_netincome", 0))
            rv = _sf(row.get(f"{tk}_revenue", 0))
            rec[f"{tk} Kurs"]       = p
            rec[f"{tk} Net Income"]  = ni
            rec[f"{tk} Revenue"]     = rv
            comb_ni  += ni
            comb_rev += rv

        # ── Historical externalities from REAL Revenue ──
        # The cancer was ALREADY growing before Flynn existed
        idx_map_hist = {"ehi": ehi_0, "hri": hri_0, "iri": iri_0}
        hist_ext_cost = 0.0
        for cat_name, cat_cfg in EXT_CATEGORIES.items():
            cat_cost = cat_cfg["rate"] * comb_rev * (1 - idx_map_hist[cat_cfg["index"]])
            rec[f"Ext. {cat_name}"] = cat_cost
            hist_ext_cost += cat_cost

        # ACCUMULATE — even in the past!
        cum_ext_cost += hist_ext_cost

        rec.update({
            "Surplus (S)": comb_ni, "Revenue": comb_rev,
            "Ext. Marktwert": comb_ni, "Ext. Externalities": hist_ext_cost,
            "Ext. True Value": comb_ni - hist_ext_cost,
            "Ext. Kum. Externalities": cum_ext_cost,
            "Ext. Kum. Wertvernichtung": -cum_ext_cost,
            "Ext. EHI": ehi_0, "Ext. HRI": hri_0, "Ext. IRI": iri_0,
            "Flynn Retained": comb_ni * 0.5, "Matrix-Kapital (Q)": comb_ni * 0.5,
            "Flynn Matrix Value": comb_ni,      # no Flynn uplift yet
            "Flynn Kum. Wertschoepfung": 0,      # Flynn didn't exist
            "Flynn EHI": ehi_0, "Flynn HRI": hri_0, "Flynn IRI": iri_0,
            "MW_Total": 0, "Matrix-Metamorphose": 0,
            "Dialyse-Durchsatz": 0, "Dialyse-Rate (DR)": 0,
            "Alpha": 1, "Delta (abs)": 0, "Delta (%)": 0,
            "Kum. Schere (abs)": -cum_ext_cost,   # only debt, no Flynn yet
            "Flynn Ext. Kosten": hist_ext_cost,
            "Flynn Jahres-Aufbau": 0,
            "Netto-Systemsaldo": -cum_ext_cost,
        })
        records.append(rec)

    # ═══════════════════════════════════════════════
    #  PHASE 2: Projected future years
    #  cum_ext_cost ALREADY carries the historical debt!
    #  Flynn starts NOW — but the damage is already done.
    # ═══════════════════════════════════════════════
    f_ehi, f_hri, f_iri = ehi_0, hri_0, iri_0
    e_ehi, e_hri, e_iri = ehi_0, hri_0, iri_0
    # cum_ext_cost already seeded from historical years!
    # cum_flynn_created starts at 0 — Flynn begins now

    for i in range(1, proj_years + 1):
        yr = current_year + i
        S = last_ni * ((1 + growth_rate) ** i)
        rec: dict = {"Jahr": yr, "Phase": "Projektion"}

        # Per-ticker projected prices & NI
        for tk in TICKERS:
            base_p = float(hist_df.loc[current_year].get(f"{tk}_price", 50) or 50)
            rec[f"{tk} Kurs"]      = base_p * ((1 + growth_rate * 0.6) ** i)
            rec[f"{tk} Net Income"] = S * ni_shares.get(tk, 0.2)
            rec[f"{tk} Revenue"]    = S * ni_shares.get(tk, 0.2) * 3.2

        # ── Total Revenue for externality base ──
        Rev = sum(rec.get(f"{tk} Revenue", 0) for tk in TICKERS)

        # ── EXTRACTIVE PATH ──
        ext_retained = S
        e_ehi = max(0.02, e_ehi * (1 - ext_degrad))
        e_hri = max(0.02, e_hri * (1 - ext_degrad * 0.8))
        e_iri = max(0.02, e_iri * (1 - ext_degrad * 0.5))

        # ── Per-category externality costs (based on REVENUE!) ──
        idx_map = {"ehi": e_ehi, "hri": e_hri, "iri": e_iri}
        ext_cost = 0.0
        for cat_name, cat_cfg in EXT_CATEGORIES.items():
            cat_cost = cat_cfg["rate"] * Rev * (1 - idx_map[cat_cfg["index"]])
            rec[f"Ext. {cat_name}"] = cat_cost
            ext_cost += cat_cost
        ext_true = ext_retained - ext_cost

        # ── FLYNN PATH ──
        Q = 0.5 * S
        f_retained = S - Q
        DR = dr_0 * (1 - beta * max(f_ehi, f_hri)) * f_iri
        dialysis_flow = DR * Q
        alpha = 1 + gamma * (DR / dr_0) if dr_0 > 0 else 1
        MQ = alpha * Q
        Q_B = q_b_share * Q
        Q_H = (1 - q_b_share) * Q

        impact_b = 0.04 * math.log1p(Q_B / (last_ni * 0.5 + 1))
        impact_h = 0.04 * math.log1p(Q_H / (last_ni * 0.5 + 1))
        f_ehi = min(1.0, f_ehi + impact_b * (1 - f_ehi))
        f_hri = min(1.0, f_hri + impact_h * (1 - f_hri))
        f_iri = min(1.0, f_iri + 0.008 * (1 - f_iri))

        MW_B = Q_B * f_ehi * 2.5
        MW_H = Q_H * f_hri * 2.5
        MW_total = MW_B + MW_H
        flynn_value = f_retained + MQ + MW_total

        delta_abs = flynn_value - ext_true
        # % Vorteil bezogen auf Brutto-Surplus (S), NICHT auf ext_true!
        # Wenn ext_true negativ ist (Externalitaeten > NI), waere Division unsinnig.
        delta_pct = (delta_abs / max(ext_retained, 1)) * 100

        # ── Flynn-path externalities (using improved Flynn indices) ──
        f_idx_map = {"ehi": f_ehi, "hri": f_hri, "iri": f_iri}
        flynn_ext_cost = sum(
            cfg["rate"] * Rev * (1 - f_idx_map[cfg["index"]])
            for cfg in EXT_CATEGORIES.values()
        )
        flynn_jahres_aufbau = (MQ - Q) + MW_total

        # ── CUMULATIVE: the cancer that never heals ──
        cum_ext_cost += ext_cost           # externalities pile up EVERY year
        cum_flynn_created += flynn_jahres_aufbau  # net value Flynn creates above baseline
        cum_schere = cum_ext_cost + cum_flynn_created  # total gap between systems

        rec.update({
            "Surplus (S)": S,
            "Revenue": Rev,
            "Ext. Marktwert": ext_retained, "Ext. Externalities": ext_cost,
            "Ext. True Value": ext_true,
            "Ext. Kum. Externalities": cum_ext_cost,
            "Ext. Kum. Wertvernichtung": -cum_ext_cost,   # negative: the debt
            "Ext. EHI": e_ehi, "Ext. HRI": e_hri, "Ext. IRI": e_iri,
            "Flynn Retained": f_retained, "Matrix-Kapital (Q)": Q,
            "Flynn Matrix Value": flynn_value,
            "Flynn Kum. Wertschoepfung": cum_flynn_created,
            "Flynn EHI": f_ehi, "Flynn HRI": f_hri, "Flynn IRI": f_iri,
            "MW_Total": MW_total, "Matrix-Metamorphose": MQ,
            "Dialyse-Durchsatz": dialysis_flow, "Dialyse-Rate (DR)": DR,
            "Alpha": alpha, "Delta (abs)": delta_abs, "Delta (%)": delta_pct,
            "Kum. Schere (abs)": cum_schere,
            "Flynn Ext. Kosten": flynn_ext_cost,
            "Flynn Jahres-Aufbau": flynn_jahres_aufbau,
            "Netto-Systemsaldo": cum_flynn_created - cum_ext_cost,
        })
        records.append(rec)

    return pd.DataFrame(records)


# ═══════════════════════════════════════════════════════════════════════════════
#  PLOTLY CHART BUILDERS
# ═══════════════════════════════════════════════════════════════════════════════

COLORS = {
    "extractive":  "#ff4d6a",
    "ext_light":   "rgba(255,77,106,0.15)",
    "flynn":       "#00e5a0",
    "flynn_light": "rgba(0,229,160,0.10)",
    "ehi":         "#34d399",
    "ehi_ext":     "#994444",
    "hri":         "#60a5fa",
    "hri_ext":     "#aa6633",
    "iri":         "#c084fc",
    "iri_ext":     "#7a447a",
    "dialysis":    "#fbbf24",
    "delta":       "#fbbf24",
    "hist_bg":     "rgba(30,50,80,0.15)",
    "grid":        "#1a2744",
    "bg":          "rgba(0,0,0,0)",
    "paper":       "rgba(10,14,23,0.0)",
    "text":        "#8fadc9",
}

def _layout_defaults() -> dict:
    return dict(
        template="plotly_dark",
        paper_bgcolor=COLORS["paper"],
        plot_bgcolor=COLORS["bg"],
        font=dict(family="Inter, system-ui, sans-serif", color=COLORS["text"], size=13),
        legend=dict(
            bgcolor="rgba(10,18,32,0.7)", bordercolor="#1a2744", borderwidth=1,
            font=dict(size=11),
        ),
        xaxis=dict(gridcolor=COLORS["grid"], zeroline=False),
        yaxis=dict(gridcolor=COLORS["grid"], zeroline=False),
        margin=dict(l=60, r=30, t=60, b=50),
    )

def _add_projection_shading(fig, df):
    """Add a vertical shaded area for projection years."""
    proj = df[df["Phase"] == "Projektion"]
    if proj.empty:
        return
    x0 = proj["Jahr"].iloc[0] - 0.5
    x1 = proj["Jahr"].iloc[-1] + 0.5
    fig.add_vrect(x0=x0, x1=x1, fillcolor="rgba(0,229,160,0.04)",
                  line_width=0, annotation_text="Projection →",
                  annotation_position="top left",
                  annotation_font=dict(size=11, color="#5fa8ff"))


def chart_stock_prices(df: pd.DataFrame) -> go.Figure:
    """Historical + projected stock prices for all tickers."""
    fig = go.Figure()
    for tk in TICKERS:
        col = f"{tk} Kurs"
        if col in df.columns:
            fig.add_trace(go.Scatter(
                x=df["Jahr"], y=df[col],
                name=f"{NAMES.get(tk, tk)} ({tk})",
                mode="lines+markers",
                line=dict(color=TICKER_COLORS.get(tk, "#aaa"), width=2.5),
                marker=dict(size=5),
                hovertemplate=f"{tk}" + " %{x}: $%{y:,.0f}<extra></extra>",
            ))
    _add_projection_shading(fig, df)
    tl = " / ".join(TICKERS)
    fig.update_layout(
        **_layout_defaults(),
        title=dict(text=f"{t('tab_stocks')} — {tl}", font=dict(size=18)),
        yaxis_title=t("year"), xaxis_title=t("year"), hovermode="x unified",
    )
    return fig


def chart_net_income(df: pd.DataFrame) -> go.Figure:
    """Grouped bar chart: Net Income per ticker by year."""
    fig = go.Figure()
    for tk in TICKERS:
        col = f"{tk} Net Income"
        if col in df.columns:
            fig.add_trace(go.Bar(
                x=df["Jahr"], y=df[col], name=f"{tk} Net Income",
                marker_color=TICKER_COLORS.get(tk, "#aaa"), opacity=0.85,
                hovertemplate="%{x}: $%{y:,.0f}<extra>" + tk + "</extra>",
            ))
    fig.add_trace(go.Scatter(
        x=df["Jahr"], y=df["Surplus (S)"], name="Combined Surplus",
        mode="lines+markers", line=dict(color="#ffffff", width=2),
        marker=dict(size=5, symbol="diamond"),
        hovertemplate="%{x}: $%{y:,.0f}<extra>Surplus</extra>",
    ))
    _add_projection_shading(fig, df)
    fig.update_layout(
        **_layout_defaults(), barmode="group",
        title=dict(text=f"{t('tab_netincome')} (Surplus) — Top {len(TICKERS)}", font=dict(size=18)),
        yaxis_title="Net Income (USD)", xaxis_title=t("year"), hovermode="x unified",
    )
    return fig


def chart_value_comparison(df: pd.DataFrame) -> go.Figure:
    """The core comparison: Extractive True Value vs Flynn Matrix Value."""
    proj = df[df["Phase"] == "Projektion"]
    # Also include last historical year as connection point
    hist_last = df[df["Phase"] == "Historisch"].tail(1)
    plot_df = pd.concat([hist_last, proj]) if not hist_last.empty else proj

    fig = go.Figure()

    # Extractive: gross (the illusion)
    fig.add_trace(go.Scatter(
        x=plot_df["Jahr"], y=plot_df["Ext. Marktwert"],
        name=t("extractive_label") + ": Gross (Illusion)", mode="lines",
        line=dict(color="#664455", width=1.5, dash="dash"),
        hovertemplate="%{x}: $%{y:,.0f}<extra>Ext. Gross</extra>",
    ))
    # Extractive: true value
    fig.add_trace(go.Scatter(
        x=plot_df["Jahr"], y=plot_df["Ext. True Value"],
        name=t("extractive_label") + ": True Value", mode="lines+markers",
        line=dict(color=COLORS["extractive"], width=3),
        marker=dict(size=6), fill="tonexty", fillcolor=COLORS["ext_light"],
        hovertemplate="%{x}: $%{y:,.0f}<extra>Ext. Netto</extra>",
    ))
    # Externality costs — TOTAL (the full destructive truth)
    fig.add_trace(go.Scatter(
        x=plot_df["Jahr"], y=plot_df["Ext. Externalities"],
        name=t("extractive_ext"), mode="lines+markers",
        line=dict(color="#ff8c42", width=3.5, dash="dot"),
        marker=dict(size=5, color="#ff8c42"),
        hovertemplate="%{x}: $%{y:,.0f}<extra>ALLE Ext.-Kosten</extra>",
    ))
    # Individual category lines (thin, stacked visibility)
    for cat_name, cat_cfg in EXT_CATEGORIES.items():
        col = f"Ext. {cat_name}"
        if col in plot_df.columns:
            fig.add_trace(go.Scatter(
                x=plot_df["Jahr"], y=plot_df[col],
                name=cat_name, mode="lines",
                line=dict(color=cat_cfg["color"], width=1, dash="dash"),
                hovertemplate="%{x}: $%{y:,.0f}<extra>" + cat_name + "</extra>",
                visible="legendonly",  # toggle-able — default hidden to avoid clutter
            ))
    # Flynn
    fig.add_trace(go.Scatter(
        x=plot_df["Jahr"], y=plot_df["Flynn Matrix Value"],
        name="Flynn Matrix Value", mode="lines+markers",
        line=dict(color=COLORS["flynn"], width=3),
        marker=dict(size=7, symbol="diamond"),
        hovertemplate="%{x}: $%{y:,.0f}<extra>Flynn</extra>",
    ))

    # ── Cumulative REAL system debt (the hidden truth) ──
    fig.add_trace(go.Scatter(
        x=plot_df["Jahr"], y=plot_df["Ext. Kum. Wertvernichtung"],
        name=t("cum_destruction_trace") + " (1996+)", mode="lines",
        line=dict(color="#ff6b6b", width=2, dash="dashdot"),
        fill="tozeroy", fillcolor="rgba(255,77,106,0.06)",
        hovertemplate="%{x}: $%{y:,.0f}<extra>Kum. Schuld</extra>",
    ))
    # ── Cumulative Flynn value creation ──
    fig.add_trace(go.Scatter(
        x=plot_df["Jahr"], y=plot_df["Flynn Kum. Wertschoepfung"],
        name=t("cum_flynn_trace"), mode="lines",
        line=dict(color="#2ecc71", width=2, dash="dashdot"),
        hovertemplate="%{x}: $%{y:,.0f}<extra>Kum. Flynn</extra>",
    ))

    # Final year annotations
    if not proj.empty:
        final = proj.iloc[-1]
        yr = final["Jahr"]
        flynn_adv = _sf(final["Delta (%)"])
        fig.add_annotation(
            x=yr, y=_sf(final["Flynn Matrix Value"]),
            text=f'+{flynn_adv:,.0f}% vs. Brutto', showarrow=True,
            arrowhead=2, arrowcolor=COLORS["flynn"], ax=45, ay=-30,
            font=dict(size=16, color=COLORS["flynn"]),
            bgcolor="rgba(0,30,20,0.85)", bordercolor=COLORS["flynn"],
        )
        ext_eff = ((_sf(final["Ext. True Value"]) / max(_sf(final["Ext. Marktwert"]), 1)) - 1) * 100
        fig.add_annotation(
            x=yr, y=_sf(final["Ext. True Value"]),
            text=f'{ext_eff:,.0f}% wahrer Wert', showarrow=True,
            arrowhead=2, arrowcolor=COLORS["extractive"], ax=45, ay=30,
            font=dict(size=14, color=COLORS["extractive"]),
            bgcolor="rgba(40,0,0,0.85)", bordercolor=COLORS["extractive"],
        )
        # Absolute gap annotation
        gap = _sf(final["Flynn Matrix Value"]) - _sf(final["Ext. True Value"])
        mid_y = (_sf(final["Flynn Matrix Value"]) + _sf(final["Ext. True Value"])) / 2
        fig.add_annotation(
            x=yr - 1.5, y=mid_y,
            text=f'Schere (jährl.): {gap/1e9:,.1f} Mrd.', showarrow=False,
            font=dict(size=14, color="#fbbf24"),
            bgcolor="rgba(20,10,0,0.85)", bordercolor="#fbbf24", borderwidth=2,
        )
        # Cumulative debt annotation
        cum_debt = _sf(final["Ext. Kum. Wertvernichtung"])
        fig.add_annotation(
            x=yr, y=cum_debt,
            text=f'Kum. Schuld: {cum_debt/1e9:,.0f} Mrd.', showarrow=True,
            arrowhead=2, arrowcolor="#ff6b6b", ax=-60, ay=40,
            font=dict(size=13, color="#ff6b6b"),
            bgcolor="rgba(40,0,0,0.85)", bordercolor="#ff6b6b", borderwidth=2,
        )

    fig.update_layout(
        **_layout_defaults(),
        title=dict(text=t("tab_comparison") + ": " + t("extractive_label") + " vs. Flynn Matrix", font=dict(size=18)),
        yaxis_title=t("system_value"), xaxis_title=t("year"), hovermode="x unified",
    )
    return fig


def chart_delta_bars(df: pd.DataFrame) -> go.Figure:
    """Bar chart: Flynn advantage % per year (vs. Brutto-Surplus S)."""
    proj = df[df["Phase"] == "Projektion"]
    colors = [COLORS["flynn"] if v >= 0 else COLORS["extractive"] for v in proj["Delta (%)"]]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=proj["Jahr"], y=proj["Delta (%)"], name=t("tab_flynn_pct"),
        marker_color=colors, opacity=0.85,
        text=[f"{v:+,.0f}%" for v in proj["Delta (%)"]],
        textposition="outside", textfont=dict(size=12, color=COLORS["text"]),
        hovertemplate="%{x}: %{y:+,.1f}%<extra></extra>",
    ))
    fig.update_layout(
        **_layout_defaults(),
        title=dict(text=t("tab_flynn_pct") + " vs. " + t("extractive_label"), font=dict(size=18)),
        yaxis_title="%", xaxis_title=t("year"), hovermode="x unified",
    )
    return fig


def chart_cumulative_destruction(df: pd.DataFrame) -> go.Figure:
    """
    THE CORE CHART: Cumulative externality destruction (the cancer)
    vs cumulative Flynn value creation.
    Externalities are NEVER repaid — they grow every single year.
    This is what stays invisible in the extractive system.
    """
    # Full timeline: historical + projection
    all_data = df.copy()
    if all_data.empty:
        return go.Figure()

    proj = df[df["Phase"] == "Projektion"]
    hist = df[df["Phase"] == "Historisch"]
    retro = df[df["Phase"] == "Retropolation"]
    # current_year = last year before projection starts
    non_proj = df[df["Phase"] != "Projektion"]
    current_year = int(non_proj["Jahr"].max()) if not non_proj.empty else 2025
    first_real = int(hist["Jahr"].min()) if not hist.empty else 2021

    fig = go.Figure()

    # ── Per-category cumulative destruction over FULL timeline ──
    # The data already has pre-computed Ext. Kum. values, but for stacked areas
    # we need per-category cumsum over ALL phases
    for cat_name in reversed(EXT_CAT_NAMES):
        col = f"Ext. {cat_name}"
        if col in all_data.columns:
            cum_cat = -all_data[col].cumsum()
            cat_cfg = EXT_CATEGORIES[cat_name]
            fig.add_trace(go.Scatter(
                x=all_data["Jahr"], y=cum_cat,
                name=f"Kum. {cat_name}",
                mode="lines", line=dict(color=cat_cfg["color"], width=0.5),
                stackgroup="ext_cats",
                hovertemplate="%{x}: %{y:$,.0f}<extra>" + cat_name + "</extra>",
            ))

    # ── Total cumulative destruction line (bold on top) ──
    fig.add_trace(go.Scatter(
        x=all_data["Jahr"], y=all_data["Ext. Kum. Wertvernichtung"],
        name=t("cum_destruction_trace") + " TOTAL",
        mode="lines+markers", line=dict(color=COLORS["extractive"], width=3),
        marker=dict(size=5),
        hovertemplate="%{x}: %{y:$,.0f}<extra>TOTAL</extra>",
    ))

    # ── Flynn: cumulative value creation (starts at 0 until projection) ──
    fig.add_trace(go.Scatter(
        x=all_data["Jahr"], y=all_data["Flynn Kum. Wertschoepfung"],
        name=t("cum_flynn_trace"),
        mode="lines+markers", line=dict(color=COLORS["flynn"], width=3),
        marker=dict(size=5),
        fill="tozeroy", fillcolor="rgba(0,229,160,0.15)",
        hovertemplate="%{x}: %{y:$,.0f}<extra>Flynn</extra>",
    ))

    # ── Zero line ──
    fig.add_hline(y=0, line_width=2, line_color="#ffffff", opacity=0.4)

    # ── Flynn-Start vertical line ──
    fig.add_vline(
        x=current_year + 0.5, line_width=2, line_dash="dash",
        line_color="#00e5a0", opacity=0.7,
    )
    fig.add_annotation(
        x=current_year + 0.5, y=0,
        text=t("flynn_starts"), showarrow=False,
        font=dict(size=13, color="#00e5a0"),
        bgcolor="rgba(0,30,20,0.85)", bordercolor="#00e5a0",
        yshift=20,
    )

    # ── Historical debt annotation at Flynn-start ──
    non_proj_last = non_proj.iloc[-1] if not non_proj.empty else None
    if non_proj_last is not None:
        hist_debt = _sf(non_proj_last.get("Ext. Kum. Externalities", 0))
        fig.add_annotation(
            x=current_year, y=_sf(non_proj_last.get("Ext. Kum. Wertvernichtung", 0)),
            text=t("legacy_30y", v=f'{hist_debt/1e9:,.0f}'),
            showarrow=True, arrowhead=2, arrowcolor="#fbbf24",
            ax=-70, ay=40,
            font=dict(size=14, color="#fbbf24"),
            bgcolor="rgba(40,20,0,0.85)", bordercolor="#fbbf24", borderwidth=2,
        )

    # ── Real-data-start annotation ──
    if not retro.empty:
        fig.add_vline(
            x=first_real - 0.5, line_width=1.5, line_dash="dot",
            line_color="#6ea8fe", opacity=0.5,
        )
        fig.add_annotation(
            x=first_real - 0.5, y=0,
            text=t("real_data_from"), showarrow=False,
            font=dict(size=11, color="#6ea8fe"),
            bgcolor="rgba(0,20,40,0.75)", bordercolor="#6ea8fe",
            yshift=40,
        )

    # ── End-year annotations ──
    if not proj.empty:
        final = proj.iloc[-1]
        schere = _sf(final["Kum. Schere (abs)"])
        yr = final["Jahr"]
        fig.add_annotation(
            x=yr, y=_sf(final["Flynn Kum. Wertschoepfung"]) * 0.5,
            text=t("gap_bn", v=f'{schere/1e9:,.0f}'),
            showarrow=True, arrowhead=2, arrowcolor="#fbbf24",
            ax=-80, ay=-40,
            font=dict(size=16, color="#fbbf24", family="Inter, sans-serif"),
            bgcolor="rgba(20,10,0,0.85)", bordercolor="#fbbf24", borderwidth=2,
        )
        fig.add_annotation(
            x=yr, y=_sf(final["Ext. Kum. Wertvernichtung"]),
            text=t("cum_debt", v=f'{_sf(final["Ext. Kum. Externalities"])/1e9:,.0f}'),
            showarrow=True, arrowhead=2, arrowcolor=COLORS["extractive"],
            ax=-80, ay=40,
            font=dict(size=14, color=COLORS["extractive"]),
            bgcolor="rgba(40,0,0,0.85)", bordercolor=COLORS["extractive"],
        )

    fig.update_layout(
        **_layout_defaults(),
        title=dict(
            text=t("chart_cum_title"),
            font=dict(size=18),
        ),
        yaxis_title=t("cumulated_value"),
        xaxis_title=t("year"),
        hovermode="x unified",
        barmode="overlay",
    )
    return fig


def chart_annual_comparison(df: pd.DataFrame) -> go.Figure:
    """
    Side-by-side per year: what the extractive system DESTROYS
    vs what Flynn CREATES. Mirror bars above/below zero.
    """
    # Full timeline — historical shows pure destruction, projection adds Flynn
    all_data = df.copy()
    if all_data.empty:
        return go.Figure()

    hist = df[df["Phase"] == "Historisch"]
    retro = df[df["Phase"] == "Retropolation"]
    proj = df[df["Phase"] == "Projektion"]
    non_proj = df[df["Phase"] != "Projektion"]
    current_year = int(non_proj["Jahr"].max()) if not non_proj.empty else 2025
    first_real = int(hist["Jahr"].min()) if not hist.empty else 2021

    fig = go.Figure()

    # ── Negative: per-category annual costs as stacked bars (ALL years) ──
    for cat_name in EXT_CAT_NAMES:
        col = f"Ext. {cat_name}"
        if col in all_data.columns:
            cat_cfg = EXT_CATEGORIES[cat_name]
            fig.add_trace(go.Bar(
                x=all_data["Jahr"],
                y=[-v for v in all_data[col]],
                name=cat_name,
                marker_color=cat_cfg["color"], opacity=0.85,
                hovertemplate="%{x}: %{y:$,.0f}<extra>" + cat_name + "</extra>",
            ))

    # Positive: Flynn generated value (MW + MQ uplift) — only in projection!
    # Historical years: Flynn = 0
    flynn_added = []
    for _, row in all_data.iterrows():
        if row["Phase"] == "Projektion":
            flynn_added.append(row["MW_Total"] + (row["Matrix-Metamorphose"] - row["Matrix-Kapital (Q)"]))
        else:
            flynn_added.append(0)
    fig.add_trace(go.Bar(
        x=all_data["Jahr"],
        y=flynn_added,
        name=t("flynn_building"),
        marker_color=COLORS["flynn"], opacity=0.85,
        text=[f'+{v/1e9:.1f}B' if v > 0 else '' for v in flynn_added],
        textposition="outside",
        textfont=dict(size=11, color=COLORS["flynn"]),
        hovertemplate="%{x}: +%{y:$,.0f}<extra>Aufbau</extra>",
    ))

    fig.add_hline(y=0, line_width=2, line_color="#ffffff", opacity=0.3)

    # ── Flynn-Start vertical line ──
    fig.add_vline(
        x=current_year + 0.5, line_width=2, line_dash="dash",
        line_color="#00e5a0", opacity=0.7,
    )
    fig.add_annotation(
        x=current_year + 0.5, y=0,
        text=t("flynn_starts"), showarrow=False,
        font=dict(size=13, color="#00e5a0"),
        bgcolor="rgba(0,30,20,0.85)", bordercolor="#00e5a0",
        yshift=20,
    )

    # ── Real-data-start marker ──
    if not retro.empty:
        fig.add_vline(
            x=first_real - 0.5, line_width=1.5, line_dash="dot",
            line_color="#6ea8fe", opacity=0.5,
        )
        fig.add_annotation(
            x=first_real - 0.5, y=0,
            text=t("real_data_from"), showarrow=False,
            font=dict(size=10, color="#6ea8fe"),
            bgcolor="rgba(0,20,40,0.75)", bordercolor="#6ea8fe",
            yshift=-20,
        )

    fig.update_layout(
        **_layout_defaults(),
        barmode="relative",
        title=dict(
            text=t("chart_cum_title"),
            font=dict(size=18),
        ),
        yaxis_title=t("system_value"), xaxis_title=t("year"), hovermode="x unified",
    )
    return fig


def chart_indices_compare(df: pd.DataFrame) -> go.Figure:
    """Side-by-side: Extractive degradation vs Flynn regeneration."""
    proj = df[df["Phase"] == "Projektion"]
    hist_last = df[df["Phase"] == "Historisch"].tail(1)
    plot_df = pd.concat([hist_last, proj]) if not hist_last.empty else proj

    fig = make_subplots(
        rows=1, cols=2, shared_yaxes=True, horizontal_spacing=0.06,
        subplot_titles=(t("extractive_label") + " — Degradation", "Flynn — Regeneration"),
    )

    for idx_name, c_ext, c_fly in [
        ("EHI", COLORS["ehi_ext"], COLORS["ehi"]),
        ("HRI", COLORS["hri_ext"], COLORS["hri"]),
        ("IRI", COLORS["iri_ext"], COLORS["iri"]),
    ]:
        fig.add_trace(go.Scatter(
            x=plot_df["Jahr"], y=plot_df[f"Ext. {idx_name}"],
            name=f"{idx_name} (ext.)", mode="lines+markers",
            line=dict(color=c_ext, width=2), marker=dict(size=4),
        ), row=1, col=1)
        fig.add_trace(go.Scatter(
            x=plot_df["Jahr"], y=plot_df[f"Flynn {idx_name}"],
            name=f"{idx_name} (Flynn)", mode="lines+markers",
            line=dict(color=c_fly, width=2.5), marker=dict(size=5),
            fill="tozeroy", fillcolor=f"rgba({','.join(str(int(c_fly.lstrip('#')[i:i+2],16)) for i in (0,2,4))},0.10)" if c_fly.startswith("#") else "rgba(50,200,150,0.10)",
        ), row=1, col=2)

    layout = _layout_defaults()
    layout.pop("xaxis", None)
    layout.pop("yaxis", None)
    fig.update_layout(
        **layout,
        title=dict(text=t("tab_indices"), font=dict(size=18)),
        hovermode="x unified",
        yaxis=dict(gridcolor=COLORS["grid"], zeroline=False, range=[0, 1.05], title="Index"),
        yaxis2=dict(gridcolor=COLORS["grid"], zeroline=False, range=[0, 1.05]),
        xaxis=dict(gridcolor=COLORS["grid"], zeroline=False, title=t("year")),
        xaxis2=dict(gridcolor=COLORS["grid"], zeroline=False, title=t("year")),
    )
    return fig


def chart_dialysis(df: pd.DataFrame) -> go.Figure:
    """Dialyse: Externalitäten ins MINUS, Flynn-Aufbau ins PLUS — Gleichgewicht bei y=0."""
    years = df["Jahr"].values

    # Externalitäten als NEGATIVE Werte (Zerstörung = unter Null!)
    ext_annual = -df["Ext. Externalities"].values / 1e9        # extraktiv → MINUS
    flynn_ext  = -df["Flynn Ext. Kosten"].values / 1e9         # Flynn-Pfad → MINUS (aber sinkend → 0)
    flynn_aufb =  df["Flynn Jahres-Aufbau"].values / 1e9       # Flynn-Aufbau → PLUS

    # Netto-Bilanz pro Jahr: Aufbau minus Zerstörung
    netto = flynn_aufb + flynn_ext   # flynn_ext ist negativ, also Aufbau + (neg. Rest-Ext.)

    fig = go.Figure()

    # ── Red area below zero: Extractive externalities (the growing disease) ──
    fig.add_trace(go.Scatter(
        x=years, y=ext_annual, fill='tozeroy',
        fillcolor='rgba(231,76,60,0.2)',
        line=dict(color=COLORS["extractive"], width=2),
        name=t("extractive_ext"),
        hovertemplate='%{x}: %{y:,.1f} Bn<extra>' + t("extractive_label") + '</extra>',
    ))

    # ── Light-red area: Flynn-path externalities still below zero but shrinking → 0 ──
    fig.add_trace(go.Scatter(
        x=years, y=flynn_ext, fill='tozeroy',
        fillcolor='rgba(255,165,0,0.12)',
        line=dict(color='#ff8c42', width=2, dash='dash'),
        name=t("flynn_residual_ext"),
        hovertemplate='%{x}: %{y:,.1f} Bn<extra>Flynn</extra>',
    ))

    # ── Green area above zero: Flynn annual creation ──
    fig.add_trace(go.Scatter(
        x=years, y=flynn_aufb, fill='tozeroy',
        fillcolor='rgba(46,204,113,0.15)',
        line=dict(color=COLORS["flynn"], width=3),
        name=t("flynn_building"),
        hovertemplate='%{x}: +%{y:,.1f} Bn<extra>Flynn</extra>',
    ))

    # ── Yellow bold: Net balance per year (the key line!) ──
    fig.add_trace(go.Scatter(
        x=years, y=netto, mode='lines',
        line=dict(color='#f1c40f', width=3),
        name=t("net_balance"),
        hovertemplate='%{x}: %{y:,.1f} Bn<extra>Net</extra>',
    ))

    # ── Gleichgewichtslinie bei y=0 ──
    fig.add_hline(
        y=0, line_dash="dash", line_color="white", line_width=1.5,
        annotation_text=t("equilibrium_zone"),
        annotation_position="top left",
        annotation_font_size=14, annotation_font_color="#f1c40f",
    )

    # ── Flynn start marker ──
    first_proj = df[df["Phase"] == "Projektion"]["Jahr"].min()
    fig.add_vline(
        x=first_proj, line_dash="dash", line_color="#2ecc71", line_width=1.5,
        annotation_text=t("flynn_starts"), annotation_position="top right",
        annotation_font_color="#2ecc71",
    )

    # ── Mark when Netto-Bilanz crosses zero (equilibrium reached!) ──
    proj = df[df["Phase"] == "Projektion"]
    if len(proj) >= 2:
        proj_aufb = proj["Flynn Jahres-Aufbau"].values / 1e9
        proj_fext = -proj["Flynn Ext. Kosten"].values / 1e9
        proj_netto = proj_aufb + proj_fext
        for i in range(1, len(proj_netto)):
            if proj_netto[i] >= 0 and proj_netto[i - 1] < 0:
                # Linear interpolation for exact crossing year
                frac = -proj_netto[i - 1] / (proj_netto[i] - proj_netto[i - 1]) if (proj_netto[i] - proj_netto[i - 1]) != 0 else 0
                eq_yr = float(proj.iloc[i - 1]["Jahr"]) + frac
                fig.add_annotation(
                    x=eq_yr, y=0,
                    text=t("equilibrium_approx", yr=f'{eq_yr:.0f}'),
                    showarrow=True, arrowhead=2, ay=-50,
                    font=dict(size=14, color="#f1c40f"),
                    bgcolor="rgba(0,0,0,0.8)", bordercolor="#f1c40f", borderwidth=2,
                )
                break

    # ── End-year annotations ──
    if len(proj) > 0:
        final_yr = int(proj.iloc[-1]["Jahr"])
        final_ext = -_sf(proj.iloc[-1]["Ext. Externalities"]) / 1e9
        final_fext = -_sf(proj.iloc[-1]["Flynn Ext. Kosten"]) / 1e9
        final_aufb = _sf(proj.iloc[-1]["Flynn Jahres-Aufbau"]) / 1e9
        fig.add_annotation(
            x=final_yr, y=final_ext,
            text=t("bn_extractive") + f': {final_ext:,.0f}',
            showarrow=True, arrowhead=2, ax=60, ay=30,
            font=dict(size=12, color=COLORS["extractive"]),
            bgcolor="rgba(40,0,0,0.85)", bordercolor=COLORS["extractive"],
        )
        fig.add_annotation(
            x=final_yr, y=final_aufb,
            text=t("bn_flynn_building") + f': +{final_aufb:,.0f}',
            showarrow=True, arrowhead=2, ax=60, ay=-30,
            font=dict(size=12, color=COLORS["flynn"]),
            bgcolor="rgba(0,30,20,0.85)", bordercolor=COLORS["flynn"],
        )

    fig.update_layout(
        **_layout_defaults(),
        title=dict(
            text=t("chart_dialysis_title"),
            font=dict(size=18),
        ),
        yaxis_title=t("annual_balance"),
        xaxis_title=t("year"),
        hovermode="x unified",
    )
    return fig


def chart_metamorphose(df: pd.DataFrame) -> go.Figure:
    """Metamorphose: Kumulative Heilung — wann ist die Systemschuld abgetragen."""
    years = df["Jahr"].values
    saldo     = df["Netto-Systemsaldo"].values / 1e9          # Netto (gelbe Linie)
    cum_ext   = (-df["Ext. Kum. Externalities"].values) / 1e9 # negativ = Schuld
    cum_flynn = df["Flynn Kum. Wertschoepfung"].values / 1e9  # positiv = Aufbau

    fig = go.Figure()

    # ── Red area: cumulative destruction (negative) ──
    fig.add_trace(go.Scatter(
        x=years, y=cum_ext, fill='tozeroy',
        fillcolor='rgba(231,76,60,0.2)',
        line=dict(color=COLORS["extractive"], width=2),
        name=t("cum_destruction_trace"),
        hovertemplate='%{x}: $%{y:,.0f} Bn<extra></extra>',
    ))

    # ── Green area: cumulative Flynn creation (positive) ──
    fig.add_trace(go.Scatter(
        x=years, y=cum_flynn, fill='tozeroy',
        fillcolor='rgba(46,204,113,0.2)',
        line=dict(color=COLORS["flynn"], width=2),
        name=t("cum_flynn_trace"),
        hovertemplate='%{x}: $%{y:,.0f} Bn<extra>Flynn</extra>',
    ))

    # ── Yellow bold line: Net system balance ──
    fig.add_trace(go.Scatter(
        x=years, y=saldo, mode='lines',
        line=dict(color='#f1c40f', width=3),
        name=t("net_system_balance"),
        hovertemplate='%{x}: $%{y:,.0f} Bn<extra></extra>',
    ))

    # ── Equilibrium line ──
    fig.add_hline(
        y=0, line_dash="dash", line_color="white", line_width=1,
        annotation_text=t("equilibrium"), annotation_position="top left",
        annotation_font_color="white",
    )

    # ── Flynn start marker ──
    first_proj = df[df["Phase"] == "Projektion"]["Jahr"].min()
    fig.add_vline(
        x=first_proj, line_dash="dash", line_color="#2ecc71", line_width=1.5,
        annotation_text=t("flynn_starts"), annotation_position="top right",
        annotation_font_color="#2ecc71",
    )

    # ── Check if / when net saldo reaches 0, or extrapolate ──
    proj = df[df["Phase"] == "Projektion"]
    eq_found = False
    if len(proj) >= 2:
        for i in range(1, len(proj)):
            prev_s = proj.iloc[i - 1]["Netto-Systemsaldo"]
            curr_s = proj.iloc[i]["Netto-Systemsaldo"]
            if curr_s >= 0 and prev_s < 0:
                frac = -prev_s / (curr_s - prev_s) if (curr_s - prev_s) != 0 else 0
                eq_yr = proj.iloc[i - 1]["Jahr"] + frac
                fig.add_annotation(
                    x=eq_yr, y=0,
                    text=t("equilibrium_approx", yr=f'{eq_yr:.0f}'),
                    showarrow=True, arrowhead=2, ay=-50,
                    font=dict(size=14, color="#f1c40f"),
                    bgcolor="rgba(0,0,0,0.8)", bordercolor="#f1c40f",
                )
                eq_found = True
                break

    if not eq_found and len(proj) >= 2:
        last_s = proj.iloc[-1]["Netto-Systemsaldo"]
        prev_s = proj.iloc[-2]["Netto-Systemsaldo"]
        annual_impr = last_s - prev_s
        if annual_impr > 0 and last_s < 0:
            yrs_to_eq = -last_s / annual_impr
            est_yr = int(proj.iloc[-1]["Jahr"] + yrs_to_eq)
            fig.add_annotation(
                x=float(proj.iloc[-1]["Jahr"]), y=saldo[-1],
                text=t("forecast_eq", yr=est_yr),
                showarrow=True, arrowhead=2, ay=-40,
                font=dict(size=12, color="#f1c40f"),
                bgcolor="rgba(0,0,0,0.7)", bordercolor="#f1c40f",
            )
        elif annual_impr <= 0:
            fig.add_annotation(
                x=float(proj.iloc[-1]["Jahr"]), y=saldo[-1],
                text=t("eq_not_reachable"),
                showarrow=True, arrowhead=2, ay=-40,
                font=dict(size=12, color="#e74c3c"),
                bgcolor="rgba(0,0,0,0.7)", bordercolor="#e74c3c",
            )

    fig.update_layout(
        **_layout_defaults(),
        title=dict(
            text=t("chart_metamorphose_title"),
            font=dict(size=18),
        ),
        yaxis_title=t("cumulated_bn"),
        xaxis_title=t("year"),
        hovermode="x unified",
    )
    return fig


# ═══════════════════════════════════════════════════════════════════════════════
#  FORMATTING HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def fmt_usd(v) -> str:
    try:
        v = float(v)
        if math.isnan(v) or math.isinf(v):
            return "$0"
    except (TypeError, ValueError):
        return "$0"
    if abs(v) >= 1e12: return f"${v/1e12:,.2f} T"
    if abs(v) >= 1e9:  return f"${v/1e9:,.2f} B"
    if abs(v) >= 1e6:  return f"${v/1e6:,.1f} M"
    return f"${v:,.0f}"


# ═══════════════════════════════════════════════════════════════════════════════
#  MAIN UI
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    # ── Language selector (top of sidebar, BEFORE any other sidebar widget) ──
    with st.sidebar:
        lang_options = list(LANGUAGES.keys())
        lang_choice = st.selectbox(
            "🌐 Language", lang_options, index=0,
            key="_lang_sel",
        )
        st.session_state["lang"] = LANGUAGES[lang_choice]

    # ── Header ──
    st.markdown("""
    <div style="text-align:center; margin-bottom:8px;">
        <span class="dashboard-badge">SOCIETAL BUSINESS THINK TANK</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; margin-top:0;'>Flynn 50/50 Matrix Dashboard</h1>",
                unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center; color:#5a7ea3; margin-top:-10px; font-size:0.92rem;'>"
        + t("subtitle") +
        "</p>", unsafe_allow_html=True
    )

    # ── Fetch REAL data ──
    tl = ", ".join(TICKERS)
    with st.spinner(f"{t('loading_data')} ({tl}) ..."):
        hist_df = get_historical_data()

    avail = _available_tickers(hist_df)
    hist_years = sorted(hist_df.index.tolist())
    current_year = hist_years[-1] if hist_years else 2025
    latest_ni = float(hist_df.loc[current_year, "Combined_NI"]) if current_year in hist_df.index else 12e9

    # ── Sidebar: Parameters ──
    with st.sidebar:
        st.markdown(f"## {t('sidebar_params')}")
        st.caption(t("sidebar_hint"))
        st.divider()

        st.markdown(f"### {t('sidebar_flynn')}")
        gamma = st.slider(t("gamma_label"), 0.0, 3.0, 1.0, 0.05,
            help=t("gamma_help"))
        dr_0 = st.slider(t("dr0_label"), 0.01, 0.20, 0.05, 0.005, format="%.3f",
            help=t("dr0_help"))
        beta = st.slider(t("beta_label"), 0.0, 0.50, 0.15, 0.01,
            help=t("beta_help"))

        st.divider()
        st.markdown(f"### {t('sidebar_indices')}")
        ehi_0 = st.slider(t("ehi_label"), 0.1, 0.9, 0.30, 0.05)
        hri_0 = st.slider(t("hri_label"),  0.1, 0.9, 0.40, 0.05)
        iri_0 = st.slider(t("iri_label"),         0.1, 0.9, 0.50, 0.05)

        st.divider()
        st.markdown(f"### {t('sidebar_alloc')}")
        q_b_share = st.slider(t("bio_share"), 0.0, 1.0, 0.50, 0.05)

        st.divider()
        st.markdown(f"### {t('sidebar_extract')}")
        ext_degrad = st.slider(t("degrad_label"), 0.01, 0.10, 0.04, 0.005, format="%.1f%%",
            help=t("degrad_help"))
        growth_rate = st.slider(t("growth_label"), 0.0, 0.15, 0.04, 0.005, format="%.1f%%")
        proj_years = st.slider(t("proj_years_label"), 5, 20, 10, 1)

    # ── Run full simulation ──
    df = run_full_simulation(
        hist_df=hist_df, proj_years=proj_years, growth_rate=growth_rate,
        gamma=gamma, dr_0=dr_0, beta=beta,
        ehi_0=ehi_0, hri_0=hri_0, iri_0=iri_0,
        q_b_share=q_b_share, ext_degrad=ext_degrad,
    )

    proj = df[df["Phase"] == "Projektion"]
    final = proj.iloc[-1] if not proj.empty else df.iloc[-1]
    hist_rows = df[df["Phase"].isin(["Historisch", "Retropolation"])]
    hist_last = hist_rows.iloc[-1] if len(hist_rows) > 0 else df.iloc[0]
    retro_start = int(df["Jahr"].min())

    # ── Live Data KPIs ──
    st.markdown("---")
    st.markdown(f"### {t('live_data_title', n=len(avail))}")
    kpi_cols = st.columns(len(avail) + 1)
    for i, tk in enumerate(avail):
        col_name = f"{tk} Kurs"
        price = hist_last.get(col_name, 0) or 0
        kpi_cols[i].metric(f"{NAMES.get(tk, tk)}", f"${price:,.0f}",
                           f"{tk}")
    ni_first = _sf(hist_df.iloc[0]["Combined_NI"], latest_ni) if not hist_df.empty else latest_ni
    ni_chg = ((latest_ni / ni_first) - 1) * 100 if ni_first else 0
    kpi_cols[-1].metric(t("combined_ni"), fmt_usd(latest_ni),
                        f"{ni_chg:+,.1f}% ({hist_years[0]}-{current_year})")

    # ── THE CANCER: Cumulative Destruction prominently displayed ──
    st.markdown("---")
    cum_ext = _sf(final.get("Ext. Kum. Externalities", 0))
    cum_flynn = _sf(final.get("Flynn Kum. Wertschoepfung", 0))
    cum_schere = cum_ext + cum_flynn

    st.markdown(
        '<div style="background: linear-gradient(135deg, rgba(60,0,0,0.4), rgba(0,40,30,0.4)); '
        'border: 1px solid #552222; border-radius: 12px; padding: 20px 24px; margin-bottom: 20px;">'
        '<h3 style="text-align:center; margin:0 0 8px 0; color:#ff6b6b;">'
        + t("cancer_title") + '</h3>'
        '<p style="text-align:center; color:#8fadc9; font-size:0.85rem; margin:0 0 12px 0;">'
        + t("cancer_desc") + '</p></div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    # Historical debt (30 years before Flynn existed)
    hist_debt = _sf(hist_last.get("Ext. Kum. Externalities", 0))
    c1.metric(
        t("legacy_debt", start=retro_start, end=current_year),
        f'-{fmt_usd(hist_debt)}',
        t("years_before_flynn", n=current_year - retro_start),
        delta_color="inverse",
    )
    c2.metric(
        t("cum_destruction_total"),
        f'-{fmt_usd(cum_ext)}',
        t("years_total", start=retro_start, end=int(final["Jahr"]), n=int(final["Jahr"]) - retro_start),
        delta_color="inverse",
    )
    c3.metric(
        t("cum_creation_flynn"),
        f'+{fmt_usd(cum_flynn)}',
        t("from_year_regen", yr=current_year+1),
    )
    c4.metric(
        t("system_gap"),
        fmt_usd(cum_schere),
        t("gap_between_systems"),
    )
    ext_last_yr = _sf(final.get("Ext. Externalities", 0))
    c5.metric(
        t("ext_only_year", yr=int(final['Jahr'])),
        fmt_usd(ext_last_yr),
        t("per_year_rising"),
        delta_color="inverse",
    )

    # ── Projection Results ──
    st.markdown("---")
    st.markdown(f"### Ergebnis {current_year + 1} – {int(final['Jahr'])} — Systemvergleich")
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Extraktiv (wahrer Wert)", fmt_usd(final["Ext. True Value"]))
    c2.metric("Flynn Matrix Value", fmt_usd(final["Flynn Matrix Value"]))
    c3.metric("Flynn-Vorteil (vs. Brutto)", f'+{final["Delta (%)"]:,.0f}%', fmt_usd(final["Delta (abs)"]))
    c4.metric("EHI: Ext. vs Flynn",
              f'{final["Ext. EHI"]:.2f} vs {final["Flynn EHI"]:.2f}')
    c5.metric("Kum. Externalitaeten", fmt_usd(cum_ext),
              "Nie abgebaut!", delta_color="inverse")

    # ── TABS ──
    st.markdown("---")
    tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
        t("tab_cum_destruction"), t("tab_annual"),
        t("tab_stocks"), t("tab_netincome"), t("tab_comparison"),
        t("tab_flynn_pct"), t("tab_indices"),
        t("tab_dialysis"), t("tab_data"),
    ])

    with tab0:
        st.plotly_chart(chart_cumulative_destruction(df), width="stretch")
        st.caption(t("cap_cum_destruction", yr=hist_years[0]))
        # ── Per-category breakdown table (ALL years: historical + projection) ──
        with st.expander(t('all_categories_title', start=retro_start), expanded=False):
            cat_cols = ["Jahr", "Phase", "Revenue"] + [f"Ext. {c}" for c in EXT_CAT_NAMES] + [
                "Ext. Externalities", "Ext. Kum. Externalities"]
            cat_cols_avail = [c for c in cat_cols if c in df.columns]
            breakdown = df[cat_cols_avail].copy()
            nice_names = {"Jahr": "Jahr", "Phase": "Phase", "Revenue": "Revenue",
                          "Ext. Externalities": "SUMME",
                          "Ext. Kum. Externalities": "Kumuliert"}
            for cn in EXT_CAT_NAMES:
                nice_names[f"Ext. {cn}"] = f"{EXT_CATEGORIES[cn]['icon']} {cn}"
            breakdown.rename(columns=nice_names, inplace=True)
            for c in breakdown.columns:
                if c not in ("Jahr", "Phase"):
                    breakdown[c] = breakdown[c].apply(lambda v: f"${_sf(v)/1e9:,.2f}B")
            st.dataframe(breakdown, width="stretch", hide_index=True)

        with st.expander(t('cum_gap_title', start=retro_start), expanded=False):
            schere_df = df[["Jahr", "Phase", "Ext. Kum. Externalities",
                              "Flynn Kum. Wertschoepfung", "Kum. Schere (abs)"]].copy()
            schere_df.columns = ["Jahr", "Phase", "Kum. Schuld (Extraktiv)",
                                 "Kum. Aufbau (Flynn)", "Schere"]
            for c in schere_df.columns:
                if c not in ("Jahr", "Phase"):
                    schere_df[c] = schere_df[c].apply(lambda v: f"${_sf(v)/1e9:,.2f}B")
            st.dataframe(schere_df, width="stretch", hide_index=True)

    with tab1:
        st.plotly_chart(chart_annual_comparison(df), width="stretch")
        st.caption(t("cap_annual"))

    with tab2:
        st.plotly_chart(chart_stock_prices(df), width="stretch")
        st.caption(t("cap_stocks"))

    with tab3:
        st.plotly_chart(chart_net_income(df), width="stretch")
        st.caption(t("cap_netincome"))

    with tab4:
        st.plotly_chart(chart_value_comparison(df), width="stretch")
        st.caption(t("cap_comparison"))

    with tab5:
        st.plotly_chart(chart_delta_bars(df), width="stretch")

    with tab6:
        st.plotly_chart(chart_indices_compare(df), width="stretch")
        st.markdown("##### {}".format(t("index_change_to", yr=int(final["Jahr"]))))
        c1, c2, c3 = st.columns(3)
        for cw, nm in [(c1, "EHI"), (c2, "HRI"), (c3, "IRI")]:
            with cw:
                st.metric(f"{nm} Extraktiv", f'{final[f"Ext. {nm}"]:.3f}',
                          f'{((final[f"Ext. {nm}"] / max(0.01, {"EHI": ehi_0, "HRI": hri_0, "IRI": iri_0}[nm])) - 1)*100:+,.0f}%')
                st.metric(f"{nm} Flynn", f'{final[f"Flynn {nm}"]:.3f}',
                          f'{((final[f"Flynn {nm}"] / max(0.01, {"EHI": ehi_0, "HRI": hri_0, "IRI": iri_0}[nm])) - 1)*100:+,.0f}%')

    with tab7:
        st.plotly_chart(chart_dialysis(df), width="stretch")
        st.caption(t("cap_dialysis"))
        st.markdown("---")
        st.plotly_chart(chart_metamorphose(df), width="stretch")
        st.caption(t("cap_metamorphose"))

    with tab8:
        with st.expander(t('data_table_title'), expanded=False):
            st.dataframe(df, width="stretch", height=500)
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(t("csv_export"), csv, "flynn_matrix_full.csv", "text/csv")

    # ── Mathematical Reference ──
    st.markdown("---")
    with st.expander(t("math_ref_title"), expanded=False):
        st.markdown(r"""
**50/50-Allokation:** $Q = 0.5 \cdot S$ wobei $S$ = kombinierter Nettogewinn aller 5 Asset Manager.

**Dialyse-Mechanismus:** $DR = DR_0 \cdot (1 - \beta \cdot \max(EHI, HRI)) \cdot IRI$

**Matrix ROI:** $\alpha = 1 + \gamma \cdot \frac{DR}{DR_0}$

**Matrix-Metamorphose:** $MQ = \alpha \cdot Q$

**Wellness-Monetarisierung:** $MW_{total} = MW_B + MW_H$, $MW_B = Q_B \cdot EHI \cdot 2.5$, $MW_H = Q_H \cdot HRI \cdot 2.5$

**Extraktive Externalitaeten (8 Kategorien, Revenue-basiert):**

| Kategorie | Formel | Index |
|-----------|--------|-------|
| Klima & CO₂ | $0.12 \cdot Rev \cdot (1-EHI)$ | EHI |
| Biodiversitaetsverlust | $0.06 \cdot Rev \cdot (1-EHI)$ | EHI |
| Wasser & Boden | $0.04 \cdot Rev \cdot (1-EHI)$ | EHI |
| Gesundheitsschaeden | $0.06 \cdot Rev \cdot (1-HRI)$ | HRI |
| Soziale Ungleichheit | $0.08 \cdot Rev \cdot (1-HRI)$ | HRI |
| Arbeitnehmerausbeutung | $0.04 \cdot Rev \cdot (1-HRI)$ | HRI |
| Systemisches Risiko | $0.07 \cdot Rev \cdot (1-IRI)$ | IRI |
| Regulat. Erfassung | $0.03 \cdot Rev \cdot (1-IRI)$ | IRI |

$$C_{ext} = \sum_{k=1}^{8} r_k \cdot Rev \cdot (1 - I_k)$$

Bei voller Degradation ($I=0$): $C_{ext} = 0.50 \cdot Rev$ — die Haelfte des gesamten Umsatzes!

**Kumulierte Wertvernichtung (NIE abgebaut):**
$$\Sigma_{ext} = \sum_{t=1}^{T} C_{ext,t}$$
Die Externalitaeten werden nicht "bezahlt" — sie akkumulieren als unsichtbare Schuld am System.

**Flynn Matrix Value:** $V_{Flynn} = S_{retained} + MQ + MW_{total}$

**Kumulierte Flynn-Wertschoepfung:**
$$\Sigma_{Flynn} = \sum_{t=1}^{T} [(MQ_t - Q_t) + MW_{total,t}]$$

**Systemschere:** $\Delta_{kum} = \Sigma_{ext} + \Sigma_{Flynn}$

**Extraktiver Wahrer Wert:** $V_{ext} = S - C_{ext}$
        """)

    st.markdown(
        "<p style='text-align:center; color:#3a5577; font-size:0.75rem; margin-top:40px;'>"
        + t("footer") + f" — {', '.join(TICKERS)}"
        "</p>", unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
