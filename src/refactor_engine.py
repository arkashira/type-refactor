import ast
import dataclasses
import json
from typing import List, Dict

@dataclasses.dataclass
class RenameCandidate:
    old_name: str
    new_name: str
    node: ast.AST

class RefactorEngine:
    def __init__(self, code: str):
        self.code = code
        self.tree = ast.parse(code)

    def detect_rename_candidates(self) -> List[RenameCandidate]:
        candidates = []
        for node in ast.walk(self.tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                candidates.append(RenameCandidate(node.name, f"new_{node.name}", node))
        return candidates

    def generate_proposal(self, candidate: RenameCandidate) -> str:
        new_code = self.code.replace(candidate.old_name, candidate.new_name)
        return new_code

    def validate_proposal(self, proposal: str) -> bool:
        try:
            ast.parse(proposal)
            return True
        except SyntaxError:
            return False
