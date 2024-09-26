from matlab.solver import Solver

class MatlabWrapper:

    _equation_parameter_file_path:str = None
    _equation_solved_file_path:str = None
    _solver: Solver = None


    def __init__(self):
        pass

    def set_solver_engine(self, solver_engine: str|Solver):
        if isinstance(solver_engine, Solver):
            self._solver = solver_engine
        else:
            try:
                self._solver = Solver[solver_engine.lower()]
            except KeyError:
                raise AttributeError(f"Select solver is not valid try using matlab or octave")
            except Exception as e:
                raise e



