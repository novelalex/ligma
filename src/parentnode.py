from .htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError('All parent nodes must have a tag.')
        
        if self.children is None:
            raise ValueError('All parent nodes must have children.')
        
        children_html = ''.join(child.to_html() for child in self.children)
        props_html = f' {self.props_to_html()}' if self.props else ''
        return f'<{self.tag}{props_html}>{children_html}</{self.tag}>'
        
        