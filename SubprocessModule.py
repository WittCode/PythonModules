import subprocess

#The run() function was added in Python 3.5. In python 3, the lone * means that the following arguments are keyword-only arguments (they can only be provided using their name).
#Positional arguments must be included in the correct order. Keyword arguments are included with a keyword and an equals sign.
#Module allows you to spawn new processes.
#It is recommended to use run() function for cases it can handle. For advanced cases use Popen().
#run() returns a CompletedProcess instance.

print('\n')
print('No Arguments')
subprocess.run('dir', shell=True)   #Note that shell=True must be used for Windows when using shell arguments (echo, dir) etc.

print('\n')
print('Capture_Output Argument:')
#If capture_output is true then stdout and stderr will be captured.
capture_output = subprocess.run("dir", shell=True, capture_output=True)   #If capture_output=True then it won't be printed to console.
print("capture_output: " + str(capture_output))   #When capture_output=True stdout and stderr will be captured.
#This is the same as above except there will be no stderr because it is the same as stdout.
stdout_err_pipe = subprocess.run("dir", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)   #A pipe passes information from one process to another.
print("stdout & stderr: " + str(stdout_err_pipe))

#Here sublime text is opened for 1 second and then closes (child process is killed), even if you're currently typing into it.
print('\n')
print('Timeout Argument:')
try :
    timeout = subprocess.run('C:\Program Files\Sublime Text 3\sublime_text.exe', timeout=1) #Throws subprocess.TimeoutExpired
except subprocess.TimeoutExpired as error:
    print("Error: " + str(error))
    print("Sublime text has finished using timeout=1, TimeoutExpired exception was thrown.") #When the process terminates it prints this statement.

print('\n')
print('Input Argument')
input_arg = subprocess.run('echo', shell=True, capture_output=True, input='GAY MEN!', text=True)
#TODO

print('\n')
print('Check Argument:')
try :
    checked = subprocess.run("exit 1", shell=True, check=True)   #Throws a CalledProcessError exception. Because shell=True there is no error but if that wasn't there then there would be an error.
except subprocess.CalledProcessError as error:
    print("Error: " + str(error))    #Here the error is that it exited with a nonzero exit code.
    print("checked = true. If process exits with a non-zero exit code, then it calls CalledProcessError exception.")

print('\n')
print('Encoding Argument:')
encode_arg = subprocess.run("echo Encoding is ascii", shell=True, capture_output=True, encoding='ascii')    #If this encoding wasn't there it would be in bytes.
print(encode_arg.stdout)

print('\n')
print('Error Argument:')
#TODO

print('\n')
print('Text Argument:')
text_arg = subprocess.run('echo text=True', shell=True, capture_output=True, text=True)
print(text_arg.stdout)  #Because text=True the stdout will be printed as text and not bytes (prefixed with b).

print('\n')
print('Env Argument:')  #Defines environment variables for the new process.
#TODO

#The return value from run() is subprocess.CompletedProcess which represents a process that has finished.
print('\n')
print('subprocess.CompletedProcess:')
completed_process = subprocess.run('exit 1', shell=True, capture_output=True, text=True)
print("Arguments: " + completed_process.args)
print("Return Code: " + str(completed_process.returncode))
print("Stdout: " + completed_process.stdout)
print("Stderr: " + completed_process.stderr)
try:
    completed_process.check_returncode()    #Throws a CalledProcessError
except subprocess.CalledProcessError as error:
    print("Error: " + str(error))

print('\n')
print('subrpocess.DEVNULL')
sub_devnull = subprocess.run('echo subprocess.DEVNULL', shell=True, stdout=subprocess.DEVNULL)
print('Stdout: ' + str(sub_devnull.stdout))   #The output is none.

print('\n')
print('subprocess.PIPE')
sub_pipe = subprocess.run('echo stdout=subprocess.PIPE', shell=True, stdout=subprocess.PIPE, text=True)
print('Stdout: ' + sub_pipe.stdout) #The output is the standard output.

print('\n')
print('subprocess.STDOUT')  #Indicates stderr should go into the same handle as stdout.
sub_stdout = subprocess.run('echo subprocess.STDOUT', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
print('stderr: ' + str(sub_stdout.stderr))  #stderr is none because it has been combined with stdout.
print('stdout: ' + str(sub_stdout.stdout))

#Creating exceptions. SubprocessError is the base class for all other exceptions.
print('\n')
print('subprocess.SubprocessError')
try:
    subprocess.run('exit 1', shell=True, check=True)    #If check isn't equal to True then the exception will not be thrown.
except subprocess.SubprocessError as error:
    print('subprocess.SubprocessError: ' + str(error))

#TimeoutExpired is a subclass of SubprocessError that is raised when a timeout expires.
print('\n')
print('subprocess.TimeoutExpired')
try :
    sub_timeout_expired = subprocess.run('C:\Program Files\Sublime Text 3\sublime_text.exe', timeout=1, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)   #TimeoutExpired if it is .01 for echo it will be thrown.
except subprocess.TimeoutExpired as error:
    print('cmd: ' + str(error.cmd))
    print('Timeout: ' + str(error.timeout))
    print('Output: ' + str(error.output))
    print('Stdout: ' + str(error.stdout))
    print('Stderr: ' + str(error.stderr))

#Subclass of SubprocessError raised by check_call() or check_output() if they return a non-zero exit status.
print('\n')
print('subprocess.CalledProcessError')  #Raised by check_call() or check_output() returning a nonzero exit status.
try:
    subprocess.check_call('exit 1', shell=True)
except subprocess.CalledProcessError as error:
    print(error.returncode)
    print(error.cmd)
    print(error.output)
    print(error.stdout)
    print(error.stderr)

'''
POPEN ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
#Executes a child program in a new process.



# print('')
# print('Popen.wait()')
# try :
#     subprocess.Popen('C:\Program Files\Sublime Text 3\sublime_text.exe').wait(timeout=1)   #If sublime text isn't terminated in 1 second throw TimeoutExpired Exception.
# except subprocess.TimeoutExpired as error:
#      print("TimeoutExpired error thrown.")


# popen_poll = subprocess.Popen('C:\Program Files\Mozilla Firefox\\firefox.exe')
# popen_poll.kill()
# print('Popen.poll() returncode: ' + str(popen_poll.poll()))
# print('Popen.poll() returncode: ' + str(popen_poll.returncode))


# soccer = subprocess.Popen(['findstr', 'f'], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
# soccer2 = soccer.communicate(input=b'soccer1 \nsoccer \nsoccer3 \nsoccer2')[0]
# print(soccer2.decode())

process = subprocess.Popen(['cat', 'test.py'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
print(stdout)
print(stderr)


























































