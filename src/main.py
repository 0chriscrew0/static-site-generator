from textnode import TextNode, TextType

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "http://boot.dev")
    print(node.__repr__())

main()