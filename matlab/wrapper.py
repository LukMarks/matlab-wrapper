from configuration.ode_configuration import OdeConfiguration
from matlab.solver import Solver


class MatlabWrapper:
    _equation_parameter_file_path: str = None
    _equation_solved_file_path: str = None
    _solver: Solver = None
    job_configuration: OdeConfiguration = None

    def __init__(self, configuration=OdeConfiguration):
        self.job_configuration = configuration
        self.set_solver_engine()

    def set_solver_engine(self):
        if isinstance(self.job_configuration.solver_engine, Solver):
            self._solver = self.job_configuration.solver_engine
        else:
            try:
                self._solver = Solver[self.job_configuration.solver_engine.lower()]
            except KeyError:
                raise AttributeError(f"Select solver is not valid try using matlab or octave")
            except Exception as e:
                raise e
