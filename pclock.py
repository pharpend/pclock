#!/usr/bin/env python3

#imports
import datetime as d
import dateutil.parser as p
import os
import time
import yaml


##
#Title: pclock
#Authors: Peter Harpending and Trevor Dick
##

class Entry:
    def __init__(self,in_time,out_time):
        #nts: "self" is similar to "this" in java
        self.in_time = p.parse(in_time)
        self.out_time = p.parse(out_time)
        assert(self.in_time < self.out_time)

#test dateutil
#print(p.parse('12/24/17 12:00 MDT'))

#nts: instanciation of class
e = Entry("12/20/2017 7:00PM MST","12/20/17 8:00PM MST")
print(e.in_time)
print(e.out_time)

class Project:
    def __init__(self, name):
        self.name = name
        self.entries = []


class Journal:
    def __init__(self, projects = []):
       self.projects = projects

    # read from yaml file and convert to string
    def from_yaml(yaml_string):
        data_load = yaml.load(f)
        print(data_load)
        
    # write to yaml file
    def to_yaml(journal):
        #with io.open('f.yaml','w') as outfile:
        #yaml.dump(f,outfile,default_flow_style = False)
        return None

p1 = Project("wrap presents")
p2 = Project("python code")
p3 = Project("find algebra books")
p4 = Project("sleep")

journal = [p1,p2,p3,p4]
print(journal)


homedir = os.environ['HOME']
#print(homedir)
print(homedir + '/.pclock.yaml')
f = open(homedir + '/.pclock.yaml','r')
print(f.read())
