# Argparse Module
## Sample code
```python
import math
import argparse

parser=argparse.ArgumentParser(description='<name of program>')
parser.add_argument('-r','--radius',type=int,metavar='',required=True,help='Radius of Cylinder')
parser.add_argument('-H,'--Height',type=int,metavar='',required=True,help='Height of Cylinder')
group=parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet',action='store_true', help='print quiet')
group.add_argument('-v', '--verbose',action='store_true', help='print verbose')
args=parser.parse_args()

def cylinder_volume(radius,height):
    return (math.pi * (radius**2) * heigh)

if __name__=='__main__':
    volume= cylinder_volume(args.radius,args.height)
    if args.quiet:
        print volume
    elif args.verbose:
        print f"Volume of a cylinder with radius {args.radius} and height {args.height} is {volume}"
    else:
	print "Volume of cylinder = %s" % volume
```

# Reference

- https://realpython.com/command-line-interfaces-python-argparse/
- https://stackoverflow.com/questions/19414060/argparse-required-argument-y-if-x-is-present
- https://gist.github.com/amarao/36327a6f77b86b90c2bca72ba03c9d3a
- https://stackoverflow.com/questions/23349349/argparse-with-required-subparser