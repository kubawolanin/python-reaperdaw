class ReaperError(Exception):
    """Raised when REAPER API request ended in error.
    Attributes:
        status_code - error code returned by Reaper
        status - more detailed description
    """

    def __init__(self, status_code, status):
        self.status_code = status_code
        self.status = status
