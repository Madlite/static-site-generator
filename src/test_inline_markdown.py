import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    # ---------------------------------------------------------------------
    # split_nodes_delimiter tests
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        facit= [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, facit)
    
    def test_double_bold(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        facit= [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, facit)

    def test_bold_multiword(self):
        node = TextNode("This is text with a *bolded word* and *another*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        facit = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded word", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("another", TextType.BOLD)
        ]
        self.assertListEqual(new_nodes, facit)
    
    def test_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        facit = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertListEqual(new_nodes, facit)

    def test_italic_and_bold(self):
        node = TextNode("*bold* and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        facit = [
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC)
        ]
        self.assertListEqual(new_nodes, facit)

    # ---------------------------------------------------------------------
    # Image Tests
    def test_image_regex(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        facit = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(result, facit)



    # ---------------------------------------------------------------------
    # Link Tests
    def test_link_regex(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        facit = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(result, facit)




if __name__ == "__main__":
    unittest.main()