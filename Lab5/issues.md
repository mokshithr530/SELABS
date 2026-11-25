# Lab 5 issues

NAME: MOKSHITREDDY NALLABALLE  
SRN: PES2UG24CS284  
Repository: L5_37_todo_manager

Line numbers refer to the original script in commit 7c281ce.

| Issue | Type | Line(s) | Description | Fix approach |
| --- | --- | --- | --- | --- |
| B605 shell execution | Security, High | 57 | User input is joined into a shell command. | Removed the shell command. The helper now prints a reminder preview and does not send email. |
| B301 unsafe loading | Security, Medium | 47 | Loading untrusted pickle data can execute code. | Replaced pickle with JSON. |
| B403 pickle import | Security, Low | 3 | Pickle use requires careful trust handling. | Removed the pickle import. |
| B311 random choice | Security warning, Low | 70 | Bandit flags random.choice for security-sensitive use. This program only suggests a task. | Used secrets.choice to clear the warning. |
| W0102 mutable default | Code quality | 11 | The default labels list is shared across calls. | Used None and created a new list inside the function. |
| C0103 names and R1710 returns | Code quality | 11-55 | Camel-case names and an implicit not-found return. | Used snake_case names and explicit return None. |
| C0114/C0116 and W1514 | Code quality | 1, 11-60 | Missing docstrings and an unspecified text encoding. | Added docstrings and UTF-8 for JSON files. |
| E225/E231/E303/E261 | Style | 12, 40, 69, 74 | Operator, comma, blank-line and comment spacing. | Fixed the formatting. |
