import json
from dataclasses import dataclass
from typing import List

@dataclass
class RefactorResult:
    success: bool
    message: str

def refactor_type_script(code: str) -> RefactorResult:
    try:
        if code is None:
            raise ValueError("Code cannot be None")
        refactored_code = code.replace('let ', 'const ')
        return RefactorResult(True, refactored_code)
    except Exception as e:
        return RefactorResult(False, str(e))

def refactor_function(code: str, func_name: str) -> RefactorResult:
    try:
        if code is None or func_name is None:
            raise ValueError("Code and function name cannot be None")
        refactored_code = code.replace(func_name, f'new_{func_name}')
        return RefactorResult(True, refactored_code)
    except Exception as e:
        return RefactorResult(False, str(e))
