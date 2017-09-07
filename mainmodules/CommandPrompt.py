import cmdcopy
import subprocess
import os
from shlex import split


class HelloWorld(cmdcopy.Cmd):
    os.chdir('user')  # changes directory to 'user'

    def do_greet(self, person):
        '''
        greet [person]
        Greet the named person
        '''
        if person:
            print('hi ' + person)
        else:
            print('hi')

    def do_EOF(self,nothing):
        print()
        return True

    """
builtins
    """


    def do_cd(self, directory): #change directory
        '''
        syntax 'cd [directory]'
        change to [directory]
        '''

        args = directory.split(' ')
        # next 6 lines are cheater proof biz
        if args[0] == 'game':
            print('not a directory')
            return
        if os.path.split(os.getcwd())[1] == 'user' and args[0] == '..':
            print('not a directory')
            return

        try:
            os.chdir(args[0])
        except OSError:
            print('not a directory')

    def do_pwd(self, nothing):
        '''
        syntax 'pwd'
        print working directory
        '''
        subprocess.check_call('pwd')

    def do_tree(self,line): # make a
        pass

    def do_ls(self,args):


        try:
            subprocess.check_call(['ls', args])
        except:
            l = os.listdir(os.getcwd())
            for file in l:
                print(file)


    def do_cat(self, file):
        try:
            subprocess.check_call(['cat', file])
            print()
        except:
            raise

    def do_altextedit(self, file):
        pass
        while True:
            raw_input()








    def do_txtedit(self, file): # writes a () to the end of the last word
        data = []
        while True:
            user_data = raw_input()
            if user_data == 'exit()':

                f = open(file, 'w')
                # print(tobewriten)
                f.write("\n".join(str(x) for x in data))
                break
            else:
                data.append(user_data)


    def do_touch(self,file):
        subprocess.call(['touch', file])

if __name__ == 'mainmodules.CommandPrompt': # it works with this!!!
    HelloWorld().cmdloop()
