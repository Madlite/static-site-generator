import unittest
from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type

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



if __name__ == "__main__":
    unittest.main()