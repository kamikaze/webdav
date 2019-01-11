class WebDavException(Exception):
    pass


class NotValid(WebDavException):
    pass


class OptionNotValid(NotValid):
    def __init__(self, name, value, ns=''):
        self.name = name
        self.value = value
        self.ns = ns

    def __str__(self):
        return f'Option ({self.ns}{self.name}={self.value}) have invalid name or value'


class CertificateNotValid(NotValid):
    pass


class NotFound(WebDavException):
    pass


class LocalResourceNotFound(NotFound):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return f'Local file: {self.path} not found'


class RemoteResourceNotFound(NotFound):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return f'Remote resource: {self.path} not found'


class RemoteParentNotFound(NotFound):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return f'Remote parent for: {self.path} not found'


class ResourceTooBig(WebDavException):
    def __init__(self, path, size, max_size):
        self.path = path
        self.size = size
        self.max_size = max_size

    def __str__(self):
        return f'Resource {self.path} is too big, it should be less then {self.max_size} but actually: {self.size}'


class MethodNotSupported(WebDavException):
    def __init__(self, name, server):
        self.name = name
        self.server = server

    def __str__(self):
        return f'Method {self.name} not supported for {self.server}'


class ConnectionException(WebDavException):
    def __init__(self, exception):
        self.exception = exception

    def __str__(self):
        return self.exception.__str__()


class NoConnection(WebDavException):
    def __init__(self, hostname):
        self.hostname = hostname

    def __str__(self):
        return f'No connection with {self.hostname}'


# This exception left only for supporting original library interface.
class NotConnection(WebDavException):
    def __init__(self, hostname):
        self.hostname = hostname

    def __str__(self):
        return f'No connection with {self.hostname}'


class ResponseErrorCode(WebDavException):
    def __init__(self, url, code, message):
        self.url = url
        self.code = code
        self.message = message

    def __str__(self):
        return f'Request to {self.url} failed with code {self.code} and message: {self.message}'


class ServerException(WebDavException):
    def __init__(self, url, code, message):
        self.url = url
        self.code = code
        self.message = message

    def __str__(self):
        return f'WebDAV server failed to process request to {self.url} failed with code {self.code} and message:' \
            f' {self.message}'


class NotEnoughSpace(WebDavException):
    def __init__(self):
        pass

    def __str__(self):
        return 'Not enough space on the server'
