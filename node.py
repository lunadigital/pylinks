from .parameter import Parameter

class Node:
    def __init__(self, ntype):
        self.ntype = ntype
        self.parameters = {
            "output": Parameter(None)
        }

    def _get_param_object(self, name):
        if name in self.parameters:
            return self.parameters[name]
        
        return None

    def add_param(self, name, value):
        self.parameters[name] = Parameter(value)

    def get_node_output(self):
        return self.parameters["output"]

    def get_param(self, name):
        param = self._get_param_object(name)

        if param:
            return param.value

        return None

    def set_param(self, name, value):
        param = self._get_param_object(name)

        if param:
            param.set_value(value)

    def link(self, name, node):
        param = self._get_param_object(name)

        if param:
            param.link = node

            output = node.get_node_output()
            output.link = self