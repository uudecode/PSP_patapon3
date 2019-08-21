from typing import Tuple, List

LOGGING_FORMAT: str = '%(asctime)-15s %(message)s'
INITIAL_GAP = 0x40
END_POINTER = 0x52088
BLOCK_SIZE = 0x188
FLOAT_FORMAT = '<f'
INT_FORMAT = '<i'
BOOL_FORMAT = '?'
BASIC_STATS: List[Tuple] = [(0x24, 'HPBase', FLOAT_FORMAT),
                            (0x28, 'HPScaling', FLOAT_FORMAT),
                            (0x30, 'FeverSpeed', FLOAT_FORMAT),
                            (0x34, 'SprintSpeed', FLOAT_FORMAT),
                            (0x38, 'AttackSpeed', FLOAT_FORMAT),
                            (0x40, 'MinDMG', FLOAT_FORMAT),
                            (0x44, 'MinDMGScaling', FLOAT_FORMAT),
                            (0x48, 'MaxDMG', FLOAT_FORMAT),
                            (0x4C, 'MaxDMGScaling', FLOAT_FORMAT),
                            (0x54, 'Power', FLOAT_FORMAT),
                            (0x58, 'PowerScaling', FLOAT_FORMAT),
                            (0x5C, 'ShieldBreak', FLOAT_FORMAT),
                            (0x60, 'ShieldBreakScaling', FLOAT_FORMAT),
                            (0xF4, 'Defense', FLOAT_FORMAT),
                            (0xF8, 'DefenseScaling', FLOAT_FORMAT),
                            (0xFC, 'Evasion', FLOAT_FORMAT),
                            (0x100, 'EvasionScaling', FLOAT_FORMAT),
                            (0x104, 'Weight', FLOAT_FORMAT),
                            (0x108, 'WeightScaling', FLOAT_FORMAT),
                            (0x6C, 'CritBase', FLOAT_FORMAT),
                            (0x88, 'CritScaling', FLOAT_FORMAT),
                            (0x70, 'KBBase', FLOAT_FORMAT),
                            (0x8C, 'KBScaling', FLOAT_FORMAT),
                            (0x74, 'StaggerRate', FLOAT_FORMAT),
                            (0x90, 'StaggerRateScaling', FLOAT_FORMAT),
                            (0x78, 'FireRate', FLOAT_FORMAT),
                            (0x94, 'FireRateScaling', FLOAT_FORMAT),
                            (0x7C, 'SleepRate', FLOAT_FORMAT),
                            (0x98, 'SleepRateScaling', FLOAT_FORMAT),
                            (0x80, 'FreezeRate', FLOAT_FORMAT),
                            (0x9C, 'FreezeRateScaling', FLOAT_FORMAT),
                            (0x84, 'PoisonRate', FLOAT_FORMAT),
                            (0xA0, 'PoisonRateScaling', FLOAT_FORMAT),
                            (0x144, 'CritRes', FLOAT_FORMAT),
                            (0x160, 'CritResScaling', FLOAT_FORMAT),
                            (0x148, 'KBRes', FLOAT_FORMAT),
                            (0x164, 'KBResScaling', FLOAT_FORMAT),
                            (0x14C, 'StaggerRes', FLOAT_FORMAT),
                            (0x168, 'StaggerResScaling', FLOAT_FORMAT),
                            (0x150, 'FireRes', FLOAT_FORMAT),
                            (0x16C, 'FireResScaling', FLOAT_FORMAT),
                            (0x154, 'SleepRes', FLOAT_FORMAT),
                            (0x170, 'SleepResScaling', FLOAT_FORMAT),
                            (0x158, 'FreezeRes', FLOAT_FORMAT),
                            (0x174, 'FreezeResScaling', FLOAT_FORMAT),
                            (0x15C, 'PoisonRes', FLOAT_FORMAT),
                            (0x178, 'PoisonResScaling', FLOAT_FORMAT),
                            (0xB4, 'DemonsX', FLOAT_FORMAT),
                            (0xD4, 'DemonsXScaling', FLOAT_FORMAT),
                            (0xB8, 'UndeadX', FLOAT_FORMAT),
                            (0xD8, 'UndeadXScaling', FLOAT_FORMAT),
                            (0xBC, 'ShellsX', FLOAT_FORMAT),
                            (0xDC, 'ShellsXScaling', FLOAT_FORMAT),
                            (0xC0, 'DragonsX', FLOAT_FORMAT),
                            (0xE0, 'DragonsXScaling', FLOAT_FORMAT),
                            (0xC4, 'GiantsX', FLOAT_FORMAT),
                            (0xE4, 'GiantsXScaling', FLOAT_FORMAT),
                            (0xC8, 'WoodX', FLOAT_FORMAT),
                            (0xE8, 'WoodXScaling', FLOAT_FORMAT),
                            (0xCC, 'StoneX', FLOAT_FORMAT),
                            (0xEC, 'StoneXScaling', FLOAT_FORMAT),
                            (0xD0, 'MetalsX', FLOAT_FORMAT),
                            (0xF0, 'MetalsXScaling', FLOAT_FORMAT),
                            (0x118, 'SlashX', FLOAT_FORMAT),
                            (0x11C, 'StrikeX', FLOAT_FORMAT),
                            (0x120, 'StabX', FLOAT_FORMAT),
                            (0x124, 'CrushX', FLOAT_FORMAT),
                            (0x128, 'FlameX', FLOAT_FORMAT),
                            (0x12C, 'IceX', FLOAT_FORMAT),
                            (0x130, 'ShockX', FLOAT_FORMAT),
                            (0x134, 'PoisonX', FLOAT_FORMAT),
                            (0x138, 'SoundX', FLOAT_FORMAT),
                            (0x13C, 'LightX', FLOAT_FORMAT),
                            (0x13C, 'DarkX', FLOAT_FORMAT),


                            ]


















CHECK_BOXES: List[Tuple] = [(0xA4, 'Slash', BOOL_FORMAT),
                            (0xA5, 'Strike', BOOL_FORMAT),
                            (0xA6, 'Stab', BOOL_FORMAT),
                            (0xA7, 'Crush', BOOL_FORMAT),
                            (0xA8, 'Fire', BOOL_FORMAT),
                            (0xA9, 'Ice', BOOL_FORMAT),
                            (0xAA, 'Lightning', BOOL_FORMAT),
                            (0xAB, 'Poison', BOOL_FORMAT),
                            (0xAC, 'Sound', BOOL_FORMAT),
                            (0xAD, 'Light', BOOL_FORMAT),
                            (0xAE, 'Darkness', BOOL_FORMAT),
                            (0xAF, 'Burn', BOOL_FORMAT),
                            (0xB0, 'Venom', BOOL_FORMAT),
                            (0x17E, 'CritImm', BOOL_FORMAT),
                            (0x17F, 'StaggerImm', BOOL_FORMAT),
                            (0x180, 'KBImm', BOOL_FORMAT),
                            (0x181, 'FireImm', BOOL_FORMAT),
                            (0x182, 'SleepImm', BOOL_FORMAT),
                            (0x183, 'IceImm', BOOL_FORMAT),
                            (0x184, 'PoisonImm', BOOL_FORMAT),
                            (0x185, 'TumbleImm', BOOL_FORMAT),





                            ]




