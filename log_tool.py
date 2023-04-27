import time

class Log(object):
    log_id = 0
    log_action = None

class LogSetup(Log):
    player_one_lives_counter = 0
    player_two_lives_counter = 0
    player_one_shells = 0
    player_two_shells = 0
    mode = 0
    
    def SetInfo( self, id, p1_lives, p2_lives, p1_shells, p2_shells, action, mode):
        self.log_id = id
        self.player_one_lives_counter = p1_lives
        self.player_two_lives_counter = p2_lives
        self.player_one_shells = p1_shells
        self.player_two_shells = p2_shells
        self.log_action = action
        self.mode = mode

    def ToString(self):
        result = "Log ID: "
        result += str(self.log_id)
        result += ", P1 Lives:"
        result += str(self.player_one_lives_counter)
        result += ", P2 Lives:"
        result += str(self.player_two_lives_counter)
        result += ", P1 Shells:"
        result += str(self.player_one_shells)
        result += ", P1 Shells:"
        result += str(self.player_two_shells)
        result += ", Action:"
        result += str(self.log_action)
        result += ", Mode:"
        result += str(self.mode)
        return result

class LogClash(Log):
    player_one_choice = 0
    player_two_choice = 0

    def SetInfo(self, p1_choice, p2_choice, id, action):
        self.player_one_choice = p1_choice
        self.player_two_choice = p2_choice
        self.log_id = id
        self.log_action = action

    def ToString(self):
        result = "Log ID: "
        result += str(self.log_id)
        result += ", P1 Choice:"
        result += str(self.player_one_choice)
        result += ", P2 Choice:"
        result += str(self.player_two_choice)
        result += ", Action:"
        result += str(self.log_action)
        return result

class LogResult(Log):
    result = 0
    number_of_rounds = 0

    def SetInfo(self, final_result, rounds, id, action):
        self.result = final_result
        self.number_of_rounds = rounds
        self.log_id = id
        self.log_action = action
        
    def ToString(self):
        result = "Log ID: "
        result += str(self.log_id)
        result += ", Result:"
        result += str(self.result)
        result += ", Number of rounds:"
        result += str(self.number_of_rounds)
        result += ", Action:"
        result += str(self.log_action)
        return result

class LogTool:
    Logs = []
    counter = 0


    def NewEntry(self,NewLog):
        self.Logs.append(NewLog)
        self.counter += 1


    def Export_as_txt(self, Name:str ):
        NameOfFile = Name + ".txt"
        with open(NameOfFile, "w") as file:
            for x in self.Logs:
                file.write(x + '\n')
            file.close()


    def GetId(self):
        return self.counter
    
    def PrintLogs(self):
        print(self.Logs)

# test

Obj_1 = LogSetup()
Obj_1.SetInfo(1,2,3,4,5,"SETUP","Player VS CPU")
print(Obj_1.ToString())