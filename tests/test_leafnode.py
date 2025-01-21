import unittest

from src.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_node_with_tag_and_value(self):
        node = LeafNode("span", "Hello world")
        expected = "<span>Hello world</span>"
        self.assertEqual(node.to_html(), expected,
                         msg="LeafNode to_html did not match expected output when tag and value are set.")

    def test_leaf_node_no_value_raises_error(self):
        node = LeafNode("span", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_node_with_empty_tag_returns_value_only(self):
        node = LeafNode("", "Just text")
        expected = "Just text"
        self.assertEqual(node.to_html(), expected,
                         msg="LeafNode did not return raw value when tag is empty.")

    def test_leaf_node_with_props(self):
        props = {"class": "myClass", "id": "myId"}
        node = LeafNode("div", "Content", props)
        html_output = node.to_html()
        # The order of properties in the string might vary depending on how props are iterated.
        # Check substrings instead of exact match for reliability.
        self.assertTrue(html_output.startswith("<div "), 
                        "HTML should start with <div and any properties.")
        self.assertIn('class="myClass"', html_output,
                      "HTML should include the class property.")
        self.assertIn('id="myId"', html_output,
                      "HTML should include the id property.")
        self.assertTrue(html_output.endswith(">Content</div>"),
                        "HTML should end with >Content</div>.")

    def test_leaf_node_with_no_props(self):
        node = LeafNode("p", "Paragraph text")
        expected = "<p>Paragraph text</p>"
        self.assertEqual(node.to_html(), expected,
                         msg="LeafNode output does not match expected output when there are no props.")


if __name__ == "__main__":
    unittest.main()