#!/usr/bin/env python3

#imports
import datetime as d
import dateutil.parser as p
import os
import time
import yaml
##

"""
pclock v0.0.0
Authors: T.Dick and P.Harpending
"""

class Entry:
    def __init__(self,in_time,out_time = None):
        """Instanciate Entry class
        asserting that in time is sooner than out time

         Keyword args:
         in_time -- clock in time
         out_time -- clock out time (Default is None)
        """
        self.in_time = p.parse(in_time)
        try:
            self.out_time = p.parse(out_time)
            assert(self.in_time < self.out_time)
        except:
            self.out_time = None


class Project:
    def __init__(self, name):
        """Instanciate Project class

        Keyword args:
        name -- name of project that will be clocked in or out of
        """
        self.name = name
        self.entries = []

    def add_entry (self, ety):
        """Takes a project and adds a new entry at the end of the list of entries"""
        self.entries.append(ety)

    def clock_in(self):
        """Pulls current time to add as in_time to an entry"""
        t = time.strftime('%c %z',time.localtime())
        self.add_entry(Entry(t ,None))
        print(t ,'\n')

    #TODO: add t as argument to pass a preset clockout time i.e. for scheduled worktimes
    def clock_out(self):
        """Checks entries to see if out_time of an entry is empty
        If empty adds current time to empty out_time of an entry
        """
        ell = len(self.entries)
        no_clockout_indeces = [i for i in range(0,ell) if None == self.entries[i].out_time]
        assert(1 == len(no_clockout_indeces))
        no_clockout_idx = no_clockout_indeces[0]
        t = time.strftime('%c %z',time.localtime())
        self.entries[no_clockout_idx].out_time = t
        print(t ,'\n')
        
    def clocked_out(self):
        """Boolean function
        Returns a truth value for whether clocked in or not"""
        ell = len(self.entries)
        no_clockout_indeces = [i for i in range(0,ell) if None == self.entries[i].out_time]

        return( 0 == (len(no_clockout_indeces)) )
   
            
class Journal:
    def __init__(self, projects = []):
        """Instanciation of Journal class

        Keyword args:
        projects -- list of current working entries denoted as a Journal (Default is set to empty)
        """
        self.projects = projects
        
       
    def from_yaml(yaml_string):
        """Read from yaml file and convert to Journal object"""
        J = Journal()
        data_load = yaml.load(yaml_string)

        for (k,v) in data_load.items():
            proj = Project(k)
            
            for e in v:
                #print(e)  #NST: Print all in an out times for all entries
                ety = Entry(**e)
                proj.add_entry(ety)

            J.projects.append(proj)

        return J

    #TODO: add ability to make new journal entry
    def add_project(prj):
        """Create a new entry in the journal, a new project"""
        pass
    
    def display_projects(jnl):
        """Print out a list of all working entries of a journal"""
##      for p in jnl.projects:
##          print(p.name)
        print([p.name for p in jnl.projects]) #TODO: get rid of quotes




def main():
    """Main method
    
    Creates menus
    Opens and reads yaml file that contains entries and times
    Stores string from yaml file as a Journal object
    """
    #TODO: make portable
    homedir = os.environ['HOME']
    yaml_file = open(homedir + '/PrgProjects/pclock/sched1.yaml','r')
    yaml_file_contents = yaml_file.read()
    jnl = Journal.from_yaml(yaml_file_contents)
    
    print('''\n pclock, v0.0.0
    i = clock in
    o = clock out
    p = projects
    s = project status
    q, x, exit, quit = exit pclock \n''')
   
    while True:
        ipt = input('pclock> ')
        ipt = ipt.strip()
        
        if 'i' == ipt:
            print('\nSelect a project to clock into: ')
            prjs = jnl.projects
            num_projects = len(prjs)
            
            for i in range(num_projects):
                this_prj = prjs[i]
                print(i, this_prj.name)
                
            n = input('\nchoose a project: ')
            num = int(n)
            
            if  num >= len(prjs):
                print('\nnot in list \n')
            else:
                print('\n',prjs[num].name)
                prjs[num].clock_in()
                
            
        elif 'o' == ipt:
            print('\nWhich project would you like to clock out of? ')
            prjs = jnl.projects
            num_projects = len(prjs)
            
            for i in range(num_projects):
                this_prj = prjs[i]
                print(i, this_prj.name)
                
            n = input('\nchoose a project to clock out: ')
            num = int(n)
            
            if  num >= len(prjs):
                print('\nnot in list \n')
            else:
                print('\n',prjs[num].name)
                prjs[num].clock_out()
            
        elif 'p' == ipt:
            print('\nYour current projects: ')
            Journal.display_projects(jnl)
            
        elif 's' == ipt:
            print('\nStatus of projects:\n')
            for p in jnl.projects:
                #print(p.clocked_out(), p.name)
                y = p.clocked_out()
                if y == True:
                    print(p.name,'is clocked out.\n')
                else:
                    print(p.name,'has not been clocked out.\n')
            
        elif ipt in ['q','x','exit','quit']:
            print('Logged out of session ')
            break
        
if '__main__' == __name__ :
    main()
