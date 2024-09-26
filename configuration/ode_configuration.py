from pydantic.dataclasses import dataclass

from configuration.post_processing_configuration import PostProcessingConfiguration
from matlab import Solver


@dataclass
class OdeConfiguration:
    function_path:str
    solver_engine: Solver = Solver.MATLAB
    post_processing: PostProcessingConfiguration = PostProcessingConfiguration