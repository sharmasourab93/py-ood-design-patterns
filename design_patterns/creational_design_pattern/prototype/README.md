# Prototype Pattern

Prototype creates new objects by cloning an existing object instead of building a new one from scratch. This is useful when object setup is expensive or when you want to preserve a configured baseline.

## Example

Source idea from `prototype_example.py`.

```python
report = Report("Monthly", ["summary", "charts"])
copy_report = report.clone()
copy_report.title = "Monthly Copy"
copy_report.sections.append("appendix")
```

The class controls whether cloning should be shallow or deep.

## Takeaway

Use Prototype when object duplication is more convenient than full reconstruction, especially when nested state is involved.
