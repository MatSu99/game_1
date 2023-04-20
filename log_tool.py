class Log(object):
    log_id = 0
    log_action = None

class LogSetup(Log):
    pass

class LogClash(Log):
    pass

class LogResult(Log):
    pass

class LogTool:
    Logs = []
    counter = 0

    def __init__(self) -> None:
        pass