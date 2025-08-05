#def text_is_not_empty_in_element(element):
    #def _predicate(_):
       # if len(element.text) > 0:
        #    return True
        #else:
       #     return False

    #return _predicate

def text_is_not_empty_in_element(locator):
    def _predicate(driver):
        element = driver.find_element(*locator)  # Используем распаковку локатора
        return len(element.text) > 0  # Возвращаем True, если текст не пустой
    return _predicate