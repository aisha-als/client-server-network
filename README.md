# client-server-network
Group Project to build a client / server network.

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
python clientserver/server.py
```

To start the client, run:
```sh
python clientserver/client.py
```

The client sends data to the server in the below formats:
- Dictionary object - option to send this as JSON, XML or binary
- .txt file - option to encrypt the file before sending

To select the data type and encryption requirement, edit `clientserver/client.py`:
```sh
if __name__ == '__main__':
    # Select which data type to be sent to the server
    # Options: json, xml, binary, txt
    format = 'binary'

    # Select if the data is to be encrypted
    # Options: True, False
    encrypt = False
```

### Unit Tests


## Contributing

Please open a PR for contributions.

## License

MIT License.

See license in [LICENSE](client-server-network/LICENSE)