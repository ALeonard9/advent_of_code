class log_style:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def log(msg, style='warn'):
    match style:
        case 'good':
            print(log_style.OKGREEN + str(msg) + log_style.ENDC)
        case 'fail':
            print(log_style.FAIL + str(msg) + log_style.ENDC)
        case 'warn':
            print(log_style.WARNING + str(msg) + log_style.ENDC)
        case 'info':
            print(log_style.OKBLUE + str(msg) + log_style.ENDC)
        case _:
            print(log_style.ENDC + str(msg) + log_style.ENDC)
