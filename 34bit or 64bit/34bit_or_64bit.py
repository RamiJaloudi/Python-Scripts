import sys
is_64bits = sys.maxsize > 2**32
file -L $(python -c 'import sys; print(sys.executable)')
