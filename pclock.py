#!/usr/bin/env python3

#imports
import datetime as d
import dateutil.parser as p
import os
import time
import yaml


##
#Title: pclock
#Authors: Peter H and Trevor D
##

class Entry:
    def __init__(self,in_time,out_time):
        #nts: "self" is similar to "this" in java
        self.in_time = p.parse(in_time)
        self.out_time = p.parse(out_time)
        assert(self.in_time < self.out_time)

#test dateutil
#print(p.parse('12/24/17 12:00 MDT'))

#nts: example instanciation of class
e = Entry("12/20/2017 7:00PM MST","12/20/17 8:00PM MST")
print(e.in_time)
print(e.out_time)

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


    # read string and convert to journal object
    def from_yaml(yaml_string):
        J = Journal()
        data_load = yaml.load(yaml_string)
        #print(data_load.keys())

        for (k,v) in data_load.items():
            proj = Project(k)
            print(k)
            
            for e in v:
                print(e)
                ety = Entry(**e)
                proj.add_entry(ety)

            J.projects.append(proj)
            
        #print(data_load)
        #print(J)

        
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



homedir = os.environ['HOME']
#print(homedir)
print(homedir + '/PrgProjects/pclock/sched1.yaml')
f = open(homedir + '/PrgProjects/pclock/sched1.yaml','r')
Journal.from_yaml(f.read())
