from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from time import sleep
from util_xpath import Dados_Page_Xpath
from base_web_selenium import iniciar_driver, input_driver_break
from base_utils import clear_terminal, simular_digitacao_lentamente


def input_accout_instagram_user():
    while True:
        try:
            user_name = str(input("Digite o nome de usuário: ")).strip()
            user_pass = str(input("Digite a senha do usuário: ")).strip()
            print(
                """
                    o Nome da conta que deseja procurar 
                    (exemplo: jonvlogs)
                    
                """
            )
            pagina = str(input("digite sem @: ")).strip()
            return user_name, user_pass, pagina
        except:
            print("Digite dados validos")
            continue


def login_bot_page(driver: vars, wait: vars, dados_xpath: Dados_Page_Xpath):
    user_input = wait.until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, dados_xpath.user_instagram_input)
        )
    )
    password_input = wait.until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, dados_xpath.password_instagram_input)
        )
    )
    account = dados_xpath.account_instagram()
    if user_input and password_input is not None:
        simular_digitacao_lentamente(user_input, account[0])
        sleep(1)
        simular_digitacao_lentamente(password_input, account[1])

    entrar_account_input = wait.until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, dados_xpath.button_entrar_account)
        )
    )
    if entrar_account_input is not None:
        sleep(1)
        entrar_account_input.click()


def visit_account_find_page(driver: vars, wait: vars, dados_xpath: Dados_Page_Xpath):
    info_button_cancelar = wait.until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, dados_xpath.button_info_page_login_cancelar)
        )
    )
    if info_button_cancelar is not None:
        sleep(1)
        info_button_cancelar.click()
    sleep(3)
    try:
        default_page = dados_xpath.page_instagram(
            f"https://www.instagram.com/{dados_xpath.account_find_instagram()}"
        )
    except:
        print(
            "Não foi possivel achar a pagina dessa pessoa, por favor insira o perfil correto"
        )
    ultima_publi = wait.until(
        expected_conditions.visibility_of_any_elements_located(
            (By.XPATH, dados_xpath.publics_posts_list)
        )
    )
    if ultima_publi is not None:
        for index, publi in enumerate(ultima_publi):
            if index == 0:
                sleep(1)
                publi.click()
            break
    try:
        curtir_publi = wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, dados_xpath.publi_curtir)
            )
        )
        try:
            check_curtida = driver.find_element(
                By.XPATH,
                dados_xpath.publi_check_curtida,
            )
        except:
            check_curtida is None
        if curtir_publi is not None and check_curtida is not None:
            sleep(1)
            curtir_publi.click()
            print("Publicaçao curtida")
            sleep(3)
    except:
        print("Publicaçao ja foi curtida, tente outra vez mais tarde")
        pass


def start_bot(conta_instagram: tuple, tempo_checagem=100):
    while True:
        try:
            clear_terminal()
            driver, wait = iniciar_driver(window_size_x=1300, window_size_y=1000)
            dados_xpath = Dados_Page_Xpath(
                username=conta_instagram[0],
                password=conta_instagram[1],
                account_find=conta_instagram[2],
                driver=driver,
            )
            sleep(3)
            dados_xpath.page_instagram("https://www.instagram.com/")
            login_bot_page(driver, wait, dados_xpath)
            visit_account_find_page(driver, wait, dados_xpath)
            input_driver_break(driver, time_break=True, timeout=tempo_checagem)
            sleep(5)
        except:
            break
