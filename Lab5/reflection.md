# Lab 5 reflection

NAME: MOKSHITREDDY NALLABALLE  
SRN: PES2UG24CS284

1. What did each tool identify, and how do their scopes differ?

Pylint found naming, docstring and mutable-default issues. Bandit found unsafe shell execution and pickle loading. Flake8 found spacing and blank-line issues.

2. Which issue was most critical, and why?

The shell command was the most critical because user input could change the command being executed. Unsafe pickle loading was another important security issue.

3. How does static analysis help in CI/CD?

Running the tools on each commit catches common problems early and keeps code style consistent. A failed check can stop a change until it is fixed.

4. What are the limitations of static analysis?

The tools do not prove that the program works correctly. I also ran the program and checked task ordering, completion, search and JSON persistence.
