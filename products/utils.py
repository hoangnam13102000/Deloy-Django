#function upload file
def handle_upload_file(f):
    with open('home/media/images/products'+f.name,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)