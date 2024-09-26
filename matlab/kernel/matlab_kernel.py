from matlab import Solver
from matlab.kernel.abstract_kernel import AbstractKernel

class MatlabKernel(AbstractKernel):

    def __init__(self):
        super.__init__()
        self.solver = Solver.MATLAB