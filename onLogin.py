import os, sys, subprocess

class userLogin():
    def __init__(self):
        pass

    def process(self, user, startupcmd):
        p = subprocess.Popen([startupcmd], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        r = p.communicate()[0]
        r = r.decode()

        return r