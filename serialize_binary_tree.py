""" Given the root to a binary tree, implement serialize(root), wich serializes the tree
to a string, and deserialize(s), which deserializes the string back into the tree """

import json

class Node:
	def __inti__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def __repr__(self):
		return str(self.data)


def serialize(root):
	if not root:
		return None


	serialize_tree_map = dict()
	serialize_left = serialize(root.left)
	serialize_right = serialize(root.right)

	serialize_tree_map['data'] = root.data
	if serialize_left:
		serialize_tree_map['left'] = serialize_left

	if serialize_right:
		serialize_tree_map['right'] = serialize_right

	return json.dumps(serialized)

def deserialize(s):
	serialized_tree_map = json.loads(s)

	node = Node(serialized_tree_map['data'])
	if 'left' in serialize_tree_map:
		node.left = deserialize(serialize_tree_map['left'])

	if 'right' in serialize_tree_map:
		node.right = deserialize(serialize_tree_map['right'])

	return node

node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')
node_e = Node('e')
node_f = Node('f')
node_g = Node('g')

node_a.left = node_b
node_a.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.left = node_f
node_c.right = node_g

serialize_a = serialize(node_a)
print(serialize_a)

deserialize_a = deserialize(serialized_a)
assert str(deserialize_a) == 'a'
