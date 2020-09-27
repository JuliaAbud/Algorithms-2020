#Use "invoke compilePQueue" to compile the .so file
from invoke import task

@task
def compileAny(c, cfile):
    c.run("gcc -c -Wall -Werror -fpic "+cfile+".c -I /usr/include/python3.8")
    c.run("gcc -shared -o "+cfile+".so "+cfile+".o")
    print("* Complete")

@task
def compilePQueue(c):
    cfile="pQueue"
    c.run("invoke compileAny --cfile "+cfile)