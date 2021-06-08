# gscObjectChangesPython
 Bangkit Final Project 2021
# Descriptions
 This source code is meant as a mediatory between the back-end infrastructure (data lake, database, and machine learning model) and the mobile app. This function will automatically triggered if there is any object changes (mainly intended for images) in a **Storage Bucket** and process it using **AutoML Vision** (at a glance, it should not be using a pre-trained machine learning model, but to provide a clear working function) to gain some labeling for further stored in the **Firestore** database.
# Instructions
 1. Create a project in Firebase console (which synchronously integrated with Google Cloud in the background procecss) via https://console.firebase.google.com
 2. Choose Storage option and follow the provided guidance to create a Cloud Storage.
 3. Choose Firestore Database option and follow the provided guidance to create a Firestore Database, **except** for the Rules, pick the Development purpose.
 4. Create a Cloud Functions from the Google Cloud Console with the specified specifications:
     - Function name: Create a semantic name for your function
     - Trigger type: **Cloud Storage**
     - Event type: **Finalize/Create**
     - Bucket: Browse > Choose the bucket that has been created previously (default bucket for a single Firebase project)
     - Click save and leave the other options as default
     - Runtime: **Python** (any version)
     - Entry point: **gcsObjectChanges**
     - Rewrite the **main.py** and **requirements.txt** using the provided source code in this repository
     - Change the endpoint url (main.py) to your AI API endpoint.
 5. Test the function by upload an image to the Storage Bucket--that has been created previously--either via Firebase Console or Google Cloud Console and see the result on the Firebase Storage.
