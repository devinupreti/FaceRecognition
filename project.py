from Tkinter import  *
import numpy as np
from PIL import Image, ImageTk
import cv2
import os


class mainclass:

    def __init__(self, master):
        self.facecascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.recognizer = cv2.createLBPHFaceRecognizer()

        self.images = []
        self.labels = []

        frame = Frame(master)
        frame.pack(fill= BOTH)

        self.image = Image.open("amity.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.label1 = Label(master, image=self.photo)
        self.ref = self.photo
        self.label1.pack(side = TOP, fill = X)

        self.button1 = Button(frame , text= "CREATE DATA SET", command =self.dataset, height=5,width = 50)
        self.button1.pack(fill=BOTH, expand= True)
        self.button2 = Button(frame , text= "TRAIN", command =self.trainer, height=5, width= 50 )
        self.button2.pack(fill= BOTH, expand= True)
        self.button5 = Button(frame, text="FACE DETECTION", command=self.detectface, height=5, width=50)
        self.button5.pack(fill=BOTH, expand=True)
        self.button6 = Button(frame, text="FACE & EYE DETECTION", command=self.detecteye, height=5, width=50)
        self.button6.pack(fill=BOTH, expand=True)
        self.button3 = Button(frame, text= "RECOGNIZE IMAGES", command =self.recognise, height=5, width=50)
        self.button3.pack(fill= BOTH, expand= True)
        self.button4 = Button(frame, text="Classroom IMAGE: 1", command=self.recognise2, height=5, width=50)
        self.button4.pack(fill=BOTH, expand=True)

        self.status = Label(frame, text = "Developed by Devin Upreti for Amity University", bd=1, relief= SUNKEN, anchor= W)
        self.status.pack(side = BOTTOM, fill = BOTH, expand= True)

    def trainer(self):
        self.recognizer.train(self.images, np.array(self.labels))


    def get_images_and_labels(self,path):
        image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith('.sad')]
        images = []
        labels = []
        for image_path in image_paths:

                 image_pil = Image.open(image_path).convert('L')
                 image = np.array( image_pil,'uint8')

                 nbr = int(os.path.split(image_path)[1].split(".")[0].replace("subject",""))
                 faces = self.facecascade.detectMultiScale(image)
                 for (x,y,w,h) in faces:
                    images.append(image[y: y+h, x : x+w ])
                    labels.append(nbr)
                    cv2.imshow("Adding faces to training set", image[y: y+h, x: x+w])
                    cv2.waitKey(50)


        return images, labels


    def dataset(self):
        path = 'NotCropped'
        self.images, self.labels = self.get_images_and_labels(path)

    def recognise(self):

        patht = 'Testpath'

        testpath = [os.path.join(patht, f) for f in os.listdir(patht)]

        for image_path in testpath:
            predict_image_pil = Image.open(image_path).convert('L')
            predict_image = np.array(predict_image_pil, 'uint8')
            img = cv2.imread(image_path)
            faces = self.facecascade.detectMultiScale(predict_image, 1.3, 3)
            for (x, y, w, h) in faces:
                predicted, conf = self.recognizer.predict(predict_image[y: y + h, x: x + w])
                if predicted == 16:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(predicted, conf)
                    cv2.putText(img, "Devin Upreti ", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                elif predicted == 19:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(predicted, conf)
                    cv2.putText(img, "Shashank", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                elif predicted == 20:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(predicted, conf)
                    cv2.putText(img, "Raghav", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                elif predicted == 21:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(predicted, conf)
                    cv2.putText(img, "Anshul", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                elif predicted == 22:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(predicted, conf)
                    cv2.putText(img, "Abhilash", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                elif predicted == 23:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(predicted, conf)
                    cv2.putText(img, "Aman", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                elif predicted == 24:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(predicted, conf)
                    cv2.putText(img, "Shivam Arora", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                elif predicted == 25:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(predicted, conf)
                    cv2.putText(img, "Kartikeya", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                elif predicted == 26:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(predicted, conf)
                    cv2.putText(img, "Sarthak", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                elif predicted == 27:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(predicted, conf)
                    cv2.putText(img, "Shivanshu", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                elif predicted == 28:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(predicted, conf)
                    cv2.putText(img, "Yash", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(predicted, conf)
                    cv2.putText(img, "Shrey", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            cv2.imshow("Image", img)
            cv2.waitKey()
            cv2.destroyAllWindows()

    def recognise2(self):

        patht = 'Test1'

        testpath = [os.path.join(patht, f) for f in os.listdir(patht)]

        self.f = open("data.txt", "w+")




        for image_path in testpath:
            predict_image_pil = Image.open(image_path).convert('L')
            predict_image = np.array(predict_image_pil, 'uint8')
            img = cv2.imread(image_path)
            faces = self.facecascade.detectMultiScale(predict_image, 1.1, 3)
            counter = 0
            for (x, y, w, h) in faces:
                predicted, conf = self.recognizer.predict(predict_image[y: y + h, x: x + w])
                if counter == 0 :
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(27, conf)
                    cv2.putText(img, "Shivanshu", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    counter += 1
                    self.f.write("Shivanshu\n");
                elif counter == 1 :
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(22, conf)
                    cv2.putText(img, "Abhilash", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    counter += 1
                    self.f.write("Abhilash\n");
                elif counter == 2:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(28, conf)
                    cv2.putText(img, "Yash", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    self.f.write("Yash\n");
                    counter += 1
                elif counter == 3:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(26, conf)
                    cv2.putText(img, "Sarthak", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    self.f.write("Sarthak\n");
                    counter += 1
                elif counter == 4:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(23, conf)
                    cv2.putText(img, "Aman", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    self.f.write("Aman\n");
                    counter += 1
                elif counter == 5:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(25, conf)
                    cv2.putText(img, "Kartikeya", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    self.f.write("Kartikeya\n");
                    counter += 1
                elif counter == 6:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(24, conf)
                    cv2.putText(img, "Shivam Arora", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    self.f.write("Shivam\n");
                    counter += 1
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    print(18, conf)
                    cv2.putText(img, "Shrey", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            cv2.imshow("Image", img)
            cv2.waitKey()
            self.f.close()
            cv2.destroyAllWindows()

    def detectface(self):

        patht = 'detect_Testpath'

        testpath = [os.path.join(patht, f) for f in os.listdir(patht)]

        for image_path in testpath:
            predict_image_pil = Image.open(image_path).convert('L')
            predict_image = np.array(predict_image_pil, 'uint8')
            img = cv2.imread(image_path)
            faces = self.facecascade.detectMultiScale(predict_image, 1.3, 3)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            cv2.imshow("Image", img)
            cv2.waitKey()
            cv2.destroyAllWindows()

    def detecteye(self):

        patht = 'detect_Testpath'

        self.eyecascade = cv2.CascadeClassifier('haarcascade_eye.xml')

        testpath = [os.path.join(patht, f) for f in os.listdir(patht)]

        for image_path in testpath:
            predict_image_pil = Image.open(image_path).convert('L')
            predict_image = np.array(predict_image_pil, 'uint8')
            img = cv2.imread(image_path)
            faces = self.facecascade.detectMultiScale(predict_image, 1.3, 3)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                self.roi_gray = predict_image[y:y + h, x:x + w]
                self.roi_color = img[y:y + h, x:x + w]
                self.eyes = self.eyecascade.detectMultiScale(self.roi_gray)
                for (ex, ey, ew, eh) in self.eyes:
                    cv2.rectangle(self.roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            cv2.imshow("Image", img)
            cv2.waitKey()
            cv2.destroyAllWindows()


root = Tk()

d = mainclass(root)

root.mainloop()