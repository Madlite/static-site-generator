import re
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


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        if images == []:
            new_nodes.append(node)
            continue

        text = node.text
        for image in images:
            tag  = image[0]
            link = image[1]
            sections = text.split(f"![{tag}]({link})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(tag, TextType.IMAGE, link))
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        if links == []:
            new_nodes.append(node)
            continue

        text = node.text
        for link in links:
            tag  = link[0]
            link = link[1]
            sections = text.split(f"[{tag}]({link})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(tag, TextType.LINK, link))
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes


def extract_markdown_images(text):
    return list(re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text))


def extract_markdown_links(text):
    return list(re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text))

