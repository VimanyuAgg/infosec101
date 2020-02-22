import time
import sys # ignore
sys.path.insert(0,'.') # ignore
import pswd


def check_password(password):
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1) # Simulates the wait time of the safe's mechanism
        if SOL_WITH_ONLY_INT:
            if int(x) != int(y):
                return False
        else:
            if x != y:
                return False
    return True


def crack_password():
    timer_start = time.time()
    actual_psw_len = ''
    start = time.time()

    while (time.time() - start) <= 0.1:
        start = time.time()
        actual_psw_len += '0'
        check_password(actual_psw_len)
    print("Password length cracked: {}".format(len(actual_psw_len)))

    psw = ''
    for i in range(len(actual_psw_len)):
        for iterator in range(256):
            if SOL_WITH_ONLY_INT:
                if not chr(iterator).isdigit():
                    continue
                try:
                    int(chr(iterator))
                except ValueError as e:
                    # This is not an int
                    continue

            tmp = psw + chr(iterator) + actual_psw_len[i+1:]  # actual psw + test_input + padding for length check
            start = time.time()
            check_password(tmp)
            if (i != len(actual_psw_len)-1) and (time.time() - start >= (i+2)*0.1):
                psw += chr(iterator)
                print("Cracked Password: {}{} in {:.2f} sec".format(psw,
                                                                ''.join(['*' for x in range(len(actual_psw_len)-len(psw))]),
                                                                time.time() - timer_start))
            elif (i == len(actual_psw_len)-1) and check_password(tmp):
                psw += chr(iterator)
                print("Cracked Password: {} in {:.2f} sec".format(psw, time.time() - timer_start))

    # Sanity check
    assert(check_password(psw))
    print(">>>>CR@C|{{3|)<<<<<")

    return psw


if __name__ == '__main__':
    SOL_WITH_ONLY_INT = False
    real_password = pswd.generate_pswd(SOL_WITH_ONLY_INT)
    crack_password()
