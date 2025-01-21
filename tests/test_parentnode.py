import unittest

from src.parentnode import ParentNode
from src.leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_parent_node_with_valid_tag_and_children(self):
        # Create some children
        child1 = LeafNode("span", "ChildOne")
        child2 = LeafNode("p", "ChildTwo")
        parent = ParentNode("div", [child1, child2])
        expected_html = "<div><span>ChildOne</span><p>ChildTwo</p></div>"
        
        self.assertEqual(
            parent.to_html(),
            expected_html,
            "ParentNode did not render expected HTML with valid tag and children."
        )

    def test_parent_node_no_tag_raises_error(self):
        child = LeafNode("span", "Child")
        parent = ParentNode(None, [child])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_parent_node_no_children_raises_error(self):
        parent = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_parent_node_empty_children_list(self):
        parent = ParentNode("section", [])
        expected_html = "<section></section>"
        
        self.assertEqual(
            parent.to_html(),
            expected_html,
            "ParentNode with an empty children list should still render opening and closing tags."
        )

    def test_parent_node_includes_props_in_html_output(self):
        child = LeafNode("span", "ChildContent")
        props = {"class": "myClass", "id": "myId"}
        parent = ParentNode("div", [child], props=props)
        html_output = parent.to_html()
        self.assertTrue(html_output.startswith("<div "))
        self.assertIn('class="myClass"', html_output)
        self.assertIn('id="myId"', html_output)
        self.assertTrue(html_output.endswith(">ChildContent</span></div>"))

if __name__ == "__main__":
    unittest.main()