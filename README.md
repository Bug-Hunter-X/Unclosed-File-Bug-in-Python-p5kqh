# Unclosed File Bug in Python

This repository demonstrates a common error in Python: forgetting to close files, especially when exceptions occur.

The `bug.py` file contains a function that opens a file but doesn't explicitly close it using `f.close()`.  If an exception is raised within the function, the file remains open, leading to potential resource leaks and data corruption.

The `bugSolution.py` file provides a corrected version, utilizing the `with` statement to ensure the file is automatically closed even if an exception is encountered.