def function_with_unclosed_file(filename):
    f = open(filename, 'w')
    # ... some code that might raise an exception ...
    f.write('some data')
    # The file remains open if an exception occurs here

# Example of calling the function
try:
    function_with_unclosed_file('my_file.txt')
except Exception as e:
    print(f"An error occurred: {e}")