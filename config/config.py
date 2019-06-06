from optparse import OptionParser
import argparse

#自定义命令行
# parser=argparse.ArgumentParser()
# parser.add_argument('-c','--collect-only',action='store_true', dest='collect_only', help='仅列出所有用例')
# parser.add_argument('--rerun-fails', action='store_true', dest='rerun_fails', help='运行上次失败的用例')
# parser.add_argument('--testlist', action='store_true', dest='testlist', help='运行test/testlist.txt列表指定用例')

# parser.add_argument('--testsuite', action='store', dest='testsuite', help='运行指定的TestSuite')
# parser.add_argument('--tag', action='store', dest='tag', help='运行指定tag的用例')
# (options, args) = parser.parse_args() 

# 命令行选项--》3.2后被弃用
parser = OptionParser()

parser.add_option('--collect-only', action='store_true', dest='collect_only', help='仅列出所有用例')
parser.add_option('--rerun-fails', action='store_true', dest='rerun_fails', help='运行上次失败的用例')
parser.add_option('--testlist', action='store_true', dest='testlist', help='运行test/testlist.txt列表指定用例')

parser.add_option('--testsuite', action='store', dest='testsuite', help='运行指定的TestSuite')
parser.add_option('--tag', action='store', dest='tag', help='运行指定tag的用例')

(options, args) = parser.parse_args() 