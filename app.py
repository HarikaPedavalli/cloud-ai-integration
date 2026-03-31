def upload_file(file_name):
    return {
        "message": "File uploaded successfully",
        "file_name": file_name,
        "storage": "AWS S3"
    }

def deploy_service():
    return {
        "message": "Service is deployment-ready",
        "platform": "AWS EC2",
        "containerized": True
    }

if __name__ == "__main__":
    print(upload_file("report.pdf"))
    print(deploy_service())
