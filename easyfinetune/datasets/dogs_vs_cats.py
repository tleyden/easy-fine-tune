import requests
import os
import zipfile

img_width = 150
img_height = 150
num_train_samples = 23000
num_validation_samples = 2000

def download_to_dest(url, destfile):
    r = requests.get(url)
    f = open(destfile, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return

def download(extract=False, dest_dir="/tmp"):

    url = "http://datasets-deep-learning.s3.amazonaws.com/dogs_vs_cats/dogs_vs_cats.zip"
    local_filename = url.split('/')[-1]
    destfile = os.path.join(dest_dir, local_filename)

    if not os.path.exists(destfile):
        download_to_dest(url, destfile)
    else:
        print("WARNING: {} already exists, skipping download.  Delete file to override this".format(destfile))

    if extract:

        extracted_to_dir = os.path.join(dest_dir, "dogscats")  # unzips to /tmp/dogscats

        if not os.path.exists(extracted_to_dir):
            zip_ref = zipfile.ZipFile(destfile, 'r')
            zip_ref.extractall(dest_dir)
            zip_ref.close()
            os.remove(destfile)  # delete the zipfile
        else:
            print("WARNING: {} already exists, skipping extract.  Delete dir to override this".format(extracted_to_dir))
            
        return extracted_to_dir

    return destfile
