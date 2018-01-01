#!/usr/bin/env python3

#imports
import datetime as d
import dateutil.parser as p
import os
import time
import yaml


class Entry:
    def __init__(self,in_time,out_time = None):
        self.in_time = p.parse(in_time)
        try:
            self.out_time = p.parse(out_time)
            assert(self.in_time < self.out_time)
        except:
            self.out_time = None


class Project:
    def __init__(self, name):
        self.name = name
        self.entries = []

    def add_entry (self, ety):
        self.entries.append(ety)
        #print(self.entries)

    def clock_in(self):
        t = time.strftime('%c %z',time.localtime())
        #t = d.datetime.now()
        self.add_entry(Entry(t ,None))
        print(t)

    #nts: add t as argument to pass a preset clockout time ie for scheduled worktimes
    def clock_out(self):
        ell = len(self.entries)
        no_clockout_indeces = [i for i in range(0,ell) if None == self.entries[i].out_time]
        assert(1 == len(no_clockout_indeces))
        no_clockout_idx = no_clockout_indeces[0]
        t = time.strftime('%c %z',time.localtime())
        self.entries[no_clockout_idx].out_time = t
        print(t)
        

class Journal:
    def __init__(self, projects = []):
       self.projects = projects
       
    # read from yaml file and convert to Journal object
    def from_yaml(yaml_string):
        J = Journal()
        data_load = yaml.load(yaml_string)
        #print(data_load.keys())

        for (k,v) in data_load.items():
            proj = Project(k)
            
            for e in v:
                #print(e)
                ety = Entry(**e)
                proj.add_entry(ety)

            J.projects.append(proj)

        return J
        
    # convert journal object to dictionry and convert to string
    # inverse of "from_yaml" function (needs to be unit tested)
##    def to_yaml(journal):
##        # make a journal into a dictionary
##        foobar = [Journal([a,b]),Journal([c,d,e]),Journal([f])]
##        d = dict([q.projects for q in foobar])
##        print(str(d))
##        print(d.keys())
##
##        # convert dictonary into string
##        data_write = open('d.yaml','w')
##        yaml.dump(d,data_write,default_flow_style = False)


    def add_project(prj):
        pass
    
    def display_projects(jnl):
##      for p in jnl.projects:
##          print(p.name)
        print([p.name for p in jnl.projects]) #nts: get rid of quotes




def main():
    #TODO: make portable
    homedir = os.environ['HOME']
    yaml_file = open(homedir + '/PrgProjects/pclock/sched1.yaml','r')
    yaml_file_contents = yaml_file.read()
    jnl = Journal.from_yaml(yaml_file_contents)
    
    print('''pclock, v0.0.0
    i = clock in
    o = clock out
    p = projects
    s = project status
    q,x,exit,quit = exit''')
   
    while True:
        ipt = input('pclock> ')
        ipt = ipt.strip()
        
        if 'i' == ipt:
            print('clock in \n')
            prjs = jnl.projects
            num_projects = len(prjs)
            
            for i in range(num_projects):
                this_prj = prjs[i]
                print(i, this_prj.name)
                
            n = input('choose a project ')
            num = int(n)
            
            if  num >= len(prjs):
                print('not in list')
            else:
                print(prjs[num].name)
                prjs[num].clock_in()
                
            
        elif 'o' == ipt:
            print('clock out')
            prjs = jnl.projects
            num_projects = len(prjs)
            
            for i in range(num_projects):
                this_prj = prjs[i]
                print(i, this_prj.name)
                
            n = input('choose a project to clock out ')
            num = int(n)
            
            if  num >= len(prjs):
                print('not in list')
            else:
                print(prjs[num].name)
                prjs[num].clock_out()
            
        elif 'p' == ipt:
            print('display projects')
            Journal.display_projects(jnl)
            
        elif 's' == ipt:
            #nst: clocked in or out
            print('display status of projects')
            
        elif ipt in ['q','x','exit','quit']:
            print('good bye')
            break
        
if '__main__' == __name__ :
    main()
