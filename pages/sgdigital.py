from selenium.webdriver import Chrome

BASE_URL = "https://www.sgdigital.com/contact"


class SgdigitalUtilities():

    def __init__(self):
        self.browser = Chrome()
        self.browser.maximize_window()
        self.browser.get(BASE_URL)

    def completeform(self, name, company, mobile, mail, messages):
        if name != None:
            fname = self.browser.find_element_by_id("wpforms-2967-field_0")
            fname.send_keys(name)
        if company != None:
            companyname = self.browser.find_element_by_id("wpforms-2967-field_4")
            companyname.send_keys(company)
        if mobile != None:
            phone = self.browser.find_element_by_id("wpforms-2967-field_8")
            phone.send_keys(mobile)
        if mail != None:
            email = self.browser.find_element_by_id("wpforms-2967-field_1")
            email.send_keys(mail)
        if messages != None:
            message = self.browser.find_element_by_id("wpforms-2967-field_2")
            message.send_keys(messages)

        submit = self.browser.find_element_by_name("wpforms[submit]")
        submit.click()

    def warning_message_name(self):
        submit_warning_message = self.browser.find_element_by_id("wpforms-2967-field_0-error")
        value = submit_warning_message.text
        return value

    def warning_message_company(self):
        submit_warning_message = self.browser.find_element_by_id("wpforms-2967-field_4-error")
        value = submit_warning_message.text
        return value

    def warning_message_mail(self):
        submit_warning_message = self.browser.find_element_by_id("wpforms-2967-field_1-error")
        value = submit_warning_message.text
        return value

    def warning_message_message(self):
        submit_warning_message = self.browser.find_element_by_id("wpforms-2967-field_2-error")
        value = submit_warning_message.text
        return value

    def close_browser(self):
        self.browser.close()
