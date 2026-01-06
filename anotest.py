import test

m1s = test.mysock()
m1s.create_sock()
m1s.bind_to_ip()
m1s.tr_listen()
print(f"tset:{m1s.msg}")
