import os
import sys
from time import sleep
import random


def func_scroll_page(driver: vars, mode: str, scroll_pixel: int):
    # Rolar até o fim da página
    if mode == "final":
        sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Rolar até o topo da página
    if mode == "inicial":
        sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    # Rolar Y quantidade em pixels(descer)
    if mode == "down":
        sleep(1)
        driver.execute_script(f"window.scrollTo(0, {scroll_pixel});")
    # Rolar Y quantidade em pixels(subir)
    if mode == "up":
        sleep(1)
        driver.execute_script(f"window.scrollTo(0, {-scroll_pixel});")


def simular_digitacao_lentamente(propriedade: vars, texto: str):
    for letra in texto:
        propriedade.send_keys(letra)
        sleep(random.randint(1, 5) / 30)


def clear_terminal():
    """Limpa o terminal."""
    if sys.platform.startswith("win"):
        # Para Windows
        _ = os.system("cls")
    else:
        # Para Linux e macOS
        _ = os.system("clear")


def checar_time(timer):
    minutos = 0
    segundos = 0

    if timer >= 60:
        minutos += timer // 60
        segundos = timer % 60
        timer = 0
        if segundos == 0:
            return f"{minutos} minuto(s)"
        else:
            return f"{minutos} minuto(s) e {segundos} segundo(s)"
    else:
        segundos = timer % 60
        return f"{segundos} segundo(s)"
