import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()