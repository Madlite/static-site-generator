


class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        props = " ".join(f'{k}="{v}"' for k,v in self.props.items())
        return f" {props}"



class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        attributes = self.props_to_html()
        return f"<{self.tag}{attributes}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return f"LeafNode({self.tag}, children: {self.children}, {self.props})"

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: All parent nodes must have a tag")
        if self.children is None:
            raise ValueError("invalid HTML: All parent nodes must have child nodes")

        attributes = self.props_to_html()
        child_nodes_html = ""
        for child in self.children:
            child_nodes_html += child.to_html()

        return f"<{self.tag}{attributes}>{child_nodes_html}</{self.tag}>"
