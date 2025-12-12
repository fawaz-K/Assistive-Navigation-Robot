import YB_Pcb_Car
import time
import speech_recognition as sr
import cv2
from cvzone.HandTrackingModule import HandDetector
import os
import RPi.GPIO as GPIO
import requests

fingersUP_List = [0,0,0,0,0,0,0,0,0,0]
words = ''
car = YB_Pcb_Car.YB_Pcb_Car()

token = '6153558498:AAH2PS-VLjEWIIVzBMnIFb0AMisg9AuTOC0'
groupID = 'obstical_warning_bot'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
GPIO_Buzzer = 12
GPIO_TRIGGER = 23
GPIO_ECHO = 24
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_Buzzer, GPIO.OUT)


try:

    def sendMSG():
        message = f'There is an obstical please remove it!'
        url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=@{groupID}&text={message}'
        res = requests.get(url)
        if   res.status_code == 200 : print('sent successfully')
        elif res.status_code != 200 : print('Error : couldn\'t sen message')

    def distance():
        GPIO_TRIGGER = 23
        GPIO_ECHO = 24
        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
        StartTime = time.time()
        StopTime = time.time()
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()
        TimeElapsed = StopTime - StartTime
        distance = (TimeElapsed * 34300) / 2
        return distance

    def car_movment(words, fingersUP_List):
        p = GPIO.PWM(12 , 440)
        counter = 0
        timer   = 0
        car = YB_Pcb_Car.YB_Pcb_Car()

        car.Ctrl_Servo(1, 90)
        car.Ctrl_Servo(2, 90)
        car.Car_Spin_Right(120, 120)
        time.sleep(0.82)
        car.Car_Stop()
        
        if (fingersUP_List[-16:].count(1)==15) or (('اول' or ' 1' or 'واحد') in words) :
            print('section1')
            if (('اول' or ' 1' or 'واحد') in words):
                os.system('mpg321 audio/tech.mp3')
                p.start(50)
            while True:
                dist = distance()
                #print(f'({counter}) , ({round(dist)})')
                if dist<=11 and 17<=counter<=18.5:
                    p.stop()
                    car.Car_Stop()
                    time.sleep(0.3)
                    car.Car_Spin_Right(120, 120)
                    time.sleep(0.82)
                    car.Car_Stop()
                    if (('اول' or ' 1' or 'واحد') in words):
                        os.system('mpg321 audio/arrive.mp3')
                    counter += 2
                elif dist<=9 and counter>=33:
                    car.Car_Stop()
                    return voice_detector()
                else:
                    if dist<=9:
                        if (fingersUP_List[-16:].count(1)==15) or counter>19 : p.start(50)
                        car.Car_Stop()
                        timer += 1
                        if timer == 50 : sendMSG()
                    else:
                        if timer < 50 : timer = 0
                        if (fingersUP_List[-16:].count(1)==15) or counter>19:p.stop()
                        car.Car_Run(50, 50)
                        counter += 0.5
                time.sleep(0.1)

        elif (fingersUP_List[-16:].count(2)==15) or (('ثان' or '2'  or 'اثنين') in words) :
            print('section2')
            if (('ثان' or '2'  or 'اثنين') in words):
                os.system('mpg321 audio/section2.mp3')
                p.start(50)
            while True:
                dist = distance()
                #print(f'({counter}) , ({round(dist)})')
                if dist<=45 and 9<=counter<=10.5 :
                    car.Car_Stop()
                    time.sleep(0.2)
                    car.Car_Spin_Right(120, 120)
                    time.sleep(0.43)
                    car.Car_Stop()
                    counter += 2
                elif dist<=9 and 18.5<=counter<=20:
                    p.stop()
                    car.Car_Stop()
                    time.sleep(0.3)
                    car.Car_Spin_Right(120, 120)
                    time.sleep(0.84)
                    car.Car_Stop()
                    if ((('ثان' or '2'  or 'اثنين') in words)):
                        os.system('mpg321 audio/arrive.mp3')
                    counter += 2
                elif dist<= 50 and 25.5<=counter<=27:
                    car.Car_Stop()
                    time.sleep(0.2)
                    car.Car_Spin_Left(120, 120)
                    time.sleep(0.43)
                    car.Car_Stop()
                    counter += 2
                elif dist <= 9 and counter>=35:
                    car.Car_Stop()
                    return voice_detector()
                else:
                    if dist <= 9   :
                        if (fingersUP_List[-16:].count(2)==15)or counter>19.5:p.start(50)
                        car.Car_Stop()
                        timer += 1
                        if timer == 50 : sendMSG()
                    else:
                        if timer < 50 : timer = 0
                        if (fingersUP_List[-16:].count(2)==15)or counter>19.5:p.stop()
                        car.Car_Run(50, 50)
                        counter+=0.5
                time.sleep(0.1)

        elif (fingersUP_List[-16:].count(3)==15) or  (('ثالث' or 'ثلاث' or '3') in words):
            print('section3')
            if (('ثالث' or 'ثلاث' or '3') in words) :
                os.system('mpg321 audio/student.mp3')
                p.start(50)
            while True:
                dist = distance()
                #print(f'({counter}) , ({round(dist)})')
                if dist<=45 and 9<=counter<=10.5 :
                    car.Car_Stop()
                    time.sleep(0.2)
                    car.Car_Spin_Left(120, 120)
                    time.sleep(0.43)
                    car.Car_Stop()
                    counter += 2
                elif dist <= 9 and 17<=counter<=18.5:
                    p.stop()
                    car.Car_Stop()
                    time.sleep(0.3)
                    car.Car_Spin_Right(120, 120)
                    time.sleep(0.82)
                    car.Car_Stop()
                    if (('ثالث' or 'ثلاث' or '3') in words):
                        os.system('mpg321 audio/arrive.mp3')
                    car.Car_Stop()
                    counter += 2
                elif dist<=50 and 25.5<=counter<=27:
                    car.Car_Stop()
                    time.sleep(0.2)
                    car.Car_Spin_Right(120, 120)
                    time.sleep(0.43)
                    car.Car_Stop()
                    counter += 2
                elif dist <= 9 and counter>=34:
                    car.Car_Stop()
                    return voice_detector()
                else:
                    if dist <= 9:
                        if (fingersUP_List[-16:].count(3)==15) or counter>19 : p.start(50)
                        car.Car_Stop()
                        timer += 1
                        if timer == 50 : sendMSG()
                    else:
                        if timer < 50 : timer = 0
                        if (fingersUP_List[-16:].count(3)==15) or counter>19:p.stop()
                        car.Car_Run(50, 50)
                        counter+=0.5
                time.sleep(0.1)

    def hand_detector():
        car = YB_Pcb_Car.YB_Pcb_Car()
        car.Ctrl_Servo(1, 90)
        car.Ctrl_Servo(2, 0)

        cap = cv2.VideoCapture(0)
        detector = HandDetector(maxHands=1)

        timer = 0
        fingersUP_List = [0,0,0,0,0,0,0,0,0,0]

        while True:
            success,img = cap.read()
            hands,img = detector.findHands(img)
            if hands:
                hand = hands[0]
                lmlist = hand['lmList']
                Handtype = hand['type']

                if timer < 200 : timer = 0

                if   Handtype == 'Right' : thumb_down = lmlist[4][0] < lmlist[3][0] ; thumb_up = lmlist[4][0] > lmlist[3][0]
                elif Handtype == 'Left'  : thumb_down = lmlist[4][0] > lmlist[3][0] ; thumb_up = lmlist[4][0] < lmlist[3][0]
                
                if   thumb_down and lmlist[8][1] < lmlist[6][1] and lmlist[12][1] > lmlist[10][1] and lmlist[16][1] > lmlist[14][1] and lmlist[20][1] > lmlist[18][1] : fingersUP_List.append(1)
                elif thumb_down and lmlist[8][1] < lmlist[6][1] and lmlist[12][1] < lmlist[10][1] and lmlist[16][1] > lmlist[14][1] and lmlist[20][1] > lmlist[18][1] : fingersUP_List.append(2)
                elif thumb_down and lmlist[8][1] < lmlist[6][1] and lmlist[12][1] < lmlist[10][1] and lmlist[16][1] < lmlist[14][1] and lmlist[20][1] > lmlist[18][1] : fingersUP_List.append(3)   
            else:
                timer += 1
                if timer == 130:
                    cap.release()
                    cv2.destroyAllWindows()
                    return voice_detector()

            cv2.imshow('image' , img) ; cv2.waitKey(1)
            
            if (fingersUP_List[-16:].count(1)==15) or (fingersUP_List[-16:].count(2)==15) or (fingersUP_List[-16:].count(3)==15):break
        
        cap.release()
        cv2.destroyAllWindows()
        car_movment(words=words, fingersUP_List=fingersUP_List)
    
    def voice_detector():

        recognizer = sr.Recognizer()
        mic = sr.Microphone()

        words = ''

        try:
            while True :
                with mic as source:
                    print('say something.....')
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source, timeout=10, phrase_time_limit=3) 

                    words = recognizer.recognize_google(audio ,language= "ar-AR")

                    if (('اول' or ' 1' or 'واحد') in words) or (('ثان' or '2'  or 'اثنين') in words)  or (('ثالث' or 'ثلاث' or '3') in words):return car_movment(words=words, fingersUP_List=fingersUP_List)
                    else: os.system('mpg321 audio/Error.mp3')

        except sr.UnknownValueError : return hand_detector()
        except sr.RequestError      : return hand_detector()
        except sr.WaitTimeoutError  : return hand_detector()

    voice_detector()

except KeyboardInterrupt: car.Car_Stop()

car.Ctrl_Servo(1, 90)
car.Ctrl_Servo(2, 90)
GPIO.cleanup()
del car        