                                PYTHON PIP
WHAT IS PIP?
Pip is a package manager for python packages, or modules if you

NOTE: If you have python version 3.4 or later, pip is included by default



                    WHAT IS A PACKAGE
A package contains all the files you need for a module
Modules are python code libraries you can include in your project



                        CHECK IF PIP IS INSTALLED
Navigate your command line to the location of pythons script directory,
and type the following
eg
check if pip is installed
pip --version


                        INSTALL PIP
If you do not have pip install, you can download and install it from this page
http://python.org



                        DOWNLOAD A PACKAGE
Downloading a package is very easy
Open the command line interface and tell pip to download the package you want

Navigate your command line to the location of pythons script directory, and type the
following
eg
Download a package named 'camelcase'
pip install camelcase


                        USING A PACKAGE
Once a package is installed, it is ready to use
import the 'camelcase' package into you project
eg
import and use camelcase

import camelcase
c = camelcase.CamelCase()
txt = 'hello world'
print(c.hump(txt))


                            FIND PACKAGE
Find more packages at this url http://pypi.org/


                            REMOVE A PACKAGE
Use the uninstall command to remove a package
eg
Uninstall the package name 'camelcase'
pip uninstall camelcase

The pip package manager will ask you to confirm that you want to remove the camelcase
package press 'y' and the package will be removed


                        LIST PACKAGE
Use the list command to list all the packages installed on your system
eg
List installed packages
pip list 