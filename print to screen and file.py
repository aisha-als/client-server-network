import sys

# This program redirects the print() to the file by routing the standard output sys.stdout
# to point to the destination file instead.
# It saves the current stdout so that we can revert sys.stdou after we complete
# our redirection

stdout_fileno = sys.stdout

sample_input = ['Hi', 'all', 'exit']

# Redirect sys.stdout to the file
sys.stdout = open('output.txt', 'w')

for ip in sample_input:
    # Prints to the redirected stdout (Output.txt)
    sys.stdout.write(ip + '\n')
    # Prints to the actual saved stdout handler
    stdout_fileno.write(ip + '\n')


# Close the file
sys.stdout.close()
# output.txt is now stored as a new text file
# Restore sys.stdout to our old saved file handler
sys.stdout = stdout_fileno

