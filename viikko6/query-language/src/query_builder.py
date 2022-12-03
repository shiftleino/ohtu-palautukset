from matchers import And, HasAtLeast, PlaysIn, Not, All, HasFewerThan, Or


class QueryBuilder:
    def __init__(self, matcher=All()):
        self._matcher_obj = matcher

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self._matcher_obj))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self._matcher_obj))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self._matcher_obj))

    def build(self):
        return self._matcher_obj
    
    def oneOf(self, matcher1, matcher2):
        return QueryBuilder(Or(matcher1, matcher2))