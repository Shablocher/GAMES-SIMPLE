import turtle
import os
import time

# --- Seleção de Cor ---
print("--- BEM-VINDO AO PING PONG ---")
escolha = input("Escolha sua cor (1 para AZUL / 2 para VERMELHO): ")
cor_jogador = "blue" if escolha == "1" else "red"
cor_ia = "red" if escolha == "1" else "blue"

# 1. Configuração da Janela
janela = turtle.Screen()
janela.title("Ping Pong Pro - Sounds & Visual Effects")
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(0)

# Placar
score_a = 0
score_ia = 0

# Função de Som (Multiplataforma)
def emitir_som(tipo):
    # tipo 1: batida parede (grave), tipo 2: raquete (médio), tipo 3: ponto (agudo)
    frequencias = {1: 300, 2: 600, 3: 1200}
    try:
        if os.name == "nt": # Windows
            import winsound
            winsound.Beep(frequencias[tipo], 100)
        else: # Mac/Linux
            print('\a') # Som de sistema padrão
    except:
        pass

# 2. Objetos
raquete_a = turtle.Turtle()
raquete_a.shape("square")
raquete_a.color(cor_jogador)
raquete_a.shapesize(stretch_wid=5, stretch_len=1)
raquete_a.penup()
raquete_a.goto(-350, 0)
raquete_a_vel = 0

raquete_ia = turtle.Turtle()
raquete_ia.shape("square")
raquete_ia.color(cor_ia)
raquete_ia.shapesize(stretch_wid=5, stretch_len=1)
raquete_ia.penup()
raquete_ia.goto(350, 0)

bola = turtle.Turtle()
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0, 0)
vel_base = 0.2
bola.dx = vel_base
bola.dy = vel_base

pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Você: 0  IA: 0", align="center", font=("Courier", 24, "normal"))

# --- Controles Suaves ---
def subir_on(): global raquete_a_vel; raquete_a_vel = 0.4
def subir_off(): global raquete_a_vel; raquete_a_vel = 0 if raquete_a_vel > 0 else raquete_a_vel
def descer_on(): global raquete_a_vel; raquete_a_vel = -0.4
def descer_off(): global raquete_a_vel; raquete_a_vel = 0 if raquete_a_vel < 0 else raquete_a_vel

janela.listen()
janela.onkeypress(subir_on, "w")
janela.onkeyrelease(subir_off, "w")
janela.onkeypress(descer_on, "s")
janela.onkeyrelease(descer_off, "s")

# --- Loop Principal ---
while True:
    janela.update()

    # Movimento Jogador
    nova_pos_y = raquete_a.ycor() + raquete_a_vel
    if 250 > nova_pos_y > -250:
        raquete_a.sety(nova_pos_y)

    # Mover bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Colisão Paredes
    if bola.ycor() > 290 or bola.ycor() < -290:
        bola.dy *= -1
        emitir_som(1) # Som de batida na parede

    # IA
    if raquete_ia.ycor() < bola.ycor() - 10:
        raquete_ia.sety(raquete_ia.ycor() + 0.25)
    elif raquete_ia.ycor() > bola.ycor() + 10:
        raquete_ia.sety(raquete_ia.ycor() - 0.25)

    # Efeito Visual de Ponto
    def efeito_ponto(cor):
        for _ in range(3): # Pisca 3 vezes
            janela.bgcolor(cor)
            janela.update()
            time.sleep(0.05)
            janela.bgcolor("black")
            janela.update()
            time.sleep(0.05)

    # Pontuação
    if bola.xcor() > 390: # Ponto do Jogador
        score_a += 1
        emitir_som(3)
        efeito_ponto(cor_jogador)
        bola.goto(0, 0)
        bola.dx = vel_base * -1
        pen.clear()
        pen.write(f"Você: {score_a}  IA: {score_ia}", align="center", font=("Courier", 24, "normal"))

    if bola.xcor() < -390: # Ponto da IA
        score_ia += 1
        emitir_som(3)
        efeito_ponto(cor_ia)
        bola.goto(0, 0)
        bola.dx = vel_base
        pen.clear()
        pen.write(f"Você: {score_a}  IA: {score_ia}", align="center", font=("Courier", 24, "normal"))

    # Colisões Raquetes
    if (bola.xcor() > 340 and bola.xcor() < 350) and (raquete_ia.ycor() + 50 > bola.ycor() > raquete_ia.ycor() - 50):
        bola.setx(340)
        bola.dx *= -1.1
        emitir_som(2) # Som de batida na raquete

    if (bola.xcor() < -340 and bola.xcor() > -350) and (raquete_a.ycor() + 50 > bola.ycor() > raquete_a.ycor() - 50):
        bola.setx(-340)
        bola.dx *= -1.1
        emitir_som(2) # Som de batida na raquete
