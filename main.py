from tkinter import *
import customtkinter as tk
from model import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib as cm
cm.use('TkAgg')

root = tk.CTk()
root.geometry("1024x768")
root.title("SolSys")
view_visivel = False
planet_positions = {}


def view3D():
    import numpy as np
    global planet_positions, fig, canvas, view_visivel

    global fig, canvas, view_visivel

    if view_visivel:
        canvas.get_tk_widget().pack_forget()
        botao_toggle_visualizacao.configure(text="Mostrar Visualização")
        view_visivel = False
    else:

        planet_positions = {
            "Sol": (0, 0, 0),

            "Mercúrio": (float(mercurio['delta']) * np.cos(np.deg2rad(float(mercurio['DEC']))) * np.cos(
                np.deg2rad(float(mercurio['RA']))),
                         float(mercurio['delta']) * np.cos(np.deg2rad(float(mercurio['DEC']))) * np.sin(
                             np.deg2rad(float(mercurio['RA']))), 0),

            "Vênus": (float(venus['delta']) * np.cos(np.deg2rad(float(venus['DEC']))) * np.cos(
                np.deg2rad(float(venus['RA']))),
                      float(venus['delta']) * np.cos(np.deg2rad(float(venus['DEC']))) * np.sin(
                          np.deg2rad(float(venus['RA']))), 0),

            "Terra": (float(terra['delta']) * np.cos(np.deg2rad(float(terra['DEC']))) * np.cos(
                np.deg2rad(float(terra['RA']))),
                      float(terra['delta']) * np.cos(np.deg2rad(float(terra['DEC']))) * np.sin(
                          np.deg2rad(float(terra['RA']))), 0),
            "Lua": (float(lua['delta']) * np.cos(np.deg2rad(float(lua['DEC']))) * np.cos(
                np.deg2rad(float(lua['RA']))),
                    float(lua['delta']) * np.cos(np.deg2rad(float(lua['DEC']))) * np.sin
                        (np.deg2rad(float(lua['RA']))), 0),

            "Marte": (float(marte['delta']) * np.cos(np.deg2rad(float(marte['DEC']))) * np.cos(
                np.deg2rad(float(marte['RA']))),float(marte['delta']) * np.cos(np.deg2rad(float(marte['DEC']))) * np.sin(
                          np.deg2rad(float(marte['RA']))), 0),

            "Júpiter": (float(jupiter['delta']) * np.cos(np.deg2rad(float(jupiter['DEC']))) * np.cos(
                np.deg2rad(float(jupiter['RA']))),
                        float(jupiter['delta']) * np.cos(np.deg2rad(float(jupiter['DEC']))) * np.sin(
                            np.deg2rad(float(jupiter['RA']))), 0),

            "Saturno": (float(saturno['delta']) * np.cos(np.deg2rad(float(saturno['DEC']))) * np.cos(
                np.deg2rad(float(saturno['RA']))),
                        float(saturno['delta']) * np.cos(np.deg2rad(float(saturno['DEC']))) * np.sin(
                            np.deg2rad(float(saturno['RA']))), 0),

            "Urano": (float(urano['delta']) * np.cos(np.deg2rad(float(urano['DEC']))) * np.cos(
                np.deg2rad(float(urano['RA']))),
                      float(urano['delta']) * np.cos(np.deg2rad(float(urano['DEC']))) * np.sin(
                          np.deg2rad(float(urano['RA']))), 0),

            "Netuno": (float(netuno['delta']) * np.cos(np.deg2rad(float(netuno['DEC']))) * np.cos(
                np.deg2rad(float(netuno['RA']))),
                       float(netuno['delta']) * np.cos(np.deg2rad(float(netuno['DEC']))) * np.sin(
                           np.deg2rad(float(netuno['RA']))), 0),

            "Plutão": (float(pluto['delta']) * np.cos(np.deg2rad(float(pluto['DEC']))) * np.cos(
                np.deg2rad(float(pluto['RA']))),
                       float(pluto['delta']) * np.cos(np.deg2rad(float(pluto['DEC']))) * np.sin(
                           np.deg2rad(float(pluto['RA']))), 0)
        }

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        for planet, pos in planet_positions.items():
            x, y, z = pos
            ax.scatter(x, y, z, label=planet)

        for planet, pos in planet_positions.items():
            x, y, z = pos
            ax.text(x, y, z, planet, fontsize=12)

        ax.set_xlabel("Eixo X (UA)")
        ax.set_ylabel("Eixo Y (UA)")
        ax.set_zlabel("Eixo Z (UA)")
        ax.set_title("Sistema Solar 3D")

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().pack()
        botao_toggle_visualizacao.configure(text="Ocultar Visualização")
        view_visivel = True

def alternarView():
    global view_visivel

    if view_visivel:
        canvas.get_tk_widget().pack_forget()
        botao_toggle_visualizacao.configure(text="Mostrar Visualização")
        view_visivel = False
    else:
        view3D()
        botao_toggle_visualizacao.configure(text="Ocultar Visualização")
        view_visivel = True

def listar_planetas():

    lista_planetas.delete(0, tk.END)

    planetas = [
        "Sol",
        "Mercúrio",
        "Vênus",
        "Terra",
        "Lua",
        "Marte",
        "Júpiter",
        "Saturno",
        "Urano",
        "Netuno",
        "Plutão"
    ]

    for planeta in planetas:
        lista_planetas.insert(tk.END, planeta)

def mostrar_dados():

    selecionado = lista_planetas.get(tk.ACTIVE)
    dados_planeta.configure(text=f"Dados de {selecionado}:\nPropriedade 1: Valor 1\nPropriedade 2: Valor 2")


botao_listar = tk.CTkButton(root, text="Listar Planetas", command=listar_planetas)
botao_listar.pack(side=tk.TOP, padx=10, pady=10)

lista_planetas = Listbox(root)
lista_planetas.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

dados_planeta = Label(root, text="", justify="left")
dados_planeta.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

botao_exibir_dados = tk.CTkButton(root, text="Exibir Dados", command=mostrar_dados)
botao_exibir_dados.pack(side=tk.BOTTOM, padx=10, pady=10)

botao_toggle_visualizacao = tk.CTkButton(root, text='Exibir Visualização 3D', command=alternarView)
botao_toggle_visualizacao.pack()

root.mainloop()
