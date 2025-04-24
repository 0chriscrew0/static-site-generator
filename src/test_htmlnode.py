import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p")
        node2 = HTMLNode("p")
        self.assertEqual(node.tag, node2.tag)

    def test_not_eq(self):
        node = HTMLNode("p", "this is a paragraph", [], {})
        node2 = HTMLNode("p", "this is a different paragraph", [], {})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("p", "this is a paragraph", [], {"href": "/", "target": "_blank"})
        node2 = HTMLNode("p", "this is a different paragraph", [], {"src": "/", "alt": "this is an image"})
        expected1 = ' href="/" target="_blank"'
        expected2 = ' src="/" alt="this is an image"'
        self.assertEqual(node.props_to_html(), expected1)
        self.assertEqual(node2.props_to_html(), expected2)

    def test_leaf_to_html_p(self):
        node = LeafNode("Hello, world!", tag="p")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("Click me!", props={"href": "https://www.google.com"}, tag="a")
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_h1(self):
        node = LeafNode("Heading", props={"class": "heading"}, tag="h1")
        self.assertEqual(node.to_html(), '<h1 class="heading">Heading</h1>')


    def test_parent_to_html_with_children(self):
        child_node = LeafNode("child", tag="span")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("grandchild", tag="b")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()