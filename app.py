from bot_funcs import start_bot, input_accout_instagram_user

if __name__ == "__main__":
    try:
        conta_instagram = input_accout_instagram_user()
        start_bot(conta_instagram=conta_instagram, tempo_checagem=100)
    except:
        exit()
