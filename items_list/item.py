import abc


class Item:
    """Represents a single row on a list"""

    @property
    @abc.abstractmethod
    def locators_template(self) -> dict:
        """
        Locators template

        Example:
        locators_template = {
            'last_name': (By.CSS_SELECTOR, "tr:nth-of-type({item_num}) td:nth-of-type(1)"),
            'first_name': (By.CSS_SELECTOR, "tr:nth-of-type({item_num}) td:nth-of-type(2)"),
            'email': (By.CSS_SELECTOR, "tr:nth-of-type({item_num}) td:nth-of-type(3)"),
        }
        """

    def __init__(self, item_number: int = 1) -> None:
        self.__locators = dict()
        self.__validate_locators_template(self.locators_template)
        self.__item_number = item_number
        self.update_item_number(item_number)

    def update_item_number(self, item_number: int) -> dict:
        self.__item_number = item_number
        self.__locators = {k: (v[0], v[1].format(item_num=item_number))
                           for k, v in self.locators_template.items()}
        return self.__locators

    @property
    def locators(self) -> dict:
        return self.__locators

    @property
    def item_number(self) -> int:
        """Returns row number of the current item"""
        return self.__item_number

    def __validate_locators_template(self, locators_template: dict):
        assert isinstance(locators_template, dict)
        for value in locators_template.values():
            assert isinstance(value, tuple)
