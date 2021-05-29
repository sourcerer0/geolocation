import subprocess
import sys

USER = "sourcerer2"
REPO = "geolocation"

try:
    TAG = sys.argv[1]
except IndexError:
    print("Missing version!")
    print("\tExample: python3 push_docker.py 1.0")
    sys.exit()

if sys.argv[1] == "--help" or sys.argv[1] == "help":
    print("Command example: python3 push_docker.py 1.0")
    sys.exit()

if (
    subprocess.run(["docker", "rmi", "{0}/{1}:latest".format(USER, REPO)]).returncode
    != 0
):
    pass  # print("Couldn't found 'latest' tag")
else:
    print("Latest tag overriden...")

if (
    subprocess.run(
        ["docker", "build", "-t", "{0}/{1}:{2}".format(USER, REPO, TAG), "."]
    ).returncode
    == 0
):
    subprocess.run(
        [
            "docker",
            "tag",
            "{0}/{1}:{2}".format(USER, REPO, TAG),
            "{0}/{1}:latest".format(USER, REPO),
        ]
    )
    """
    subprocess.run(
        [
            "docker",
            "push",
            "{0}/{1}:{2}".format(USER, REPO, TAG),
        ]
    )
    subprocess.run(
        [
            "docker",
            "push",
            "{0}/{1}:latest".format(USER, REPO),
        ]
    )"""

else:
    print("Couldn't build image... Finish program")
