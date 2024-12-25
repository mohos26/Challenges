# https://edabit.com/challenge/5S97Me79PDAefLEXv
# 19.03.2023
# Expect


def lambda_to_def(code):
    code = code.split('lambda', maxsplit=1)
    code = {
        'name': code[0].split('=', maxsplit=1)[0].strip(),
        'parameters': code[1].split(':', maxsplit=1)[0].strip(),
        'code': code[1].split(':', maxsplit=1)[1].strip()
    }
    return f'def {code["name"]}({code["parameters"]}):\n\treturn {code["code"]}'

def lambda_to_def2(code):
    code = code.split('lambda', maxsplit=1)
    code = [code[0].split('=', maxsplit=1)[0].strip(), code[1].split(':', maxsplit=1)]
    return f'def {code[0]}({code[1][0].strip()}):\n\treturn {code[1][1].strip()}'


def lambda_to_def3(code):
    return f'def {code.split("lambda", maxsplit=1)[0].split("=", maxsplit=1)[0].strip()}({code.split("lambda", maxsplit=1)[1].split(":", maxsplit=1)[0].strip()}):\n\treturn {code.split("lambda", maxsplit=1)[1].split(":", maxsplit=1)[1].strip()}'

def lambda_to_def_gpt(code_str):
    name, args_str = code_str.split(' = ')
    args = args_str.split(':')[0].replace('lambda ', '')
    body = code_str.split(':')[1].strip()
    return f"def {name}({args}):\n\treturn {body}"

def lambda_to_def_gpt2(code):
    name, expr = code.split(' = ')
    args, body = eval(expr).__code__.co_varnames[:eval(expr).__code__.co_argcount], eval(expr).__code__.co_consts[0]
    body_str = str(body).strip('()')
    return f"def {name}({', '.join(args)}):\n\treturn {body_str}"
