from enum import Enum

from .leafnode import LeafNode

class TextType(Enum):
    TEXT = "Normal text"
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
    
    def to_html_node(text_node):
        match text_node.text_type:
            case TextType.TEXT:
                return LeafNode(None, text_node.text)
            case TextType.BOLD:
                return LeafNode('b', text_node.text)
            case TextType.ITALIC:
                return LeafNode('i', text_node.text)
            case TextType.CODE:
                return LeafNode('code', text_node.text)
            case TextType.LINK:
                return LeafNode('a', text_node.text, {'href': text_node.url})
            case TextType.IMAGE:
                return LeafNode('img', '', {'src': text_node.url, 'alt': text_node.text})
            case _:
                raise ValueError("Invaled TextType.")