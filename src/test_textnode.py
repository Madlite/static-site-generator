import unittest
import pprint
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    # ---------------------------------------------------------------------
    # TextNode tests
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://link.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://link.com")
        self.assertEqual(node, node2)

    def test_None_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://haslink.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_diff_types(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    # ---------------------------------------------------------------------
    # text_node_to_html_node tests
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a bold node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, 'https://test-link.com')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.props['href'], 'https://test-link.com')
        self.assertEqual(html_node.to_html(), '<a href="https://test-link.com">This is a link node</a>')

    def test_img(self):
        node = TextNode("This is an image node", TextType.IMAGE, 'https://test-img.com')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props['src'], 'https://test-img.com')
        self.assertEqual(html_node.props['alt'], 'This is an image node')
        self.assertEqual(html_node.to_html(), '<img src="https://test-img.com" alt="This is an image node"></img>')

    def test_raise(self):
        node = TextNode("This is an movie node", "movie")
        self.assertRaises(ValueError, text_node_to_html_node, node)




if __name__ == "__main__":
    unittest.main()