import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from planos.models import Attendance
from utils.browser import make_chrome_browser


class BaseFunctionalTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()
    
    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()
    
    def sleep(self, seconds=5):
        time.sleep(seconds)
    
class FunctionalTests(BaseFunctionalTest):
    def test_form_is_invalid_when_you_do_not_fill_in_the_name(self):
        # User open browser
        self.browser.get(
            self.live_server_url + reverse('planos:planos')
        )

        form = self.browser.find_element(By.TAG_NAME, 'form')

        # User sees name
        name = self.browser.find_element(By.ID, 'id_name')
        name.send_keys(' ')

        # User sees "eu sou"
        solution = Select(self.browser.find_element(By.ID, 'id_iam'))
        solution.select_by_index(1)

        # User adds an email
        email = self.browser.find_element(By.ID, 'id_email')
        email.send_keys('walex@email.com')
        
        # User adds an phone number
        phone_number = self.browser.find_element(By.ID, 'id_phone_number')
        phone_number.send_keys('899880415155484515')

        # User adds an solution
        solution = Select(self.browser.find_element(By.ID, 'id_solution'))
        solution.select_by_index(1)

        self.sleep()

        # User send form
        form.submit()
        self.assertIn(
            "Este campo é obrigatório.",
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

        self.sleep()

    
    def test_form_is_invalid_when_you_do_not_fill_in_a_valid_email(self):
        # User open browser
        self.browser.get(
            self.live_server_url + reverse('planos:planos')
        )

        # User open form
        form = self.browser.find_element(By.TAG_NAME, 'form')

        # User sees name
        name = self.browser.find_element(By.ID, 'id_name')
        name.send_keys('Walex')

        # User sees "eu sou"
        solution = Select(self.browser.find_element(By.ID, 'id_iam'))
        solution.select_by_index(1)

        # User adds an email
        email = self.browser.find_element(By.ID, 'id_email')
        email.send_keys('walexemail.com')
        
        # User adds an little phone number 

        phone_number = self.browser.find_element(By.ID, 'id_phone_number')
        phone_number.send_keys('899880415155484515')

        # User adds an solution
        solution = Select(self.browser.find_element(By.ID, 'id_solution'))
        solution.select_by_index(1)


        self.sleep()

        # User send form
        form.submit()

        self.assertIn(
            "Informe um endereço de email válido.",
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
        self.sleep()



    def test_form_is_invalid_when_the_i_am_is_not_filled_in(self):
        # User open browser
        self.browser.get(
            self.live_server_url + reverse('planos:planos')
        )

        form = self.browser.find_element(By.TAG_NAME, 'form')

        # User sees name
        name = self.browser.find_element(By.ID, 'id_name')
        name.send_keys('Walex')

        # User adds an email
        email = self.browser.find_element(By.ID, 'id_email')
        email.send_keys('walex@email.com')
        
        # User adds an phone number
        phone_number = self.browser.find_element(By.ID, 'id_phone_number')
        phone_number.send_keys('899880415155484515')

        # User adds an solution
        solution = Select(self.browser.find_element(By.ID, 'id_solution'))
        solution.select_by_index(1)

        self.sleep()

        # User send form
        form.submit()

        self.assertIn(
            "'Eu sou' é um campo obrigatório",
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
        self.sleep()

    
    def test_form_is_invalid_when_the_phone_number_is_less_than_16_characters(self):
        # User open browser
        self.browser.get(
            self.live_server_url + reverse('planos:planos')
        )

        # User open form
        form = self.browser.find_element(By.TAG_NAME, 'form')

        # User sees name
        name = self.browser.find_element(By.ID, 'id_name')
        name.send_keys('Walex')

        # User sees "eu sou"
        solution = Select(self.browser.find_element(By.ID, 'id_iam'))
        solution.select_by_index(1)

        # User adds an email
        email = self.browser.find_element(By.ID, 'id_email')
        email.send_keys('walex@email.com')
        
        # User adds an little phone number 

        phone_number = self.browser.find_element(By.ID, 'id_phone_number')
        phone_number.send_keys('10')

        # User adds an solution
        solution = Select(self.browser.find_element(By.ID, 'id_solution'))
        solution.select_by_index(1)

        self.sleep()

        # User send form
        form.submit()

        self.assertIn(
            "Este campo deve ter no mínimo 16 caracteres.",
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
        self.sleep()

    
    def test_form_is_invalid_when_the_solution_is_not_filled_in(self):
        # User open browser
        self.browser.get(
            self.live_server_url + reverse('planos:planos')
        )

        form = self.browser.find_element(By.TAG_NAME, 'form')

        # User sees name
        name = self.browser.find_element(By.ID, 'id_name')
        name.send_keys('Walex')

        # User adds an email
        email = self.browser.find_element(By.ID, 'id_email')
        email.send_keys('walex@email.com')
        
        # User adds an phone number
        phone_number = self.browser.find_element(By.ID, 'id_phone_number')
        phone_number.send_keys('899880415155484515')

        self.sleep()

        # User send form
        form.submit()

        self.assertIn(
            "Solução é um campo obrigatório",
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
        self.sleep()

    
    def test_request_is_created_when_all_required_fields_are_valid(self):
        # User open browser
        self.browser.get(
            self.live_server_url + reverse('planos:planos')
        )
        self.sleep()

        # User open form
        form = self.browser.find_element(By.TAG_NAME, 'form')

        # User sees name
        name = self.browser.find_element(By.ID, 'id_name')
        name.send_keys('Walex')

        # User sees "eu sou"
        solution = Select(self.browser.find_element(By.ID, 'id_iam'))
        solution.select_by_index(1)

        # User adds an email
        email = self.browser.find_element(By.ID, 'id_email')
        email.send_keys('walex@email.com')
        
        # User adds an little phone number 

        phone_number = self.browser.find_element(By.ID, 'id_phone_number')
        phone_number.send_keys('899880415155484515')

        # User adds an solution
        solution = Select(self.browser.find_element(By.ID, 'id_solution'))
        solution.select_by_index(1)

        # User send form
        form.submit()

        self.sleep()


        self.assertIn(
            "Solicitação enviada com sucesso!",
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

        # check in the database
        attendance = Attendance.objects.filter().exists()
        self.sleep()

        self.assertTrue(attendance)
        self.sleep()


