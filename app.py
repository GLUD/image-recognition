import tornado
import tornado.ioloop
import tornado.web
import os, uuid
import classify
from tornado.escape import json_encode

__UPLOADS__ = "uploads/"

class ProccessImage(tornado.web.RequestHandler):
    def post(self):
         fileinfo = self.request.files['file'][0]
        #  print "fileinfo is", fileinfo
         fname = fileinfo['filename']
         extn = os.path.splitext(fname)[1]
         cname = str(uuid.uuid4()) + extn
         filePath = __UPLOADS__ + cname
         fh = open(filePath, 'w')
         fh.write(fileinfo['body'])
         fh.close()
         keywords = classify.run_inference_on_image(filePath)
         self.write(json_encode(keywords))

def make_app():
    return tornado.web.Application([
        (r"/images",ProccessImage)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
