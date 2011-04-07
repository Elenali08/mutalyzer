"""HGVS variant nomenclature checker."""


import os


# On the event of a new release, we update the __version_info__ and __date__
# package globals and set RELEASE to True.
# After a release, a development version is denoted by a __version_info__
# ending with a 'dev' item. Also, RELEASE is set to False (indicating that
# the __date__ value is to be ignored).

RELEASE = False

__version_info__ = ('2', '0', 'beta-9', 'dev')
__date__ = '31 Jan 2011'


__version__ = '.'.join(__version_info__)
__author__ = 'Leiden University Medical Center'
__contact__ = 'humgen@lumc.nl'
__homepage__ = 'http://mutalyzer.nl'


NOMENCLATURE_VERSION_INFO = ('2', '0')
NOMENCLATURE_VERSION = '.'.join(NOMENCLATURE_VERSION_INFO)


def package_root():
    """
    Get the absolute path to the mutalyzer package. This is usefull for
    things like locating HTML templates (which are in a subdirectory of the
    package).

    @return: Absolute path to the mutalyzer package.
    @rtype:  string
    """
    return os.path.realpath(os.path.split(__file__)[0])


def is_test():
    """
    Check if we are in a test environment. This is determined by the
    MUTALYZER_ENV environment variable, which should then be set to 'test'.

    @return: True if we are in a test environment, False otherwise.
    @rtype:  bool
    """
    return 'MUTALYZER_ENV' in os.environ \
           and os.environ['MUTALYZER_ENV'] == 'test'