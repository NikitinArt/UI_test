
class FinishPage:
    def __init__(self, driver):
        self.driver = driver

    def check(self, errors):
        assert not errors, "errors occured:\n{}".format("\n".join(errors))
