from settings import version, readme_content
import os


def map_value(current_min, current_max, new_min, new_max, value):
    current_range = current_max - current_min
    new_range = new_max - new_min
    return new_min + new_range  * ((value - current_min)/current_range)



def Create_readme():
    if os.path.exists("README.txt"):
        f = open("README.txt", 'r')
        if str(f.readline()) != (version + "\n"):
            f.close()
            os.remove("README.txt")
            f = open("README.txt", 'w')
            f.writelines(readme_content)
        
        f.close()


    else:
        f = open("README.txt", 'w')
        f.writelines(readme_content)
        f.close()