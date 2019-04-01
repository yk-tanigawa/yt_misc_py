import subprocess

def sshcmd(host, command, user=None, stdin=None, check=False):
    ''' Runs ssh command via subprocess.  Assuming .ssh/config is configured.

    Args:
        host: target host to send the command to
        command: command to run on the host (string or (array or tupple) of strings)
        user: (optional) user to use to login to host
        stdin: (optional) override sys.stdin
        check: (optional) pass to *subprocess.run*; if set, checks return code
            and raises subprocess.CalledProcessError, if none-zero result

    Returns:
        subprocess.CompletedProcess object
        
    This version is modified based on the original version in here:
    https://acrisel.github.io/posts/2017/08/ssh-made-easy-using-python/        
    '''
    subprocess_run_config = {
            'shell' : False,
            'stdin' : stdin,
            'stdout' : subprocess.PIPE,
            'stderr' : subprocess.PIPE,
            'check' : check        
    }
    if(isinstance(command, str)):
        return subprocess.run(
            (
                'ssh', 
                (host if user is None else '@'.join([user, host])), 
                command
            ),
            **subprocess_run_config,
        )
    else:
        return subprocess.run(
            (
                'ssh', 
                (host if user is None else '@'.join([user, host])), 
                *command
            ),
            **subprocess_run_config,
        )        
    