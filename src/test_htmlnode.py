import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    # ---------------------------------------------------------------------
    # HTMLNode tests
    def test__repr__(self):
        node = HTMLNode(tag="test-tag", value="The same text")
        return_string = "HTMLNode(test-tag, The same text, None, None)"
        self.assertEqual(node.__repr__(), return_string)

    def test_to_html(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html)

    def test_to_props(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=props)
        return_string = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), return_string)

    # ---------------------------------------------------------------------
    # LeafNode Tests
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_href(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_href(self):
        node = LeafNode("b", "Very important point!")
        self.assertEqual(node.to_html(), '<b>Very important point!</b>')

    def test_leaf_to_html_href(self):
        node = LeafNode(None, "Very important point!")
        self.assertEqual(node.to_html(), 'Very important point!')

    # ---------------------------------------------------------------------
    # ParentNode Tests
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren_1(self):
        grandchild_node1 = LeafNode("b", "grandchild1", {'href' : 'value', 'size' : '4'})
        grandchild_node2 = LeafNode(None, "grandchild2")
        grandchild_node3 = LeafNode("i", "grandchild3")
        parent_node1 = ParentNode("div", [grandchild_node2]) 
        child_node = ParentNode("span", [grandchild_node1, grandchild_node2, grandchild_node3, parent_node1])
        parent_node = ParentNode("div", [child_node], {'href' : 'value', 'size' : '4'})
        self.assertEqual(
            parent_node.to_html(),
            '<div href="value" size="4"><span><b href="value" size="4">grandchild1</b>grandchild2<i>grandchild3</i><div>grandchild2</div></span></div>'
        )

    # ---------------------------------------------------------------------




if __name__ == "__main__":
    unittest.main()