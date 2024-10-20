import tree_sitter

from constants import Language
from treesitter.treesitter import Treesitter, TreesitterMethodNode, TreesitterExpressionNode
from treesitter.treesitter_registry import TreesitterRegistry


class TreesitterPython(Treesitter):
    def __init__(self):
        super().__init__(
            Language.PYTHON, "function_definition", "identifier", "expression_statement"
        )

    def parse(self, file_bytes: bytes):
        self.tree = self.parser.parse(file_bytes)
        result = []

        expressions = self._query_all_expressions(self.tree.root_node)
        for expression in expressions:
            expression_names = self._find_variable_names(expression)
            if len(expression_names) == 1:
                result.append(TreesitterExpressionNode(expression_names[0], None, expression))

        methods = self._query_all_methods(self.tree.root_node)
        for method in methods:
            method_name = self._query_method_name(method)
            doc_comment = self._query_doc_comment(method)
            result.append(TreesitterMethodNode(method_name, doc_comment, None, method))

        return result
    
    def _find_variable_names(self, node):
        variable_names = []
        if node.type == 'expression_statement':
            for child in node.children:
                if child.type == 'assignment':
                    variable_name = child.child_by_field_name('left').text.decode('utf8')
                    variable_names.append(variable_name)
        for child in node.children:
            variable_names.extend(self._find_variable_names(child))
        return variable_names

    def _query_all_expressions(self, node: tree_sitter.Node):
        expressions = []
        for child in node.children:
            if child.type == "expression_statement":
                expressions.append(child)
        return expressions

    def _query_method_name(self, node: tree_sitter.Node):
        if node.type == self.method_declaration_identifier:
            for child in node.children:
                if child.type == self.method_name_identifier:
                    return child.text.decode()
        return None

    def _query_all_methods(self, node: tree_sitter.Node):
        methods = []
        for child in node.children:
            if child.type == self.method_declaration_identifier:
                methods.append(child)
            if child.type == "class_definition":
                class_body = child.children[-1]
                for child_node in class_body.children:
                    if child_node.type == self.method_declaration_identifier:
                        methods.append(child_node)
        return methods

    def _query_doc_comment(self, node: tree_sitter.Node):
        query_code = """
            (function_definition
                body: (block . (expression_statement (string)) @function_doc_str))
        """
        doc_str_query = self.language.query(query_code)
        doc_strs = doc_str_query.captures(node)

        if doc_strs:
            return doc_strs[0][0].text.decode()
        else:
            return None


TreesitterRegistry.register_treesitter(Language.PYTHON, TreesitterPython)
