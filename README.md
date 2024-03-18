# client-server-network
This is a Python package to build a client / server network using the `socket` library.

The client provides different data options to send to the server with the option to encrypt the data using symmetric encryption.

This package is written using PEP 8 guidelines.

## Table of Contents

- [Install](#Install)
- [Usage](#Usage)
- [Contributing](#Contributing)
- [License](#License)

## Install

This package is written using `Python 3.12.2`.

To install this package use pip:
```sh
pip install git+https://github.com/aisha-als/client-server-network.git
```

To install the dependencies use pip:
```sh
pip install -r requirements.txt
```

## Usage

You can use this package to create a client / server network.

To start the server, run:
```sh
cd clientserver
python clientserver/server.py
```

To start the client, run:
```sh
cd clientserver
python clientserver/client.py
```

The client sends data to the server in the below formats:
- Dictionary object - option to send this as JSON, XML or binary
- .txt file - option to encrypt the file before sending

The encryption uses the `Fernet` module from the `cryptography` package which uses an AES-128 in CBC mode symmetric 
encryption key .

To select the data type and encryption requirement, edit `clientserver/client.py` and update the values of `format`
and `encrypt`:
```sh
if __name__ == '__main__':
    # Select which data type to be sent to the server
    # Options: json, xml, binary, txt
    format = 'binary'

    # Select if the data is to be encrypted
    # Options: True, False
    encrypt = False
```


The server provides an option to save the data received to an output file called `output.txt`.

To select whether to save received data to an output file, edit `clientserver/server.py` and update the value of 
`print_to_file`:
```sh
if __name__ == '__main__':
    # Select if the data is to be print to file
    # Options: True, False
    print_to_file = True

    # Call the main script
    receive_data(print_to_file)
```

### Unit Tests

Unit tests are run using `pytest`.

To run the unit tests, run the below command:
```sh
pytest
```

## Contributing

Please open a PR for contributions.

## License

MIT License.

See license in [LICENSE](client-server-network/LICENSE)