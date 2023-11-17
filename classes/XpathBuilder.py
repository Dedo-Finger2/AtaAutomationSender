class XpathBuilder:
    html_tag, html_attribute, value = None, None, None

    @staticmethod
    def simple_xpath(html_tag: str, html_attribute: str, value: str):
        final_xpath = f"//{html_tag.lower()}[@{html_attribute.lower()}='{value}']"
        return final_xpath
