import sys
import datetime

def writ(input_data):
    stdout_fileno = sys.stdout

    # Generate a unique filename based on the current timestamp
    filename = "output_{}.txt".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    
    # Redirect sys.stdout to the file
    with open(filename, 'wb') as file:
        if isinstance(input_data, bytes):
            file.write(input_data)
        else:
            # If input_data is not bytes, join list into a single string and encode to bytes
            file.write(bytes(''.join(input_data), encoding='utf-8'))

    # Restore sys.stdout to our old saved file handler
    sys.stdout = stdout_fileno

    return filename

if __name__ == '__main__':
    # Call the main script
    filename = writ(sample_input)
    print(filename)
