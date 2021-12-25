#Creating our class URL_extractor receiving olny the object url.
import re
class URL_extractor:
    def __init__(self, url):
        self.url = url
        self.url_validation()

# region - Validating the url to avoid it to be empty, equals nome or different from the pattern at all.
    def url_validation(self):
        url_pattern = re.compile('(http(s)?://)?(www.)?twitter.com/search')
        match = url_pattern.match(self.url)
        if not match:
            raise ValueError("A url está vazia.")
# endregion

# region - Getting the url's base.
    def get_url_base(self):
        index_qm = self.url.find('?')
        url_base = self.url[:index_qm]
        return url_base

# endregion

# region - Getting the url's parameters.
    def get_url_parameter(self):
        index_qm = self.url.find('?')
        url_parameter = self.url[index_qm+1:]
        return url_parameter
# endregion

# region - Getting the values from the parameters.
    def get_value(self, parameter_search):
        index_parameter = self.get_url_parameter().find(parameter_search)
        index_value = index_parameter + 1 + len(parameter_search)
        index_and = self.get_url_parameter().find('&', index_value)
        if index_and == -1:
            value = self.get_url_parameter()[index_value:]
        else:
            value = self.get_url_parameter()[index_value: index_and]
        return value

# endregion

# region - Calling for len method in order to get the length from the url.
    def __len__(self):
        return len(self.url)
# endregion

# region - Calling for str method in order to make it easier to present the information.
    def __str__(self):
        return f'URL: {self.url} \n' \
               f'Base: {self.get_url_base()} \n' \
               f'Parameters: {self.get_url_parameter()}'
# endregion

# Using the eq method to match same url string instead of returning the memory spot.
    def __eq__(self, other):
        return self.url == other.url
