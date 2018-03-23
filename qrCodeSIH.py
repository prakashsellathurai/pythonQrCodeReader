import zbar #sudo apt-get install libzbar-dev # sudo apt-get install python3-dev  #pip install zbar
import cv2
from PIL import Image  #pip install Pillow

def main():
    capture = cv2.VideoCapture(0)
    while True:
        # To quit this program press q.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Breaks down the video into frames
        ret, frame = capture.read()

        # Displays the current frame
        #cv2.imshow('Current', frame)

        # Converts image to grayscale.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Uses PIL to convert the grayscale image into a ndary array that ZBar can understand.
        image = Image.fromarray(gray)
        width, height = image.size

        zbar_image = zbar.Image(width, height, 'Y800', image.tobytes())
        
        scanner = zbar.ImageScanner()
        scanner.scan(zbar_image)        # Prints data from image.
        for decoded in zbar_image:
           print(decoded.data)


if __name__ == "__main__":
    main()

