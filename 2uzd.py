import configparser 
config = configparser.ConfigParser()
config.read('config.ini')
y_axis =int(config.get('axis', 'y_axis'))
x_axis=int(config.get("axis","x_axis"))
rem_gab=y_axis*x_axis
while True:
    if rem_gab==0:
        print("Gabalinu vairs nav")
        break
    gab=int(input("Cik gabalinus velaties nolauzt?: "))
    if rem_gab<gab:
        print("Nepietiek atpalikusie gabalini ir :",rem_gab,"nevis: ",gab)
        break
    if gab==0:
        print("Jus izvelejaiet 0 gabalinus palika: ",rem_gab)
        continue
    if rem_gab==gab:
        print("0 lauzumi")
        break
    if rem_gab%gab==0:
        rem_gab=rem_gab-gab
        print("1 lazieni")
        print("Atpalikusi ",rem_gab," gabalini")
        continue
    if rem_gab%2==0:
        if rem_gab%gab==5:
            rem_gab=rem_gab-gab
            print("3 lauzumi")
            print("Atpalikusi ",rem_gab," gabalini")
            continue
    print(rem_gab%gab,"lauzumi")
    rem_gab=rem_gab-gab
    print("Atpalikusi ",rem_gab," gabalini")