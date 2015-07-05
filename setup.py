
from setuptools import setup, find_packages
from os import walk
from os.path import join, dirname, sep
import os
import glob

# NOTE: All package data should also be set in MANIFEST.in

packages = find_packages()

package_data = {'': ['*.tmpl',
                     '*.patch', ], }

data_files = []

# By specifying every file manually, package_data will be able to
# include them in binary distributions. Note that we have to add
# everything as a 'pythonforandroid' rule, using '' apparently doesn't
# work.
def recursively_include(results, directory, patterns):
    for root, subfolders, files in walk(directory):
        for fn in files:
            if not any([glob.fnmatch.fnmatch(fn, pattern) for pattern in patterns]):
                continue
            filename = join(root, fn)
            directory = 'pythonforandroid'
            if directory not in results:
                results[directory] = []
            results[directory].append(join(*filename.split(sep)[1:]))

recursively_include(package_data, 'pythonforandroid/recipes', ['*.patch', 'Setup'])
recursively_include(package_data, 'pythonforandroid/bootstraps',
                    ['*.properties', '*.xml', '*.java', '*.tmpl', '*.txt', '*.png',
                     '*.mk', '*.c'])

setup(name='python-for-android',
      version='0.2',
      description='Android APK packager for Python scripts and apps',
      author='Alexander Taylor',
      author_email='kivy-dev@googlegroups.com',
      url='https://github.com/inclement/python-for-android-revamp', 
      license='MIT', 
      install_requires=['appdirs', 'colorama', 'sh', 'jinja2', 'argparse'],
      entry_points={
          'console_scripts': [
              'python-for-android = pythonforandroid.toolchain:ToolchainCL',
              'p4a = pythonforandroid.toolchain:ToolchainCL',
              ],
          'distutils.commands': [
              'bdist_apk = pythonforandroid.bdist_apk:BdistAPK',
              ],
          },
      classifiers = [
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: OS Independent',
          'Operating System :: POSIX :: Linux',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: C',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development',
          'Topic :: Utilities',
          ],
      packages=packages,
      package_data=package_data,
      )
