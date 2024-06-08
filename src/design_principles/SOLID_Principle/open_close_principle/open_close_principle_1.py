"""
SOLID Principles: Open Close Principle
Software Entities like classes, modules and functions
should be *open for extention* but
closed for modification.
"""


# Example 1
class SurveryValidator:
    def __init__(self):
        pass
    
    def validate(self):
        if self.data.answer1 is None:
            raise ValidationError("No answer 1 provided")
        if self.data.answer2 is None:
            raise ValidationError("No answer 2 provided")


class SimpleSurveyValidator(SurveryValidator):
    def validate(self):
        if self.data.answer1 is None:
            raise ValidationError("No answer 1 provided")


class ComplexSurveyValidator(SurveryValidator):
    def validate(self):
        super(ComplexSurveyValidator, self).validate()
        if self.data.answer3 is None:
            raise ValidationError("No answer 3 provided")
