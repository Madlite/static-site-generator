import unittest
from markdown_blocks import markdown_to_html_node, markdown_to_blocks, block_to_block_type, BlockType, extract_title

class TestBlockMarkdown(unittest.TestCase):
    # ---------------------------------------------------------------------
    # Markdown block Tests
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        facit = [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items"
        ]
        self.assertEqual(blocks, facit)

    # ---------------------------------------------------------------------
    # Block Type Tests
    def test_block_to_block_type(self):
        HEADING_BLOCK = "# This is a heading"
        result = block_to_block_type(HEADING_BLOCK)
        facit = BlockType.HEADING
        self.assertEqual(result, facit)
        # ----
        CODE_BLOCK = """```
    This is code and some more code,
    with realer code
        and results
```
"""
        result = block_to_block_type(CODE_BLOCK)
        facit = BlockType.CODE
        self.assertEqual(result, facit)
        # ----
        QUOTE_BLOCK = "> This is a quote"
        result = block_to_block_type(QUOTE_BLOCK)
        facit = BlockType.QUOTE
        self.assertEqual(result, facit)
        # ----
        UNORDERED_LIST_BLOCK = "- This is a list\n- with items"
        result = block_to_block_type(UNORDERED_LIST_BLOCK)
        facit = BlockType.UNORDERED_LIST
        self.assertEqual(result, facit)
        # ----
        ORDERED_LIST_BLOCK = "1. This is a list\n2. with items"
        result = block_to_block_type(ORDERED_LIST_BLOCK)
        facit = BlockType.ORDERED_LIST
        self.assertEqual(result, facit)
        # ----
        PARAGRAPH = "This is a paragraph"
        result = block_to_block_type(PARAGRAPH)
        facit = BlockType.PARAGRAPH
        self.assertEqual(result, facit)

        def test_paragraph(self):
            md = """
    This is **bolded** paragraph
    text in a p
    tag here

    """

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
                "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
            )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_extract_title_one_line(self):
        md = """# Hello"""

        result = extract_title(md)
        facit = "Hello"
        self.assertEqual(result, facit)

    def test_extract_title_multiline(self):
        md = """
# Hello this is the thing.

What is money
"""

        result = extract_title(md)
        facit = "Hello this is the thing."
        self.assertEqual(result, facit)


if __name__ == "__main__":
    unittest.main()