"""Gráficos do painel estado-ano (homicídios CDC e registros RAND)."""

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.ticker import FuncFormatter


AZUL = "#2a78d6"
LARANJA = "#eb6834"
CINZA = "#b5b4ae"
TEXTO = "#0b0b0b"
TEXTO_2 = "#52514e"
FUNDO = "#fcfcfb"
ESCALA_AZUL = LinearSegmentedColormap.from_list(
    "azul", ["#e9f1fc", "#b7d3f6", "#6da7ec", "#2a78d6", "#184f95", "#0d366b"])


VIRGULA = FuncFormatter(lambda valor, _: f"{valor:g}".replace(".", ",").replace("-", "\u2212"))


def _limpar(ax, grade="x"):
    ax.set_facecolor(FUNDO)
    for lado in ("top", "right", "left"):
        ax.spines[lado].set_visible(False)
    ax.spines["bottom"].set_color("#d6d5cf")
    ax.tick_params(colors=TEXTO_2, length=0, labelsize=9)
    ax.grid(axis=grade, color="#e7e6e1", linewidth=0.8)
    ax.set_axisbelow(True)


def _titulo(ax, titulo, subtitulo=None):
    ax.set_title(titulo, loc="left", fontsize=12, color=TEXTO, fontweight="bold",
                 pad=22 if subtitulo else 10)
    if subtitulo:
        ax.text(0, 1.012, subtitulo, transform=ax.transAxes, fontsize=9, color=TEXTO_2, va="bottom")


def mapa_homicidios(painel):
    """Uma linha por estado e uma coluna por ano; cor mais escura = taxa maior."""
    tabela = painel.pivot(index="state", columns="year", values="homicide_rate")
    tabela = tabela.loc[tabela.mean(axis=1).sort_values(ascending=False).index]
    fig, ax = plt.subplots(figsize=(6.4, 13), facecolor=FUNDO)
    imagem = ax.imshow(tabela.to_numpy(), cmap=ESCALA_AZUL, aspect="auto", vmin=0)
    ax.set_xticks(range(tabela.shape[1]), tabela.columns)
    ax.set_yticks(range(tabela.shape[0]), tabela.index)
    ax.xaxis.tick_top()
    ax.tick_params(colors=TEXTO_2, length=0, labelsize=9)
    for lado in ax.spines.values():
        lado.set_visible(False)
    ax.set_xticks([x - 0.5 for x in range(1, tabela.shape[1])], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, tabela.shape[0])], minor=True)
    ax.grid(which="minor", color=FUNDO, linewidth=2)
    ax.tick_params(which="minor", length=0)
    limite = tabela.to_numpy().max() * 0.5
    for i in range(tabela.shape[0]):
        for j in range(tabela.shape[1]):
            valor = tabela.iat[i, j]
            ax.text(j, i, f"{valor:.1f}".replace(".", ","), ha="center", va="center", fontsize=8,
                    color="white" if valor > limite else TEXTO)
    barra = fig.colorbar(imagem, ax=ax, orientation="horizontal", fraction=0.025, pad=0.012)
    barra.outline.set_visible(False)
    barra.ax.tick_params(colors=TEXTO_2, length=0, labelsize=8)
    barra.set_label("homicídios por 100 mil habitantes", color=TEXTO_2, fontsize=9)
    barra.ax.xaxis.set_major_formatter(VIRGULA)
    fig.text(0.02, 0.988, "Taxa de homicídios por estado e ano", fontsize=12, fontweight="bold", color=TEXTO)
    fig.text(0.02, 0.975, "Estados ordenados pela média de 2019 a 2024. Fonte: CDC.",
             fontsize=9, color=TEXTO_2)
    fig.subplots_adjust(left=0.24, right=0.98, top=0.95, bottom=0.03)
    return fig


def linhas_homicidios(painel, destaques=("Mississippi", "Louisiana", "New Hampshire")):
    """Cada linha cinza é um estado; a linha azul é a média simples dos 50."""
    fig, ax = plt.subplots(figsize=(8, 4.8), facecolor=FUNDO)
    _limpar(ax, grade="y")
    for estado, grupo in painel.groupby("state"):
        marcado = estado in destaques
        ax.plot(grupo["year"], grupo["homicide_rate"], color=TEXTO_2 if marcado else CINZA,
                linewidth=1.2 if marcado else 0.7, alpha=1 if marcado else 0.55, zorder=2 if marcado else 1)
        if marcado:
            ax.text(2024.08, grupo["homicide_rate"].iloc[-1], estado, fontsize=8.5, color=TEXTO_2, va="center")
    media = painel.groupby("year")["homicide_rate"].mean()
    ax.plot(media.index, media.values, color=AZUL, linewidth=2.2, marker="o", markersize=5, zorder=3)
    ax.text(2024.08, media.iloc[-1], "média dos 50", fontsize=8.5, color=TEXTO, va="center", fontweight="bold")
    ax.set_xlim(2018.8, 2025.3)
    ax.set_ylim(0, None)
    ax.set_xticks(range(2019, 2025))
    ax.set_ylabel("homicídios por 100 mil habitantes", color=TEXTO_2, fontsize=9)
    _titulo(ax, "A taxa subiu em 2020 e 2021 e depois caiu",
            "Cada linha cinza é um estado. A linha azul é a média simples entre estados, não a taxa nacional.")
    fig.tight_layout()
    return fig


def regras_por_estado(painel, inicio=2019, fim=2024):
    """Contagem de registros no começo e no fim do período, para cada estado."""
    a = painel[painel["year"] == inicio].set_index("state")
    b = painel[painel["year"] == fim].set_index("state")
    ordem = b["restrictive_records"].sort_values().index
    fig, eixos = plt.subplots(1, 2, figsize=(9, 11), sharey=True, facecolor=FUNDO,
                              gridspec_kw={"width_ratios": [3, 1.3]})
    partes = [("restrictive_records", "Registros restritivos", AZUL),
              ("permissive_records", "Registros permissivos", LARANJA)]
    for ax, (coluna, nome, cor) in zip(eixos, partes):
        _limpar(ax, grade="x")
        y = range(len(ordem))
        ax.hlines(y, a.loc[ordem, coluna], b.loc[ordem, coluna], color=TEXTO_2, linewidth=1.2, zorder=2)
        ax.scatter(a.loc[ordem, coluna], y, s=34, facecolor=FUNDO, edgecolor=TEXTO_2, linewidth=1.1,
                   zorder=3, label=str(inicio))
        ax.scatter(b.loc[ordem, coluna], y, s=38, color=cor, edgecolor=FUNDO, linewidth=1, zorder=4, label=str(fim))
        ax.set_yticks(list(y), ordem)
        ax.set_ylim(-0.8, len(ordem) - 0.2)
        ax.set_xlim(0, None)
        ax.set_title(nome, loc="left", fontsize=10.5, color=TEXTO, fontweight="bold")
    eixos[0].legend(loc="lower right", frameon=False, fontsize=9, labelcolor=TEXTO_2, handletextpad=0.2,
                    title="fim do ano", title_fontsize=9)
    fig.text(0.02, 0.985, "Registros RAND vigentes em 31/12, por estado", fontsize=12, fontweight="bold", color=TEXTO)
    fig.text(0.02, 0.969, "Ponto vazado: 2019. Ponto cheio: 2024. Um ponto só quer dizer que a contagem não mudou. "
             "As duas escalas são diferentes.", fontsize=9, color=TEXTO_2)
    fig.tight_layout(rect=(0, 0, 1, 0.965))
    return fig


def relacao(painel, rotulos_nivel=(), rotulos_mudanca=()):
    """Esquerda: comparação entre estados. Direita: mudança dentro de cada estado."""
    p = painel.sort_values(["state", "year"])
    nivel = p[p["year"] == 2023].set_index("state")[["restrictive_records"]].join(
        p[p["year"] == 2024].set_index("state")["homicide_rate"])
    antes = p[p["year"] == 2019].set_index("state")["restrictive_records"]
    mudanca = (nivel["restrictive_records"] - antes).to_frame("d_regras").join(
        (p[p["year"] == 2024].set_index("state")["homicide_rate"]
         - p[p["year"] == 2020].set_index("state")["homicide_rate"]).rename("d_taxa"))
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.8), facecolor=FUNDO)
    for ax in (ax1, ax2):
        _limpar(ax, grade="both")
    ax1.scatter(nivel["restrictive_records"], nivel["homicide_rate"], s=42, color=AZUL,
                edgecolor=FUNDO, linewidth=1, alpha=0.9)
    for estado in rotulos_nivel:
        ax1.annotate(estado, (nivel.at[estado, "restrictive_records"], nivel.at[estado, "homicide_rate"]),
                     xytext=(5, 4), textcoords="offset points", fontsize=8, color=TEXTO_2)
    ax1.set_xlabel("registros restritivos em 31/12/2023", color=TEXTO_2, fontsize=9)
    ax1.set_ylabel("taxa de homicídios em 2024", color=TEXTO_2, fontsize=9)
    ax1.set_ylim(0, None)
    _titulo(ax1, "Entre estados", "Estados com mais registros tendem a ter taxa menor.")
    ax2.axhline(0, color="#c9c8c2", linewidth=1)
    ax2.axvline(0, color="#c9c8c2", linewidth=1)
    ax2.scatter(mudanca["d_regras"], mudanca["d_taxa"], s=42, color=AZUL, edgecolor=FUNDO, linewidth=1, alpha=0.9)
    for estado in rotulos_mudanca:
        ax2.annotate(estado, (mudanca.at[estado, "d_regras"], mudanca.at[estado, "d_taxa"]),
                     xytext=(5, 4), textcoords="offset points", fontsize=8, color=TEXTO_2)
    ax2.set_xlabel("mudança nos registros restritivos (fim de 2019 a fim de 2023)", color=TEXTO_2, fontsize=9)
    ax2.set_ylabel("mudança na taxa (2020 a 2024)", color=TEXTO_2, fontsize=9)
    ax2.xaxis.set_major_formatter(VIRGULA)
    ax2.yaxis.set_major_formatter(VIRGULA)
    ax1.yaxis.set_major_formatter(VIRGULA)
    _titulo(ax2, "Dentro do mesmo estado", "Quem ganhou registros não teve queda maior na taxa.")
    fig.tight_layout()
    return fig, nivel, mudanca


def coeficientes(tabela):
    """Coeficiente e intervalo de 95% para cada data de corte testada."""
    fig, eixos = plt.subplots(1, 2, figsize=(9.5, 3.2), sharey=True, sharex=True, facecolor=FUNDO)
    partes = [("restritivos", "Registros restritivos", AZUL), ("permissivos", "Registros permissivos", LARANJA)]
    y = list(range(len(tabela)))[::-1]
    for ax, (chave, nome, cor) in zip(eixos, partes):
        _limpar(ax, grade="x")
        ax.axvline(0, color=TEXTO_2, linewidth=1)
        ax.hlines(y, tabela[chave + "_min"], tabela[chave + "_max"], color=cor, linewidth=2)
        ax.scatter(tabela[chave], y, s=55, color=cor, edgecolor=FUNDO, linewidth=1.2, zorder=3)
        for yi, valor in zip(y, tabela[chave]):
            ax.text(valor, yi + 0.22, f"{valor:+.2f}".replace(".", ","), ha="center", fontsize=8.5, color=TEXTO)
        ax.set_yticks(y, tabela["medida"])
        ax.set_ylim(-0.6, len(tabela) - 0.3)
        ax.set_title(nome, loc="left", fontsize=10.5, color=TEXTO, fontweight="bold")
        ax.set_xlabel("pontos na taxa por registro a mais", color=TEXTO_2, fontsize=9)
        ax.xaxis.set_major_formatter(VIRGULA)
    fig.text(0.02, 0.93, "Todos os intervalos de 95% passam pelo zero", fontsize=12, fontweight="bold", color=TEXTO)
    fig.tight_layout(rect=(0, 0, 1, 0.9))
    return fig
