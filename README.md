# PY120: Object-Oriented Programming with Python

**Repository:** [https://github.com/christinelinster/ls-py120](https://github.com/christinelinster/ls-py120)

A comprehensive deep dive into the Object-Oriented Programming (OOP) paradigm within Python. This course focuses on demystifying OOP concepts, designing robust modular code, and mastering the "Pythonic" way of handling classes, objects, and inheritance.

## Core Concepts Mastered

### Classes & Objects
* **Blueprint Design:** Creating classes to act as blueprints for objects, handling instantiation, and managing object lifecycles.
* **Methods & Scope:** Distinguishing between **Instance**, **Class**, and **Static** methods and variables.
* **Encapsulation:** Hiding internal state and requiring all interaction to occur through an object's methods.
* **Properties:** Using decorators (`@property`) to manage attribute access pythonically.

### Inheritance & Polymorphism
* **Class Hierarchies:** Using inheritance to facilitate code reuse and logical structuring.
* **Mix-ins:** utilizing multiple inheritance to compose behavior across unrelated classes.
* **Duck Typing:** Leveraging Python's dynamic nature to treat objects based on what they *do* rather than what they *are*.
* **Method Resolution Order (MRO):** Understanding the complex lookup chain in multiple inheritance scenarios.

### Advanced Python Features
* **Magic Methods:** Customizing object behavior using dunder methods (e.g., `__str__`, `__eq__`, `__add__`).
* **Truthiness:** defining custom boolean evaluation for objects.
* **Exceptions:** Handling errors within class structures and creating custom exception types.

### Design Methodologies
* **CRC Cards:** Using **Class-Responsibility-Collaborator** cards to model object interactions and architecture before writing code.
* **Collaborator Objects:** Designing systems where objects hold references to other objects to perform complex tasks (Composition).



## Projects

### OO Rock Paper Scissors
A refactoring of the classic procedural game into an Object-Oriented design.
* **Focus:** Introduction to classes, modeling `Player` and `Move` objects, and basic inheritance structures.
* **Features:** Game history tracking, customizable rules, and computer personalities.

### OO Tic Tac Toe
An intermediate implementation requiring strict separation of concerns between the display logic and game engine.
* **Focus:** Collaborator objects (`Board`, `Square`, `Player`), managing complex game state, and building an extensible AI.
* **Features:** Scalable board size and intelligent computer defense/offense.

### OO Twenty-One (Blackjack)
A complex simulation of the card game involving dealer logic, variable ace values, and bankroll management.
* **Focus:** Deep polymorphism (treating `Player` and `Dealer` similarly via a common superclass), specialized containers (Deck/Hand), and flow control.

## Repository Structure

```text
ls-py120/
├── lesson_1/              # OO Readings & Fundamentals (Classes, Objects)
├── lesson_2/              # Inheritance, Polymorphism & RPS Project
├── lesson_3/              # Variable Scope, Exceptions, and Custom Operators
├── lesson_4/              # Practice Problems (Easy, Medium, Hard)
└── lesson_5/              # Slightly Larger OO Programs (Tic Tac Toe, Twenty-One)
