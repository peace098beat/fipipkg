
import os
import sys

def main():
	print("Hello Im fipipkg!")
	print("This file path",os.path.dirname(os.path.abspath(__file__)))
	print("cwd(Current Working Dir", os.getcwd())

if __name__ == '__main__':
	main()