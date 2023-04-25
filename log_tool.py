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

    def ProduceString(self):
        pass

class LogClash(Log):
    player_one_choice = 0
    player_two_choice = 0

    def SetInfo(self, p1_choice, p2_choice):
        self.player_one_choice = p1_choice
        self.player_two_choice = p2_choice

    def ProduceString(self):
        pass

class LogResult(Log):
    result = 0
    number_of_rounds = 0

    def SetInfo(self, final_result, rounds):
        self.result = final_result
        self.number_of_rounds = rounds
        
    def ProduceString(self):
        pass

class LogTool:
    Logs = []
    counter = 0

    def Export_as_txt(self):
        pass