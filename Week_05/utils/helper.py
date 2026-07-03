import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {
    "pdf",
    "doc",
    "docx"
}


def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


def save_resume(file, upload_folder):

    if file and allowed_file(file.filename):

        filename = secure_filename(
            file.filename
        )

        path = os.path.join(
            upload_folder,
            filename
        )

        file.save(path)

        return filename

    return None