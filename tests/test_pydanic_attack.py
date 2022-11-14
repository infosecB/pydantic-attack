from context import models

class TestClasses:
    def test_technique(self):
        t = models.Technique(techniqueID="T1083", tactic="Collection")
        assert t is not None
    