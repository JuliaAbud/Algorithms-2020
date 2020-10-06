#Use "invoke compileht" to compile the .so file
from invoke import task

@task
def compileAny(c, cfile):
    c.run("gcc -c -Wall -Werror -fpic "+cfile+".c -I /usr/include/python3.8")
    c.run("gcc -shared -o "+cfile+".so "+cfile+".o")
    print("* Complete")

@task
def compileht(c):
    cfile="Hashtable"
    c.run("invoke compileAny --cfile "+cfile)

@task
def compileTry(c):
    cfile="Hashtable"
    c.run("gcc -o "+cfile+" "+cfile+".c -lm")
    print("* Complete")