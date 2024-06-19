import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO
from tkinter import messagebox

# Inicialização da janela
window = tk.Tk()
window.geometry("600x500")
window.title("Pypokedex")
window.config(padx=10, pady=10)

# Título
title_label = tk.Label(window, text="Raphadex")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

# Imagem do Pokémon
pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=10)

# Informação do Pokémon
pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial", 20))
pokemon_information.pack(padx=10, pady=10)

# Tipos do Pokémon
pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)


def load_pokemon(event=None):
    # Obtém o texto da entrada
    query = text_id_name.get("1.0", "end-1c").strip()

    if not query:
        messagebox.showerror("Error", "Por favor, insira um ID ou nome de Pokémon válido.")
        return

    try:
        # Obtém o Pokémon usando o pypokedex
        pokemon = pypokedex.get(name=query) if not query.isdigit() else pypokedex.get(dex=int(query))

        http = urllib3.PoolManager()
        response = http.request("GET", pokemon.sprites.front.get("default"))
        image = PIL.Image.open(BytesIO(response.data))
        img = PIL.ImageTk.PhotoImage(image)

        # Atualiza a imagem do Pokémon
        pokemon_image.config(image=img)
        pokemon_image.image = img

        # Atualiza a informação do Pokémon
        pokemon_information.config(text=f"{pokemon.dex}. {pokemon.name}")
        pokemon_types.config(text=' - '.join([i for i in pokemon.types]))
    except Exception as e:
        messagebox.showerror("Error", f"Erro ao carregar o Pokémon: {e}")


# Rótulo e campo de entrada para ID ou Nome do Pokémon
label_id_name = tk.Label(window, text="Pokemon ID or Name")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)
text_id_name.bind("<Return>", load_pokemon)  # Vincula a tecla Enter à função load_pokemon

# Botão para carregar o Pokémon
btn_load = tk.Button(window, text="Load", command=load_pokemon)
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)

# Inicializa o loop principal da janela
window.mainloop()
