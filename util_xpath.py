class Dados_Page_Xpath:
    user_instagram_input = "//input[@name='username']"
    password_instagram_input = "//input[@name='password']"
    button_entrar_account = "//div[text()='Entrar']"
    button_info_page_login_cancelar = "//div[text()='Agora não']"
    button_pesquisa = "svg[aria-label='Pesquisa']"
    publics_posts_list = "//div[@class='_aagw']"
    publi_curtir = "//section[@class='_aamu _ae3_ _ae47 _ae48']//span[@class='_aamw']//div[@role='button']"

    def __init__(
        self,
        username: str,
        password: str,
        account_find: str,
        driver: vars,
    ):
        self.username_accout_instagram = username
        self.password_accout_instagram = password
        self.accout_find = account_find
        self.driver = driver

    def account_instagram(self):
        return self.username_accout_instagram, self.password_accout_instagram

    def account_find_instagram(self):
        return self.accout_find

    def page_instagram(self, web_page):
        return self.driver.get(web_page)
