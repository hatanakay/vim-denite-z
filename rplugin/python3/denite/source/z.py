from .base import Base
import subprocess


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'z'
        self.kind = 'directory'

    def gather_candidates(self, context):
        cmd = ['cat ~/.z', '|',  'awk', '\'{print $2}\'']
        return [{'word': path, 'action__path': path}
                for path
                in subprocess.run(cmd,
                                  check=True,
                                  universal_newlines=True,
                                  stdout=subprocess.PIPE
                                  ).stdout.split()]
