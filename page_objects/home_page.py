import allure
from locators.home_page_locators import HomePageLocators
from page_objects.base_page import BasePage


class HomePage(BasePage):

    @allure.step('Ожидание нужного номера ответа в окне "Вопросы о важнoм"')
    def wait_visibility_of_faq_answer(self, data):
        self.wait_visibility_of_element(HomePageLocators.answers_faq[data])

    @allure.step('Клик по кнопке "Заказать" в хэдере')
    def click_order_button_in_header(self):
        self.click_on_element(HomePageLocators.order_button_in_header)

    @allure.step('Подождать прогрузки части лого с надписью "Самокат" в хэдере')
    def wait_visibility_header_logo_scooter(self):
        self.wait_visibility_of_element(HomePageLocators.header_logo_scooter)

    @allure.step('Подождать прогрузки логотипа "Яндекс"')
    def wait_visibility_logo_yandex(self):
        self.wait_visibility_of_element(HomePageLocators.header_logo_yandex)

    @allure.step('Клик по лого "Самокат"')
    def click_header_logo_scooter(self):
        self.click_on_element(HomePageLocators.header_logo_scooter)

    @allure.step('Ожидание загрузки кнопки "Заказать"')
    def wait_visibility_order_button_in_header(self):
        self.wait_visibility_of_element(HomePageLocators.order_button_in_header)

    @allure.step('Клик по лого "Яндекс"')
    def click_on_logo_yandex(self):
        self.click_on_element(HomePageLocators.header_logo_yandex)

    @allure.step('Получить текст нужного номера ответа в окне "Вопросы о важнoм"')
    def get_displayed_text_from_faq_answer(self, data):
        return self.get_text_on_element(HomePageLocators.answers_faq[data])

    @allure.step('Подождать прогрузки отображения заголовка главной страницы')
    def wait_visibility_of_main_header(self):
        self.wait_visibility_of_element(HomePageLocators.main_header)

    @allure.step('Проверить отображение заголовка главной страницы')
    def check_displaying_of_main_header(self):
        return self.check_displaying_of_element(HomePageLocators.main_header)

    @allure.step('Проскроллить до секции "Вопросы о важном"')
    def scroll_to_faq_section(self):
        self.scroll_to_element(HomePageLocators.faq_section)

    @allure.step('Подождать прогрузки нужного номера вопроса в аккордеоне "Вопросы о важнoм"')
    def wait_visibility_of_faq_items(self, data):
        self.wait_visibility_of_element(HomePageLocators.questions_faq[data])

    @allure.step('Клик на нужный номер вопроса в аккордеоне "Вопросы о важнoм"')
    def click_on_faq_items(self, data):
        self.click_on_element(HomePageLocators.questions_faq[data])



