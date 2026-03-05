class DeploymentNotFound(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class NameInvalid(Exception):
    def __init__(self):
        self.message = "error: user name or db name invalid"
        super().__init__(self.message)


class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)