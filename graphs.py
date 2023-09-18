import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io
from matplotlib.backends.backend_pdf import PdfPages

from csvAnalyzer import playerStats as data


for player in data:
    for stat in data[player]:
        if data[player][stat] == 'NA':
            data[player][stat] = np.nan


df = pd.DataFrame(data).T

num_players = len(df)
color_map = plt.get_cmap('tab20')
player_colors = color_map(np.linspace(0, 1, num_players))

player_color_dict = {player: color for player,
                     color in zip(df.index, player_colors)}


for stat in df.columns:
    plt.figure(figsize=(10, 6))

    sorted_df = df[[stat]].sort_values(by=stat)

    for player in sorted_df.index:
        value = sorted_df.loc[player, stat]

        formatted_value = '{:.4f}'.format(value)
        plt.bar(player, value, color=player_color_dict[player])
        plt.annotate(formatted_value, xy=(
            player, value), ha='center', va='bottom')

    plt.title(stat)
    plt.ylabel(stat)
    plt.xlabel('Player')
    plt.xticks(rotation=45)
    plt.tight_layout()

pdf_buffer = io.BytesIO()
with PdfPages(pdf_buffer) as pdf:
    for fig in plt.get_fignums():
        pdf.savefig(plt.figure(fig))
        plt.close(fig)

pdf_filename = 'player_statistics.pdf'
with open(pdf_filename, 'wb') as f:
    f.write(pdf_buffer.getvalue())


print("PDF opened in the default viewer.")
