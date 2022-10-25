import subprocess


class ShellRunner:
    @staticmethod
    def run_command(command):
        subprocess.call(command, shell=True)
