from abc import ABC, abstractmethod


class Authentication(ABC):
    @abstractmethod
    def authenticate(self, credential):
        pass


class PasswordAuthentication(Authentication):
    def __init__(self, stored_password):
        self.stored_password = stored_password

    def authenticate(self, credential):
        return credential == self.stored_password


class OTPAuthentication(Authentication):
    def __init__(self, generated_otp):
        self.generated_otp = generated_otp

    def authenticate(self, credential):
        return credential == self.generated_otp


class BiometricAuthentication(Authentication):
    def __init__(self, registered_fingerprint):
        self.registered_fingerprint = registered_fingerprint

    def authenticate(self, credential):
        return credential == self.registered_fingerprint


def login(method, credential):
    """Works with any Authentication object through the abstract interface."""
    status = "SUCCESS" if method.authenticate(credential) else "FAILED"
    print(f"{type(method).__name__}: {status}")


login(PasswordAuthentication("secret@123"), "secret@123")
login(OTPAuthentication("482910"), "111111")
login(BiometricAuthentication("FP-A1B2C3"), "FP-A1B2C3")
