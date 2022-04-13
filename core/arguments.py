import argparse
from pathlib import Path

from etc import constants


def create_parser():
    parser = argparse.ArgumentParser(description='Checkmarx API adapter')
    parser.add_argument('-u', '--url', type=str, default='http://localhost/CxRestAPI',
                        help='Checkmarx link. Default is http://localhost/CxRestAPI')
    parser.add_argument('-l', '--login', type=str, default=None,
                        help='user name (login)')
    parser.add_argument('-p', '--password', type=str, default=None,
                        help='user password')
    # parser.add_argument('-t', '--token', type=str, default=None,
    #                     help='access token')
    parser.add_argument('-n', '--project', type=str, default=None,
                        help='project name')
    parser.add_argument('-s', '--scan-folder', type=str, default=Path(__file__).parents[1],
                        help=f'Scan folder for analyzing. Default is this {Path(__file__).parents[1]}')
    parser.add_argument('-o', '--output', type=str, default=None,
                        help='Output file for data')
    parser.add_argument('-f', '--format', type=str, default=None,
                        help=f'Output format. Supported values: {constants.REPORT_TYPES}')
    parser.add_argument('-d', '--delete', default=False, action='store_true',
                        help='Remove project in the end')
    parser.add_argument('-dp', '--delete-previous', default=False, action='store_true',
                        help='Remove all previous projects generated by this tool')
    return parser.parse_args()


cli_arguments = create_parser()
