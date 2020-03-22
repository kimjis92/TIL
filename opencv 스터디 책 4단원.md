# 파이썬 함수

## 1.이미지 입력

cv2.imread(filename, flags=)  #올바른경로가 아니라면 None을 반환

```python
img=cv2.imread(pic[i], cv2.IMREAD_UNCHANGED) 

#cv2.imread(pic[i], cv2.IMREAD_COLOR) 하면 원본색이랑 다른 파란색으로 나옴 원본은 BGR 여#기는 RGB

b, g, r=cv2.split(img)
img2=cv2.merge([r, g, b])
```



## 2.이미지 출력

src=cv2.imread("OpenCV_Logo.png", cv2.IMREAD_GRAYSCALE)

cv2.namewindow("src", flags=cv2.WINDOW_FREERATO)

cv2.resizeWindow("src", 400, 200)

cv2.imshow("src", src)

cv2.waitkey(0)

cv2.destroyWindow("src")



## 3.동영상 출력

코덱: 음성 또는 영상의 신호를 디지털 신호로 변환해주는것



```python
while True:
	ret, frame=capture.read()
  					 		
    if(capture.get(cv2.CAP_PROP_POS_FRAMES)==capture.get(cv2.CAP_PROP_FRAME_COUNT)):
		capture.open("Star.mp4")
	#cv2.CAP_PROP_POS_FRAMES :현재 프레임개수,  cv2.CAP_PROP_FRAME_COUNT :총 프레임개수
        
    cv2.imshow("VideoFrame", frame)
    if cv2.waitKey(33)==ord('q'):break    #q가 입력되면 while문 탈출
        
capture.release()
cv2.destroyAllWindows()

```

​	

#### FPS(Frame Per Second)

: 초당 프레임 --> 사진들이 순차적으로 출력되어 하나의 연속되는 영상을 만듬



FPS = 1000 / Interval

초당 프레임수가 높아질수록 영상이 매끄러워진다.







## 4.카메라 출력

```python
import cv2

capture=cv2.VideoCapture(0)
capture.set(CV2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(CV2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
	ret, frame=capture.read()  					
    if ret==True:
        cv2.imshow("VideoFrame",frame)
        if cv2.waitKey(33)==ord('q'):break
    else:
        break
  
capture.release()
cv2.destroyAllWindows()
```

