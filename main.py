import requests, json
# Import standart google service library
from google.cloud import firestore

# Creates a client
firestoreClient = firestore.Client()

def gcsObjectChanges(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event

    # Get the recent uploaded image from Google Storage Bucket
    # Define image file name and bucket name
    fileName = file["name"]
    bucketName = file["bucket"]

    # Send a POST request to Machine Learning Instance through an API endpoint
    # Analyze the recent uploaded image in the Google Cloud Storage
    url = 'CLOUD_RUN_ENDPOINT/analyze'
    analyzeRequest = requests.post(
        url + 
        "?uri=gs://" + 
        bucketName + 
        "/&fileName=" + 
        fileName
    )
    requestDict = json.loads(analyzeRequest.text)
    information = requestDict["message"]["information"]

    # Post the image name and labels as an data information in Firestore
    # Store data in the 'images' collection and use the file name as the document ID
    documentReference = firestoreClient.collection(u"images").document(fileName)
    documentReference.set(
        {
            u"imagePath": fileName,
            u"information": information
        }
    )