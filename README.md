# PyLinks
PyLinks is a bare-bones collection of object definitions for developing node-based, "linked list" style applications and data trees.

## Simple example

Let's create a simple address book, where we can store basic info about a person and their connections to other people.

```python
import pylinks

'''
First, create a node for John and give it an arbitrary node type.

This type can be any string - it's really meant for you to organize your nodes.
'''
john = pylinks.Node("person")

'''
Add some basic parameters to John's address book entry.

Each parameter is initialized with a name and an initial value.
'''
john.add_param("name", "John Smith")
john.add_param("address", "123 Hometown Road")
john.add_param("age", 35)
john.add_param("connected_to", None)

'''
Now let's do the same for Sam.
'''
sam = pylinks.Node("person")
sam.add_param("name", "Sam Smith")
sam.add_param("address", "45 Main Street")
sam.add_param("age", 32)
sam.add_param("connected_to", None)

'''
John and Sam are brothers, so we want to link their address entries together. Every parameter we add is "pluggable", meaning it can be linked with another node.

When linking nodes, you must call the "link()" method on the downstream node. In this example, the output of Sam's entry will be connected to the "connected_to" parameter of John's.
'''
john.link("connected_to", sam)
```