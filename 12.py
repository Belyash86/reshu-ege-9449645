for ed in range(51):
    for dv in range(100):
        for tr in range(100):
            s = '0'+'1'*ed+'2'*dv+'3'*tr
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01','30',1)
                s = s.replace('02','101',1)
                s = s.replace('03','202',1)
            if (s.count('1') == 20) and (s.count('2') == 10) and (s.count('3') == 70):
                print(ed)
                exit()