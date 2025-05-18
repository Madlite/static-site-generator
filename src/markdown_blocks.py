from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH       = "paragraph"
    HEADING         = "heading"
    CODE            = "code"
    QUOTE           = "quote"
    UNORDERED_LIST  = "unordered_list"
    ORDERED_LIST    = "ordered_list"


def block_to_block_type(block):
    patterns = {
        "HEADING": re.compile(r"^#{1,6} .+$"),
        "CODE": re.compile(r"^```[\s\S]*```$"),
        "QUOTE": re.compile(r"^(> .*\n?)+$"),
        "UNORDERED_LIST": re.compile(r"^(?:- .*\n?)+$"),
        "ORDERED_LIST": re.compile(r"^\d+\. "),    
    }

    for label, pattern in patterns.items():
        if pattern.match(block):
            return BlockType[label]
    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    blocks = list(map(str.strip, filter(None, markdown.split("\n\n"))))
    return blocks

