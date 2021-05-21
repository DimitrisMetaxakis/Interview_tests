import time

from selenium.webdriver import Chrome

BASE_URL = "http://375.synergatos.gr/en/propertyDetails/13079"


class SpitogatosUtilities(object):

    def __init__(self):
        self.browser = Chrome()
        self.browser.maximize_window()
        self.browser.get(BASE_URL)

    def completeform(self, name, lastname, mobile, mail, messages, check):
        if name != None:
            fname = self.browser.find_element_by_name("firstName")
            fname.send_keys(name)
        if lastname != None:
            lname = self.browser.find_element_by_name("lastName")
            lname.send_keys(lastname)
        if mobile != None:
            phone = self.browser.find_element_by_name("phoneNumber")
            phone.send_keys(mobile)
        if mail != None:
            email = self.browser.find_element_by_name("contactEmail")
            email.send_keys(mail)
        if messages != None:
            message = self.browser.find_element_by_name("messageText")
            message.send_keys(messages)

        if check == True:
            checkbox = self.browser.find_element_by_css_selector("div.ts-box label.custom-control-label")
            checkbox.click()
        submit = self.browser.find_element_by_css_selector("button.btn.btn-primary.float-right")
        submit.click()
        time.sleep(2)

    def success_message(self):
        submit_popup = self.browser.find_element_by_css_selector("h4.modal-title")
        value = submit_popup.text
        return value

    def warning_message_fName(self):
        submit_warning_message = self.browser.find_element_by_id("firstName-error")
        value = submit_warning_message.text
        return value

    def warning_message_lName(self):
        submit_warning_message = self.browser.find_element_by_id("lastName-error")
        value = submit_warning_message.text
        return value

    def warning_message_phone(self):
        submit_warning_message = self.browser.find_element_by_id("phone-number-error")
        value = submit_warning_message.text
        return value

    def warning_message_mail(self):
        submit_warning_message = self.browser.find_element_by_id("contactEmail-error")
        value = submit_warning_message.text
        return value

    def warning_message_terms(self):
        submit_warning_message = self.browser.find_element_by_id("acceptTermsOfUse-error")
        value = submit_warning_message.text
        return value

    def close_browser(self):
        self.browser.close()
