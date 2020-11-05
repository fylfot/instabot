class TwoFactorRequiredException(Exception):
    device_id = None
    two_factor_identifier = None

    def __init__(self, message, device_id, two_factor_identifier):
        super().__init__(message)
        self.device_id = device_id
        self.two_factor_identifier = two_factor_identifier


class CheckpointChallengeRequiredException(Exception):
    challenge_url = None

    def __init__(self, message, challenge_url):
        super().__init__(message)
        self.challenge_url = challenge_url


class InstagramCredentialsException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
