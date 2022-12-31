class SSHConfig(object):

    def __init__(self, filename=None):
        if filename is not None:
            self.read(filename)
        else:
            self.conf = dict()

    def read(self, filename):
        self.conf = dict(line.decode("utf-8").rstrip().split(" ", 1) for line in open(filename))

    def write(self, filename):
        with open(filename, "w") as f:
            for key, value in self.conf.items():
                f.write("%s %s\n".encode("utf-8") % (key, value))

    def set(self, key, value):
        self.conf[key] = value

    def get(self, key):
        return self.conf.get(key, None)
