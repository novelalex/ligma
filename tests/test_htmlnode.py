import unittest

from src.htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_init_empty(self):
        """Test creating an HTMLNode with no parameters"""
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_init_with_all_parameters(self):
        """Test creating an HTMLNode with all parameters"""
        children = [HTMLNode(), HTMLNode()]
        props = {"class": "test-class", "id": "test-id"}
        node = HTMLNode(
            tag="div",
            value="test value",
            children=children,
            props=props
        )
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "test value")
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, props)

    def test_props_to_html(self):
        """Test converting properties to HTML attribute string"""
        node = HTMLNode(props={"class": "test-class", "id": "test-id"})
        html_props = node.props_to_html()
        # Since dictionary order isn't guaranteed, we need to check for both possible orderings
        possible_outputs = [
            'class="test-class" id="test-id"',
            'id="test-id" class="test-class"'
        ]
        self.assertIn(html_props, possible_outputs)

    def test_props_to_html_empty_props(self):
        """Test props_to_html with empty properties"""
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_to_html_raises_not_implemented(self):
        """Test that to_html raises NotImplementedError"""
        node = HTMLNode()
        with self.assertRaises(NotImplementedError) as context:
            node.to_html()
        self.assertEqual(
            str(context.exception),
            "This method should be overridden by children."
        )

    def test_repr(self):
        """Test string representation of HTMLNode"""
        node = HTMLNode(
            tag="div",
            value="test",
            children=[],
            props={"class": "test"}
        )
        expected = "HTMLNode(div, test, [], {'class': 'test'})"
        self.assertEqual(repr(node), expected)

    def test_init_with_none_values(self):
        """Test that None values are handled correctly"""
        node = HTMLNode(tag=None, value=None, children=None, props=None)
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    
    @unittest.skip("Not implemented")
    def test_props_to_html_with_special_characters(self):
        """Test props_to_html with properties containing special characters"""
        node = HTMLNode(props={"data-test": "hello & world", "class": "test\"quote"})
        html_props = node.props_to_html()
        possible_outputs = [
            'data-test="hello & world" class="test\\"quote"',
            'class="test\\"quote" data-test="hello & world"'
        ]
        self.assertIn(html_props, possible_outputs)

    def test_init_with_empty_lists(self):
        """Test initialization with empty lists"""
        node = HTMLNode(children=[], props={})
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})