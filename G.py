for t in range(int(input())):
    ip = list(map(lambda x: int("{:b}".format(int(x))),  input().split('.')))
    sip = list(map(int, input().split('.')))
    if ip[0] == sip[0] and ip[1] == sip[1] and ip[2] == sip[2] and ip[3] == sip[3]:
        print("Case {}: Yes".format(t+1))
    else:
        print("Case {}: No".format(t+1))
