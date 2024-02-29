import os
import sys


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
