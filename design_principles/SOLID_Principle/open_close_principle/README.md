# Open/Closed Principle

The Open/Closed Principle says software should be open for extension but closed for modification. The goal is to add new behavior with new code instead of repeatedly editing stable code.

## Example 1: Extend A Validator Through Inheritance

Source idea from `open_close_principle_1.py`.

```python
class SurveryValidator:
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
```

## Example 2: Different Pieces, Same Contract

Source idea from `open_close_principle_2.py`.

```python
class Piece:
    def move(self):
        raise Exception("Not Implemented")


class Horse(Piece):
    def move(self):
        pass


class Tower(Piece):
    def move(self):
        pass
```

## Takeaway

If every new variation forces you to edit a central `if/elif` chain, the design is not very open for extension.
