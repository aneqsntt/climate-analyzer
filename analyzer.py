"""
Climate Analyzer - Professional Portfolio Script
Author: Ane
Description: Simulated climate data analyzer with scientific-style output,
plots and automatic PNG export for portfolio display.
"""

from datetime import datetime
import random
import numpy as np
import matplotlib.pyplot as plt
import os

# --- Configuração geral ---
LOCAL = "Fortaleza, CE - Brasil"
COORDS = (-3.73, -38.52)
OUTPUT_DIR = "output"  # pasta onde salvamos imagens

# certifica que a pasta existe
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Dados simulados por dia (cada lista é leituras horárias simuladas)
SIMULATED_DAYS = [
    {"date": "2025-11-01", "temps": [27, 30, 32, 28, 26, 29]},
    {"date": "2025-11-02", "temps": [29, 31, 33, 30, 27, 28]},
    {"date": "2025-11-03", "temps": [25, 26, 28, 29, 27, 26]},
    {"date": "2025-11-04", "temps": [28, 30, 31, 29, 28, 27]},
]

# -------- Funções --------
def analyze_day(day_record):
    arr = np.array(day_record["temps"], dtype=float)
    mean = float(np.mean(arr))
    maximum = float(np.max(arr))
    minimum = float(np.min(arr))
    std = float(np.std(arr))
    return {
        "date": day_record["date"],
        "mean": round(mean, 1),
        "max": maximum,
        "min": minimum,
        "std": round(std, 2),
        "hourly": arr.tolist()
    }

def build_report(records):
    print("="*72)
    print("CLIMATE ANALYZER — SCIENTIFIC REPORT")
    print("="*72)
    print(f"Location: {LOCAL} | Coordinates: {COORDS[0]}°, {COORDS[1]}°")
    print(f"Generated at: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("-"*72)
    analysis = []
    for r in records:
        a = analyze_day(r)
        analysis.append(a)
        print(f"Date: {a['date']}")
        print(f"  Mean: {a['mean']} °C  |  Max: {a['max']} °C  |  Min: {a['min']} °C  |  Std: {a['std']}")
        print("-"*72)
    return analysis

def plot_analysis(analysis):
    dates = [d["date"][5:] for d in analysis]  # mostra apenas MM-DD
    means = [d["mean"] for d in analysis]
    maxs = [d["max"] for d in analysis]
    mins = [d["min"] for d in analysis]

    plt.style.use('seaborn-v0_8-darkgrid')  # estilo limpo e profissional
    fig, ax = plt.subplots(figsize=(9,5))

    ax.plot(dates, means, marker='o', linewidth=2, label='Mean (°C)')
    ax.plot(dates, maxs, linestyle='--', marker='^', label='Max (°C)', alpha=0.8)
    ax.plot(dates, mins, linestyle='--', marker='v', label='Min (°C)', alpha=0.8)

    ax.set_title(f"TEMPERATURA DIÁRIA — {LOCAL}", fontsize=14, weight='bold')
    ax.set_xlabel("Date (MM-DD)")
    ax.set_ylabel("Temperature (°C)")
    ax.legend()
    ax.grid(alpha=0.35)

    # Salvar a figura em PNG para mostrar no GitHub
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(OUTPUT_DIR, f"temperature_summary_{timestamp}.png")
    fig.tight_layout()
    fig.savefig(filename, dpi=150)
    print(f"\nPlot saved to: {filename}")
    plt.show(block=True)  # abre a janela até você fechar

# -------- Execução principal --------
if __name__ == "__main__":
    analysis = build_report(SIMULATED_DAYS)
    plot_analysis(analysis)

