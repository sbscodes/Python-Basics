'''this module is used to pass command line arguments
here we can pass postional or keyword arguments
'''
import argparse

parser=argparse.ArgumentParser(description="this is simple demo on the argparser module"
                                           "below two argemuntes are type of keyword arguments"
                               "and other tow are positonal arguments "
                                           "we can combine postional as well as"
                                           "keyword in same progarm")
# # parser.add_argument("-n", "--Name", help="Enter Your Name", type=str, default="Unknown")
# parser.add_argument("-r", "--RollNo", help="Enter Your Roll No", type=int, default=0)
parser.add_argument("--Name", help="Enter Your Name", type=str, default="Unknown")
parser.add_argument("--RollNo", help="Enter Your Roll No", type=int, default=0)
#here we can also pass the group of arguments using add_argument_group() function
args = parser.parse_args()#parse the given cmd arguments to the variable

name=args.Name
rno=args.RollNo
print("Hello {0} Your Roll No is{1}".format(name,rno))