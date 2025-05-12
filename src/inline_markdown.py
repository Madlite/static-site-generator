from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_nodes = []
        substrings = node.text.split(delimiter)
        if len(substrings) % 2 == 0:
            raise Exception("invalid markdown syntax: delimiter not closed")
        for i in range(len(substrings)):
            if substrings[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(substrings[i], node.text_type))
            else:
                split_nodes.append(TextNode(substrings[i], text_type))
        new_nodes.extend(split_nodes)
        
    return new_nodes