import hashlib


class DuplicateFilter:
    """
    Filters out duplicated messages
    """

    def __init__(self, logger):
        self.msg_hashes = set()
        self.logger = logger

    def filter(self, record):
        msg = str(record.msg).encode("utf8")
        msg_hash = hashlib.blake2s(msg)
        if msg_hash not in self.msg_hashes:
            self.msg_hashes.add(msg_hash)
            return msg
        else:
            return None

    def __enter__(self):
        self.logger.addFilter(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.logger.removeFilter(self)
