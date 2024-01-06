export newip=192.168.88.2
export targetip=10.1.1.2
# cat 1 | sed -r "s/(\b[0-9]{1,3}\.){3}[0-9]{1,3}\b/$newip/g"
sed -r "s/(\b[0-9]{1,3}\.){3}[0-9]{1,3}\b/$newip/g" -i *.rc
sed -r "s/rhosts (\b[0-9]{1,3}\.){3}[0-9]{1,3}\b/rhosts $targetip/g" -i *.rc
sed -r "s/srvhost (\b[0-9]{1,3}\.){3}[0-9]{1,3}\b/srvhost 0.0.0.0/g" -i *.rc
