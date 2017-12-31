#!/usr/bin/env python3

#imports
import datetime as d
import dateutil.parser as p
import os
import time
import yaml



class Entry:
    def __init__(self,in_time,out_time):
        self.in_time = p.parse(in_time)
        self.out_time = p.parse(out_time)
        assert(self.in_time < self.out_time)


class Project:
    def __init__(self, name):
        self.name = name
        self.entries = []

    def add_entry (self, ety):
        self.entries.append(ety)
        #print(self.entries)
        

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
    def to_yaml(journal):
        # make a journal into a dictionary
        foobar = [Journal([a,b]),Journal([c,d,e]),Journal([f])]
        d = dict([q.projects for q in foobar])
        print(str(d))
        print(d.keys())

        # convert dictonary into string
        data_write = open('d.yaml','w')
        yaml.dump(d,data_write,default_flow_style = False)


def display_projects(yaml_string):
    jnl = Journal.from_yaml(yaml_string)
##    for p in jnl.projects:
##        print(p.name)
    print([p.name for p in jnl.projects]) #nts: get rid of quotes

def main():
    #TODO: make portable
    homedir = os.environ['HOME']
    yaml_file = open(homedir + '/PrgProjects/pclock/sched1.yaml','r')
    yaml_file_contents = yaml_file.read()

    
    print('''pclock, v0.0.0
    a = add entry
    p = projects
    s = project status
    q,x,exit,quit = exit''')
   
    while True:
        ipt = input('pclock> ')
        ipt = ipt.strip()
        if 'a' == ipt:
            print('add entry')
            
        elif 'p' == ipt:
            print('display projects')
            display_projects(yaml_file_contents)
            
        elif 's' == ipt:
            print('display status of projects')
            
        elif ipt in ['q','x','exit','quit']:
            print('good bye')
            break
        
if '__main__' == __name__ :
    main()
