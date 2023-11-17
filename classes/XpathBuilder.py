class XpathBuilder:
    html_tag, html_attribute, value = None, None, None

    @staticmethod
    def simple_xpath(html_tag: str, html_attribute: str, value: str):
        final_xpath = f"//{html_tag.lower()}[@{html_attribute.lower()}='{value}']"
        return final_xpath

    @staticmethod
    def nested_xpath(layers, complement):
        layers[0] = "/"+layers[0]
        return '/' + '/'.join(layers) + f"[{complement}]"



