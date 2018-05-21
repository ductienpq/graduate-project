class portJSON():
    def __init__(self,define,name):
        print "[JSON] INIT", name
        self.Define      =   define
        self.Name        =   name      
        self.Details     =   None
        self.State       =   None
        self.Start       =   None
        self.End         =   None

    def newJSON(self,start,end,state, Debug=None):
        if Debug:
            print "[JSON] NEW"
        if state!=self.State:
            self.State       =   int(state)
                    
        if start!=self.Start:
            self.Start       =   start
        
        if end!=self.End:
            self.End         =   end

    def showJSON(self):
        print "[SHOW] NAME:%s | State:%s | Start:%s | End:%s" %(self.Name,self.State,self.Start,self.End)

        

if __name__=='__main__':
    pass
    #p=portJSON("A","PORT A")
