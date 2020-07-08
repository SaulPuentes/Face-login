import numpy as np
import cv2

from fr_light import fr_light
from fr_api import fr_api
from timer import Timer

class FrLogin:

    def start(self):
        fr_light(0, self.face_detected)
        

    def face_detected(self, path, img):

        if t.seconds() > 4:
                
            # Save image
            cv2.imwrite(path, img)

            # Call FR_API
            fr_api(path, img)
            
            
            t.restart()
            
            # Save JSON_RESULT
    

fr = FrLogin()
t = Timer()

t.start()
fr.start()
