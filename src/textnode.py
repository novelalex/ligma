from enum import Enum

class TextType(Enum):
    NORMAL = "Normal text"
    BOLD = "Bold text"
    ITALIC = "Italic text"
    CODE = "Code text"
    LINK = "Links"
    IMAGE = "Images"
    
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        is_text_same = self.text == other.text
        is_text_type_same = self.text_type == other.text_type
        is_url_same = self.url == other.url
        return is_text_same and is_text_type_same and is_url_same
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'