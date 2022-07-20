import json


def generate_variable_json(directory: str, variables: list[str]):
    functions = f"""import json


def read_json() -> dict:
    with open("sys_variables.json", "r") as f:
        data: dict = json.load(f)
        return data

def write_json(data: dict):
    with open("sys_variables.json", "w") as f:
        json.dump(data, f)
        
"""
    for variable in variables:
        functions = functions + f"""
def get_{variable}() -> dict:
    data = read_json()
    return data.get("{variable}")


def set_{variable}(new_data):
    data = read_json()
    data["{variable}"] = new_data
    write_json(data)
    
"""
    with open(directory + "/json_settings.py", 'w') as f:
        f.write(functions)

    data = {}
    for variable in variables:
        data[f"{variable}"] = ""

    with open(directory + "/sys_variables.json", 'w') as f:
        json.dump(data, f)


def get_dir() -> str:
    directory = input("Enter your project directory\n>> ")
    double_check = input(f"You entered '{directory}', is that correct? (y/n): \n>> ")
    while double_check.lower() not in "y":
        _directory = input("Enter your project directory\n>> ")
        double_check = input(f"You entered '{directory}', is that correct? (y/n): \n>> ")
    return directory


def get_vars() -> list[str]:
    variables = []
    variable_check = " "
    while variable_check.lower() not in "y":
        variable = input("Enter a variable name. (If you have no more variables to add press enter.)\n>> ")
        variables.append(variable)
        print("\nvariables =", variables)
        while variable != "":
            variable = input("Enter a variable name. (If you have no more variables to add press enter.)\n>> ")
            if variable:
                variables.append(variable)
                print("\nvariables =", variables)
        print(variables)
        variable_check = input("all variables look good? (y/n)\n>> ")
    return variables


def build():
    directory = get_dir()
    variables = get_vars()
    print("building...")
    generate_variable_json(directory, variables)
    print("Done!")


if __name__ == "__main__":
    build()
