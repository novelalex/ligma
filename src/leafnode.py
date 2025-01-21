from .htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")

        if not self.tag:
            return self.value

        props_html = f" {self.props_to_html()}" if self.props else ""
        
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"