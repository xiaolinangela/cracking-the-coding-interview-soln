class Call():
    def __init__(self):
        self.employee = None
    
    def get_handler():
        #check if employee is free to take the call or not
        return employee

    def apologize_and_wait(self):
        return print("All of our representitives are busy now, please wait")

class CallHandler:
    def __init__(self):
        self.respondents = ["respondents", "managers", "directors"]
        self.callQueues = deque()
    
    def dispatch(self,call):
        employee = call.get_handler()
        if employee:
            employee.receiveCall(call)
            call.setHandler(employee)
            self.callQueues.popleft()
        else:
            call.reply("please wait for free emplyee to reply")
            self.callQueues.append(call)

class Employee:
    def __init__(self,name,manager):
        self.name = name
        self.manager = manager
        self.call = None
    
    def isFree(self,call):
        if not self.call:
            self.call = call
            self.call.employee = self
        else:
            self.escalte(call)
    
    def escalate(self,call):
        if self.manager:
            self.manager.isFree(call)
        else:
            call.apologize_and_wait()

class Respondent(Employee):
    pass

class Manager(Employee):
    pass

class Director(Employee):
    pass