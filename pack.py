import os
import subprocess




def main():
    os.mkdir("packed-plugins")
    for dir_name in os.listdir("."):
        if not dir_name.startswith(".") and os.path.isdir(dir_name):
            output_name = "packed-plugins/"
            subprocess.run(["mcdreforged", "pack", "-i", dir_name, "-o", output_name])


if __name__ == "__main__":
    main()