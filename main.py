from curses import wrapper

from pydantic import TypeAdapter

from configuration.ode_configuration import OdeConfiguration
import sys
import json

from matlab import MatlabWrapper


def set_ode_configuration(configuration_path: str) -> OdeConfiguration:
    try:
        with open(configuration_path, "r") as configuration_file:
            configurations = json.load(configuration_file)
            configuration_file.close()
        return TypeAdapter(OdeConfiguration).validate_python(configurations)
    except FileNotFoundError as file_not_found:
        raise FileNotFoundError("Could not find the configuration file, please verify your cli parameter")


if __name__ == '__main__':

    configuration = set_ode_configuration(sys.argv[1])
    matlab_wrappler = MatlabWrapper(configuration)
