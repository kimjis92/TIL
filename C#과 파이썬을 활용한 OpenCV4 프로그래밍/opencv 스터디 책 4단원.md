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



카메라 출력프레임은 종속적 

ex) 640 x 140 <-- 비율이 안맞음 110에 근접한 비율인 144로 변형되고 144와 비율이 맞도록 640값이 176으로 변형됨



## 5.도형 그리기

주로 OpenCV의 도형 그리기 함수는 주로 검출 결과를 시각적으로 표시하는데 사용



#### 선형 타입



##### 브레젠험 알고리즘: 

컴퓨터 그래픽스에서 복잡하고 계싼을 느리게만드는 실수계산을 배제하고 정수계산만으로 직선을 그리위해 만들어진 알고리즘

ex) y축의 두 점 y와 y+1중 사이에 있을때 더 가까운 쪽을 선택

4연결 방식: 상 하 좌 우 고려

8연결 방식: 대각선 방향까지 추가해서 고려



##### 안티에일리어싱:

주파수 문제때문에 인접한 스펙트럼이 겹쳐서 출력이 왜곡되는 현상인 계단현상을 방지하는 기술





#### 비트시프트

###### 사전적 의미

:0100 --> 0010 --> 0001      한칸씩 쉬프트한경우 

###### OpenCV에서의 비트시프트 의미

:도형 그리기 함수에서 사용하는 값은 일반적으로 정수인데 비트 시프트를 활용하면 실수값 좌표로 표현가능



ex)    (2, 2) 에서 (8 5) 로 이어진 선분에 비트시프트 1적용 



 







