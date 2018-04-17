import boto3
import pprint
from botocore.exceptions import ClientError
from mail import mailer
def recog(bucket,source_fname,target_fname="Myimage.jpg"): #takes bucket_name, image_source_name, image_taregt_name
        print ("Starting recog engine..")
        path = "E:\\CV2_Snaps\\"+source_fname
        print (path)
        client = boto3.client('rekognition',region_name='us-east-1')
        s3_bucketName = bucket
        s3_sf_object = source_fname
        s3_tf_object = target_fname
        Source_image = dict()
        Target_image = dict()
        Source_image['S3Object'] = {'Bucket':'','Name':''}
        Target_image['S3Object'] = {'Bucket':'','Name':''}
        Source_image['S3Object']['Bucket'] = s3_bucketName
        Target_image['S3Object']['Bucket'] = s3_bucketName
        Source_image['S3Object']['Name'] = s3_sf_object
        Target_image['S3Object']['Name'] = s3_tf_object
        try:
                response = client.compare_faces(SimilarityThreshold=70,SourceImage=Source_image,TargetImage=Target_image)
                confidence = ''
                print ("Analysed.. Fetching Results...")
                for faceMatch in response['FaceMatches']:
                #position = faceMatch['Face']['BoundingBox']
                        confidence = str(faceMatch['Face']['Confidence'])
                        print (confidence)
                        
        except:
                mailer(imagename=source_fname,path=path)

if __name__ == '__main__':
        pass
        # bucketName = "recogssp"
        # source_object  = "Myimage.jpg"
        # target_object  = "1477472596813.jpg"
        # print ('The match is %s matching' %(recog(bucketName,source_object,target_object)))