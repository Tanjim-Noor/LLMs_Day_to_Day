import os
import yaml
import subprocess
import sys

def get_installed_packages():
    # Full path to your conda executable
    conda_path = r"E:\Anaconda\Scripts\conda.exe"  # Update this path to where your conda.exe is located

    # Ensure the conda executable exists
    if not os.path.exists(conda_path):
        print(f"Conda executable not found at {conda_path}")
        sys.exit(1)

    # Get installed conda packages
    conda_packages = subprocess.check_output([conda_path, 'list']).decode().split('\n')
    conda_packages = [line.split()[0] for line in conda_packages[3:] if line and not line.startswith('#')]

    # Get installed pip packages
    pip_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'list']).decode().split('\n')
    pip_packages = [line.split()[0] for line in pip_packages[2:] if line]

    return conda_packages, pip_packages

def read_environment_yml(file_path='environment.yml'):
    with open(file_path, 'r') as file:
        env = yaml.safe_load(file)
    conda_deps = []
    pip_deps = []
    for dep in env['dependencies']:
        if isinstance(dep, dict) and 'pip' in dep:
            pip_deps.extend(dep['pip'])
        else:
            conda_deps.append(dep.split('=')[0])
    return conda_deps, pip_deps

def main():
    conda_deps, pip_deps = read_environment_yml()
    conda_packages, pip_packages = get_installed_packages()

    missing_conda = [pkg for pkg in conda_deps if pkg not in conda_packages]
    missing_pip = [pkg.split('==')[0].split('>=')[0].split('<')[0] for pkg in pip_deps if pkg.split('==')[0].split('>=')[0].split('<')[0] not in pip_packages]

    if not missing_conda and not missing_pip:
        print("\nAll packages from environment.yml are installed.")
    else:
        print("\nSome packages from environment.yml are missing:")
        if missing_conda:
            print("\nMissing Conda packages:")
            for pkg in missing_conda:
                print(f" - {pkg}")
        if missing_pip:
            print("\nMissing Pip packages:")
            for pkg in missing_pip:
                print(f" - {pkg}")

if __name__ == "__main__":
    main()