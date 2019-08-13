from typing import Tuple, List

LOGGING_FORMAT: str = '%(asctime)-15s %(message)s'
INITIAL_GAP = 0x40
BLOCK_SIZE = 0x188
FLOAT_FORMAT = '<f'
INT_FORMAT = '<i'
BASIC_STATS: List[Tuple] = [(0x24, 'HPBase', FLOAT_FORMAT),
                            (0x28, 'HPScaling', FLOAT_FORMAT)]