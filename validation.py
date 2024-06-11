import re
from flask import abort

def validate_location(location):
    # Verifica se a localização contém apenas letras e espaços
    if not re.match("^[a-zA-Z\s]*$", location):
        raise ValueError(f"Invalid location: {location}")
