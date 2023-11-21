import os
import argparse


class DirectoryTree:
	def __init__(self, root_dir, only_dirs=False, filter_out=None, filter_in=None):
		self.root_dir = root_dir
		self.only_dirs = only_dirs
		self.filter_out = set(filter_out or [])
		self.filter_in = set(filter_in or [])

	def _filter_files(self, files):
		if self.filter_out:
			files = [f for f in files if not any(f.endswith(ext) for ext in self.filter_out)]
		if self.filter_in:
			files = [f for f in files if any(f.endswith(ext) for ext in self.filter_in)]
		return files

	def generate_tree(self):
		for root, dirs, files in os.walk(self.root_dir):
			level = root.replace(self.root_dir, '').count(os.sep)
			indent = ' ' * 4 * level
			print('{}{}/'.format(indent, os.path.basename(root)))
			if not self.only_dirs:
				files = self._filter_files(files)
				for f in files:
					print('{}    {}'.format(indent, f))


def main():
	parser = argparse.ArgumentParser(
		description='Display directory tree',
		epilog='Examples:'
			   '\n  python tree.py "some/dir" - Show the tree structure of "some/dir".'
			   '\n  python tree.py "some/dir" -d - Show only directories in "some/dir".'
			   '\n  python tree.py "some/dir" -fo .py .txt - Exclude .py and .txt files.'
			   '\n  python tree.py "some/dir" -f .py - Show only directories and .py files.',
		formatter_class=argparse.RawTextHelpFormatter
	)

	parser.add_argument('directory', help='Directory path')
	parser.add_argument('-d', action='store_true', help='Show only directories')
	parser.add_argument('-fo', '--filter_out', nargs='+', help='Filter out files with these extensions')
	parser.add_argument('-f', '--filter', nargs='+', help='Filter files with these extensions')
	args = parser.parse_args()

	tree = DirectoryTree(args.directory, args.d, args.filter_out, args.filter)
	tree.generate_tree()


if __name__ == '__main__':
	main()
