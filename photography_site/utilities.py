import os


def gen_file_ext(filepath):
    file = os.path.basename(filepath)
    name, ext = os.path.splitext(file)
    return name, ext


def file_upload_name(instance, filename):
    name, ext = gen_file_ext(filename)
    upload_name = f"{instance.id}-{instance.title}.{ext}"
    return f"photos/{upload_name}"


def file_upload_gallery_image(instance, filename):
    name, ext = gen_file_ext(filename)
    upload_name = f"{instance.id}-{instance.title}.{ext}"
    return f"products/galleries/{upload_name}"
