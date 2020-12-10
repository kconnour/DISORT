import glob
import os
import setuptools
import sys


class SetupDISORT:
    def __init__(self):
        self.project_path = os.path.dirname(os.path.realpath(__file__))
        self.disort_folder_name = 'disort4.0.99'
        self.module_name = 'disort'

        self.compile_disort_so_file()
        self.so_file_name = self.get_so_file_name()
        self.move_so_file_up_one_directory()
        self.setup_package()

    def compile_disort_so_file(self):
        os.chdir(os.path.join(self.project_path, self.disort_folder_name))
        os.system(
            f'{sys.executable} -m numpy.f2py -c BDREF.f DISOBRDF.f DISORT.f ERRPACK.f LAPACK.f LINPAK.f RDI1MACH.f '
            f'-m {self.module_name}')

    @staticmethod
    def get_so_file_name():
        disort_binary_filename = glob.glob('*.so')[0]
        return disort_binary_filename

    def move_so_file_up_one_directory(self):
        os.rename(os.path.join(os.path.join(self.project_path, self.disort_folder_name), self.so_file_name),
                  os.path.join(self.project_path, self.so_file_name))

    def setup_package(self):
        os.chdir(self.project_path)
        setuptools.setup(
            name='DISORT',
            version='0.0.1',
            description='Make an importable .so file to call DISORT from Python',
            url='https://github.com/kconnour/DISORT',
            author='kconnour',
            python_requires='>=3.8',
            install_requires=[
                'numpy>=1.19.1',
            ],
            # I have no clue why I need to go up a directory when I'm already in the correct directory
            packages=[''],
            package_data={'': [self.so_file_name]}
        )


SetupDISORT()
