from abc import ABC, abstractmethod

from matlab import Solver


class AbstractKernel(ABC):

    solver: Solver = None
    result_path:str = None
    template: str = None

    def __init__(self):
        ...

    @abstractmethod
    def set_template(self):
        ...

    @abstractmethod
    def start_external_execution(self):
        ...

    @abstractmethod
    def start_file_watcher(self):
        ...