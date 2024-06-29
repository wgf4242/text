import os
import re


class SSHConfig1(object):

    def __init__(self, filename=None):
        self.conf = open(filename, 'r', encoding='utf16', errors='ignore').read()
        return

    def write(self, filename):
        with open(filename, 'w', encoding='utf16') as f:
            f.write(self.conf)

    def set(self, key, value):
        pattern = rf'(^ *{key}) (.*)'

        def repl(match_obj: re.Match):
            key, *_ = match_obj.groups()
            res = ' '.join([key, value])

            if not match_obj:
                res = "\n" + res
            return res

        new_conf = re.sub(pattern, repl, self.conf, flags=re.M)
        if new_conf == self.conf:
            # not find match , add to conf end
            self.conf += ' '.join([key, value])
        else:
            self.conf = new_conf


if __name__ == '__main__':
    user = 'kali'
    pwd = 'kali'
    host = '192.168.158.129'

    os.system(rf"""powershell -command " ssh {user}:{pwd}@{host}  'cat /etc/ssh/sshd_config' > sshd_config" """)
    os.system(rf"""powershell -command " cat ~/.ssh/id_rsa.pub | ssh {user}:{pwd}@{host} 'cat >> ~/.ssh/authorized_keys' " """)

    conf = SSHConfig1('sshd_config')
    conf.set('PasswordAuthentication', "no")
    conf.write('ss1')

    os.system(rf"""powershell -command " cat ss1 | ssh {user}:{pwd}@{host} 'cat >> ~/sshd_config ' " """)
    os.system(rf"""powershell -command " echo {pwd} | ssh -t {user}:{pwd}@{host} 'sudo -S bash -c \"\"cp ~/sshd_config /etc/ssh/sshd_config;systemctl restart sshd\"\" '" """)

