import pandas as pd
from tkinter import *
from tkinter import messagebox

# Leia o arquivo Excel
df = pd.read_excel('questions.xlsx')
questions = df.to_dict('records')

# Crie a janela principal
main = Tk()
main.title('Quiz da Marvel')
main.geometry('400x450')

# Defina as cores
background_color = "#ECECEC"
text_color = "#333333"
button_color = "#4CAF50"

# Configurações da janela principal
main.config(bg=background_color)
main.option_add('*Font', 'Arial')

# Carregar a imagem e definir como ícone do aplicativo
app_icon = PhotoImage(file="download.png")
main.iconphoto(False, app_icon)

# Adicionar o rótulo com a imagem
app_label = Label(main, image=app_icon, bg=background_color)
app_label.pack(pady=10)

# Adicionar o rótulo para mostrar as perguntas
questions_label = Label(main, text="", wraplength=300, bg=background_color, fg=text_color, font=("Arial", 12, "bold"))
questions_label.pack(pady=20)

# Variável para manter a pontuação e índice da pergunta atual
score = 0
question_index = 0

# Função para mostrar a pergunta atual
def show_question():
    global question_index
    if question_index < len(questions):
        questions_label.config(text=questions[question_index]['pergunta'])
        for i, btn in enumerate(option_buttons):
           btn.config(text=eval(questions[question_index]['op'])[i])

    else:
        questions_label.config(text=f"Fim do Quiz! Sua pontuação: {score}/{len(questions)}")
        for btn in option_buttons:
            btn.pack_forget()

# Função para verificar a resposta
def check_answer(selected_option):
    global score, question_index
    if selected_option == questions[question_index]['res']:
        score += 1
    question_index += 1
    show_question()

# Adicionar botões de resposta
option_buttons = []
for i in range(4):
    btn = Button(main, text="", bg=button_color, command=lambda i=i: check_answer(i))
    btn.pack(pady=5)
    option_buttons.append(btn)

# Exibir a primeira pergunta
show_question()

# Inicia o loop principal da janela
main.mainloop()
