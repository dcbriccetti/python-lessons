import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger('permute')


def chars_range(start, end):
    return [chr(a) for a in range(ord(start), ord(end) + 1)]


class Permuter:
    def __init__(self, chars, length):
        self.chars = chars
        self.length = length
        self.generated = 0

    def next(self, starting_sequence=''):
        log.debug('next(%s)' % starting_sequence)
        for char in self.chars:
            result = starting_sequence + char
            self._count()
            yield result
            if len(result) < self.length:
                for nested_result in self.next(result):
                    self._count()
                    yield nested_result

    def _count(self):
        self.generated += 1
        if self.generated % 1000000 == 0:
            log.info('Generated %.3e', self.generated)
