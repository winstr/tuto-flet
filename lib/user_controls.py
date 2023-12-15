import base64
from threading import Thread
from traceback import print_exc

import cv2
import flet as ft


class VideoStreamer(ft.UserControl):

    def __init__(self, source, dsize=(640, 480)):
        super().__init__()
        self.img = ft.Image()
        self.cap = cv2.VideoCapture(source)
        self.dsize = dsize
        assert self.cap.isOpened(), 'error: cap.isOpened()'

    def __del__(self):
        self.cap.release()

    def update_frame(self,):
        try:
            while True:
                succeed, frame = self.cap.read()
                assert succeed, 'error: cap.read()'
                frame = cv2.resize(frame, dsize=self.dsize)
                succeed, png = cv2.imencode('.png', frame)
                assert succeed, 'error: cv2.imencode(...)'
                self.img.src_base64 = base64.b64encode(png).decode('utf-8')
                self.update()
        except:
            print_exc()
        finally:
            self.__del__()

    def did_mount(self):
        self.running = True
        self.th = Thread(target=self.update_frame, args=(), daemon=True)
        self.th.start()

    def will_unmount(self):
        self.running = False

    def build(self):
        self.img.fit=ft.ImageFit.FILL
        return self.img
