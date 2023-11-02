import sys

sys.path.append('./mqtt')
import simple_sub as simple_sub

sub_demo = False

def main():
    if sub_demo:
        simple_sub.main()

main()
