class DeploymentNotFound(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class NameInvalid(Exception):
    def __init__(self):
        self.message = "error: user name or db name invalid"
        super().__init__(self.message)


class InvalidUsername(Exception):
    def __init__(self):
        self.message = "error: user name doesnt match ths deployment"
        super().__init__(self.message)


class MongoError(Exception):
    def __init__(self):
        self.message = "an error occurred using mongodb"
        super().__init__(self.message)


class AuthorizationError(Exception):
    def __init__(self):
        self.message = "error: authorization failed"
        super().__init__(self.message)
