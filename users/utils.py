#function upload file
def handle_upload_file(f):
    with open('home/media/images/employees'+f.name,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)