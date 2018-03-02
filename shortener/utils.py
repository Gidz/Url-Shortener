import random
import string

def codegen(size=6, alphabet=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    code = ''
    for i in range(6):
        code += random.choice(alphabet)
    return code
