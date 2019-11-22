from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage():
    def __init__(self, driver):
        self.driver = driver

    def user_is_logged_in(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.avatar-w'))
        )
        return True

    def get_transactions_table(self):
        original_table = []
        table = self.driver.find_element_by_xpath('//table[@id="transactionsTable"]')
        for row in table.find_elements_by_xpath(".//tr"):
            original_table.append([td.text for td in row.find_elements_by_xpath('.//td')])

        original_table.pop(0)
        return original_table

    def get_amount_order(self, table):
        amount_list = []
        for x in table:
            if (len(x) == 5):
                money = x[4].split(' ')
                number_without_comma = (money[0] + money[1]).replace(',', '')
                amount_list.append(float(number_without_comma))
        return amount_list

    def validate_amount_order(self, amount_original, amount_new):
        valid = True
        for i in range(len(amount_original)):
            if amount_original[i] != amount_new[i]:
                valid = False
                break
        return valid

    def validate_table_data(self, original_table, new_table):
        valid = True
        for x in new_table:
            valid = self.validate_row(original_table, x)
            if valid == False:
                break
        return valid

    def validate_row(self, original_table, row):
        valid = False
        for x in original_table:
            if x[0] == row[0] and x[1] == row[1] and x[2] == row[2] and x[3] == row[3] and x[4] == row[4]:
                valid = True
                break
        return valid

    def click_amount_header(self):
        amount_header = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'amount'))
        )
        amount_header.click()

    def click_compare_expenses(self):
        compare_expenses = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'showExpensesChart'))
        )
        compare_expenses.click()

    def flash_sale_is_present(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'flashSale'))
            )
            is_present = True
        except:
            is_present = False
        return is_present

    def flash_sale2_is_present(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'flashSale2'))
            )
            is_present = True
        except:
            is_present = False
        return is_present
