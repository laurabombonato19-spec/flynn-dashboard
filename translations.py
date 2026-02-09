#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Flynn 50/50 Matrix Dashboard — Internationalization (i18n)
7 Languages: EN (default), DE, IT, FR, ES, JA, ZH
"""

LANGUAGES = {
    "English":  "en",
    "Deutsch":  "de",
    "Italiano": "it",
    "Français": "fr",
    "Español":  "es",
    "日本語":    "ja",
    "中文":      "zh",
}

# ─── Master Translation Dictionary ──────────────────────────────────────────
# Keys are short identifiers, values are dicts per language code.

T = {
    # ═══════════════════════ HEADER / GENERAL ═══════════════════════
    "subtitle": {
        "en": "C-Level Comparison: Extractive Capitalism vs. Regenerative Economy<br>"
              "Top 5 Asset Managers — 30 Years Legacy Debt (1996–2025) + Flynn Future Projection",
        "de": "C-Level Gegenstellung: Extraktiver Kapitalismus vs. Regenerative Oekonomie<br>"
              "Top 5 Asset Manager — 30 Jahre Altlasten (1996–2025) + Flynn-Zukunftsprojektion",
        "it": "Confronto C-Level: Capitalismo Estrattivo vs. Economia Rigenerativa<br>"
              "Top 5 Gestori Patrimoniali — 30 Anni di Debito Ereditato (1996–2025) + Proiezione Flynn",
        "fr": "Comparaison C-Level : Capitalisme Extractif vs. Économie Régénérative<br>"
              "Top 5 Gestionnaires d'Actifs — 30 Ans de Dette Héritée (1996–2025) + Projection Flynn",
        "es": "Comparación C-Level: Capitalismo Extractivo vs. Economía Regenerativa<br>"
              "Top 5 Gestores de Activos — 30 Años de Deuda Heredada (1996–2025) + Proyección Flynn",
        "ja": "C-レベル比較：採取型資本主義 vs. 再生型経済<br>"
              "トップ5資産運用会社 — 30年間の遺産債務（1996–2025） + フリン将来予測",
        "zh": "C级对比：攫取型资本主义 vs. 再生型经济<br>"
              "前5大资产管理公司 — 30年遗留债务（1996–2025）+ Flynn未来预测",
    },
    "loading_data": {
        "en": "Loading historical market data",
        "de": "Lade historische Boersendaten",
        "it": "Caricamento dati storici di borsa",
        "fr": "Chargement des données boursières historiques",
        "es": "Cargando datos históricos del mercado",
        "ja": "過去の市場データを読み込み中",
        "zh": "正在加载历史市场数据",
    },

    # ═══════════════════════ SIDEBAR ═══════════════════════
    "sidebar_params": {
        "en": "Scenario Parameters",
        "de": "Szenario-Parameter",
        "it": "Parametri dello Scenario",
        "fr": "Paramètres du Scénario",
        "es": "Parámetros del Escenario",
        "ja": "シナリオパラメータ",
        "zh": "情景参数",
    },
    "sidebar_hint": {
        "en": "Move sliders = instant update",
        "de": "Regler verschieben = Sofort-Update",
        "it": "Sposta i cursori = aggiornamento immediato",
        "fr": "Déplacez les curseurs = mise à jour instantanée",
        "es": "Mover deslizadores = actualización instantánea",
        "ja": "スライダー移動 = 即時更新",
        "zh": "移动滑块 = 即时更新",
    },
    "sidebar_flynn": {
        "en": "Flynn Model",
        "de": "Flynn-Modell",
        "it": "Modello Flynn",
        "fr": "Modèle Flynn",
        "es": "Modelo Flynn",
        "ja": "Flynnモデル",
        "zh": "Flynn模型",
    },
    "gamma_label": {
        "en": "gamma — Value Creation Factor",
        "de": "gamma — Value Creation Factor",
        "it": "gamma — Fattore di Creazione di Valore",
        "fr": "gamma — Facteur de Création de Valeur",
        "es": "gamma — Factor de Creación de Valor",
        "ja": "gamma — 価値創造係数",
        "zh": "gamma — 价值创造因子",
    },
    "gamma_help": {
        "en": "Alpha multiplier. Higher = stronger Matrix leverage.",
        "de": "Multiplikator alpha. Hoeher = staerkerer Matrix-Hebel.",
        "it": "Moltiplicatore alpha. Più alto = leva Matrix più forte.",
        "fr": "Multiplicateur alpha. Plus élevé = levier Matrix plus fort.",
        "es": "Multiplicador alpha. Mayor = mayor apalancamiento Matrix.",
        "ja": "アルファ乗数。高い = マトリックスレバレッジが強い。",
        "zh": "Alpha乘数。越高 = 矩阵杠杆越强。",
    },
    "dr0_label": {
        "en": "DR0 — Base Dialysis Rate",
        "de": "DR0 — Basis-Dialyse-Rate",
        "it": "DR0 — Tasso Base di Dialisi",
        "fr": "DR0 — Taux de Dialyse de Base",
        "es": "DR0 — Tasa Base de Diálisis",
        "ja": "DR0 — 基本透析率",
        "zh": "DR0 — 基础透析率",
    },
    "dr0_help": {
        "en": "Base rate of capital transformation.",
        "de": "Basis-Rate der Kapital-Transformation.",
        "it": "Tasso base della trasformazione del capitale.",
        "fr": "Taux de base de la transformation du capital.",
        "es": "Tasa base de transformación del capital.",
        "ja": "資本変換の基本レート。",
        "zh": "资本转型基础率。",
    },
    "beta_label": {
        "en": "beta — Feedback Dampening",
        "de": "beta — Feedback-Daempfung",
        "it": "beta — Smorzamento Feedback",
        "fr": "beta — Amortissement du Feedback",
        "es": "beta — Amortiguación de Feedback",
        "ja": "beta — フィードバック減衰",
        "zh": "beta — 反馈阻尼",
    },
    "beta_help": {
        "en": "How strongly rising indices throttle the DR.",
        "de": "Wie stark steigende Indizes die DR drosseln.",
        "it": "Quanto gli indici in crescita frenano il DR.",
        "fr": "À quel point les indices croissants freinent le DR.",
        "es": "Cuánto los índices crecientes frenan el DR.",
        "ja": "上昇するインデックスがDRをどれだけ抑制するか。",
        "zh": "上升指数对DR的抑制程度。",
    },
    "sidebar_indices": {
        "en": "Index Starting Values (today)",
        "de": "Index-Startwerte (heute)",
        "it": "Valori Iniziali degli Indici (oggi)",
        "fr": "Valeurs Initiales des Indices (aujourd'hui)",
        "es": "Valores Iniciales de los Índices (hoy)",
        "ja": "インデックス初期値（現在）",
        "zh": "指数初始值（今天）",
    },
    "ehi_label": {
        "en": "EHI0 — Ecological Health",
        "de": "EHI0 — Ecological Health",
        "it": "EHI0 — Salute Ecologica",
        "fr": "EHI0 — Santé Écologique",
        "es": "EHI0 — Salud Ecológica",
        "ja": "EHI0 — 生態系健全性",
        "zh": "EHI0 — 生态健康",
    },
    "hri_label": {
        "en": "HRI0 — Human Resilience",
        "de": "HRI0 — Human Resilience",
        "it": "HRI0 — Resilienza Umana",
        "fr": "HRI0 — Résilience Humaine",
        "es": "HRI0 — Resiliencia Humana",
        "ja": "HRI0 — 人的レジリエンス",
        "zh": "HRI0 — 人类韧性",
    },
    "iri_label": {
        "en": "IRI0 — Integrity",
        "de": "IRI0 — Integrity",
        "it": "IRI0 — Integrità",
        "fr": "IRI0 — Intégrité",
        "es": "IRI0 — Integridad",
        "ja": "IRI0 — 整合性",
        "zh": "IRI0 — 完整性",
    },
    "sidebar_alloc": {
        "en": "Allocation",
        "de": "Allokation",
        "it": "Allocazione",
        "fr": "Allocation",
        "es": "Asignación",
        "ja": "配分",
        "zh": "配置",
    },
    "bio_share": {
        "en": "Biosphere share of Q",
        "de": "Biosphaere-Anteil von Q",
        "it": "Quota biosfera di Q",
        "fr": "Part biosphère de Q",
        "es": "Participación biosfera de Q",
        "ja": "Qの生物圏割合",
        "zh": "Q的生物圈份额",
    },
    "sidebar_extract": {
        "en": "Extractive System",
        "de": "Extraktives System",
        "it": "Sistema Estrattivo",
        "fr": "Système Extractif",
        "es": "Sistema Extractivo",
        "ja": "採取型システム",
        "zh": "攫取型系统",
    },
    "degrad_label": {
        "en": "Annual Index Degradation",
        "de": "Jaehrl. Index-Degradation",
        "it": "Degradazione Annuale Indice",
        "fr": "Dégradation Annuelle de l'Indice",
        "es": "Degradación Anual del Índice",
        "ja": "年間指数劣化率",
        "zh": "年度指数退化",
    },
    "degrad_help": {
        "en": "Annual deterioration under status quo.",
        "de": "Jaerl. Verschlechterung unter Status Quo.",
        "it": "Deterioramento annuale sotto lo status quo.",
        "fr": "Détérioration annuelle sous le statu quo.",
        "es": "Deterioro anual bajo el statu quo.",
        "ja": "現状維持下の年間悪化率。",
        "zh": "维持现状下的年度恶化率。",
    },
    "growth_label": {
        "en": "Annual Surplus Growth",
        "de": "Jaehrl. Surplus-Wachstum",
        "it": "Crescita Annuale del Surplus",
        "fr": "Croissance Annuelle du Surplus",
        "es": "Crecimiento Anual del Superávit",
        "ja": "年間剰余成長率",
        "zh": "年度盈余增长",
    },
    "proj_years_label": {
        "en": "Projection Period (years)",
        "de": "Projektionszeitraum (Jahre)",
        "it": "Periodo di Proiezione (anni)",
        "fr": "Période de Projection (années)",
        "es": "Período de Proyección (años)",
        "ja": "予測期間（年）",
        "zh": "预测期（年）",
    },
    "language": {
        "en": "Language",
        "de": "Sprache",
        "it": "Lingua",
        "fr": "Langue",
        "es": "Idioma",
        "ja": "言語",
        "zh": "语言",
    },

    # ═══════════════════════ LIVE DATA ═══════════════════════
    "live_data_title": {
        "en": "Real Market Data — Top {n} Asset Managers",
        "de": "Echte Boersendaten — Top {n} Asset Manager",
        "it": "Dati Reali di Borsa — Top {n} Gestori Patrimoniali",
        "fr": "Données Boursières Réelles — Top {n} Gestionnaires d'Actifs",
        "es": "Datos Reales del Mercado — Top {n} Gestores de Activos",
        "ja": "実際の市場データ — トップ{n}資産運用会社",
        "zh": "真实市场数据 — 前{n}大资产管理公司",
    },
    "combined_ni": {
        "en": "Combined Net Income",
        "de": "Komb. Net Income",
        "it": "Utile Netto Combinato",
        "fr": "Résultat Net Combiné",
        "es": "Ingreso Neto Combinado",
        "ja": "合計純利益",
        "zh": "合计净利润",
    },

    # ═══════════════════════ CANCER BOX ═══════════════════════
    "cancer_title": {
        "en": "30 Years Legacy Debt — 8 Externality Categories (Revenue-based)",
        "de": "30 Jahre Altlasten &mdash; 8 Externality-Kategorien (Revenue-basiert)",
        "it": "30 Anni di Debito Ereditato &mdash; 8 Categorie di Esternalità (basate sui ricavi)",
        "fr": "30 Ans de Dette Héritée &mdash; 8 Catégories d'Externalités (basées sur le chiffre d'affaires)",
        "es": "30 Años de Deuda Heredada &mdash; 8 Categorías de Externalidades (basadas en ingresos)",
        "ja": "30年間の遺産債務 &mdash; 8つの外部性カテゴリ（収益ベース）",
        "zh": "30年遗留债务 &mdash; 8个外部性类别（基于收入）",
    },
    "cancer_desc": {
        "en": "Since 1996, climate, biodiversity, water, health, inequality, exploitation, "
              "systemic risk, and regulation have accumulated — based on TOTAL revenue. "
              "This debt was NEVER settled. Flynn starts TODAY against this legacy.",
        "de": "Seit 1996 akkumulieren Klima, Biodiversitaet, Wasser, Gesundheit, Ungleichheit, "
              "Ausbeutung, Systemrisiko, Regulierung &mdash; basiert auf dem GESAMTEN Umsatz. "
              "Diese Schuld wurde NIE beglichen. Flynn startet ab heute GEGEN diese Altlast.",
        "it": "Dal 1996 si accumulano clima, biodiversità, acqua, salute, disuguaglianza, sfruttamento, "
              "rischio sistemico e regolamentazione — basati sul fatturato TOTALE. "
              "Questo debito non è MAI stato saldato. Flynn parte OGGI contro questa eredità.",
        "fr": "Depuis 1996, climat, biodiversité, eau, santé, inégalité, exploitation, "
              "risque systémique et réglementation s'accumulent — basés sur le chiffre d'affaires TOTAL. "
              "Cette dette n'a JAMAIS été réglée. Flynn démarre AUJOURD'HUI contre cet héritage.",
        "es": "Desde 1996 se acumulan clima, biodiversidad, agua, salud, desigualdad, explotación, "
              "riesgo sistémico y regulación — basados en los ingresos TOTALES. "
              "Esta deuda NUNCA se saldó. Flynn comienza HOY contra esta herencia.",
        "ja": "1996年以来、気候、生物多様性、水、健康、不平等、搾取、"
              "システミックリスク、規制が蓄積 — 総収益に基づく。"
              "この負債は決して清算されていない。Flynnは今日、この遺産に対抗して始まる。",
        "zh": "自1996年以来，气候、生物多样性、水资源、健康、不平等、剥削、"
              "系统性风险和监管持续累积——基于总收入。"
              "这笔债务从未清偿。Flynn从今天开始对抗这一遗产。",
    },

    # ═══════════════════════ KPI LABELS ═══════════════════════
    "legacy_debt": {
        "en": "Legacy Debt {start}–{end}",
        "de": "Altlast {start}–{end}",
        "it": "Debito Ereditato {start}–{end}",
        "fr": "Dette Héritée {start}–{end}",
        "es": "Deuda Heredada {start}–{end}",
        "ja": "遺産債務 {start}–{end}",
        "zh": "遗留债务 {start}–{end}",
    },
    "years_before_flynn": {
        "en": "{n} years BEFORE Flynn!",
        "de": "{n} Jahre VOR Flynn!",
        "it": "{n} anni PRIMA di Flynn!",
        "fr": "{n} ans AVANT Flynn !",
        "es": "¡{n} años ANTES de Flynn!",
        "ja": "Flynn開始{n}年前！",
        "zh": "Flynn之前{n}年！",
    },
    "cum_destruction_total": {
        "en": "Cum. Value Destruction (TOTAL)",
        "de": "Kum. Wertvernichtung (GESAMT)",
        "it": "Distruzione di Valore Cum. (TOTALE)",
        "fr": "Destruction de Valeur Cum. (TOTAL)",
        "es": "Destrucción de Valor Acum. (TOTAL)",
        "ja": "累積価値破壊（合計）",
        "zh": "累计价值毁灭（总计）",
    },
    "years_total": {
        "en": "{start}–{end} ({n} years!)",
        "de": "{start}–{end} ({n} Jahre!)",
        "it": "{start}–{end} ({n} anni!)",
        "fr": "{start}–{end} ({n} ans !)",
        "es": "{start}–{end} (¡{n} años!)",
        "ja": "{start}–{end}（{n}年！）",
        "zh": "{start}–{end}（{n}年！）",
    },
    "cum_creation_flynn": {
        "en": "Cum. Value Creation (Flynn)",
        "de": "Kum. Wertschoepfung (Flynn)",
        "it": "Creazione di Valore Cum. (Flynn)",
        "fr": "Création de Valeur Cum. (Flynn)",
        "es": "Creación de Valor Acum. (Flynn)",
        "ja": "累積価値創造（Flynn）",
        "zh": "累计价值创造（Flynn）",
    },
    "from_year_regen": {
        "en": "From {yr} — Regenerative",
        "de": "Ab {yr} — Regenerativ",
        "it": "Da {yr} — Rigenerativo",
        "fr": "À partir de {yr} — Régénératif",
        "es": "Desde {yr} — Regenerativo",
        "ja": "{yr}年から — 再生型",
        "zh": "自{yr}年 — 再生型",
    },
    "system_gap": {
        "en": "System Gap (Total)",
        "de": "Systemschere (Gesamt)",
        "it": "Divario Sistemico (Totale)",
        "fr": "Écart Systémique (Total)",
        "es": "Brecha Sistémica (Total)",
        "ja": "システムギャップ（合計）",
        "zh": "系统差距（总计）",
    },
    "gap_between_systems": {
        "en": "Gap between the systems",
        "de": "Kluft zwischen den Systemen",
        "it": "Divario tra i sistemi",
        "fr": "Écart entre les systèmes",
        "es": "Brecha entre los sistemas",
        "ja": "システム間のギャップ",
        "zh": "系统间差距",
    },
    "ext_only_year": {
        "en": "Externalities ONLY {yr}",
        "de": "Externalitaeten NUR {yr}",
        "it": "Esternalità SOLO {yr}",
        "fr": "Externalités SEULEMENT {yr}",
        "es": "Externalidades SOLO {yr}",
        "ja": "外部性（{yr}年のみ）",
        "zh": "外部性（仅{yr}年）",
    },
    "per_year_rising": {
        "en": "Per year — and rising!",
        "de": "Pro Jahr — und steigend!",
        "it": "All'anno — e in crescita!",
        "fr": "Par an — et en hausse !",
        "es": "¡Por año — y en aumento!",
        "ja": "年間 — そして増加中！",
        "zh": "每年——且在上升！",
    },

    # ═══════════════════════ PROJECTION RESULTS ═══════════════════════
    "result_title": {
        "en": "Result {start} – {end} — System Comparison",
        "de": "Ergebnis {start} – {end} — Systemvergleich",
        "it": "Risultato {start} – {end} — Confronto Sistemico",
        "fr": "Résultat {start} – {end} — Comparaison Systémique",
        "es": "Resultado {start} – {end} — Comparación Sistémica",
        "ja": "結果 {start} – {end} — システム比較",
        "zh": "结果 {start} – {end} — 系统比较",
    },
    "extractive_true": {
        "en": "Extractive (true value)",
        "de": "Extraktiv (wahrer Wert)",
        "it": "Estrattivo (valore reale)",
        "fr": "Extractif (valeur réelle)",
        "es": "Extractivo (valor real)",
        "ja": "採取型（真の価値）",
        "zh": "攫取型（真实价值）",
    },
    "flynn_advantage": {
        "en": "Flynn Advantage (vs. Gross)",
        "de": "Flynn-Vorteil (vs. Brutto)",
        "it": "Vantaggio Flynn (vs. Lordo)",
        "fr": "Avantage Flynn (vs. Brut)",
        "es": "Ventaja Flynn (vs. Bruto)",
        "ja": "Flynn優位性（vs. 総額）",
        "zh": "Flynn优势（vs. 总额）",
    },
    "cum_externalities": {
        "en": "Cum. Externalities",
        "de": "Kum. Externalitaeten",
        "it": "Esternalità Cum.",
        "fr": "Externalités Cum.",
        "es": "Externalidades Acum.",
        "ja": "累積外部性",
        "zh": "累计外部性",
    },
    "never_repaid": {
        "en": "Never repaid!",
        "de": "Nie abgebaut!",
        "it": "Mai ripagato!",
        "fr": "Jamais remboursé !",
        "es": "¡Nunca pagado!",
        "ja": "返済されず！",
        "zh": "从未偿还！",
    },

    # ═══════════════════════ TAB NAMES ═══════════════════════
    "tab_cum_destruction": {
        "en": "Cum. Destruction",
        "de": "Kum. Zerstoerung",
        "it": "Distruz. Cum.",
        "fr": "Destruct. Cum.",
        "es": "Destruc. Acum.",
        "ja": "累積破壊",
        "zh": "累计毁灭",
    },
    "tab_annual": {
        "en": "Annual Balance",
        "de": "Jaehrl. Bilanz",
        "it": "Bilancio Annuale",
        "fr": "Bilan Annuel",
        "es": "Balance Anual",
        "ja": "年間収支",
        "zh": "年度收支",
    },
    "tab_stocks": {
        "en": "Stock Prices",
        "de": "Aktienkurse",
        "it": "Prezzi Azionari",
        "fr": "Cours Boursiers",
        "es": "Precios de Acciones",
        "ja": "株価",
        "zh": "股票价格",
    },
    "tab_netincome": {
        "en": "Net Income",
        "de": "Nettogewinn",
        "it": "Utile Netto",
        "fr": "Résultat Net",
        "es": "Ingreso Neto",
        "ja": "純利益",
        "zh": "净利润",
    },
    "tab_comparison": {
        "en": "Value Comparison",
        "de": "Wertvergleich",
        "it": "Confronto Valore",
        "fr": "Comparaison Valeur",
        "es": "Comparación Valor",
        "ja": "価値比較",
        "zh": "价值比较",
    },
    "tab_flynn_pct": {
        "en": "Flynn Advantage %",
        "de": "Flynn-Vorteil %",
        "it": "Vantaggio Flynn %",
        "fr": "Avantage Flynn %",
        "es": "Ventaja Flynn %",
        "ja": "Flynn優位性%",
        "zh": "Flynn优势%",
    },
    "tab_indices": {
        "en": "Index Comparison",
        "de": "Index-Vergleich",
        "it": "Confronto Indici",
        "fr": "Comparaison Indices",
        "es": "Comparación Índices",
        "ja": "指数比較",
        "zh": "指数比较",
    },
    "tab_dialysis": {
        "en": "Dialysis & Metamorphosis",
        "de": "Dialyse & Metamorphose",
        "it": "Dialisi & Metamorfosi",
        "fr": "Dialyse & Métamorphose",
        "es": "Diálisis & Metamorfosis",
        "ja": "透析＆変態",
        "zh": "透析与蜕变",
    },
    "tab_data": {
        "en": "Data Table",
        "de": "Datentabelle",
        "it": "Tabella Dati",
        "fr": "Tableau de Données",
        "es": "Tabla de Datos",
        "ja": "データテーブル",
        "zh": "数据表",
    },

    # ═══════════════════════ CHART TITLES & CAPTIONS ═══════════════════════
    "chart_cum_title": {
        "en": "1996–Future: 30 Years Cumulative Value Destruction vs. Flynn (from today)",
        "de": "1996–Zukunft: 30 Jahre Kumulierte Wertvernichtung vs. Flynn (ab heute)",
        "it": "1996–Futuro: 30 Anni Distruzione Cumulativa vs. Flynn (da oggi)",
        "fr": "1996–Futur : 30 Ans Destruction Cumulative vs. Flynn (à partir d'aujourd'hui)",
        "es": "1996–Futuro: 30 Años Destrucción Acumulada vs. Flynn (desde hoy)",
        "ja": "1996–将来：30年間の累積価値破壊 vs. Flynn（今日から）",
        "zh": "1996–未来：30年累计价值毁灭 vs. Flynn（从今天起）",
    },
    "cap_cum_destruction": {
        "en": "FROM 1996: 30 years externalities accumulate (stacked below zero). "
              "Blue dotted line = real data from {yr}. Green dashed line = Flynn starts. "
              "The 30-YEAR legacy was ALREADY THERE before Flynn even begins!",
        "de": "AB 1996: 30 Jahre Externalitäten akkumulieren (gestapelt unter Null). "
              "Blaue gepunktete Linie = echte Daten ab {yr}. "
              "Grüne gestrichelte Linie = Flynn startet. "
              "Die Altlast von 30 JAHREN war SCHON DA bevor Flynn überhaupt beginnt!",
        "it": "DAL 1996: 30 anni di esternalità si accumulano (impilate sotto zero). "
              "Linea blu tratteggiata = dati reali da {yr}. Linea verde tratteggiata = Flynn inizia. "
              "Il debito di 30 ANNI c'era GIÀ prima che Flynn cominci!",
        "fr": "DEPUIS 1996 : 30 ans d'externalités s'accumulent (empilées sous zéro). "
              "Ligne bleue pointillée = données réelles depuis {yr}. Ligne verte = Flynn démarre. "
              "La dette de 30 ANS était DÉJÀ LÀ avant que Flynn ne commence !",
        "es": "DESDE 1996: 30 años de externalidades se acumulan (apiladas bajo cero). "
              "Línea azul punteada = datos reales desde {yr}. Línea verde = Flynn comienza. "
              "¡La deuda de 30 AÑOS YA ESTABA antes de que Flynn comience!",
        "ja": "1996年から：30年間の外部性が蓄積（ゼロ以下に積み重ね）。"
              "青点線 = {yr}年からの実データ。緑破線 = Flynn開始。"
              "30年間の遺産債務はFlynnが始まる前から既に存在していた！",
        "zh": "自1996年：30年外部性积累（零线以下堆叠）。"
              "蓝色虚线 = 自{yr}年的真实数据。绿色虚线 = Flynn启动。"
              "30年的遗留债务在Flynn开始之前就已经存在！",
    },
    "cap_annual": {
        "en": "FULL Timeline 1996–Future: 30 years 8 categories stacked (below zero) vs. Flynn (above zero). "
              "Green line = Flynn starts. LEFT: ONLY destruction over decades. "
              "RIGHT: Flynn begins building, but costs continue.",
        "de": "VOLLE Timeline 1996–Zukunft: 30 Jahre 8 Kategorien gestapelt (unter Null) vs. Flynn (ueber Null). "
              "Grüne Linie = Flynn startet. LINKS davon: NUR Zerstörung über Jahrzehnte. "
              "RECHTS: Flynn beginnt aufzubauen, aber die Kosten laufen weiter.",
        "it": "Timeline COMPLETA 1996–Futuro: 30 anni 8 categorie impilate (sotto zero) vs. Flynn (sopra zero). "
              "Linea verde = Flynn inizia. SINISTRA: SOLO distruzione per decenni. "
              "DESTRA: Flynn inizia a costruire, ma i costi continuano.",
        "fr": "Timeline COMPLÈTE 1996–Futur : 30 ans 8 catégories empilées (sous zéro) vs. Flynn (au-dessus de zéro). "
              "Ligne verte = Flynn démarre. GAUCHE : UNIQUEMENT destruction pendant des décennies. "
              "DROITE : Flynn commence à construire, mais les coûts continuent.",
        "es": "Timeline COMPLETA 1996–Futuro: 30 años 8 categorías apiladas (bajo cero) vs. Flynn (sobre cero). "
              "Línea verde = Flynn comienza. IZQUIERDA: SOLO destrucción durante décadas. "
              "DERECHA: Flynn comienza a construir, pero los costos continúan.",
        "ja": "完全タイムライン 1996–将来：30年間8カテゴリ（ゼロ以下に積み重ね）vs Flynn（ゼロ以上）。"
              "緑線 = Flynn開始。左側：数十年間の破壊のみ。右側：Flynn建設開始、しかしコストは継続。",
        "zh": "完整时间线 1996–未来：30年8个类别堆叠（零以下）vs Flynn（零以上）。"
              "绿线 = Flynn启动。左侧：数十年仅有破坏。右侧：Flynn开始建设，但成本仍在继续。",
    },
    "cap_stocks": {
        "en": "Historical quarterly closing prices via yfinance. Projection based on surplus growth rate.",
        "de": "Historische Quartalsschlusskurse via yfinance. Projektion basiert auf Surplus-Wachstumsrate.",
        "it": "Prezzi di chiusura trimestrali storici via yfinance. Proiezione basata sul tasso di crescita del surplus.",
        "fr": "Prix de clôture trimestriels historiques via yfinance. Projection basée sur le taux de croissance du surplus.",
        "es": "Precios de cierre trimestrales históricos via yfinance. Proyección basada en la tasa de crecimiento del superávit.",
        "ja": "yfinanceによる過去の四半期終値。剰余成長率に基づく予測。",
        "zh": "通过yfinance获取的历史季度收盘价。基于盈余增长率的预测。",
    },
    "cap_netincome": {
        "en": "Real annual financial statements (Income Statement) + projection.",
        "de": "Reale Jahresabschluesse (Income Statement) + Projektion.",
        "it": "Bilanci annuali reali (Conto Economico) + proiezione.",
        "fr": "Comptes annuels réels (Compte de Résultat) + projection.",
        "es": "Estados financieros anuales reales (Estado de Resultados) + proyección.",
        "ja": "実際の年次決算書（損益計算書）+ 予測。",
        "zh": "真实年度财务报表（利润表）+ 预测。",
    },
    "cap_comparison": {
        "en": "Dashed = Gross illusion. Red = true value after externalities. "
              "Green = Flynn Matrix Value (Retained + Matrix Metamorphosis + Wellness). "
              "Red dash-dotted = CUMULATIVE system debt since 1996 (far negative!). "
              "The real system value is MASSIVELY negative — annual values near zero are deceptive!",
        "de": "Gestrichelt = Brutto-Illusion. Rot = wahrer Wert nach Externalitaeten. "
              "Gruen = Flynn Matrix Value (Retained + Matrix-Metamorphose + Wellness). "
              "Rot-strichpunktiert = KUMULIERTE Systemschuld seit 1996 (weit im Minus!). "
              "Der wahre Systemwert ist MASSIV negativ — die jaehrlichen Werte nahe Null taeuschen!",
        "it": "Tratteggiato = Illusione lorda. Rosso = valore reale dopo esternalità. "
              "Verde = Flynn Matrix Value (Mantenuto + Metamorfosi + Wellness). "
              "Rosso trattopunto = Debito sistemico CUMULATO dal 1996 (molto negativo!). "
              "Il valore reale del sistema è MASSIVAMENTE negativo — i valori annuali vicini allo zero ingannano!",
        "fr": "Pointillé = Illusion brute. Rouge = valeur réelle après externalités. "
              "Vert = Flynn Matrix Value (Retenu + Métamorphose + Wellness). "
              "Rouge mixte = Dette systémique CUMULÉE depuis 1996 (très négatif !). "
              "La valeur réelle du système est MASSIVEMENT négative — les valeurs annuelles proches de zéro trompent !",
        "es": "Discontinua = Ilusión bruta. Rojo = valor real tras externalidades. "
              "Verde = Flynn Matrix Value (Retenido + Metamorfosis + Wellness). "
              "Rojo mixta = Deuda sistémica ACUMULADA desde 1996 (¡muy negativa!). "
              "¡El valor real del sistema es MASIVAMENTE negativo — los valores anuales cercanos a cero engañan!",
        "ja": "破線 = 総額の幻想。赤 = 外部性後の真の価値。"
              "緑 = Flynn Matrix Value（保留 + マトリックス変態 + ウェルネス）。"
              "赤一点鎖線 = 1996年以降の累積システム負債（大幅にマイナス！）。"
              "実際のシステム価値は大幅にマイナス — ゼロ付近の年間値は欺瞞的！",
        "zh": "虚线 = 总额幻象。红色 = 外部性后的真实价值。"
              "绿色 = Flynn矩阵价值（保留 + 矩阵蜕变 + 健康）。"
              "红色点划线 = 自1996年以来的累计系统债务（远低于零！）。"
              "真实系统价值为大幅负值——接近零的年度值具有欺骗性！",
    },
    "cap_dialysis": {
        "en": "BELOW ZERO = Destruction (Externalities). Red = extractive (growing), "
              "Orange = Flynn residual externalities (shrinking → 0). "
              "ABOVE ZERO = Restoration (Flynn building). "
              "Yellow line = Net balance per year. "
              "Equilibrium (y=0) = Flynn building fully compensates residual externalities!",
        "de": "UNTER NULL = Zerstörung (Externalitäten). Rot = extraktiv (wachsend), "
              "Orange = Flynn-Restexternalitäten (sinkend → 0). "
              "ÜBER NULL = Wiederherstellung (Flynn Aufbau). "
              "Gelbe Linie = Netto-Bilanz pro Jahr. "
              "Gleichgewicht (y=0) = Flynn-Aufbau kompensiert Rest-Externalitäten vollständig!",
        "it": "SOTTO ZERO = Distruzione (Esternalità). Rosso = estrattivo (in crescita), "
              "Arancione = Esternalità residue Flynn (in calo → 0). "
              "SOPRA ZERO = Ripristino (Costruzione Flynn). "
              "Linea gialla = Bilancio netto annuale. "
              "Equilibrio (y=0) = Costruzione Flynn compensa completamente le esternalità residue!",
        "fr": "SOUS ZÉRO = Destruction (Externalités). Rouge = extractif (croissant), "
              "Orange = Externalités résiduelles Flynn (décroissant → 0). "
              "AU-DESSUS DE ZÉRO = Restauration (Construction Flynn). "
              "Ligne jaune = Bilan net annuel. "
              "Équilibre (y=0) = La construction Flynn compense entièrement les externalités résiduelles !",
        "es": "BAJO CERO = Destrucción (Externalidades). Rojo = extractivo (creciente), "
              "Naranja = Externalidades residuales Flynn (decrecientes → 0). "
              "SOBRE CERO = Restauración (Construcción Flynn). "
              "Línea amarilla = Balance neto anual. "
              "¡Equilibrio (y=0) = La construcción Flynn compensa completamente las externalidades residuales!",
        "ja": "ゼロ以下 = 破壊（外部性）。赤 = 採取型（増加中）、"
              "オレンジ = Flynn残余外部性（減少 → 0）。"
              "ゼロ以上 = 復元（Flynn構築）。"
              "黄色線 = 年間純収支。"
              "均衡（y=0）= Flynn構築が残余外部性を完全に補償！",
        "zh": "零以下 = 破坏（外部性）。红色 = 攫取型（增长中），"
              "橙色 = Flynn残余外部性（下降 → 0）。"
              "零以上 = 恢复（Flynn建设）。"
              "黄线 = 年度净平衡。"
              "均衡（y=0）= Flynn建设完全补偿残余外部性！",
    },
    "cap_metamorphose": {
        "en": "Cumulative balance: Red = accumulated system debt since 1996. "
              "Green = Cumulative Flynn value creation. "
              "Yellow line = Net system balance — Equilibrium when balance = 0.",
        "de": "Kumulative Bilanz: Rot = aufgelaufene Systemschuld seit 1996. "
              "Grün = Kumulierte Flynn-Wertschöpfung. "
              "Gelbe Linie = Netto-Systemsaldo — Gleichgewicht wenn Saldo = 0.",
        "it": "Bilancio cumulativo: Rosso = debito di sistema accumulato dal 1996. "
              "Verde = Creazione di valore Flynn cumulata. "
              "Linea gialla = Saldo netto del sistema — Equilibrio quando saldo = 0.",
        "fr": "Bilan cumulatif : Rouge = dette systémique accumulée depuis 1996. "
              "Vert = Création de valeur Flynn cumulée. "
              "Ligne jaune = Solde net du système — Équilibre quand solde = 0.",
        "es": "Balance acumulativo: Rojo = deuda sistémica acumulada desde 1996. "
              "Verde = Creación de valor Flynn acumulada. "
              "Línea amarilla = Saldo neto del sistema — Equilibrio cuando saldo = 0.",
        "ja": "累積収支：赤 = 1996年以降の累積システム負債。"
              "緑 = 累積Flynn価値創造。"
              "黄色線 = 純システム残高 — 残高 = 0で均衡。",
        "zh": "累计收支：红色 = 自1996年以来累积的系统债务。"
              "绿色 = 累计Flynn价值创造。"
              "黄线 = 净系统余额——余额 = 0时达到均衡。",
    },
    "data_table_title": {
        "en": "Complete Simulation Data",
        "de": "Komplette Simulationsdaten",
        "it": "Dati Completi della Simulazione",
        "fr": "Données Complètes de Simulation",
        "es": "Datos Completos de Simulación",
        "ja": "完全シミュレーションデータ",
        "zh": "完整模拟数据",
    },
    "csv_export": {
        "en": "CSV Export",
        "de": "CSV Export",
        "it": "Esporta CSV",
        "fr": "Export CSV",
        "es": "Exportar CSV",
        "ja": "CSVエクスポート",
        "zh": "CSV导出",
    },
    "math_ref_title": {
        "en": "Mathematical Framework — Reference",
        "de": "Mathematisches Regelwerk — Referenz",
        "it": "Quadro Matematico — Riferimento",
        "fr": "Cadre Mathématique — Référence",
        "es": "Marco Matemático — Referencia",
        "ja": "数学的フレームワーク — 参照",
        "zh": "数学框架 — 参考",
    },
    "footer": {
        "en": "Flynn 50/50 Matrix Dashboard | Societal Business Think Tank | Data source: yfinance",
        "de": "Flynn 50/50 Matrix Dashboard | Societal Business Think Tank | Datenquelle: yfinance",
        "it": "Flynn 50/50 Matrix Dashboard | Societal Business Think Tank | Fonte dati: yfinance",
        "fr": "Flynn 50/50 Matrix Dashboard | Societal Business Think Tank | Source : yfinance",
        "es": "Flynn 50/50 Matrix Dashboard | Societal Business Think Tank | Fuente: yfinance",
        "ja": "Flynn 50/50 Matrix Dashboard | Societal Business Think Tank | データソース：yfinance",
        "zh": "Flynn 50/50 Matrix Dashboard | Societal Business Think Tank | 数据来源：yfinance",
    },

    # ═══════════════════════ CHART INTERNALS ═══════════════════════
    "year": {
        "en": "Year", "de": "Jahr", "it": "Anno", "fr": "Année", "es": "Año", "ja": "年", "zh": "年",
    },
    "cumulated_value": {
        "en": "Cumulated Value (USD)", "de": "Kumulierter Wert (USD)",
        "it": "Valore Cumulato (USD)", "fr": "Valeur Cumulée (USD)",
        "es": "Valor Acumulado (USD)", "ja": "累積価値（USD）", "zh": "累计价值（USD）",
    },
    "system_value": {
        "en": "System Value (USD)", "de": "Systemwert (USD)",
        "it": "Valore del Sistema (USD)", "fr": "Valeur du Système (USD)",
        "es": "Valor del Sistema (USD)", "ja": "システム価値（USD）", "zh": "系统价值（USD）",
    },
    "annual_balance": {
        "en": "Annual Balance (Bn USD)", "de": "Jährl. Bilanz (Mrd. USD)",
        "it": "Bilancio Annuale (Mld USD)", "fr": "Bilan Annuel (Mrd USD)",
        "es": "Balance Anual (Mm USD)", "ja": "年間収支（十億USD）", "zh": "年度收支（十亿美元）",
    },
    "cumulated_bn": {
        "en": "Cumulated (Bn USD)", "de": "Kumuliert (Mrd. USD)",
        "it": "Cumulato (Mld USD)", "fr": "Cumulé (Mrd USD)",
        "es": "Acumulado (Mm USD)", "ja": "累積（十億USD）", "zh": "累计（十亿美元）",
    },
    "flynn_starts": {
        "en": "Flynn starts", "de": "Flynn startet", "it": "Flynn inizia",
        "fr": "Flynn démarre", "es": "Flynn comienza", "ja": "Flynn開始", "zh": "Flynn启动",
    },
    "equilibrium_zone": {
        "en": "EQUILIBRIUM ZONE", "de": "GLEICHGEWICHTSZONE",
        "it": "ZONA DI EQUILIBRIO", "fr": "ZONE D'ÉQUILIBRE",
        "es": "ZONA DE EQUILIBRIO", "ja": "均衡ゾーン", "zh": "均衡区域",
    },
    "equilibrium": {
        "en": "Equilibrium", "de": "Gleichgewicht", "it": "Equilibrio",
        "fr": "Équilibre", "es": "Equilibrio", "ja": "均衡", "zh": "均衡",
    },
    "equilibrium_approx": {
        "en": "Equilibrium ~{yr}", "de": "Gleichgewicht ~{yr}", "it": "Equilibrio ~{yr}",
        "fr": "Équilibre ~{yr}", "es": "Equilibrio ~{yr}", "ja": "均衡 ~{yr}", "zh": "均衡 ~{yr}",
    },
    "forecast_eq": {
        "en": "Forecast: Equilibrium ~{yr}", "de": "Prognose: Gleichgewicht ~{yr}",
        "it": "Previsione: Equilibrio ~{yr}", "fr": "Prévision : Équilibre ~{yr}",
        "es": "Pronóstico: Equilibrio ~{yr}", "ja": "予測：均衡 ~{yr}", "zh": "预测：均衡 ~{yr}",
    },
    "eq_not_reachable": {
        "en": "Equilibrium not reachable at current pace",
        "de": "Gleichgewicht bei aktuellem Tempo nicht erreichbar",
        "it": "Equilibrio non raggiungibile al ritmo attuale",
        "fr": "Équilibre non atteignable au rythme actuel",
        "es": "Equilibrio inalcanzable al ritmo actual",
        "ja": "現在のペースでは均衡到達不可能",
        "zh": "以目前速度无法达到均衡",
    },
    "real_data_from": {
        "en": "Real data from here", "de": "Echte Daten ab hier",
        "it": "Dati reali da qui", "fr": "Données réelles à partir d'ici",
        "es": "Datos reales desde aquí", "ja": "ここから実データ", "zh": "从此处为真实数据",
    },
    "legacy_30y": {
        "en": "30Y Legacy: -{v} Bn", "de": "30J Altlast: -{v} Mrd.",
        "it": "Debito 30A: -{v} Mld", "fr": "Dette 30A : -{v} Mrd",
        "es": "Deuda 30A: -{v} Mm", "ja": "30年遺産: -{v}十億", "zh": "30年遗留: -{v}十亿",
    },
    "cum_debt": {
        "en": "Cum. Debt: {v} Bn", "de": "Kum. Schuld: {v} Mrd.",
        "it": "Debito Cum.: {v} Mld", "fr": "Dette Cum. : {v} Mrd",
        "es": "Deuda Acum.: {v} Mm", "ja": "累積負債: {v}十億", "zh": "累计债务: {v}十亿",
    },
    "gap_bn": {
        "en": "Gap: {v} Bn USD", "de": "Schere: {v} Mrd. USD",
        "it": "Divario: {v} Mld USD", "fr": "Écart : {v} Mrd USD",
        "es": "Brecha: {v} Mm USD", "ja": "ギャップ: {v}十億USD", "zh": "差距: {v}十亿美元",
    },

    # ═══════════════════════ CHART-SPECIFIC ═══════════════════════
    "chart_dialysis_title": {
        "en": "Dialysis: Destruction (−) vs. Restoration (+) — Path to Equilibrium",
        "de": "Dialyse: Zerstörung (−) vs. Wiederherstellung (+) — Weg zum Gleichgewicht",
        "it": "Dialisi: Distruzione (−) vs. Ripristino (+) — Percorso verso l'Equilibrio",
        "fr": "Dialyse : Destruction (−) vs. Restauration (+) — Chemin vers l'Équilibre",
        "es": "Diálisis: Destrucción (−) vs. Restauración (+) — Camino al Equilibrio",
        "ja": "透析：破壊（−）vs. 復元（+）— 均衡への道",
        "zh": "透析：破坏（−）vs. 恢复（+）— 通往均衡之路",
    },
    "chart_metamorphose_title": {
        "en": "Metamorphosis: Cumulative Healing — System Debt vs. Flynn Building",
        "de": "Metamorphose: Kumulative Heilung — Systemschuld vs. Flynn-Aufbau",
        "it": "Metamorfosi: Guarigione Cumulativa — Debito Sistemico vs. Costruzione Flynn",
        "fr": "Métamorphose : Guérison Cumulative — Dette Systémique vs. Construction Flynn",
        "es": "Metamorfosis: Sanación Acumulativa — Deuda Sistémica vs. Construcción Flynn",
        "ja": "変態：累積的治癒 — システム負債 vs. Flynn構築",
        "zh": "蜕变：累积治愈 — 系统债务 vs. Flynn建设",
    },
    "extractive_ext": {
        "en": "Extractive Externalities (Destruction)",
        "de": "Extraktive Externalitäten (Zerstörung)",
        "it": "Esternalità Estrattive (Distruzione)",
        "fr": "Externalités Extractives (Destruction)",
        "es": "Externalidades Extractivas (Destrucción)",
        "ja": "採取型外部性（破壊）",
        "zh": "攫取型外部性（破坏）",
    },
    "flynn_residual_ext": {
        "en": "Flynn Residual Externalities (shrinking → 0)",
        "de": "Flynn-Restexternalitäten (sinkend → 0)",
        "it": "Esternalità Residue Flynn (in calo → 0)",
        "fr": "Externalités Résiduelles Flynn (décroissant → 0)",
        "es": "Externalidades Residuales Flynn (decrecientes → 0)",
        "ja": "Flynn残余外部性（減少 → 0）",
        "zh": "Flynn残余外部性（下降 → 0）",
    },
    "flynn_building": {
        "en": "Flynn Annual Building (Restoration)",
        "de": "Flynn Jahres-Aufbau (Wiederherstellung)",
        "it": "Costruzione Annuale Flynn (Ripristino)",
        "fr": "Construction Annuelle Flynn (Restauration)",
        "es": "Construcción Anual Flynn (Restauración)",
        "ja": "Flynn年間構築（復元）",
        "zh": "Flynn年度建设（恢复）",
    },
    "net_balance": {
        "en": "Net Balance (Building − Residual Ext.)",
        "de": "Netto-Bilanz (Aufbau − Rest-Ext.)",
        "it": "Bilancio Netto (Costruzione − Est. Residue)",
        "fr": "Bilan Net (Construction − Ext. Résiduelles)",
        "es": "Balance Neto (Construcción − Ext. Residuales)",
        "ja": "純収支（構築 − 残余外部性）",
        "zh": "净平衡（建设 − 残余外部性）",
    },
    "cum_destruction_trace": {
        "en": "Cum. Value Destruction",
        "de": "Kum. Wertvernichtung",
        "it": "Distruzione Valore Cum.",
        "fr": "Destruction Valeur Cum.",
        "es": "Destrucción Valor Acum.",
        "ja": "累積価値破壊",
        "zh": "累计价值毁灭",
    },
    "cum_flynn_trace": {
        "en": "Cum. Flynn Building",
        "de": "Kum. Flynn-Aufbau",
        "it": "Costruzione Flynn Cum.",
        "fr": "Construction Flynn Cum.",
        "es": "Construcción Flynn Acum.",
        "ja": "累積Flynn構築",
        "zh": "累计Flynn建设",
    },
    "net_system_balance": {
        "en": "Net System Balance",
        "de": "Netto-Systemsaldo",
        "it": "Saldo Netto del Sistema",
        "fr": "Solde Net du Système",
        "es": "Saldo Neto del Sistema",
        "ja": "純システム残高",
        "zh": "净系统余额",
    },
    "index_change_to": {
        "en": "Index Change to {yr}",
        "de": "Index-Veraenderung bis {yr}",
        "it": "Variazione Indice fino a {yr}",
        "fr": "Variation de l'Indice jusqu'à {yr}",
        "es": "Cambio del Índice hasta {yr}",
        "ja": "{yr}年までの指数変化",
        "zh": "到{yr}年的指数变化",
    },
    "extractive_label": {
        "en": "Extractive", "de": "Extraktiv", "it": "Estrattivo",
        "fr": "Extractif", "es": "Extractivo", "ja": "採取型", "zh": "攫取型",
    },
    "bn_extractive": {
        "en": "Bn (Extractive)", "de": "Mrd. (Extraktiv)", "it": "Mld (Estrattivo)",
        "fr": "Mrd (Extractif)", "es": "Mm (Extractivo)", "ja": "十億（採取型）", "zh": "十亿（攫取型）",
    },
    "bn_flynn_building": {
        "en": "Bn (Flynn Building)", "de": "Mrd. (Flynn Aufbau)", "it": "Mld (Costruzione Flynn)",
        "fr": "Mrd (Construction Flynn)", "es": "Mm (Construcción Flynn)",
        "ja": "十億（Flynn構築）", "zh": "十亿（Flynn建设）",
    },
    "all_categories_title": {
        "en": "All 8 Externality Categories per Year ({start}–Future, Revenue-based)",
        "de": "Alle 8 Externality-Kategorien pro Jahr ({start}–Zukunft, Revenue-basiert)",
        "it": "Tutte le 8 Categorie di Esternalità per Anno ({start}–Futuro, basate sui ricavi)",
        "fr": "Les 8 Catégories d'Externalités par An ({start}–Futur, basées sur le CA)",
        "es": "Las 8 Categorías de Externalidades por Año ({start}–Futuro, basadas en ingresos)",
        "ja": "年間8つの外部性カテゴリ（{start}–将来、収益ベース）",
        "zh": "每年8个外部性类别（{start}–未来，基于收入）",
    },
    "cum_gap_title": {
        "en": "Cumulative System Gap ({start}–Future)",
        "de": "Kumulierte Systemschere ({start}–Zukunft)",
        "it": "Divario Sistemico Cumulativo ({start}–Futuro)",
        "fr": "Écart Systémique Cumulé ({start}–Futur)",
        "es": "Brecha Sistémica Acumulada ({start}–Futuro)",
        "ja": "累積システムギャップ（{start}–将来）",
        "zh": "累计系统差距（{start}–未来）",
    },
}
