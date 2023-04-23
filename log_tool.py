class Log(object):
    log_id = 0
    log_action = None

class LogSetup(Log):
    player_one_lives_counter = 0
    player_two_lives_counter = 0
    player_one_shells = 0
    player_two_shells = 0
    
    def SetInfo( self, id, p1_lives, p2_lives, p1_shells, p2_shells, action):
        self.log_id = id
        self.player_one_lives_counter = p1_lives
        self.player_two_lives_counter = p2_lives
        self.player_one_shells = p1_shells
        self.player_two_shells = p2_shells
        self.log_action = action

class LogClash(Log):
    pass

class LogResult(Log):
    pass

class LogTool:
    Logs = []
    counter = 0

    def __init__(self) -> None:
        pass