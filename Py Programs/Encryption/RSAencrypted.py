from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import time

private_key = rsa.generate_private_key(
public_exponent=65537,
key_size=2048,
     backend=default_backend()
      )