from etc.constants import REPORT_TYPES


def get_format() -> str:
    report_code = 0
    for types in REPORT_TYPES:
        print("\t[{}]".format(report_code), types)
        report_code += 1
    report_code = int(input("- Choose report type:"))
    return REPORT_TYPES[report_code].lower()
