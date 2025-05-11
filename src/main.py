from textnode import TextNode
from textnode import TextType

def main():
    a = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(a)


if __name__ == "__main__":
    main()
