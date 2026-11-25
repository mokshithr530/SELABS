# Software Engineering Laboratory

Lab submissions for **PES2UG24CS284 - Mokshitreddy Nallaballe**.

## Lab 3: Component Modelling and Architectural Pattern Selection

Assigned scenario: **Problem Statement 30 - Airport Lost Luggage Claim & Tracking Portal**

The selected architectural style is **Microservices Architecture**. The `Lab3` folder contains the UML component diagram and the one-page architecture justification.

### Submitted files

- `PES2UG24CS284_Lab3_Component_Diagram.pdf`
- `PES2UG24CS284_Lab3_Component_Diagram.png`
- `PES2UG24CS284_Lab3_Architecture_Justification.pdf`
- `PES2UG24CS284_Lab3_Architecture_Justification.docx`

The diagram models nine internal components, labelled interfaces, external dependencies, provided and required interface notation, and request/event flow. The written justification occupies one page, with the component diagram included as a landscape appendix in the Word document and its PDF export.

---

## Lab 5: Static Code Analysis

Assigned repository: **L5_37_todo_manager** (`todo_manager.py`)

Static analysis performed using **Bandit**, **Pylint**, and **Flake8** to detect and remediate security vulnerabilities, logic smells, and PEP 8 style violations.

### Deliverables (`Lab5/`)
- `todo_manager.py`: Cleaned and refactored script.
- `pylint_report.txt` & `pylint_report_before.txt`: Improved score from **5.09/10** to **10.00/10**.
- `bandit_report.txt` & `bandit_report_before.txt`: Eliminated all High (CWE-78) and Medium (CWE-502) severity issues (0 alerts).
- `flake8_report.txt` & `flake8_report_before.txt`: Resolved all PEP 8 formatting violations (0 errors).
- `issues.md`: Detailed documentation table of all identified issues and remediation approaches.
- `reflection.md`: In-depth answers to static code analysis reflection questions.
