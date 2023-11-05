import subprocess


cmd = "sudo systemctl restart lavazza_cfds_service_management.service"

p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
(stdout, stderr) = p.communicate()







