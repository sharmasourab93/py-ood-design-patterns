# Python Design Patterns

This repository is a personal learning and revision guide for Python object-oriented programming, software design principles, and design patterns.

The code in this repository is intentionally example-driven. Many files show:

- a naive or tightly coupled approach
- a cleaner refactor
- one way to explain the trade-offs behind the concept

This makes the repository useful for quick revision as well as deeper concept review.

## How To Use This Repository

If you are revisiting a concept quickly:

1. Start with the section README.
2. Open the concept-level README inside that section.
3. Use the file list there to jump directly to the example you want.

If you are learning from scratch:

1. Begin with [Basics OOP](basics_oop/README.md).
2. Continue to [Design Principles](design_principles/README.md).
3. Finish with [Design Patterns](design_patterns/README.md).

## Repository Structure

### Core Learning Sections

- [Basics OOP](basics_oop/README.md)  
  Foundational Python OOP concepts such as classes, inheritance, abstract base classes, properties, and method types.

- [Design Principles](design_principles/README.md)  
  Principles that guide maintainable design, with the current focus on SOLID.

- [Design Patterns](design_patterns/README.md)  
  Behavioral, creational, and structural pattern examples with applied and comparison-based implementations.

- [Resources](resources/README.md)  
  Supporting learning material, including archived course resources.

## What To Expect From The Code

- Examples are small and focused on one idea at a time.
- Some files intentionally demonstrate a violation or an imperfect design before showing an improved approach.
- Naming and implementation style vary because the repository captures learning notes and examples from multiple points in time.

For a public-facing learning repository, treat the code as teaching material first and production code second.

## Tooling

Project formatting configuration lives in [pyproject.toml](pyproject.toml). The repository currently includes configuration for:

- `black`
- `isort`
- `python-semantic-release`

## Recommended Revision Path

- Python object basics and class behavior
- Inheritance and composition
- SOLID principles
- Behavioral patterns
- Creational patterns
- Structural patterns

## Notes

- Binary archives under `resources/` are reference material and not part of the main code walkthrough.
- Some folders contain incomplete or placeholder examples; the READMEs point that out where relevant.
