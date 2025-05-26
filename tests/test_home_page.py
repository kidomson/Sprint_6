import allure
from page_objects.home_page import HomePage
from conftest import driver
from data import TestData
import pytest


class TestHomePageFaq:
    @allure.title('Проверка окна "Вопросы о важном"')
    @allure.description('Проверка появления текста при нажатии на каждую иконку развертывания в окне')
    @pytest.mark.parametrize('question_number, expected_answer', TestData.test_data_faq)
    def test_click_faq_expand_icons_text_is_expected(self, driver, question_number, expected_answer):
        main_page = HomePage(driver)
        main_page.scroll_to_faq_section()
        main_page.wait_visibility_of_faq_items(question_number)
        main_page.click_on_faq_items(question_number)
        main_page.wait_visibility_of_faq_answer(question_number)
        assert main_page.get_displayed_text_from_faq_answer(question_number) == expected_answer