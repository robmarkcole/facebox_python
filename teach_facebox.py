# MIT License
#
# Copyright (c) 2018 Peshmerge Morad
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import base64
import os
import requests

# The api url which can be used to teach the machineboxx/facebox.
teach_api_url = "http://localhost:8080/facebox/teach"

# Health API url as defined by MachineBox to fetch the status/health of the box
health_api_url = "http://localhost:8080/readyz"


def _extract_base64_contents(image_file):
    return base64.b64encode(image_file.read()).decode('ascii')


def main():
    failed_images_list=[]
    total_succeeded = 0
    total_failed = 0
    try:
        json_response = requests.get(health_api_url)
    except requests.exceptions.RequestException as e:
        print("Facebox is unreachable......... Please check if it's up and running! ")
        print(e)
    else:
        if json_response.status_code == 200:
            folders = [dir for dir in os.listdir('.')
                       if os.path.isdir(os.path.join('.', dir)) and not dir.startswith('.')]

            # ID's here are just integers you can replace this by any other number. You can also edit this and make the
            # ID's be for example names of the folders (in case they are numbers)
            i = 1
            # sort the folder names alphabetically
            folders.sort(key=str.lower)
            for folder_name in folders:
                succeeded = 0
                total = 0
                print("Started training for " + folder_name)
                for file in os.listdir(os.getcwd() + "/" + folder_name):
                    total += 1
                    if file.endswith(('.jpg', '.png','.jpeg')):
                        json_data = {
                            "name": folder_name,
                            "id": i
                        }
                        print(
                            "Sending request to " + teach_api_url + " to train it with this file "
                            + file + " with with this ID = " + str(i))
                        json_response = (requests.post(
                            teach_api_url,
                            data=json_data,
                            files={'file': open(folder_name + '/' + file, 'rb')}
                        ))
                        if json_response.status_code == 200:
                            print("Training for " + file + " has succeeded! ")
                            succeeded += 1
                        elif json_response.status_code == 400:
                            print(json_response.text + " on the following image " + file)
                            failed_images_list.append(json_response.text + " on the following image " + file)
                        else:
                            print("Something went wrong! Please check the docker instance if it's alive")
                print(" The training for " + folder_name + " has succeeded for " + str(
                    succeeded) + " images! " + ", but failed to train  " + str(total - succeeded) + " images !")
                i += 1
                total_succeeded += succeeded
                total_failed += total - succeeded
            print("Total succeeded trainings/images is: ", total_succeeded)
            print("Total failed trainings/images is: ", total_failed)
            with open('failed_log.txt', 'w') as log_file:
                for failed_image in failed_images_list:
                    log_file.write("%s\n" % failed_image)

        else:
            print("The Machinebox/Facebox isn't ready! Please check if the docker instance is up an running!")


if __name__ == '__main__':
    main()
