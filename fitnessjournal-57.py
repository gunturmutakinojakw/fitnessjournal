# === Stage 57: Add structured result objects for command handlers ===
# Project: FitnessJournal
class Result:
    def __init__(self, status, data=None, message=None):
        self.status = status
        self.data = data
        self.message = message

    def to_dict(self):
        payload = {"status": self.status}
        if self.data is not None:
            payload["data"] = self.data
        if self.message:
            payload["message"] = self.message
        return payload


class OkResult:
    def __init__(self, data=None, message=None):
        self._result = Result("ok", data, message)

    def to_dict(self):
        return self._result.to_dict()


class BadRequestResult:
    def __init__(self, message=None):
        self._result = Result("bad_request", None, message)

    def to_dict(self):
        return self._result.to_dict()


class NotFoundResult:
    def __init__(self, message=None, resource=None):
        self._result = Result("not_found", {"resource": resource}, message)

    def to_dict(self):
        return self._result.to_dict()


class ConflictResult:
    def __init__(self, message=None):
        self._result = Result("conflict", None, message)

    def to_dict(self):
        return self._result.to_dict()
