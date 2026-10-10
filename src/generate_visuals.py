#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Diagramas e Infografías de Preparación de Datos y Data Warehousing.
Genera las 5 infografías visuales para la secuencia de aprendizaje en alta resolución (300 DPI).
"""

import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent.parent / "diagrams"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------------------------------
# 1. MAPA MENTAL: FUENTES Y TIPOS DE DATOS
# -----------------------------------------------------------------------------
def generate_mindmap():
    fig, ax = plt.subplots(figsize=(12, 7), dpi=300)
    fig.patch.set_facecolor("#0f172a")
    ax.set_facecolor("#0f172a")

    # Center Node
    center = patches.FancyBboxPatch((4.5, 3.2), 3, 1.2, boxstyle="round,pad=0.2",
                                    facecolor="#0284c7", edgecolor="#38bdf8", linewidth=2)
    ax.add_patch(center)
    ax.text(6.0, 3.8, "UNIVERSO DE\nDATOS DEPORTIVOS", color="#ffffff",
            fontsize=12, fontweight="bold", ha="center", va="center")

    branches = [
        (2.0, 5.5, "#10b981", "1. ESTRUCTURADOS\n(SQL, CSV, Tablas)", "Esquemas RDBMS, Tipos fijos,\nAlta integridad ACID"),
        (10.0, 5.5, "#a855f7", "2. SEMIESTRUCTURADOS\n(JSON, XML, NoSQL)", "APIs REST, Key-Value,\nEsquema flexible"),
        (2.0, 1.5, "#f59e0b", "3. NO ESTRUCTURADOS\n(Video, Texto, Audio)", "Transmisiones MP4, Crónicas,\nComentarios en vivo"),
        (10.0, 1.5, "#ef4444", "4. FUENTES EXTERNAS\n(Web Scrapers, Sensores)", "Parse.bot Scrapers, GPS Tracking,\nRadar ABS / Hawk-Eye")
    ]

    for x, y, color, title, desc in branches:
        box = patches.FancyBboxPatch((x - 1.5, y - 0.6), 3.0, 1.2, boxstyle="round,pad=0.15",
                                     facecolor="#1e293b", edgecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y + 0.2, title, color=color, fontsize=10, fontweight="bold", ha="center", va="center")
        ax.text(x, y - 0.3, desc, color="#94a3b8", fontsize=8, ha="center", va="center")

        # Connect line
        ax.annotate("", xy=(x, y - 0.6 if y > 3.8 else y + 0.6), xytext=(6.0, 3.8),
                    arrowprops=dict(arrowstyle="->", color=color, lw=2, shrinkA=10, shrinkB=10))

    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")
    plt.title("FASE 1: MAPA MENTAL DE TIPOS Y FUENTES DE DATOS", color="#f8fafc", fontsize=14, fontweight="bold", pad=20)
    plt.tight_layout()
    plt.savefig(OUT_DIR / "mapa_mental_fuentes_datos.png", facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close()
    print(" [*] Generado: mapa_mental_fuentes_datos.png")


# -----------------------------------------------------------------------------
# 2. CUADRO COMPARATIVO DE TIPOS DE DATOS
# -----------------------------------------------------------------------------
def generate_comparison_table():
    fig, ax = plt.subplots(figsize=(13, 6.5), dpi=300)
    fig.patch.set_facecolor("#0f172a")
    ax.set_facecolor("#0f172a")

    columns = ["Categoría", "Tipo de Dato", "Definición Formal", "Ejemplo Caso Deportivo", "Tratamiento en ETL"]
    data = [
        ["Numérico", "Entero (INT)", "Valores discretos sin decimales", "Goles (2), Faltas (14)", "Casting directo, control de nulos a 0"],
        ["Numérico", "Flotante (FLOAT)", "Valores continuos con precisión", "Momio Decimal (1.85), xG (1.42)", "Redondeo estándar, filtrado negativos"],
        ["Temporal", "Fecha / Hora (DATETIME)", "Momento temporal UTC ISO 8601", "2026-10-09T19:00:00Z", "Normalización de zonas horarias"],
        ["Texto", "Cadena / Categórico (TEXT)", "Nombres y etiquetas canónicas", "'Borussia Dortmund', 'BUNDESLIGA'", "Trim, mayúsculas, mapeo a IDs canónicos"],
        ["Booleano", "Lógico (BOOL)", "Valores binarios (True/False)", "Es_Titular (1), Partido_Jugado (0)", "Conversión a bits 1/0"],
        ["Complejo", "JSON / Semi-estructurado", "Estructuras anidadas clave-valor", "{'pases': 450, 'posesion': 58%}", "Parseo con json.loads a columnas planas"]
    ]

    table = ax.table(cellText=data, colLabels=columns, loc='center', cellLoc='left')
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2.2)

    # Style header
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_facecolor("#0284c7")
            cell.set_text_props(color="#ffffff", fontweight="bold")
        else:
            cell.set_facecolor("#1e293b" if row % 2 == 0 else "#141e33")
            cell.set_text_props(color="#e2e8f0")
        cell.set_edgecolor("#334155")

    ax.axis("off")
    plt.title("FASE 2: CUADRO COMPARATIVO DE TIPOS DE DATOS", color="#f8fafc", fontsize=14, fontweight="bold", pad=20)
    plt.tight_layout()
    plt.savefig(OUT_DIR / "cuadro_comparativo_tipos.png", facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close()
    print(" [*] Generado: cuadro_comparativo_tipos.png")


# -----------------------------------------------------------------------------
# 3. ESQUEMA ESTRELLA (DATA WAREHOUSE)
# -----------------------------------------------------------------------------
def generate_star_schema():
    fig, ax = plt.subplots(figsize=(13, 8), dpi=300)
    fig.patch.set_facecolor("#0f172a")
    ax.set_facecolor("#0f172a")

    # Center Fact Table
    fact = patches.FancyBboxPatch((4.5, 2.8), 4.0, 2.5, boxstyle="round,pad=0.2",
                                  facecolor="#1e293b", edgecolor="#00e676", linewidth=2.5)
    ax.add_patch(fact)
    ax.text(6.5, 4.8, "FACT_FIXTURES (Hechos)", color="#00e676", fontsize=11, fontweight="bold", ha="center")
    fact_cols = "• fixture_id (PK)\n• date_id (FK)\n• league_id (FK)\n• home_team_id (FK)\n• away_team_id (FK)\n• home_score, away_score\n• odds_home, odds_away\n• elo_home, elo_away"
    ax.text(4.7, 3.6, fact_cols, color="#f8fafc", fontsize=8.5, va="center")

    # Dimensions
    dims = [
        (1.5, 5.8, "DIM_LEAGUES", "• league_id (PK)\n• name\n• country\n• tier", "#38bdf8"),
        (11.5, 5.8, "DIM_TEAMS", "• team_id (PK)\n• name, code\n• venue\n• current_elo", "#38bdf8"),
        (1.5, 1.2, "DIM_DATE", "• date_id (PK)\n• full_date\n• year, month, day\n• day_of_week", "#a855f7"),
        (11.5, 1.2, "DIM_PLAYERS", "• player_id (PK)\n• full_name\n• position\n• nationality", "#f59e0b")
    ]

    for x, y, title, cols, color in dims:
        box = patches.FancyBboxPatch((x - 1.5, y - 0.8), 3.0, 1.8, boxstyle="round,pad=0.15",
                                     facecolor="#1e293b", edgecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y + 0.6, title, color=color, fontsize=10, fontweight="bold", ha="center")
        ax.text(x - 1.3, y - 0.1, cols, color="#cbd5e1", fontsize=8)

        # Connection line to fact table
        ax.annotate("", xy=(5.5 if x < 6 else 7.5, 3.8), xytext=(x + (1.2 if x < 6 else -1.2), y),
                    arrowprops=dict(arrowstyle="<->", color=color, lw=1.8, shrinkA=5, shrinkB=5))

    ax.set_xlim(0, 13)
    ax.set_ylim(0, 8)
    ax.axis("off")
    plt.title("FASE 3: MODELADO DE DATA WAREHOUSE (ESQUEMA ESTRELLA)", color="#f8fafc", fontsize=14, fontweight="bold", pad=20)
    plt.tight_layout()
    plt.savefig(OUT_DIR / "esquema_estrella_dwh.png", facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close()
    print(" [*] Generado: esquema_estrella_dwh.png")


# -----------------------------------------------------------------------------
# 4. INFOGRAFÍA: 6 TÉCNICAS DE LIMPIEZA DE DATOS
# -----------------------------------------------------------------------------
def generate_cleaning_infographic():
    fig, ax = plt.subplots(figsize=(13, 7.5), dpi=300)
    fig.patch.set_facecolor("#0f172a")
    ax.set_facecolor("#0f172a")

    steps = [
        ("1. Imputación & Nulos", "Reemplazo de NaN/Null por valores canónicos o reglas de negocio (0 en goles, TBD en fechas).", "#38bdf8"),
        ("2. Desduplicación", "Identificación y remoción de registros idénticos basados en clave primaria compuesta.", "#00e676"),
        ("3. Normalización Textual", "Unificación de nombres de clubes (ej. 'B. Dortmund' -> 'Borussia Dortmund').", "#a855f7"),
        ("4. Estandarización Fechas", "Conversión de formatos mixtos (DD/MM/YYYY, ISO) a estándar canónico ISO 8601 UTC.", "#f59e0b"),
        ("5. Detección de Outliers", "Filtrado de cuotas y estadísticas imposibles (momios negativos, marcadores > 20).", "#ef4444"),
        ("6. Auditoría Temporal", "Eliminación de fugas del futuro (Data Leakage) y validación point-in-time.", "#3b82f6")
    ]

    for idx, (title, desc, color) in enumerate(steps):
        row = idx // 2
        col = idx % 2
        x = 1.0 + col * 5.8
        y = 5.0 - row * 2.2

        card = patches.FancyBboxPatch((x, y), 5.4, 1.8, boxstyle="round,pad=0.2",
                                      facecolor="#1e293b", edgecolor=color, linewidth=2)
        ax.add_patch(card)

        # Step badge
        badge = patches.Circle((x + 0.4, y + 1.3), 0.35, facecolor=color)
        ax.add_patch(badge)
        ax.text(x + 0.4, y + 1.3, str(idx + 1), color="#000", fontweight="bold", fontsize=10, ha="center", va="center")

        ax.text(x + 1.0, y + 1.3, title, color="#f8fafc", fontsize=11, fontweight="bold", va="center")
        ax.text(x + 0.3, y + 0.5, desc, color="#94a3b8", fontsize=8.5, wrap=True)

    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7.5)
    ax.axis("off")
    plt.title("FASE 4: INFOGRAFÍA DE TÉCNICAS DE LIMPIEZA DE DATOS", color="#f8fafc", fontsize=14, fontweight="bold", pad=20)
    plt.tight_layout()
    plt.savefig(OUT_DIR / "infografia_tecnicas_limpieza.png", facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close()
    print(" [*] Generado: infografia_tecnicas_limpieza.png")


# -----------------------------------------------------------------------------
# 5. FLUJO DEL PROCESO ETL
# -----------------------------------------------------------------------------
def generate_etl_flow():
    fig, ax = plt.subplots(figsize=(13, 6), dpi=300)
    fig.patch.set_facecolor("#0f172a")
    ax.set_facecolor("#0f172a")

    nodes = [
        (1.5, 3.0, "EXTRACCIÓN (E)", "• APIs REST\n• Web Scrapers\n• Archivos CSV Raw\n• Fuentes NoSQL", "#38bdf8"),
        (5.5, 3.0, "TRANSFORMACIÓN (T)", "• Limpieza de Nulos\n• Mapeo Canónico\n• Casting de Tipos\n• Filtro Temporal", "#a855f7"),
        (9.5, 3.0, "CARGA (L)", "• Esquema Estrella DWH\n• SQLite 3 Relacional\n• Tablas de Hechos\n• CSVs Auditados", "#00e676"),
        (12.0, 3.0, "CONSUMO BI", "• Redes Neuronales\n• Dashboards Web\n• Modelos Poisson", "#f59e0b")
    ]

    for idx, (x, y, title, details, color) in enumerate(nodes):
        w = 2.4 if idx < 3 else 2.0
        box = patches.FancyBboxPatch((x - w/2, y - 1.2), w, 2.4, boxstyle="round,pad=0.15",
                                     facecolor="#1e293b", edgecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y + 0.7, title, color=color, fontsize=10, fontweight="bold", ha="center")
        ax.text(x, y - 0.2, details, color="#cbd5e1", fontsize=8, ha="center")

        if idx < len(nodes) - 1:
            next_x = nodes[idx + 1][0]
            ax.annotate("", xy=(next_x - 1.25, y), xytext=(x + w/2 + 0.05, y),
                        arrowprops=dict(arrowstyle="->", color="#64748b", lw=2.5, shrinkA=5, shrinkB=5))

    ax.set_xlim(0, 13.5)
    ax.set_ylim(0, 6)
    ax.axis("off")
    plt.title("FASE 5: DOCUMENTACIÓN DEL FLUJO ETL (EXTREME PIPELINE)", color="#f8fafc", fontsize=14, fontweight="bold", pad=20)
    plt.tight_layout()
    plt.savefig(OUT_DIR / "flujo_proceso_etl.png", facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close()
    print(" [*] Generado: flujo_proceso_etl.png")


if __name__ == "__main__":
    generate_mindmap()
    generate_comparison_table()
    generate_star_schema()
    generate_cleaning_infographic()
    generate_etl_flow()
    print("\n[!] Todas las infografías y diagramas han sido generados exitosamente.")
