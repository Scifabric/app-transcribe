This is a transcription and proof-editing application for the PyBossa_
crowd-sourcing platform.

It is useful both in its own right but also as a template for building your own
custom transcription and proof-editing apps.

How to Setup
============

- The app uses images. So, first make sure you have images. If you have a PDF
  file, convert it into images. (Note: Imagemagick can convert PDF to images
  ```convert path/to/pdffile.pdf imagefile.png```)
- Upload all the images to a hosting service, S3, flickr, or imgur are
  recommended.
- Create a CSV file or Google Doc file with header ```image_url``` followed by
  link to each image.

.. _PyBossa: http://pybossa.com/

