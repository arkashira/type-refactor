from src.refactor import refactor_type_script, refactor_function
import pytest

def test_refactor_type_script():
    code = "let x = 5; let y = 10;"
    result = refactor_type_script(code)
    assert result.success
    assert result.message == "const x = 5; const y = 10;"

def test_refactor_type_script_failure():
    code = None
    result = refactor_type_script(code)
    assert not result.success
    assert "Code cannot be None" in result.message

def test_refactor_function():
    code = "function add(a, b) { return a + b; }"
    result = refactor_function(code, "add")
    assert result.success
    assert result.message == "function new_add(a, b) { return a + b; }"

def test_refactor_function_failure():
    code = "function add(a, b) { return a + b; }"
    result = refactor_function(code, None)
    assert not result.success
    assert "Code and function name cannot be None" in result.message
