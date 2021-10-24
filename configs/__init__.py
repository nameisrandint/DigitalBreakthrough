import os
import shlex
import argparse
import logging
from typing import Optional, Union, Dict, List

import yaml
import numpy as np

logger = logging.getLogger(__name__)
__file_path = os.path.realpath(__file__)  # abs path to this script
CONFIGS_DIR = os.path.dirname(__file_path)


class NotRealized(Exception):
    pass


class ProjConfig:
    logger = logging.getLogger(__name__ + ".ProjConfig")

    class YMLConfigNotExists(Exception):
        pass

    class NumpyFileNotExists(Exception):
        pass

    def __init__(
            self, vk_token: str, qboard_access_key: str,
            dist_mat: Optional[Union[str, np.ndarray]] = None,
            qubo_mat: Optional[Union[str, list, np.ndarray, np.matrix]] = None,
            **kwargs
    ):
        self.logger.debug("Starting init of ProjConfig")
        if len(kwargs) > 0:
            self.logger.warning(f'Number of unknown params passed in: {len(kwargs)}. Values: {kwargs}')

        self.vk_token = vk_token
        self.qboard_access_key = qboard_access_key
        # If self.dist_mat, than it should be created randomly and self.qubo_mat should be calculated over it
        self.dist_mat: Optional[np.ndarray] = None  # distance matrix between N points
        self.qubo_mat: Optional[np.matrix] = None  # predefined Q matrix (the dist_mat will have no influence)
        if dist_mat is not None:
            self.dist_mat = self.load_dist_mat(dist_mat)
        if qubo_mat is not None:
            self.set_qubo_mat(qubo_mat)
        self.logger.debug("End init of ProjConfig")

    @classmethod
    def load_dist_mat(cls, dist_mat: Union[str, list, np.ndarray]) -> np.ndarray:
        if isinstance(dist_mat, str):
            # Expected to be path to '.npy' file:
            with open(dist_mat, 'rb') as f:
                cls.logger.info(f'Loading dist_mat from file: "{dist_mat}"')
                _dist_mat = np.load(f)
                cls.logger.debug(f'Loaded dist_mat: {_dist_mat}. type(_dist_mat)={type(_dist_mat)}')
                return _dist_mat

        elif isinstance(dist_mat, list):
            return np.array(dist_mat, dtype=float)

        elif isinstance(dist_mat, np.ndarray):
            return dist_mat

        else:
            raise TypeError(f"Not supported type of dist_mat={type(dist_mat)}. "
                            f"Available: Union[str, list, np.ndarray]")

    @classmethod
    def set_qubo_mat(cls, qubo_mat: Union[str, list, np.ndarray, np.matrix]) -> np.matrix:
        if isinstance(qubo_mat, str):
            # Expected to be path to '.npy' file:
            with open(qubo_mat, 'rb') as f:
                cls.logger.info(f'Loading qubo_mat from file: "{qubo_mat}"')
                _qubo_mat = np.load(f)
                cls.logger.debug(f'Loaded qubo_mat: {_qubo_mat}. type(qubo_mat)={type(_qubo_mat)}')
                return _qubo_mat

        if isinstance(qubo_mat, list):
            return np.matrix(qubo_mat)

        elif isinstance(qubo_mat, np.ndarray):
            return np.matrix(qubo_mat)

        elif isinstance(qubo_mat, np.matrix):
            return qubo_mat

        else:
            raise TypeError(f"Not supported type of qubo_mat={type(qubo_mat)}. "
                            f"Available: Union[str, list, np.ndarray, np.matrix]")

    @classmethod
    def init_from_yml(cls, yml_path: str):
        if not os.path.exists(yml_path):
            raise cls.YMLConfigNotExists(f'Not exists: "{yml_path}"')
        
        with open(yml_path, 'r') as stream:
            cls.logger.info(f'Opened YML-file: "{yml_path}"')
            yml_args: Dict[str, str] = yaml.load(stream, Loader=yaml.FullLoader)
        cls.logger.debug(f'Loaded params: {yml_args}')
        return cls(**yml_args)

    def load_dist_mat_excel(self, excel_path: str):
        raise NotRealized("Not added yet: loading of distance matrix from Excel-like files: '.csv'")

    @classmethod
    def argument_parser(cls) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(
            """
                Example of usage (for linux):
            $ python main.py -h  # to see this help 
            $ python main.py -yml "/home/user/repo/production.yml"
            
                Example of usage (for windows):
            $ TODO:
            $ TODO:
            """)
        # CONFIGS PARAMS:
        parser.add_argument("-yml", "--yml_path", type=str, required=True,
                            help='Path to YML-config with "vk_token", "qboard_access_key", "dist_mat", '
                                 r'"qubo_mat" keys. Example: {-yml "c:\repo\production.yml"} (for windows), '
                                 r'{-yml "/home/user/repo/production.yml"} (for linux). Required: True')

        # LOGGING PARAMS:
        parser.add_argument("-log", "--log_level",
                            # default=logging.INFO,
                            # type=lambda x: getattr(logging, x),
                            default='warning',
                            type=str,
                            choices=['debug', 'info', 'warning', 'error', 'critical'],
                            help="Provide logging level. Example: '--loglevel debug'. Default='warning'")
        parser.add_argument('-d', '--debug', action="store_const", dest="log_level",
                            const=logging.getLevelName(logging.DEBUG),
                            help="Sets the DEBUG-mode to logging. Using of this argument "
                                 "may overwrite the value of --log_level")
        parser.add_argument('-v', '--verbose', action="store_const", dest="log_level",
                            const=logging.getLevelName(logging.INFO),
                            help="Set the verbose mode to log level (INFO)")
        return parser
