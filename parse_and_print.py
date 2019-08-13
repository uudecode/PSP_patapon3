import logging
from struct import unpack_from
from typing import List, Tuple

LOGGING_FORMAT: str = '%(asctime)-15s %(message)s'
DATA_DIRECTORY = r'data'
DATA_FILE = f'{DATA_DIRECTORY}/originstatusparam'
INITIAL_GAP = 0x40
BLOCK_SIZE = 0x188
BASIC_STATS: List[Tuple] = [(0x24, 'HP Base', '<f'),
                            (0x28, 'HP Scaling', '<f')]

def print_weapon_info(block: bytearray) -> None:
    weapon_name = block[0: 0 + 0x10].decode('utf-8')
    print(f'Weapon: {weapon_name}')
    print('Basic stats')
    for element in BASIC_STATS:
        value = unpack_from(element[2], block,element[0])
        print(f'{element[1]} {value}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT)
    logger = logging.getLogger('Parser Patapon file')
    logger.info('Parsing %s', DATA_FILE)
    with open(DATA_FILE, 'rb') as data_file:
        file_body = bytearray(data_file.read())
    file_length = len(file_body)
    logger.info('Read %s bytes', file_length)
    pointer: int = INITIAL_GAP
    while (pointer < file_length):
        print_weapon_info(file_body[pointer:pointer + BLOCK_SIZE])
        pointer += BLOCK_SIZE
