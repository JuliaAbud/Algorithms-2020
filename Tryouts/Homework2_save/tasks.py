#Use "invoke compilerxsort" to compile the .so file
from invoke import task

@task
def compileAny(c, cfile):
    c.run("gcc -c -Wall -Werror -fpic "+cfile+".c -I /usr/include/python3.8")
    c.run("gcc -shared -o "+cfile+".so "+cfile+".o")
    print("* Complete")

@task
def compilerxsort(c):
    cfile="rxSort"
    cfile2="queue"
    c.run("gcc -c -Wall -Werror -fpic "+cfile2+".c -I /usr/include/python3.8")
    c.run("gcc -c -Wall -Werror -fpic "+cfile+".c -I /usr/include/python3.8")
    c.run("gcc -shared -o "+cfile+".so "+cfile+".o "+cfile2+".o")
    print("* Complete")
    #c.run("invoke compileAny --cfile "+cfile2)