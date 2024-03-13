import subprocess

def run_command(command):
    """Run a shell command."""
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print("Error executing command:", e.output.decode())

def main():
    # Update the system
    run_command("yum update -y")

    # Install Docker
    run_command("yum install docker -y")

    # Start and enable Docker service
    run_command("systemctl enable --now docker")

    # Verify Docker installation
    run_command("docker run hello-world")

    # Clone the Sophos Central Integration repository
    run_command("git clone https://github.com/sophos/Sophos-Central-SIEM-Integration.git")
    run_command("cd Sophos-Central-SIEM-Integration && cd docker_samples")

    # Note: Additional steps like updating Dockerfile and configuring 'config.ini'
    # might require manual intervention or advanced scripting beyond this basic automation.

    # Build the Docker image
    run_command("docker build -t sophos-siem .")

    # Run the Docker container
    run_command("docker run sophos-siem")



if __name__ == "__main__":
    main()
