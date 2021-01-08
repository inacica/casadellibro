from selenium.webdriver.common.by import By


class Locators:

    SEARCH = (By.XPATH, '//input[@class="book-finder"]')
    ACCEPT_COOKIES = (By.ID, 'onetrust-accept-btn-handler')
    ENTER_SEARCH = (By.XPATH, '//input[@aria-label="Caja de búsqueda"]')
    FILTER_BY = (By.XPATH, '//h1[@class="ebx-facet__title"]//span[contains(.,"Idioma")]')
    LANGUAGE = (By.XPATH, '//button[@class="ebx-filter__label"]//span[contains(.,"Inglés")]')
    SELECT_BOOK = (By.XPATH, '//img[@src="https://imagessl5.casadellibro.com/a/l/t1/35/9780141185835.jpg"]')

    ADD_TO_CART = (By.XPATH, '//span[@class="v-btn__content" and contains(.,"Añadir a la cesta")]')
    PAY_BUTTON = (By.XPATH, '//span[@class="v-btn__content" and contains(.,"Ir a pagar")]')


    NAME = (By.XPATH,'//label[@class="v-label theme--light" and contains(.,"Nombre")]')
    NAME_FILL = (By.XPATH, '(//input[starts-with(@id, "input-")])[1]')
    SURNAME = (By.XPATH, '//label[@class="v-label theme--light" and contains(.,"Apellidos")]')
    SURNAME_FILL = (By.XPATH, '(//input[starts-with(@id, "input-")])[2]')
    EMAIL = (By.XPATH, '(//label[@class="v-label theme--light" and contains(.,"Email")])')
    EMAIL_FILL = (By.XPATH, '(//input[starts-with(@id, "input-")])[3]')
    PASSWORD = (By.XPATH, '(//label[@class="v-label theme--light" and contains(.,"Contraseña")])')
    PASSWORD_FILL = (By.XPATH, '(//input[starts-with(@id, "input-")])[4]')
    CONTINUE_BUTTON = (By.XPATH, '(//span[@class="v-btn__content" and contains(.,"Continuar")])[1]')


    ADDRESS = (By.ID, "direccionEnvio")
    POSTCODE = (By.ID, "cpEnvio")
    PHONE = (By.ID, "telefEnvio")
    ACCEPT_POLICY = (By.XPATH, '(//div[@class="v-input--selection-controls__ripple"])[3]')
    FINAL_PAY = (By.XPATH, '//span[@class="v-btn__content" and contains(.,"Pagar y finalizar la compra")]')
    PAYMENT_ERROR = (By.XPATH, '//div[@class="v-snack__content" and contains(.,"Debes seleccionar un tipo de pago.")]')
