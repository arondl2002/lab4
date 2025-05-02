from setuptools import find_packages, setup

package_name = 'camera_pipeline'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/pipeline.launch.py']),
        ('share/' + package_name, ['config/ost.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='jonakselm@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            f"gaussian_blur = {package_name}.gaussian_blur:main",
            f"canny_edge = {package_name}.canny_edge:main",
        ],
    },
)
