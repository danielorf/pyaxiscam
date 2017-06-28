import requests
import io
from PIL import Image


class AxisCam:
    def __init__(self, host, username, password):
        """Initializes the AxisCam object

        :param host (str):      The camera's IP address or host name
        :param username (str):  Camera username
        :param password (str):  Camera password
        """
        self.base_url = 'http://{}:{}@{}/axis-cgi/'.format(username, password, host)

    def get_supported_VAPIX_version(self):
        """Returns the version of Axis VAPIX camera API supported by the camera"""
        r = requests.get(self.base_url + 'param.cgi?action=list&group=Properties.API.HTTP.Version')
        print('Return status: ' + str(r.status_code))
        print(r.content.decode('utf-8'))
        return r.status_code, r.content.decode('utf-8')

    def get_supported_resolutions(self):
        """Returns the available resolutions supported by the camera"""
        r = requests.get(self.base_url + 'param.cgi?action=list&group=Properties.Image.Resolution')
        print('Return status: ' + str(r.status_code))
        print(r.content.decode('utf-8'))

    def get_supported_image_formats(self):
        """Returns the image formats supported by the camera"""
        r = requests.get(self.base_url + 'param.cgi?action=list&group=Properties.Image.Format')
        print('Return status: ' + str(r.status_code))
        print(r.content.decode('utf-8'))

    def get_default_resolution(self):
        """Returns the camera's default image and video resolution"""
        r = requests.get(self.base_url + 'imagesize.cgi?camera=1')
        print('Return status: ' + str(r.status_code))
        print(r.content.decode('utf-8'))

    def get_live_image(self):
        """Gets the latest image from the camera and displays it using PIL package"""
        r = requests.get(self.base_url + 'jpg/image.cgi')
        print('Return status: ' + str(r.status_code))
        if r.status_code == 200:
            f = io.BytesIO(r.content)
            img = Image.open(f)
            img.show()
        return r.status_code

        # TODO
        # https://stackoverflow.com/questions/21702477/how-to-parse-mjpeg-http-stream-from-ip-camera
        # def get_MJPEG_stream(self):
        #     r = requests.get(self.base_url + 'mjpg/video.cgi')
        #     print('Return status: ' + str(r.status_code))
        #     print(r.content.decode('utf-8'))
