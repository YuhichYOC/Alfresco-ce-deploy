import subprocess

APPLY_AMPS_SH = '[apply_amps_sh]'

if __name__ == '__main__':
    p = subprocess.Popen(APPLY_AMPS_SH, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    resp = '\n\n'
    p.communicate(input=resp.encode())
