import boto3
import os
from AWS_Reckognition import recog
def s3_uploader(bucket,filepath="E:\\CV2_Snaps\\Myimage.jpg",filename="Myimage.jpg"):
    s3_res = boto3.resource('s3')
    try:
        s3_res.Bucket(bucket).upload_file(filepath, filename)
        print ("File Uploaded successfully..")
        recog(bucket=bucket,source_fname=filename)
    except FileNotFoundError:
        return "File Not Found.."
