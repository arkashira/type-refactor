import pytest
from refactor_engine import RefactorEngine, RenameCandidate

def test_detect_rename_candidates():
    code = """
def foo():
    pass

class Bar:
    pass
"""
    engine = RefactorEngine(code)
    candidates = engine.detect_rename_candidates()
    assert len(candidates) == 2
    assert candidates[0].old_name == "foo"
    assert candidates[1].old_name == "Bar"

def test_generate_proposal():
    code = """
def foo():
    pass
"""
    engine = RefactorEngine(code)
    candidate = RenameCandidate("foo", "new_foo", None)
    proposal = engine.generate_proposal(candidate)
    assert proposal == """
def new_foo():
    pass
"""

def test_validate_proposal():
    code = """
def foo():
    pass
"""
    engine = RefactorEngine(code)
    proposal = """
def new_foo():
    pass
"""
    assert engine.validate_proposal(proposal)

def test_validate_proposal_syntax_error():
    code = """
def foo():
    pass
"""
    engine = RefactorEngine(code)
    proposal = """
def new_foo:
    pass
"""
    assert not engine.validate_proposal(proposal)
