from .base import Base
import subprocess


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'z'
        self.kind = 'directory'

    def gather_candidates(self, context):
        cmd = 'cat ~/.z | cut -d"|" -f 1 | sort | uniq'
        proc = subprocess.Popen(
                cmd, 
                shell=True, 
                stdout=subprocess.PIPE,
                universal_newlines=True)
        path = proc.comminucate().split()
        return [{'word': path, 'action__path': path}]
