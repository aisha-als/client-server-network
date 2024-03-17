import sys

# This program redirects the print() to the file by routing the standard output sys.stdout
# to point to the destination file instead.
# It saves the current stdout so that we can revert sys.stdou after we complete
# our redirection

sample_input = ['Hi', 'all', 'exit']


def writ(input_data):
    stdout_fileno = sys.stdout

    # Redirect sys.stdout to the file
    sys.stdout = open('output.txt', 'wb')

    if type(input_data) is bytes:
        sys.stdout.write(input_data)
    else:
        input_data = bytes(input_data, encoding='utf-8')
        sys.stdout.write(input_data)

    # Close the file
    sys.stdout.close()

    # Restore sys.stdout to our old saved file handler
    sys.stdout = stdout_fileno

    my_file = open("output.txt", "r")
    return my_file


if __name__ == '__main__':
    # Call the main script
    writ(sample_input)
