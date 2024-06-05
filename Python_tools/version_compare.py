




def compare_version(v1, v2):
    division_version_1 = version_1.split('.')
    division_version_2 = version_2.split('.')
    version_1_lenght = len(division_version_1)
    version_2_lenght = len(division_version_2)
    if version_1_lenght >= version_2_lenght:
        for i in range(version_1_lenght):
            if i < version_2_lenght:
                if int(division_version_1[i]) > int(division_version_2[i]):
                    print('V1')
                    return v1
                if int(division_version_1[i]) < int(division_version_2[i]):
                    print('V2')
                    return v2
                if int(division_version_1[i]) == int(division_version_2[i]):
                    continue
            else:
                if int(division_version_1[i]) > 0:
                    print('V1')
                    return v1
                else:
                    if int(division_version_1[i]) == 0:
                        continue
        else:
            print('V1 = V2')
    else:
        for i in range(version_2_lenght):
            if i < version_1_lenght:
                if int(division_version_1[i]) > int(division_version_2[i]):
                    print('V1')
                    return v1
                if int(division_version_1[i]) < int(division_version_2[i]):
                    print('V2')
                    return v2
                if int(division_version_1[i]) == int(division_version_2[i]):
                    continue
            else:
                if int(division_version_2[i]) > 0:
                    print('V2')
                    break
                else:
                    if int(division_version_2[i]) == 0:
                        continue
        else:
            print('V1 = V2')


version_1 = input('请输入第一个版本号, V1: ')
version_2 = input('请输入第二个版本号, V2: ')
compare_version(version_1, version_2)