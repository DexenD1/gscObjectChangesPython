import io, os, tempfile
# Import standart google service library
from google.cloud import storage, vision, firestore

# Creates a client
gcsClient = storage.Client()
visionClient = vision.ImageAnnotatorClient()
firestoreClient = firestore.Client()

def gcsObjectChanges(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event

    # Define image file name and bucket name
    fileName = file["name"]
    bucketName = file["bucket"]
    print(f"FILE NAME: {fileName}")
    print(f"BUCKET NAME: {bucketName}")

    # Get the recent uploaded image from Google Storage Bucket
    blobFile = gcsClient.bucket(bucketName).get_blob(fileName)
    blobFileUri = f"gs://{bucketName}/{fileName}"
    print(f"BLOB FILE: {blobFile}")
    print(f"BLOB FILE URI: {blobFileUri}")
    blobImageFile = vision.Image(source=vision.ImageSource(image_uri=blobFileUri))

    # Perform label detection
    result = visionClient.label_detection(image=blobImageFile)
    labels = result.label_annotations
    information = []
    print("LABELS:")
    for label in labels:
        print(label.description)
        information.append(label.description)

    # Post the image name and labels as information to Firestore
    documentReference = firestoreClient.collection(u"images").document(fileName)
    documentReference.set(
        {
            u"imagePath": fileName,
            u"information": information
        }
    )