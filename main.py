import yaml
import json

def read_file(file_path):
    """
    Read the contents of a file and return it as a string.

    Parameters:
        file_path (str): The path to the file to read.

    Returns:
        str: The contents of the file.

    Raises:
        IOError: If the file cannot be opened or read.
    """
    with open(file_path, 'r') as f:
        tokens = json.load(f)
        return tokens

def read_lexer_config(config_file_name):
    """
    Read a YAML configuration file for the lexer and return the configuration data.

    Parameters:
        config_file_name (str): The path to the YAML configuration file.

    Returns:
        dict: The lexer configuration data parsed from the YAML file.

    Raises:
        IOError: If the file cannot be opened or read.
        yaml.YAMLError: If there is an error parsing the YAML file.
    """
    with open(config_file_name, 'r') as file:
        data = yaml.safe_load(file)
    return data

def iterate_tokens(tokens):
    print('tokens ==> ', tokens)
    for item in tokens:
        # Perform your arbitrary operations here
        print(f"Value: {item['value']}, Type: {item['type']}")

def build_ast(input):
    ast = {'type': "program", 'body': []}
    ast['body'] = iterate_tokens(input)
    return ast

def generate_abstract_syntax_tree(file_path):
    tokens = read_file(file_path)
    return build_ast(tokens)

print(generate_abstract_syntax_tree('output.json'))

