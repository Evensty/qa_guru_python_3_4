def func_reader(func_name, *args):
    result_name = func_name.__name__.replace('_', ' ').title()
    print(result_name, *args)


def open_browser(browser_name):
    func_reader(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    func_reader(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    func_reader(find_registration_button_on_login_page, page_url, button_text)


open_browser(browser_name='Chrome')
go_to_companyname_homepage(page_url='https://habr.com/ru/all/')
find_registration_button_on_login_page(page_url='https://account.habr.com/login/?state=46cb9b1f68f8e42090fabeaa55eacbc5'
                                                '&consumer=habr&host=habr.com&hl=ru_RU', button_text='Зарегистрируйтесь')






