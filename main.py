import pyautogui
import tkinter as tk
import keyboard
import mouse

# Variáveis globais
click_position = None
infinite_clicks = False
hotkey = 'f8'
overlay = None

def set_click_position():
    global click_position
    # janela.iconify()  # Minimiza a janela

    # Janela para clicar
    overlay = tk.Toplevel()
    overlay.attributes('-fullscreen', True)  # Tela cheia
    overlay.attributes('-topmost', True)  # Sempre acima das outras janelas
    overlay.attributes('-alpha', 1)  # Transparência
    overlay.configure(bg='black')

    mouse.wait('left') # Espera até que o usuário clique
    click_position = pyautogui.position()
    
    overlay.destroy()
    
    pos_label.config(text=f'Posição: {click_position}')
    janela.deiconify()

def toggle_infinite():
    global infinite_clicks
    infinite_clicks = checkbox_var.get()
    if infinite_clicks:
        entry_clicks.config(state=tk.DISABLED)
    else:
        entry_clicks.config(state=tk.NORMAL)

def set_hotkey():
    global hotkey
    hotkey_label.config(text='Pressione uma tecla...')
    hotkey = keyboard.read_event().name
    hotkey_label.config(text=f'Tecla de ação: {hotkey.upper()}')

def start_clicking():
    global clicks, infinite_clicks, click_position
    if click_position is None:
        return
    
    if not infinite_clicks:
        clicks = int(entry_clicks.get())
        for _ in range(clicks):
            pyautogui.click(click_position)
    else:
        while not keyboard.is_pressed(hotkey):
            pyautogui.click(click_position)

# Criar janela
janela = tk.Tk()
janela.title("Macro Clicker")
janela.geometry("500x300")

# Obter largura e altura da tela
alturaTela = janela.winfo_screenheight()

# largura e altura da janela
larguraJanela = 500
alturaJanela = 300

posX = 0
posY = alturaTela - (alturaJanela + alturaTela // 10)

janela.geometry(f"{larguraJanela}x{alturaJanela}+{posX}+{posY}")

# Layout esquerdo
frame_left = tk.Frame(janela)
frame_left.pack(side=tk.LEFT, padx=20, pady=20)

# Campo para número de cliques
tk.Label(frame_left, text='Contagem de cliques').pack()
entry_clicks = tk.Entry(frame_left)
entry_clicks.pack()

# Checkbox para clique infinito
checkbox_var = tk.BooleanVar()
tk.Checkbutton(frame_left, text='Click infinito', variable=checkbox_var, command=toggle_infinite).pack()

# Botão para definir local do clique
pos_label = tk.Label(frame_left, text='Posição: Não definido')
pos_label.pack()
tk.Button(frame_left, text='Definir Local', command=set_click_position).pack()

# Divisória
tk.Frame(janela, width=2, bg='gray').pack(side=tk.LEFT, fill=tk.Y, padx=10)

# Layout direito
frame_right = tk.Frame(janela)
frame_right.pack(side=tk.RIGHT, padx=20, pady=20)

# Botão para definir tecla de ação
tk.Label(frame_right, text='Selecionar tecla de ação').pack()
hotkey_label = tk.Label(frame_right, text=f'Tecla de ação: {hotkey.upper()}', font=('Arial', 16))
hotkey_label.pack()
tk.Button(frame_right, text='Definir Tecla', command=set_hotkey).pack()

# Botão para iniciar
tk.Button(janela, text='Iniciar', bg='red', fg='white', font=('Arial', 12), command=start_clicking).pack(side=tk.BOTTOM, pady=10)

janela.mainloop()
