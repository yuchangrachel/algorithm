def getImportance(self, employees: List['Employee'], id: int) -> int:
        '''
        TOPIC: DFS 
        directed, weighted connected graph
        visited -> no need, since relation only one direction
        map{id: employees' info}
        THIS KIND RECURSION DONT HAVE BASE CASE
        '''
        self.dic = {}
        self.total = 0
        #store id: infor(include importance, list of subordinates)
        for employee in employees:
            self.dic[employee.id] = employee
        
        def subtotal(id2):
            self.total += self.dic[id2].importance
            for n_id in self.dic[id2].subordinates:
                subtotal(n_id)
            return self.total
        
        subtotal(id)
        return self.total