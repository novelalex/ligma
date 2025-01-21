import unittest

from src.textnode import TextNode, TextType
from src.leafnode import LeafNode
from enum import Enum

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is an link node", TextType.LINK, "https://novelalex.com")
        self.assertNotEqual(node, node2)
        
    def test_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)
        self.assertIsNotNone(node.text)
        self.assertIsNotNone(node.text_type)
        
    def test_has_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://novelalex.com")
        self.assertIsNotNone(node.url)
        self.assertIsNotNone(node.text)
        self.assertIsNotNone(node.text_type)
        

    def test_plain_text(self):
        """Test conversion of plain text node"""
        text_node = TextNode("Hello world", TextType.TEXT)
        html_node = TextNode.to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertIsNone(html_node.tag)
        self.assertEqual(html_node.value, "Hello world")
        self.assertIsNone(html_node.props)

    def test_bold_text(self):
        """Test conversion of bold text node"""
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = TextNode.to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")
        self.assertIsNone(html_node.props)

    def test_italic_text(self):
        """Test conversion of italic text node"""
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = TextNode.to_html_node(text_node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")
        self.assertIsNone(html_node.props)

    def test_code_text(self):
        """Test conversion of code text node"""
        text_node = TextNode("Code text", TextType.CODE)
        html_node = TextNode.to_html_node(text_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code text")
        self.assertIsNone(html_node.props)

    def test_link(self):
        """Test conversion of link node"""
        text_node = TextNode("Click me", TextType.LINK, "https://example.com")
        html_node = TextNode.to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_image(self):
        """Test conversion of image node"""
        text_node = TextNode("Image description", TextType.IMAGE, "image.jpg")
        html_node = TextNode.to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props, 
            {"src": "image.jpg", "alt": "Image description"}
        )

    def test_invalid_text_type(self):
        """Test handling of invalid text type"""
        # Assuming TextType is an Enum, create an invalid type for testing
        class InvalidTextType(Enum):
            INVALID = "invalid"
            
        text_node = TextNode("Invalid", InvalidTextType.INVALID)
        with self.assertRaises(ValueError) as context:
            TextNode.to_html_node(text_node)
        self.assertEqual(str(context.exception), "Invaled TextType.")

    def test_link_without_url(self):
        """Test link node without URL"""
        text_node = TextNode("Broken link", TextType.LINK)
        html_node = TextNode.to_html_node(text_node)
        self.assertEqual(html_node.props, {"href": None})

    def test_image_without_url(self):
        """Test image node without URL"""
        text_node = TextNode("Missing image", TextType.IMAGE)
        html_node = TextNode.to_html_node(text_node)
        self.assertEqual(
            html_node.props, 
            {"src": None, "alt": "Missing image"}
        )

if __name__ == "__main__":
    unittest.main()