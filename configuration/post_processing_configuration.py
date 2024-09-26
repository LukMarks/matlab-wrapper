from pydantic.dataclasses import dataclass


@dataclass
class PostProcessingConfiguration:
    save:bool= False
    result_file_path:str = None
    show_plot: bool = False

