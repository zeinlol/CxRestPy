from etc.constants import REPORT_TYPES


def get_format() -> str:
    report_code = 0
    print('* Output format not selected. Please, choose one:')
    for types in REPORT_TYPES:
        print("\t[{}]".format(report_code), types)
        report_code += 1
    report_code = int(input("- Report type number:"))
    return REPORT_TYPES[report_code].lower()
