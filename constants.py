from typing import Tuple, List

LOGGING_FORMAT: str = '%(asctime)-15s %(message)s'
INITIAL_GAP = 0x40
END_POINTER = 0x52088
BLOCK_SIZE = 0x188
FLOAT_FORMAT = '<f'
INT_FORMAT = '<i'
BASIC_STATS: List[Tuple] = [(0x24, 'HPBase', FLOAT_FORMAT),
                            (0x28, 'HPScaling', FLOAT_FORMAT),
                            (0x30, 'FeverSpeed', FLOAT_FORMAT),
                        (0x34, 'SprintSpeed', FLOAT_FORMAT),
(0x40, 'MinDMG', FLOAT_FORMAT),
(0x44, 'MinDMGScaling', FLOAT_FORMAT),
(0x4C, 'MaxDMG', FLOAT_FORMAT),
(0x50, 'MaxDMGScaling', FLOAT_FORMAT),
(0x58, 'Power', FLOAT_FORMAT),
(0x5C, 'PowerScaling', FLOAT_FORMAT),
(0x60, 'ShieldBreak', FLOAT_FORMAT),
(0x64, 'ShieldBreakScaling', FLOAT_FORMAT),
(0xF4, 'Defense', FLOAT_FORMAT),
(0xF8, 'DefenseScaling', FLOAT_FORMAT),
(0xFC, 'Evasion', FLOAT_FORMAT),
(0x100, 'EvasionScaling', FLOAT_FORMAT),
(0x104, 'Weight', FLOAT_FORMAT),
(0x108, 'WeightScaling', FLOAT_FORMAT),
]

